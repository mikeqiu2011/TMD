import os
import time
import csv
import logging
import socket
import sys

# set logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

# file handler
hostname = socket.gethostname()
file_handler = logging.FileHandler(hostname + ".log")
file_handler.setFormatter(formatter)

# console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# bind handler
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# read parameter file
import configparser

config = configparser.ConfigParser()
config.read('file_details.ini')
root_dir = config.get(section='file', option='root_dir')
size_above = int(config.get(section='file', option='size_above'))
not_accessed_threshold = int(config.get(section='file', option='not_accessed_threshold'))
not_modified_threshold = int(config.get(section='file', option='not_modified_threshold'))


def get_file_details(dir, size_above):
    """
    Generator, To get all files details under a given directory recursively
    :param dir: shall be a valid root_dir path
    :param size_above: file with size above this threshold will be returned
    :return: generator
    """
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            try:
                path = os.path.join(dirpath, filename)

                size = round(os.path.getsize(path) / 1024)
                access_timestamp = os.path.getatime(path)
                modify_timestamp = os.path.getmtime(path)
                now_timestamp = time.time()
                not_modified_for_days = round((now_timestamp - modify_timestamp) / 3600 / 24)
                not_accessed_for_days = round((now_timestamp - access_timestamp) / 3600 / 24)

                if size > size_above and not_accessed_for_days > not_accessed_threshold and not_modified_for_days > not_modified_threshold:
                    type = filename.split(".")[-1]

                    record = {"type": type, "size_KB": size, "not_accessed_for_days": not_accessed_for_days,
                              "not_modified_for_days": not_modified_for_days, "path": path}
                    logger.info(record)
                    yield record
            except Exception as e:
                logger.error(e)




file_detail_gen = get_file_details(root_dir, size_above)

import operator
file_list = [file for file in file_detail_gen]
file_list_sorted = sorted(file_list, key=operator.itemgetter('size_KB','not_accessed_for_days','not_modified_for_days'),reverse=True)

# write to a CSV file
with open(hostname + '_file_usage_report.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)

    # write title for CSV
    writer.writerow(['Type', 'size_KB', 'not_accessed_for_days', 'not_modified_for_days', "Path"])

    for file in file_list_sorted:
        writer.writerow(file.values())
