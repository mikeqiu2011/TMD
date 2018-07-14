# import socket
#
# print(socket.gethostname())

# import configparser
# config = configparser.ConfigParser()
# config.read('file_details.ini')
# print(config.get(section='file', option='root_dir'))

# nlist = [i for i in range(11) if i%2 != 0]
# print(nlist)

# ndict = {x:x*2 for x in range(10)}
# print(ndict)
# import operator
# x = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
# sorted_x = sorted(x, key=operator.itemgetter('age'), reverse=True)
# print(sorted_x)

import commands
mount = commands.getoutput('df -h')
lines = mount.split('\n')
print(lines)
points = map(lambda line: line.split()[-1], lines[1:])
# print(type(points))
print(points)
points.remove('/')
print(points)

path = '/'

def get_mount(path, mount_list):
    for mount_point in mount_list:
        if path.startswith(mount_point):
            return mount_point
    return '/'

mp = get_mount(path, points)
print(mp)