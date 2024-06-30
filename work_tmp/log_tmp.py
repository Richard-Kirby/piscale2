#import logging
import logging.config
import log2

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('scaleLogger')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

log2.dum()