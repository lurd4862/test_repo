print('hello world from python')
import sys


args = sys.argv

with open('/test_folder/test_file_from_docker.txt', 'w') as f:
    f.write(f'haha hello this is arg 1: {args[1]}')