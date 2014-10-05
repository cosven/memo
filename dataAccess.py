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

'''
assume that filename is date.json
memo id is date
the id of each content in memo is number
'''

def save(dictdata):
    '''
    1. judge if exists the file
        yes: write jsondata
        no: new the file and write jsondata
    '''
    filename = dictdata['id'] + '.json'
    f = open(filename, 'w')
    jsondata = json.dumps(dictdata)
    f.write(jsondata)
    f.close

def read(date):
    '''
    1. if exist today's file
        a. judge finish or not and directly load it
    2. not exist
        a. init the today's file
            1. to check log and get lastmemo file
    3. finally, return a unfinished content list
    '''
    contentlist = []

    filename = date + '.json'
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
