import logging
import inspect


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # filehandler object

        logger.setLevel(logging.INFO)
        logger.debug("A debug statement is executed")
        logger.info("Information statement")
        logger.warning("Something is in warning mode")
        logger.error("A major error has happened")
        logger.critical("Critical issue")
        return logger
