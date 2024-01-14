import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%s %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


#####+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# # Utilities/customLogger.py
#
# import logging
# import os
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         log_folder = os.path.join(os.path.dirname(__file__), '..', 'Configuration', 'Logs')
#         if not os.path.exists(log_folder):
#             os.makedirs(log_folder)
#
#         log_file = os.path.join(log_folder, "automation.log")
#
#         logging.basicConfig(filename=log_file,
#                             format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%m/%d/%Y %I:%M:%S %p')
#
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger
#
#
#
