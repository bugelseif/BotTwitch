from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini', encoding='utf-8')

TOKEN = config.get('config', 'token')
USERNAME = config.get('config', 'username')
BOTS = config.get('config', 'bots').split()
BOTS.append(USERNAME)
