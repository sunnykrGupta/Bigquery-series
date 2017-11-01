#!/usr/bin/env python

import redis
import json
import time
#Faker : https://github.com/joke2k/faker
from faker import Faker

streamRedis = redis.Redis(host='127.0.0.1',
             port='6379',
            password='')

fake = Faker()

def profile_generator():
    tmpProfile = fake.simple_profile(sex=None)
    print tmpProfile
    return tmpProfile
    # {   'address': 'USNS Anderson\nFPO AA 75268',
    #     'birthdate': '1981-09-24',
    #     'mail': 'kpierce@hotmail.com',
    #     'name': 'Glenda Ryan',
    #     'sex': 'F',
    #     'username': 'unorris'}

def main():
    while True:
        try:
            streamRedis.lpush("redisList", json.dumps(profile_generator()) )
        except Exception as e:
            print (e)
        #sleep 200ms
        time.sleep(0.2)

if __name__ == "__main__":
    main()
