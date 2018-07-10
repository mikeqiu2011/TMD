import os
import time


def get_files(dir,size_above):
    """
    To get all files details under a given directory recursively
    :param dir: shall be a valid root path
    :param size_above: file with size above this threshold will be returned
    :return:
    """
    files = os.listdir(dir)
    for file in files:
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            size = round(os.path.getsize(path) / 1024)
            if size > size_above:
                type = file.split(".")[-1]
                access_timestamp = os.path.getatime(path)
                modify_timestamp = os.path.getmtime(path)
                now_timestamp = time.time()
                not_modified_for_days = round((now_timestamp - modify_timestamp) / 3600 / 24)
                not_accessed_for_days = round((now_timestamp - access_timestamp) / 3600 / 24)
                record = {"path": path, "type": type, "size_KB": size, "not_accessed_for_days": not_accessed_for_days,
                          "not_modified_for_days": not_modified_for_days}
                result.append(record)
        elif os.path.isdir(path):
            get_files(path,size_above)


# root = "/Users/mike/PycharmProjects/"
root = input("pls input valid root path\n")

result = []
get_files(root, 5)

for i in result:
    print(i)

print(len(result))
