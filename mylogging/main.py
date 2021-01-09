import helper
import logging

FORMAT = '%(asctime)-15s %(name)s %(levelname)-8s %(message)s'
logging.basicConfig(
    level=logging.DEBUG,
    format=FORMAT,
    datefmt='%m/%d/%Y %H:%M%S'
)
