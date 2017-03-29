import json
from datetime import datetime

import utils
from slackentities.slack_users import SlackUser

__author__ = "José Luis Valencia Herrera"


class ChannelTopic:
    def __init__(self):
        self.value = ""
        self.creator = SlackUser()
        self.last_set = 0

    def map_json_to_self(self, channel_topic_json: dict):
        self.value = channel_topic_json.get("value", self.value)
        self.creator.id = channel_topic_json.get("creator", self.creator.id)
        self.last_set = channel_topic_json.get("last_set", self.last_set)


class ChannelPurpose:
    def __init__(self):
        self.value = ""
        self.creator = SlackUser()
        self.last_set = 0

    def map_json_to_self(self, channel_purpose_json: dict):
        self.value = channel_purpose_json.get("value", self.value)
        self.creator.id = channel_purpose_json.get("creator", self.creator.id)
        self.last_set = channel_purpose_json.get("last_set", self.last_set)


class SlackChannel:
    @property
    def id(self):
        self.sync()
        return self.__id

    @id.setter
    def id(self, channel_id):
        self.__id = channel_id
        self.__has_been_modified = True

    @property
    def name(self):
        self.sync()
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        self.__has_been_modified = True

    @property
    def created(self):
        self.sync()
        return self.__created

    @created.setter
    def created(self, created):
        self.__created = created
        self.__has_been_modified = True

    @property
    def creator(self):
        self.sync()
        return self.__creator

    @creator.setter
    def creator(self, creator):
        self.__creator = creator
        self.__has_been_modified = True

    @property
    def is_archived(self):
        self.sync()
        return self.__is_archived

    @property
    def is_general(self):
        self.sync()
        return self.__is_general

    @is_general.setter
    def is_general(self, is_general):
        self.__is_general = is_general
        self.__has_been_modified = True

    @property
    def is_member(self):
        self.sync()
        return self.__is_member

    @is_member.setter
    def is_member(self, is_member):
        self.__is_member = is_member
        self.__has_been_modified = True

    @property
    def members(self):
        self.sync()
        return self.__members

    @members.setter
    def members(self, members):
        self.__members = members
        self.__has_been_modified = True

    @property
    def topic(self):
        self.sync()
        return self.__topic

    @topic.setter
    def topic(self, topic):
        self.__topic = topic
        self.__has_been_modified = True

    @property
    def purpose(self):
        self.sync()
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose):
        self.__purpose = purpose
        self.__has_been_modified = True

    @property
    def last_read(self):
        self.sync()
        return self.__last_read

    @last_read.setter
    def last_read(self, last_read):
        self.__last_read = last_read
        self.__has_been_modified = True

    @property
    def latest(self):
        self.sync()
        return self.__latest

    @latest.setter
    def latest(self, latest):
        self.__latest = latest
        self.__has_been_modified = True

    @property
    def unread_count(self):
        self.sync()
        return self.__unread_count

    @unread_count.setter
    def unread_count(self, unread_count):
        self.__unread_count = unread_count
        self.__has_been_modified = True

    @property
    def unread_count_display(self):
        self.sync()
        return self.__unread_count_display

    @unread_count_display.setter
    def unread_count_display(self, unread_count_display):
        self.__unread_count_display = unread_count_display
        self.__has_been_modified = True

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__created = 0
        self.__creator = SlackUser()
        self.__is_archived = False
        self.__is_general = False
        self.__is_member = False
        self.__members = []
        self.__topic = ChannelTopic()
        self.__purpose = ChannelPurpose()
        self.__last_read = ""
        self.__latest = {}
        self.__unread_count = 0
        self.__unread_count_display = 0
        self.__has_been_loaded = False
        self.__has_been_modified = False

    def sync(self):
        if not self.__has_been_loaded:
            try:
                self.load()
                self.__has_been_loaded = True
            except Exception:
                pass

    def map_json_to_self(self, channel_json: dict):
        self.__id = channel_json.get("id", self.__id)
        self.__name = channel_json.get("name", self.__name)
        self.__created = channel_json.get("created", self.__created)
        self.__creator.id = channel_json.get("creator", self.__creator.id)
        self.__is_archived = channel_json.get("is_archived", self.__is_archived)
        self.__is_general = channel_json.get("is_general", self.__is_general)
        self.__is_member = channel_json.get("is_member", self.__is_member)
        self.load_members_from_json(channel_json.get("members", self.__members))
        self.__topic.map_json_to_self(channel_json.get("topic", self.__topic))
        self.__purpose.map_json_to_self(channel_json.get("purpose", self.__topic))
        self.__last_read = channel_json.get("last_read", self.__last_read)
        self.__latest = channel_json.get("latest", self.__latest)
        self.__unread_count = channel_json.get("unread_count", self.__unread_count)
        self.__unread_count_display = channel_json.get("unread_count_display", self.__unread_count_display)

    def load_members_from_json(self, members_json: dict):
        self.__members.clear()

        for member_json in members_json:
            new_member = SlackUser()
            new_member.id = member_json
            self.__members.append(new_member)

    def load(self):
        if not self.__id:
            raise Exception("Failed to load the channel's information. Channel doesn't have an ID.")

        api_response = utils.sc.api_call("channels.info", token=utils.bot_token, channel=self.__id)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to load the channel's information. API call was unsuccessful.")

        self.map_json_to_self(response_json["channel"])

    @staticmethod
    def load_all_channels(exclude_archived: bool):
        channels = []
        api_response = utils.sc.api_call("channels.list", token=utils.bot_token, exclude_archived=exclude_archived)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to list all channels. API call was unsuccessful.")

        for channel_json in response_json["channels"]:
            channel = SlackChannel()
            channel.map_json_to_self(channel_json)
            channels.append(channel)

        return channels

    def archive(self):
        api_response = utils.sc.api_call("channels.archive", token=utils.bot_token, channel=self.__id)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to archive channel. API call was unsuccessful.")

    def unarchive(self):
        api_response = utils.sc.api_call("channels.unarchive", token=utils.bot_token, channel=self.__id)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to unarchive channel. API call was unsuccessful.")

    @staticmethod
    def create_channel(name: str):
        channel = SlackChannel()
        api_response = utils.sc.api_call("channels.create", token=utils.bot_token, name=name)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to create channel. API call was unsuccessful.")

        channel.map_json_to_self(response_json["channel"])
        return channel

    def invite_user_to_channel(self, user: SlackUser):
        api_response = utils.sc.api_call("channels.invite", token=utils.bot_token, channel=self.__id, user=user.id)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to invite user to channel. API call was unsuccessful.")

        self.map_json_to_self(response_json["channel"])

    def kick_user_from_channel(self, user: SlackUser):
        api_response = utils.sc.api_call("channels.kick", token=utils.bot_token, channel=self.__id, user=user.id)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to kick user from channel. API call was unsuccessful.")

    def rename(self, new_name: str):
        api_response = utils.sc.api_call("channels.rename", token=utils.bot_token, channel=self.__id, name=new_name)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to rename channel. API call was unsuccessful.")

        self.map_json_to_self(response_json["channel"])

    @staticmethod
    def join_channel(name: str):
        api_response = utils.sc.api_call("channels.join", token=utils.bot_token, name=name)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to join channel. API call was unsuccessful.")

    def join_channel(self):
        api_response = utils.sc.api_call("channels.join", token=utils.bot_token, name=self.__name)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to join channel. API call was unsuccessful.")

    @staticmethod
    def leave_channel(channel_id: str):
        api_response = utils.sc.api_call("channels.leave", token=utils.bot_token, channel=channel_id)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to leave channel. API call was unsuccessful.")

    def leave_channel(self):
        api_response = utils.sc.api_call("channels.leave", token=utils.bot_token, channel=self.__id)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to leave channel. API call was unsuccessful.")

    def set_topic(self, new_topic: str):
        api_response = utils.sc.api_call("channels.setTopic", token=utils.bot_token, channel=self.__id, topic=new_topic)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to change channel's topic. API call was unsuccessful.")

        self.topic.value = response_json["topic"]

    def set_purpose(self, new_purpose: str):
        api_response = utils.sc.api_call("channels.setPurpose", token=utils.bot_token, channel=self.__id,
                                         purpose=new_purpose)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to change channel's purpose. API call was unsuccessful.")

        self.purpose.value = response_json["purpose"]

    def mark(self, timestamp: float):
        api_response = utils.sc.api_call("channels.mark", token=utils.bot_token, channel=self.__id, ts=timestamp)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to move the read cursor. API call was unsuccessful.")

    def get_message_history(self, params: dict):
        latest = params.get("latest", datetime.timestamp())
        oldest = params.get("oldest", 0)
        inclusive = params.get("inclusive", False)
        count = params.get("count", 100)
        unreads = params.get("unreads", False)

        api_response = utils.sc.api_call("channels.history",
                                         token=utils.bot_token,
                                         channel=self.__id,
                                         latest=latest,
                                         oldest=oldest,
                                         inclusive=inclusive,
                                         count=count,
                                         unreads=unreads)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to fetch channel history. API call was unsuccessful.")

        return response_json["messages"]


if __name__ == "__main__":
    theChannels = SlackChannel.load_all_channels(True)
    print(theChannels[0].creator.profile.real_name_normalized)
