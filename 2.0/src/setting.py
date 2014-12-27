#-*- coding: utf8 -*-

# =============================================================================
#      FileName: setting.py
#          Desc: 设置全局变量
#        Author: ysw(zjuysw)
#         Email: yinshaowen241@gmail.com
#      HomePage: http://my.oschina.net/zjuysw
#       Version: 0.0.1
#    LastChange: 2014-12-27 21:24:55
#       History:
# =============================================================================

'''
这里主要设置了程序的共用的变量 \
如果以后一些资源文件路径发生变化，只需要改变这里的变量即可
'''

UBUNTU = False
WINDOWS = False

IMGPATH = '../img/'
DATAPATH = '../data/'

LEVEL = 0   # 0 for dev, 1 for INFO, 2 for release

CONFIGJSONFILE = DATAPATH + 'config.json'
LOGFILE = DATAPATH + 'error.log'
