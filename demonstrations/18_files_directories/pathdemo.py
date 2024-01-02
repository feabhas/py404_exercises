from pathlib import Path
from datetime import datetime

print(Path('pathex.py').exists())

dir = Path('../..')
file = dir.joinpath('demonstrations', 'ch20_os')
print(file)
file = dir / 'demonstrations' / 'ch20_os'
print(file)

for pathname in Path('..').iterdir():
    print('{}{}'.format(pathname, '/' if pathname.is_dir() else ''))
    stats = pathname.stat()
    print('{:20s}{:8d} {:%d-%b-%Y %H:%M}'.format(
        pathname.name + ('/' if pathname.is_dir() else ''),
        stats.st_size,
        datetime.fromtimestamp(stats.st_mtime)))

print(Path('~/course-material').expanduser())
print(Path.home() / 'course-material')

pathname = Path('/home/feabhas/pathex.py')
dir = pathname.parent
filename = pathname.name
name = pathname.stem
ext = pathname.suffix
print(dir, filename, name, ext)

for pathname in Path('.').glob('*.py'):
    print(pathname)

for filename in Path('..').glob('**/*.py'):
    print(filename)

stats = Path('pathdemo.py').stat()
print(stats)

print(stats.st_size)
print(datetime.fromtimestamp(stats.st_mtime))

print('Name           Lines Bytes')
for path in sorted(Path('.').iterdir()):
    if path.is_file():
        with path.open(mode='r') as fp:
            print('{:15s} {:4d} {:5d}'.format(
                str(path), len(fp.readlines()), path.stat().st_size))
