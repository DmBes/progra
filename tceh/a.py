import requests
import time
from tqdm import tqdm

HOST = 'https://api.vk.com/method'
VERSION = '5.80'
access_token = '227c33ee227c33ee227c33eee322191a042227c227c33ee7939b8760814e8ed7add2ba3'

r = requests.get(HOST + 'user.get', params={'user_ids': '1, 2'})  # hz

r.json()