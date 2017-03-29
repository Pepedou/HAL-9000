import time

from hal_commands import *
from utils import load_users, load_channels, sc, hal_user_id_mention
from utils import log


def process_response(the_response):
    for event in the_response:
        if 'type' not in event:
            return

        if event['type'] == 'message':
            process_message(event)
            return


def message_is_for_hal(text_message):
    return text_message.startswith(hal_user_id_mention)


def message_is_from_group(message_event):
    return message_event['text'].startswith("G")


def process_message(message_event):
    if 'text' not in message_event:
        return

    if not message_is_for_hal(message_event['text']):
        return

    hal_command = HalCommandBuilder.build_command_from_event(message_event)

    if 'channel' not in message_event:
        return

    if message_is_from_group(message_event):
        post_message_params = {
            'token': utils.bot_token,
            'channel': message_event['channel'],
            'text': hal_command.execute(),
        }
        sc.api_call('chat.postMessage', post_message_params)
    else:
        sc.rtm_send_message(message_event['channel'], hal_command.execute())


def work():
    while True:
        try:
            response = sc.rtm_read()
            process_response(response)
            time.sleep(1)

        except KeyboardInterrupt:
            log("HAL-9000 stopped at {0}".format(time.strftime("%c")))
            exit(0)
        except Exception as e:
            log(str(e))


if __name__ == "__main__":
    log("HAL-9000 started at {0}".format(time.strftime("%c")))
    if sc.rtm_connect():
        try:
            load_users()
            load_channels()
            work()
        except Exception as ex:
            log(str(ex))
    else:
        log("Connection Failed")
