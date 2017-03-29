import json

import utils

__author__ = "José Luis Valencia Herrera"


class UserProfile:
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
        self.__has_been_modified = True

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
        self.__has_been_modified = True

    @property
    def real_name(self):
        return self.__real_name

    @real_name.setter
    def real_name(self, real_name):
        self.__real_name = real_name
        self.__has_been_modified = True

    @property
    def real_name_normalized(self):
        return self.__real_name_normalized

    @real_name_normalized.setter
    def real_name_normalized(self, real_name_normalized):
        self.__real_name_normalized = real_name_normalized
        self.__has_been_modified = True

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__first_name = title
        self.__has_been_modified = True

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
        self.__has_been_modified = True

    @property
    def skype(self):
        return self.__skype

    @skype.setter
    def skype(self, skype):
        self.__skype = skype
        self.__has_been_modified = True

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone
        self.__has_been_modified = True

    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__real_name = ""
        self.__real_name_normalized = ""
        self.__title = ""
        self.__email = ""
        self.__skype = ""
        self.__phone = ""
        self.__has_been_modified = False

    def map_json_to_self(self, user_profile_json: dict):
        self.first_name = user_profile_json.get("first_name", self.first_name)
        self.last_name = user_profile_json.get("last_name", self.last_name)
        self.real_name = user_profile_json.get("real_name", self.real_name)
        self.real_name_normalized = user_profile_json.get("real_name_normalized", self.real_name_normalized)
        self.title = user_profile_json.get("title", self.title)
        self.email = user_profile_json.get("email", self.email)
        self.skype = user_profile_json.get("skype", self.skype)
        self.phone = user_profile_json.get("phone", self.phone)


class UserPresence:
    @property
    def presence(self):
        return self.__presence

    @presence.setter
    def presence(self, presence):
        self.__presence = presence
        self.__has_been_modified = True

    @property
    def online(self):
        return self.__online

    @online.setter
    def online(self, online):
        self.__online = online
        self.__has_been_modified = True

    @property
    def auto_away(self):
        return self.__auto_away

    @auto_away.setter
    def auto_away(self, auto_away):
        self.__auto_away = auto_away
        self.__has_been_modified = True

    @property
    def manual_away(self):
        return self.__manual_away

    @manual_away.setter
    def manual_away(self, manual_away):
        self.__manual_away = manual_away
        self.__has_been_modified = True

    @property
    def connection_count(self):
        return self.__connection_count

    @connection_count.setter
    def connection_count(self, connection_count):
        self.__connection_count = connection_count
        self.__has_been_modified = True

    @property
    def last_activity(self):
        return self.__last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        self.__last_activity = last_activity
        self.__has_been_modified = True

    def __init__(self):
        self.__presence = ""
        self.__online = ""
        self.__auto_away = False
        self.__manual_away = False
        self.__connection_count = 0
        self.__last_activity = 0
        self.__has_been_modified = False

    def map_json_to_self(self, user_presence_json: dict):
        self.presence = user_presence_json.get("presence", self.presence)
        self.online = user_presence_json.get("online", self.online)
        self.auto_away = user_presence_json.get("auto_away", self.auto_away)
        self.manual_away = user_presence_json.get("manual_away", self.manual_away)
        self.connection_count = user_presence_json.get("connection_count", self.connection_count)
        self.last_activity = user_presence_json.get("last_activity", self.last_activity)


