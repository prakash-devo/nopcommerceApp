import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="logs.log",
                            format='%(asctime)s : %(levelname)s : %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
