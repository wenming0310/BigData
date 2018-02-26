import urllib.request as urlrequest
import time
import random

IMG_PATH = './imgs/{}.jpg'
DATA_FILE = './data/votes.csv'
STORED_IMG_ID_FILE = './data/cached_img.txt'
STORED_IMG_IDS = set()
IMG_URL = 'https://maps.googleapis.com/maps/api/streetview?size=400x300&location={},{}'
proxy = urlrequest.ProxyHandler({'https': '47.91.78.201:3128'})
opener = urlrequest.build_opener(proxy)

opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30')]

urlrequest.install_opener(opener)
with open(STORED_IMG_ID_FILE) as input_file:
    for line in input_file:
        STORED_IMG_IDS.add(line.strip())
with open(DATA_FILE) as input_file:
    skip_first_line = True
    for line in input_file:
        if skip_first_line:
            skip_first_line = False
            continue
        left_id, right_id, winner, left_lat, left_long, right_lat, right_long, category = line.split(',')

        if left_id not in STORED_IMG_IDS:
            print ('saving img {}...'.format(left_id))
            urlrequest.urlretrieve(IMG_URL.format(left_lat, left_long), IMG_PATH.format(left_id))
            STORED_IMG_IDS.add(left_id)
            with open(STORED_IMG_ID_FILE, 'a') as output_file:
                output_file.write('{}\n'.format(left_id))
            time.sleep(1)  # wait some time, trying to avoid google forbidden (of crawler)

        if right_id not in STORED_IMG_IDS:
            print ('saving img {}...'.format(right_id))
            urlrequest.urlretrieve(IMG_URL.format(right_lat, right_long), IMG_PATH.format(right_id))
            STORED_IMG_IDS.add(right_id)
            with open(STORED_IMG_ID_FILE, 'a') as output_file:
                output_file.write('{}\n'.format(right_id))
            time.sleep(1)  # wait some time, trying to avoid google forbidden (of crawler)