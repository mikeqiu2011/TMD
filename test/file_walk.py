import os
import time
import csv
import logging
import socket
import sys

# set logger
logger = logging.getLogger()
logger.setLevel(logging.WARN)
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
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('file_details.ini')
root_dir = config.get(section='file', option='root_dir')
size_above = int(config.get(section='file', option='size_above'))
not_accessed_threshold = int(config.get(section='file', option='not_accessed_threshold'))
not_modified_threshold = int(config.get(section='file', option='not_modified_threshold'))

#get all OS mount points
import commands

mount = commands.getoutput('df -h')
lines = mount.split('\n')
logger.info(lines)
mount_points = map(lambda line: line.split()[-1], lines[1:])
mount_points.remove('/')
logger.info(mount_points)


def get_mount(path, mount_list):
    for mount_point in mount_list:
        if path.startswith(mount_point):
            return mount_point
    return '/'



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

                size = round(os.path.getsize(path) / 1024, 0)
                access_timestamp = os.path.getatime(path)
                modify_timestamp = os.path.getmtime(path)
                now_timestamp = time.time()
                not_modified_for_days = round((now_timestamp - modify_timestamp) / 3600 / 24)
                not_accessed_for_days = round((now_timestamp - access_timestamp) / 3600 / 24)

                if size > size_above and not_accessed_for_days > not_accessed_threshold and not_modified_for_days > not_modified_threshold:
                    type = filename.split(".")[-1]
                    mount_point = get_mount(path, mount_points)
                    record = {"type": type, "size_KB": size, "mount_point": mount_point,
                              "not_accessed_for_days": not_accessed_for_days,
                              "not_modified_for_days": not_modified_for_days, "path": path}
                    # logger.info(record)
                    yield record
            except Exception as e:
                logger.error(e)


file_detail_gen = get_file_details(root_dir, size_above)

#sort the list
import operator

# file_list = [file for file in file_detail_gen]
file_list = list(file_detail_gen)
file_list_sorted = sorted(file_list,
                          key=operator.itemgetter('size_KB', 'not_accessed_for_days', 'not_modified_for_days'),
                          reverse=True)

# write to a CSV file
with open(hostname + '_file_aging_profile.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)

    # write title for CSV
    writer.writerow(['mount_point', 'size_KB', 'not_modified_for_days', 'not_accessed_for_days', "Path", 'Type'])

    for file in file_list_sorted:
        # logger.info(file["type"],file["size_KB"],file["mount_point"],file["not_accessed_for_days"],file["not_modified_for_days"],file["path"])
        writer.writerow(file.values())
        # content = file["type"] + "," + str(file["size_KB"]) + "," + file["mount_point"] + "," + str(file["not_accessed_for_days"]) + "," + str(file["not_modified_for_days"]) + "," + file["path"]
        # writer.writerow(content)
