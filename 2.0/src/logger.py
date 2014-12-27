#-*- coding:utf8 -*-

# =============================================================================
#      FileName: logger.py
#          Desc: log模块
#        Author: ysw(zjuysw)
#         Email: yinshaowen241@gmail.com
#      HomePage: http://my.oschina.net/zjuysw
#       Version: 0.0.1
#    LastChange: 2014-12-27 20:50:01
#       History:
# =============================================================================

'''
介绍：
    这个模块可以用来显示一些提示信息
    用这个模块来代替print
使用：
    其他程序可以导入该模块的log对象
'''

import logging

import setting

# 设置log的输出格式
# CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
if setting.LEVEL == 0:
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)s] [%(filename)s line:%(lineno)d] : %(message)s"
    )
elif setting.LEVEL == 1:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] [%(filename)s line:%(lineno)d] : %(message)s"
    )
else:   # 2
    logging.basicConfig(
        level=logging.WARNING,
        format="[%(levelname)s] [%(filename)s line:%(lineno)d] : %(message)s",
        filename=setting.LOGFILE,
        filemode='w'
    )

# 这个log对象给其他模块调用的
log = logging.getLogger("log")

if __name__ == "__main__":
    print u"这个是一个log模块"
    print __doc__
