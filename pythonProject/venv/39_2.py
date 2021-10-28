import logging

# 改变默认级别
# logging.basicConfig(level=logging.DEBUG)
# 输出到文件中，并指定输出格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# 指定时间格式
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
# 获取日志对象
logger = logging.getLogger()
logger.setLevel("DEBUG")
# 文件处理器，输出到文件，日志名一般取工程名
file_handler = logging.FileHandler("39.log", mode="a", encoding="UTF-8")
# 流处理器，控制输出到控制台
steam_handler = logging.StreamHandler()
# 错误日志单独输出到一个文件中
error_handler = logging.FileHandler("error.log", mode="a", encoding="UTF-8")
# 每个handler可以自由支配输出的级别
error_handler.setLevel(logging.ERROR)
# 将所有的处理器添加到logger中
logger.addHandler(file_handler)
logger.addHandler(steam_handler)
logger.addHandler(error_handler)
# 格式化
formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
# 设置格式化器，需要针对每一个处理器分别设置
file_handler.setFormatter(formatter)
steam_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# 过滤器，过滤出想看到的日志，需要在打印之前进行设置
my_filter = logging.Filter("hhh")
file_filter = logging.Filter("这是")
file_filter_log = file_handler.addFilter(my_filter)
logging.info("日志打印hhh")
logging.error("这是一个错误日志")
print(file_filter_log)
