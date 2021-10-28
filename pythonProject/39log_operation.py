import logging

# 改变默认级别
# logging.basicConfig(level=logging.DEBUG)
# 输出到文件中，并指定输出格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# 指定时间格式
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
logging.basicConfig(filename="my.log", level=logging.DEBUG,
                    format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