class SlackUser:
    @property
    def id(self):
        self.sync()
        return self.__id

    @id.setter
    def id(self, user_id):
        self.__id = user_id
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
    def real_name(self):
        self.sync()
        return self.__real_name

    @real_name.setter
    def real_name(self, real_name):
        self.__real_name = real_name
        self.__has_been_modified = True

    @property
    def status(self):
        self.sync()
        return self.__real_name

    @status.setter
    def status(self, status):
        self.__status = status
        self.__has_been_modified = True

    @property
    def team_id(self):
        self.sync()
        return self.__team_id

    @team_id.setter
    def team_id(self, team_id):
        self.__team_id = team_id
        self.__has_been_modified = True

    @property
    def deleted(self):
        self.sync()
        return self.__deleted

    @deleted.setter
    def deleted(self, deleted):
        self.__deleted = deleted
        self.__has_been_modified = True

    @property
    def color(self):
        self.sync()
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
        self.__has_been_modified = True

    @property
    def profile(self):
        self.sync()
        return self.__profile

    @profile.setter
    def profile(self, profile):
        self.__profile = profile
        self.__has_been_modified = True

    @property
    def status(self):
        self.sync()
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status
        self.__has_been_modified = True

    @property
    def presence(self):
        self.sync()
        return self.__presence

    @presence.setter
    def presence(self, presence):
        self.__presence = presence
        self.__has_been_modified = True

    @property
    def tz(self):
        self.sync()
        return self.__tz

    @tz.setter
    def tz(self, tz):
        self.__tz = tz
        self.__has_been_modified = True

    @property
    def tz_label(self):
        self.sync()
        return self.__tz_label

    @tz_label.setter
    def tz_label(self, tz_label):
        self.__tz_label = tz_label
        self.__has_been_modified = True

    @property
    def tz_offset(self):
        self.sync()
        return self.__tz_offset

    @tz_offset.setter
    def tz_offset(self, tz_offset):
        self.__tz_offset = tz_offset
        self.__has_been_modified = True

    @property
    def is_admin(self):
        self.sync()
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        self.__is_admin = is_admin
        self.__has_been_modified = True

    @property
    def is_bot(self):
        self.sync()
        return self.__is_bot

    @is_bot.setter
    def is_bot(self, is_bot):
        self.__is_bot = is_bot
        self.__has_been_modified = True

    @property
    def is_owner(self):
        self.sync()
        return self.__is_owner

    @is_owner.setter
    def is_owner(self, is_owner):
        self.__is_owner = is_owner
        self.__has_been_modified = True

    @property
    def is_primary_owner(self):
        self.sync()
        return self.__is_owner

    @is_primary_owner.setter
    def is_primary_owner(self, is_primary_owner):
        self.__is_primary_owner = is_primary_owner
        self.__has_been_modified = True

    @property
    def is_restricted(self):
        self.sync()
        return self.__is_restricted

    @is_restricted.setter
    def is_restricted(self, is_restricted):
        self.__is_restricted = is_restricted
        self.__has_been_modified = True

    @property
    def is_ultra_restricted(self):
        self.sync()
        return self.__is_ultra_restricted

    @is_ultra_restricted.setter
    def is_ultra_restricted(self, is_ultra_restricted):
        self.__is_ultra_restricted = is_ultra_restricted
        self.__has_been_modified = True

    @property
    def has_2fa(self):
        self.sync()
        return self.__has_2fa

    @has_2fa.setter
    def has_2fa(self, has_2fa):
        self.__has_2fa = has_2fa
        self.__has_been_modified = True

    @property
    def has_files(self):
        self.sync()
        return self.__has_files

    @has_files.setter
    def has_files(self, has_files):
        self.__has_files = has_files
        self.__has_been_modified = True

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__real_name = ""
        self.__status = ""
        self.__team_id = ""
        self.__deleted = False
        self.__color = ""
        self.__profile = UserProfile()
        self.__status = ""
        self.__presence = UserPresence()
        self.__tz = ""
        self.__tz_label = ""
        self.__tz_offset = 0
        self.__is_admin = False
        self.__is_bot = False
        self.__is_owner = False
        self.__is_primary_owner = False
        self.__is_restricted = False
        self.__is_ultra_restricted = False
        self.__has_2fa = False
        self.__has_files = False
        self.__has_been_loaded = False
        self.__has_been_modified = False

    def sync(self):
        if not self.__has_been_loaded:
            try:
                self.load()
                self.__has_been_loaded = True
            except Exception:
                pass

    def load(self):
        if not self.__id:
            raise Exception("Failed to load the user's information. User doesn't have an ID.")

        api_response = utils.sc.api_call("users.info", token=utils.bot_token, user=self.__id)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to load the user's information. API call was unsuccessful.")

        self.map_json_to_self(response_json["user"])

    @staticmethod
    def load_user_information(user_id: str):
        new_user = SlackUser()
        api_response = utils.sc.api_call("users.info", token=utils.bot_token, user=user_id)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to load the user's information. API call was unsuccessful.")

        new_user.map_json_to_self(response_json["user"])
        return new_user

    def map_json_to_self(self, user_json: dict):
        self.__id = user_json.get("id", self.__id)
        self.__name = user_json.get("name", self.__name)
        self.__real_name = user_json.get("real_name", self.__real_name)
        self.__status = user_json.get("status", self.__status)
        self.__team_id = user_json.get("team_id", self.__team_id)
        self.__deleted = user_json.get("deleted", self.__deleted)
        self.__color = user_json.get("color", self.__color)
        self.__profile.map_json_to_self(user_json.get("profile", {}))
        self.__status = user_json.get("status", self.__status)
        self.__presence.map_json_to_self(user_json.get("presence", {}))
        self.__tz = user_json.get("tz", self.__tz)
        self.__tz_label = user_json.get("tz_label", self.__tz_label)
        self.__tz_offset = user_json.get("tz_offset", self.__tz_offset)
        self.__is_admin = user_json.get("is_admin", self.__is_admin)
        self.__is_bot = user_json.get("is_bot", self.__is_bot)
        self.__is_owner = user_json.get("is_owner", self.__is_owner)
        self.__is_primary_owner = user_json.get("is_primary_owner", self.__is_primary_owner)
        self.__is_restricted = user_json.get("is_restricted", self.__is_restricted)
        self.__is_ultra_restricted = user_json.get("is_ultra_restricted", self.__is_ultra_restricted)
        self.__has_2fa = user_json.get("has_2fa", self.__has_2fa)
        self.__has_files = user_json.get("has_files", self.__has_files)

    @staticmethod
    def load_all_users():
        users = []
        api_response = utils.sc.api_call("users.list", token=utils.bot_token, presence=True)

        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to load user list. API call was unsuccessful.")

        for user_json in response_json["members"]:
            new_user = SlackUser()
            new_user.map_json_to_self(user_json)
            users.append(new_user)

        return users

    def load_presence(self):
        api_response = utils.sc.api_call("users.getPresence", token=utils.bot_token, user=self.__id)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to load user's presence. API call was unsuccessful.")

        self.presence.map_json_to_self({key: value for key, value in response_json.items() if key != "ok"})

    def set_presence(self, presence: str):
        api_response = utils.sc.api_call("users.setPresence", token=utils.bot_token, presence=presence)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to set user's presence. API call was unsuccessful.")

        self.__presence.presence = presence

    def set_active(self):
        api_response = utils.sc.api_call("users.setActive", token=utils.bot_token)
        response_json = json.loads(api_response.decode("utf-8"))

        if response_json["ok"] is False:
            raise Exception("Failed to set user as active. API call was unsuccessful.")

        self.__presence.presence = "active"


if __name__ == "__main__":
    user = SlackUser()
    user.id = utils.hal_user_id
    print(user.profile.real_name)
