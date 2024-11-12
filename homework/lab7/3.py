import sys, os

def error(msg):
    print(f'[ERROR] {msg}')


if len(sys.argv) != 2:
    error(f'Usage: python {sys.argv[0]} <directory>')
    sys.exit(1)

total_size = 0 # bytes
try:
    if not os.path.isdir(sys.argv[1]):
        raise NotADirectoryError(f'{sys.argv[1]} is not a directory')
    if not os.access(sys.argv[1], os.R_OK):
        raise PermissionError(f'Access to {sys.argv[1]} is denied')
    
    for root, dirs, files in os.walk(sys.argv[1]):
        for dir in dirs:
            if not os.access(os.path.join(root, dir), os.R_OK):
                error(f'Access to {os.path.join(root, dir)} is denied')
        for file in files:
            try:
                total_size += os.path.getsize(os.path.join(root, file))
            except:
                error(f'Cannot access {os.path.join(root, file)}')
except Exception as e:
    error(e)

print(f'Total size of {sys.argv[1]} is {total_size} bytes')
    