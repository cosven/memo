# -*- coding:utf8 -*-

# =============================================================================
#      FileName: dataIO.py
#          Desc: 负责文件的数据交互
#        Author: ysw(zjuysw)
#         Email: yinshaowen241@gmail.com
#      HomePage: http://my.oschina.net/zjuysw
#       Version: 0.0.1
#    LastChange: 2014-12-27 22:57:23
#       History:
# =============================================================================

"""
该模块负责程序与文件数据的交互:
    1. 从文件中读取json
    2. 保存json进入文件

该模块基于的假设：
    1. 程序每次运行完毕时，把当日所有未完成和完成的任务写入date.json
        也就是会调用 write 函数

    test_data = {
        'datetime': '2014-12-28',
        'memo_list': [
            {
                'id': '1',
                'title': 'homework',
                'start_time': '2012-12-28',
                'content': 'hello',
                'deadline': '2013-12-21',
                'finished': True
            }
        ],
    }

    config_data = {
        'last_date': ''
    }
"""

import os
import json

from logger import log
import setting


def update_config_file(date):
    """

    @note:
        更新config文件

    @param:
        date

    @attention::
        把含有中文的json以中文形式写入文件
        import json
        data = {}
        data['title'] = unicode(title)
        f = open("test.json", 'w')
        data = json.dumps(data, indent=4, sort_keys=True,
            ensure_ascii=False).encode('utf8')
        f.write(data)
        f.close()
    """
    f = open(setting.CONFIGJSONFILE, 'w')  # 创建配置文件
    config_data = {'last_date': date}
    write_in_data = json.dumps(config_data)  # 转换为可写入文件的形式
    f.write(write_in_data)
    f.close()
    # log.info("Update Config File Finished!")


def read(date):
    """

    @note:
        每次程序运行，都会调用这个函数

        读取log.json,读取其中保存的日期，从而读取相应的文件
        如果log.json不存在，说明第一次运行程序。

    @param date: 就是当天的日期
        >>> from PyQt4.QtCore import QDate
        >>> date = QDate.currentDate()
        >>> date.toString("yyyy-MM-dd")
        2012-12-15

    @return memo_list: 返回memo列表
    """
    # log.info("Enter in read func!")
    memo_list = []  # return data

    file_name = date + '.json'
    file_path = setting.DATAPATH + file_name
    if os.path.exists(file_path):  # 今天非第一次打开程序
        f = open(file_path, 'r')  # @attention: open a file for read
        data = json.load(f)  # may cause error
        f.close()
        memo_list = data['memo_list']
    else:
        if not os.path.exists(setting.CONFIGJSONFILE):  # 第一次启动程序
            update_config_file(date)
        else:  # 今天第一次打开程序
            f = open(setting.CONFIGJSONFILE, 'r')  # 从配置文件中读取上一次
            data = json.load(f)  # 打开程序的日期, 来读取
            f.close()  # 上次的数据
            date = data['last_date']
            last_file_name = date + '.json'
            last_file_path = setting.DATAPATH + last_file_name
            f = open(last_file_path, 'r')  # @attention
            data = json.load(f)
            f.close()
            memo_list = data['memo_list']
    for each in memo_list:  # if not understand, @see: test/listremove.py
        if each['finished']:
            memo_list.remove(each)

    # log.info("Leave read func!")
    return memo_list


def write(date, data):
    """

    :type date: QDate
    @note:
        当程序退出时，先调用这个函数
        保存当天的memo
        更新config文件

    @param data: 程序结束时保存的memo_list，json类型

    """
    # log.info("Enter write func!")
    file_name = date + '.json'
    file_path = setting.DATAPATH + file_name
    f = open(file_path, 'w')
    write_in_data = json.dumps(data)
    f.write(write_in_data)
    f.close()  # 写入今日的完成和未完成任务
    update_config_file(date)
    # log.info("Leave write func!")


if __name__ == "__main__":
    test_data = {
        'datetime': '2014-12-28',
        'memo_list': [
            {
                'id': '1',
                'title': 'homework',
                'start_time': '2012-12-28',
                'content': 'hello',
                'deadline': '2013-12-21',
                'finished': True
            }
        ],
    }
    date = '2014-12-28'
    read(date)
    write(date, test_data)
