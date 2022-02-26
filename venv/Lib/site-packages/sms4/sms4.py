"""
SMS4 Python Client

Simple and straightforward way to send text messages from your code
"""

import os
import requests
import threading

SMS4_ENDPOINT = 'https://sms4.dev/send'

# Send a message and return response from the server
def send(to=None, message=None, api_token=None, server_response=None):
  message = SMS4(
    to,
    message,
    api_token=api_token
  )

  return message.send_server_request()


# Send a message inside the separate thread
def nonblocking_send(to=None, message=None, api_key=None):
  try:
    sms4_thread = threading.Thread(target=send, args=(to, message, api_key))
    sms4_thread.start()
  except:
    pass


class SMS4(object):

    def __init__(self, to, message, subject=None, api_token=None):
      if not api_token:
        self.api_token = os.environ.get('SMS4_TOKEN')
      else:
        self.api_token = api_token

      self.to = to
      self.message = message
      self.subject = subject


    def is_valid_input(self):
      if type(self.to) != str and type(self.to) != list:
        print 'Recepients string is invalid. Please refer to our documentation at https://sms4.dev to see correct options.'
        return False
      
      if type(self.message) != str:
        print 'SMS4 Error: Message string is invalid. Please refer to our documentation at https://sms4.dev to see correct options.'
        return False

      if not self.api_token:
        print 'SMS4 token is not defined. To fix this you have to either:\n1) Set environment variable SMS4_TOKEN\nor\n2) Pass the token as the 3rd argument to the send function.'
        return False

      return True

    def send_server_request(self):
      if not self.is_valid_input():
        return False

      to = None
      if type(self.to) == list:
        to = ','.join(self.to)
      else:
        to = self.to
      
      sms4_params = {
        'to': to,
        'message': self.message,
        'token': self.api_token,
      }

      r = requests.post(SMS4_ENDPOINT, json=sms4_params)

      return r.json()
      