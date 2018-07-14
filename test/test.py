# import socket
#
# print(socket.gethostname())

import configparser
config = configparser.ConfigParser()
config.read('file_details.ini')
print(config.get(section='file', option='root_dir'))