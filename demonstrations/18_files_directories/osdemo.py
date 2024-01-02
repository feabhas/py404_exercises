import os
import glob
from datetime import datetime

print(os.path.exists('pathex.py'))

dir = '../..'
file = os.path.join(dir, 'demonstrations', 'ch20_os')
print(file)

dir = '..'
for name in os.listdir(dir):
    path = os.path.join(dir, name)
    print('{:20s}{:8d} {:%d-%b-%Y %H:%M}'.format(
          name +('/' if os.path.isdir(path) else ''),
          os.path.getsize(path),
          datetime.fromtimestamp(os.path.getmtime(path))))

print(os.path.expanduser('~/course-material'))

print(os.path.expandvars('$HOME/course-material'))
print(os.path.expandvars('$HOMEPATH'))

pathname = '/home/feabhas/pathex.py'
dir, filename = os.path.split(pathname)
name, ext = os.path.splitext(filename)
print(dir, filename, name, ext)

print(glob.glob('*.py'))
for path in glob.iglob('*.py'):
    print(path)

for filename in glob.iglob('../**/*.py', recursive=True):
    print(filename)

stats = os.stat('pathdemo.py')
print(stats)

print(stats.st_size)
print(datetime.fromtimestamp(stats.st_mtime))

print(os.path.getsize('pathdemo.py'))
print(datetime.fromtimestamp(os.path.getmtime('pathdemo.py')))
