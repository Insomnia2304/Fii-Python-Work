import sys, os

def error(msg):
    print(f'[ERROR] {msg}')

def error_handling_dir(dir_path):
    if not os.path.isdir(dir_path):
        error(f'{dir_path} is not a directory.')
        sys.exit(1)
    if not os.access(dir_path, os.R_OK):
        error(f'Access to {dir_path} is denied.')
        sys.exit(1)

def error_handling_args():
    if len(sys.argv) != 2:
        error(f'Usage: python {sys.argv[0]} <directory>')
        sys.exit(1)
    
    error_handling_dir(sys.argv[1])


error_handling_args()

ext = {}
for root, dirs, files in os.walk(sys.argv[1]):
    for dir in dirs:
        if not os.access(os.path.join(root, dir), os.R_OK):
            error(f'Access to {os.path.join(root, dir)} is denied')
    for file in files:
        tokens = file.split('.')
        if len(tokens) == 1:
            continue
        if tokens[-1] not in ext:
            ext[tokens[-1]] = 1
        else:
            ext[tokens[-1]] += 1

sorted_ext = dict(sorted(ext.items(), key=lambda item: item[1], reverse=True))
print(sorted_ext)
