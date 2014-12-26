# -*- coding:utf8 -*-
#! /usr/bin/python

'''
dictdata = {
        'id': '2012', 
        'datetime': '10',
        'memoList': [
            {
                'id': '1',
                'pid': '2012',
                'content': 'hello',
                'deadline': '2013',
                'finished': True,
                },
            ],
        'notfinish': [],
        }
'''

import os
import json

import setting

'''
假设文件名是 data.json
memo 的id是日期
memolist 的每一条内容的id是一个数字
'''

def save(dictdata):
    '''
    这个函数在程序退出的时候调用
    保存今天没有完成的memo
    '''
    filename = dictdata['id'] + '.json'
    filename = setting.DATAPATH + filename
    f = open(filename, 'w')
    jsondata = json.dumps(dictdata)
    f.write(jsondata)
    f.close()

def read(date):
    '''
    判断是否存在文件名为今天的文件:
        如果存在，判断哪些完成了，哪些没有完成, 然后直接把没完成了加载
        如果不存在，创建今天的json，检测log.json,昨天的有哪些还没有完成
    最后，程序返回没有完成的memolist
    '''
    contentlist = []

    filename = date + '.json'
    filename = setting.DATAPATH + filename
    if os.path.exists(filename):
        f = open(filename, 'r')
        jsondata = json.load(f)
        f.close()
        memolist = jsondata['memolist']
        for each in memolist:
            if not each['finished']:
                contentlist.append(each)
    else:
        f = open('log.json', 'r')
        jsondata = json.load(f)
        f.close()
        lastmemo = jsondata['last']
        filename = lastmemo + '.json'
        filename = setting.DATAPATH + filename
        f = open(filename, 'r')
        jsondata = json.load(f)
        f.close()
        memolist = jsondata['memolist']
        for each in memolist:
            if not each['finished']:
                contentlist.append(each)
    return contentlist

if __name__ == "__main__":
    data = {
        'id': '2012',
        'datetime': '10',
        'memolist': [
            {
                'id': '1',
                'pid': '2012',
                'content': 'hello',
                'deadline': '2013',
                'finished': False,
                },
            {
                'id': '2',
                'pid': '2012',
                'content': 'world',
                'deadline': '2013',
                'finished': False,
                },
            ],
        'notfinish': [],
        }
    save(data)
    r = read(data['id'])
