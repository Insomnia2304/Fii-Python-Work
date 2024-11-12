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

cnt = 1
for file in os.listdir(sys.argv[1]):
    old_file_path = os.path.join(sys.argv[1], file)

    tokens = file.split('.')
    tokens[0] = f'{tokens[0]}{cnt}'
    new_file_path = os.path.join(sys.argv[1], '.'.join(tokens))

    if not os.path.isfile(old_file_path):
        continue
    try:
        os.rename(old_file_path, new_file_path)
        cnt += 1
    except Exception as e:
        error(e)
        