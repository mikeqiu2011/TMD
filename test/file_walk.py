import os
import time


def get_file_details(dir, size_above):
    """
    Generator, To get all files details under a given directory recursively
    :param dir: shall be a valid root path
    :param size_above: file with size above this threshold will be returned
    :return: generator
    """
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            path = os.path.join(dirpath, filename)

            size = round(os.path.getsize(path) / 1024)
            if size > size_above:
                type = filename.split(".")[-1]
                access_timestamp = os.path.getatime(path)
                modify_timestamp = os.path.getmtime(path)
                now_timestamp = time.time()
                not_modified_for_days = round((now_timestamp - modify_timestamp) / 3600 / 24)
                not_accessed_for_days = round((now_timestamp - access_timestamp) / 3600 / 24)
                record = {"path": path, "type": type, "size_KB": size, "not_accessed_for_days": not_accessed_for_days,
                          "not_modified_for_days": not_modified_for_days}

                yield record

root = "/Users/mike/PycharmProjects"
size_above = 5

file_gen = get_file_details(root, size_above)

count=0 #count of all files
for i in file_gen:
    print(i)
    count += 1

print("*"*100)
print("total number of files is %d" % (count))
