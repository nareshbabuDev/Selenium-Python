from faker import Faker
from random import randint
import json
import os
from datetime import date

import json  # json library imported
# json data string
file_path = os.getcwd()
with open(file_path+'\\utils\\Test.json') as json_data:
    data = json.load(json_data)


# get current filepath

# json file read
with open(file_path+'\\utils\\config.json') as json_file:
    configdata = json.load(json_file)
saucelabsconfig = configdata["SAUCELABS"]
env = data[configdata['ENVIRONMENT']]
saucelabs = configdata["SAUCELABS"]
scriptstatus = configdata["SCRIPTSTATUS"]
# random Address
fake = Faker()
address = fake.street_address()
# random text
mailsubject = fake.word()
FolderName = fake.word()
randomint = randint(1,999)
# random date
statuseffectivedate = (str(randint(1, 12)) + "/" + str(randint(1, 28)) + "/" + str(randint(2000, 2018)))
# today date
today = date.today()
todaydate = today.strftime("%d-%b-%Y")