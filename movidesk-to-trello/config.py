'''
File created to define the FIXED Variables
'''

from decouple import config

'''
Debugging mode from project
'''
DEBUG = config("DEBUG", default=True, cast=bool)

'''
Variables for Trello API
'''
TRELLO_BASE_URL = "api.trello.com"
TRELLO_CREATE_CARDS = "1/cards"
TRELLO_KEY = config('TRELLO_KEY')
TRELLO_ID_LIST = config("TRELLO_ID_LIST")
TRELLO_TOKEN = config("TRELLO_TOKEN")