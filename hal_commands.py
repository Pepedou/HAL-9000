__author__ = 'José Luis Valencia Herrera'

import os
import plivo_text_to_speech
import utils


class HalCommandTypes:
    COFFEE_COMMAND = "coffee"


class HalCommand:
    def __init__(self):
        self.raw_request = ""
        self.requesting_user = ""
        self.command_arguments = []

    def execute(self):
        pass


class HalCommandParser:
    @staticmethod
    def parse_command_from_message_text(message_text: str):
        parsed_command = {}

        split_message = message_text.split(' ')

        if split_message[1] == str(HalCommandTypes.COFFEE_COMMAND):
            parsed_command['command_type'] = HalCommandTypes.COFFEE_COMMAND
            parsed_command['command_arguments'] = message_text.split('"')[1:]
        else:
            raise Exception("Unable to parse command type")

        return parsed_command


class CoffeeCommand(HalCommand):
    COFFEE_HOUSE_NUMBER = os.environ.get('COFFEE_HOUSE_NUMBER', "")

    def execute(self):
        try:
            success = plivo_text_to_speech.send_call(self.COFFEE_HOUSE_NUMBER,
                                                     self.requesting_user['real_name_normalized'],
                                                     self.command_arguments[0],
                                                     self.command_arguments[1])

            if success:
                if "tarjeta" in self.command_arguments[1].lower():
                    response_ending = "and a terminal should be brought to you for payment."
                else:
                    response_ending = "and I've requested change for a ${0} bill.".format(self.command_arguments[1])

                response = "Affirmative, {0}. I've placed the order \"{1}\" " \
                           "{2}".format(
                        self.requesting_user['first_name'],
                        self.command_arguments[0], response_ending)
            else:
                response = "I'm sorry {0}, I'm afraid I can't do that. There was an error sending the message. " \
                           "I think you know what the problem is just as well as I do.".format(
                        self.requesting_user['first_name'])
        except Exception as e:
            response = "I'm sorry {0}, I'm afraid I can't do that. There was an error sending the message. " \
                       "I think you know what the problem is just as well as I do. Error: {1}".format(
                    self.requesting_user['first_name'], str(e))

        return response


class HalCommandBuilder:
    @staticmethod
    def build_command_from_event(command_event):
        parsed_command = HalCommandParser.parse_command_from_message_text(command_event['text'])

        if parsed_command['command_type'] == HalCommandTypes.COFFEE_COMMAND:
            coffee_command = CoffeeCommand()
            coffee_command.requesting_user = utils.get_user_by_id(command_event['user'])['profile']
            coffee_command.command_arguments = parsed_command['command_arguments']

            return coffee_command
        else:
            raise Exception("Unhandled command type")
