#coding=utf-8
import logging
import logging.config
def log_test():
	CONF_LOG = "./logConfig.conf"
	logging.config.fileConfig(CONF_LOG)
	logger = logging.getLogger('wmr')
	logger.debug('hello world')

	logger = logging.getLogger()
	while True:
		logger.info('Hello World!')

if __name__ == '__main__':log_test()
