from redis_dict import RedisDict
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
ADMIN = os.getenv('ADMIN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
database = RedisDict('ustozshogird_bot_db')


