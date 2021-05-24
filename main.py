import hashlib
import string
import random
import json
import time
import os
from collections import  OrderedDict

def random_string_data():
    new_pw_len = 10 # 새 비밀번호 길이
    pw_candidate = string.ascii_letters + string.digits + string.punctuation
    new_pw = ""
    for i in range(new_pw_len):
        new_pw += random.choice(pw_candidate)
    return  new_pw

def user_string_data():
    data = input("문자을 작성해주세요 :")
    return data

def add_block(data):
    myHash = hashlib.sha512(str(data).encode('utf-8')).hexdigest()
    return myHash

def json_data_read(hash, data):
    with open('data/block.json', 'r') as f:
        read = json.load(f)
    num = int(json.dumps(read["block"]["num"]))
    num += 1
    json_data_write(hash = hash, data = data, nums = num)

def json_data_write(hash,data,nums):
    times = time.strftime('%Y-%m-%d %h-%m-%s', time.localtime(time.time()))
    file_data = OrderedDict()

    datas = {"hash" : hash,"text" : data ,"num" : nums, "time" : times}
    file_data["block"] = datas

    with open("data/block.json", "a", encoding ="utf-8", newline ="") as datas:
        json.dump(file_data, datas, indent = 4)

def add_json_make(hash,data):
    times = time.strftime('%Y-%m-%d %h-%m-%s', time.localtime(time.time()))

    datas = {"hash" : hash, "text" : data, "time" : times}
    with open("data/block/" + data + ".json", "w", encoding = "utf-8", newline = "") as datad:
        json.dump(datas, datad, indent = 4)

def block_all_rm():
    os.rmdir("data/block")
    os.mkdir("data/block")

if __name__ == '__main__':
    text = random_string_data()
    hashs = add_block(data = text)

    add_json_make(hash = hashs, data = text)

    try:
        json_data_read(hash = hashs , data = text)
    except KeyError:
        json_data_write(hash = hashs , data = text, nums = 1)

#작성완료