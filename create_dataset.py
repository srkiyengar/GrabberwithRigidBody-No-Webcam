__author__ = 'srkiyengar'

import random
import time
import logging


LOG_LEVEL = logging.DEBUG

MIN_RANDOM_NUMBER = 10000000
MAX_RANDOM_NUMBER = 99999999


# Set up a logger with output level set to debug; Add the handler to the logger
my_logger = logging.getLogger("My_Logger")


class dataset:

    def __init__(self):
        self.data_elements = []
        self.timestamp = time.localtime()
        my_logger.info("Dataset creating begun at " + time.strftime("%d-%b-%Y %H:%M:%S", time.localtime()))

    def append(self,new_data):
        self.data_elements.append(new_data)

    def insert_image_filename(self,imagefile):
        self.data_elements[-1]["webcam_image"]= imagefile

    def log_dataset(self):
        for i in self.data_elements:
            my_logger.info("No. {} - Creation Time: {} Object Identifier: {}".format(i,
                self.data_elements[i]["creation_time"],self.data_elements[i]["unique_object_number"]))


class data:

    def __init__(self,my_dataset):
        t = time.localtime()
        creation_time = time.strftime("%d-%b-%Y %H:%M:%S", time.localtime())
        unique_object_no = random.randrange(MIN_RANDOM_NUMBER,MAX_RANDOM_NUMBER)
        my_logger.info("Unique Number {} generated at "+creation_time.format(unique_object_no))
        self.param = {"unique_object_number": unique_object_no,"creation_time":creation_time}
        my_dataset.append(self.param)

