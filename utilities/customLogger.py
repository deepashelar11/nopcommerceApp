import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename='.\\Logs\\automation.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        return logger
