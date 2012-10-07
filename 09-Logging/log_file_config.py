import logging.config

logging.config.fileConfig('09-Logging/fileconfig.ini')

root = logging.getLogger()
mylogger = logging.getLogger('mylogger')

root.error('Info from root')
mylogger.error('Info from mylogger')
