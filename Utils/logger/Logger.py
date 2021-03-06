import os
import time
import logging
import inspect

"""
python:能自动记录时间，动作发生的所在文件和行数的日志类

每天产生一个新文件 2018-05-18.log

"""

class Logger(object):
    def timeNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def dateNow(self):
        return time.strftime('%Y-%m-%d', time.localtime())

    # 定义 日志输出路径,默认保存到当前路径,也可以传入参数 手动指定

    def __init__(self, loggerPath='/'):
        self.__logger = logging.getLogger()
        if loggerPath != '/':
            path = loggerPath + "/" + self.dateNow() + ".log"
        else:
            path = os.path.abspath(self.dateNow() + ".log")
        handler = logging.FileHandler(path)
        self.__logger.addHandler(handler)
        self.__logger.setLevel(logging.NOTSET)

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]
        # 打印到控制台
        print("[%s] [%s] [%s - %s - %s] %s" % (self.timeNow(), level, filename, lineNo, functionName, message))
        '''日志格式：[时间] [类型] [记录代码] 信息'''
        return "[%s] [%s] [%s - %s - %s] %s" % (self.timeNow(), level, filename, lineNo, functionName, message)

    def info(self, message):
        message = self.getLogMessage("info", message)
        self.__logger.info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)
        self.__logger.error(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)
        self.__logger.warning(message)

    def debug(self, message):
        message = self.getLogMessage("debug", message)
        self.__logger.debug(message)

    def critical(self, message):
        message = self.getLogMessage("critical", message)
        self.__logger.critical(message)


if __name__ == "__main__":
    loggerPath = 'D:\WorkSpace\PycharmProjects\TensorFlow\MachineLearninginAction'
    logger = Logger(loggerPath)
    logger.info("hello")

