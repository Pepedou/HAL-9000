import os
import json
import time

from slackclient import SlackClient

__author__ = 'José Luis Valencia Herrera'
bot_token = os.environ.get("BOT_TOKEN", "")
hal_user_id = 'U0E804Q93'
hal_user_id_mention = '<@{0}>'.format(hal_user_id)
sc = SlackClient(bot_token)
users = None
channels = None


def log(text: str):
    print(text)
    log_file = open("/var/log/hal-9000/{0}.log".format(time.strftime("%Y-%m-%d")), "a")
    if log_file is not None:
        log_file.write(text + "\n")
        log_file.close()


def load_users():
    global users
    users = json.loads(sc.api_call("users.list").decode('utf-8'))['members']
    return users


def load_channels():
    global channels
    channels = json.loads(sc.api_call("channels.list").decode('utf-8'))['channels']
    return channels


def get_user_id_by_username(username):
    return next(user['id'] for user in users if user['name'] == username)


def get_user_by_id(id):
    return next(user for user in users if user['id'] == id)


def get_channel_id(channel_name):
    return next(channel['id'] for channel in channels if channel['name'] == channel_name)
