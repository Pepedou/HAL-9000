import os
import plivo

__author__ = 'José Luis Valencia Herrera'

auth_id = os.environ.get("PLIVO_AUTH_ID", "")
auth_token = os.environ.get("PLIVO_AUTH_TOKEN", "")

p = plivo.RestAPI(auth_id, auth_token)


def send_sms(phone, text: str):
    params = {
        'src': os.environ.get("SENDERS_PHONE_NUMBER", ""),  # Sender's phone number with country code
        'dst': phone,  # Receiver's phone Number with country code
        'text': text,
        'url': "http://morning-ocean-4669.herokuapp.com/report/",  # URL where response is sent
        'method': 'GET'  # The method used to call the url
    }
    response = p.send_message(params)

    return response[0] == 202


if __name__ == "__main__":
    print(send_sms(os.environ.get("SENDERS_PHONE_NUMBER", ""), "Hello? Can you hear me"))
