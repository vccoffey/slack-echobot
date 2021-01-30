#!/usr/bin/env python

from time import sleep
# from slack import SlackClient
from slack import WebClient
import os

slack_token = os.environ.get('TOKEN', None) # found at https://api.slack.com/web#authentication
print('found token',slack_token[0:6],'...')

client = WebClient(token=slack_token)
print(client.rtm_connect() )


# sc = WebClient(token=token)
# if sc.rtm_connect() == True:
#   print('Connected.')
#   while True:
#     response = sc.rtm_read()
#     for part in response:
#       if part['type'] == 'message':
#         if part['text'].lower().startswith('echo: '):
#           sc.api_call("chat.postMessage", channel=part['channel'], text=part['text'][len('echo: '):], username='echobot', icon_emoji=':robot_face:')
#     sleep(1)
# else:
#   print('Connection Failed, invalid token?')
