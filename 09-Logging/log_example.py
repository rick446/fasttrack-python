import logging.config

logging.basicConfig(
    level=logging.INFO,
    format='%(pathname)s:%(lineno)s %(levelname)s %(levelname)-8s %(name)-15s %(message)s'
    )
log = logging.getLogger()
log.info('Log here')

log.info("And here")
