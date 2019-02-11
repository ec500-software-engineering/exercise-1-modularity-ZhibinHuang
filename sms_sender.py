# https://github.com/ec500-software-engineering/exercise-1-modularity-mdche001/blob/master/sms_sender.py #

from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# data type from the common_types
class Message(object):
    def __init__(self, content, urgency):
        self._content = content
        self._urgency = urgency

    def get_msg_content(self):
        return self._content

    def get_urgency(self):
        return self._urgency


# Your Account Sid and Auth Token from twilio.com/console
# accountSID='authToken'
# authToken='authToken'
# myNumber='myNumber'
# twilioNumber='twilioNumber'
# message= "" #Message you want to send

# for general information #
class Contact(object):
    def __init__(self, name, sms_info, email_info):
        self._name = name
        self._sms_info = sms_info
        self._email_info = email_info

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email_info

    def get_sms(self):
        return self._sms_info



def textmyself(source_phone_num, destination_phone_num,message):
    """fuction to  send messages to the phone by twilio number"""
    # Getting the Authorization of the twilio
    twilioCli = Client(accountSID,authToken)

    #send message by twilio api
    # twilioCli.api.account.messages.create(body=message,from_=twilioNumber,to=myNumber)//python2
    twilioCli.messages.create(body=message,from_=twilioNumber,to=myNumber)#python3


def callmyself(source_phone_num, destination_phone_num,message):
    """ call the phone number by using an trial voice"""
    # Getting the Authorization of the twilio
    twilioCli = Client(accountSID, authToken)
    # call the phone number
    testcall = twilioCli.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml', # the trial voice's url
                            to='source_phone_num',   #your twilio num
                            from_='destination_phone_num' #any phone num you want
                        )

    print(testcall.sid)


# @app.route("/")
# def hello():
#     return "Hello World!"

# replying message by flask
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Thanks for you reply, we'll deal with it as soon as possible!")

    return str(resp)

if __name__ == "__main__":
    Msg = Message ('The patient is blooding', 0)
    # textmyself(myNumber,twilioNumber,message)
    callmyself(myNumber,twilioNumber,message)
    textmyself(myNumber,twilioNumber,Msg.get_msg_content())
    app.run(debug=True)
