import sys, os

def error(msg):
    print(f'[ERROR] {msg}')


if len(sys.argv) != 3:
    error(f'Usage: python {sys.argv[0]} <directory> <file_extension>')
    sys.exit(1)

try:
    if not os.path.isdir(sys.argv[1]):
        raise NotADirectoryError(f'{sys.argv[1]} is not a directory')
    if not os.access(sys.argv[1], os.R_OK):
        raise PermissionError(f'Access to {sys.argv[1]} is denied')
    if not sys.argv[2].startswith('.'):
        raise ValueError('File extension must start with a dot')
    
    for root, dirs, files in os.walk(sys.argv[1]):
        for dir in dirs:
            if not os.access(os.path.join(root, dir), os.R_OK):
                error(f'Access to {os.path.join(root, dir)} is denied')
        for file in files:
            if file.endswith(sys.argv[2]):
                try:
                    with open(os.path.join(root, file)) as f:
                        print(f'{os.path.join(root, file)}: {f.read()}')
                except:
                    error(f'Cannot read {os.path.join(root, file)}')
except Exception as e:
    error(e)
    