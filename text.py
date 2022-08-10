from twilio.rest import Client
import tkinter.messagebox as messagebox
from decouple import config,UndefinedValueError

def load_configurations():
        try:
            twilio_account_sid = config("TWILIO_ACCOUNT_SID")
            twilio_auth_token = config("TWILIO_ACCOUNT_TOKEN")
            twilio_phone_number = config("TWILIO_NUMBER")
        except UndefinedValueError:
            messagebox.showwarning('Zoom Count Error', "There is a problem with your environment variables, kindly make sure you have all of them")

        if not all([twilio_account_sid,twilio_auth_token,twilio_phone_number]):
            raise Exception("Not all configuration were run")

        return (twilio_account_sid,twilio_auth_token,twilio_phone_number)

class Text():

    def __init__(self):
        (
            twilio_account_sid,
            twilio_auth_token,
            twilio_phone_number
        ) = load_configurations()

        self.twilio_number = twilio_phone_number
        self.twilio_client = Client(twilio_account_sid,twilio_auth_token)
        self.message_body = "Hello {}, the number of zoom attendees today is {}."

    def send_text(self,receiver_number:str,receiver_name:str,zoom_attendance:int):
        try:
            self.twilio_client.messages.create(to=receiver_number,from_=self.twilio_number,body=self.message_body.format(receiver_name,zoom_attendance))
        except Exception as e:
            messagebox.showwarning('Zoom Count Error', "There was a problem sending the message, please make sure your credentials are correct.")