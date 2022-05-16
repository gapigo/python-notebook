import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def execute_file(exec_file):
    try:
        exec(open(f"./{exec_file}").read())
        print(f'\n\n\n{"="*50}\n{exec_file} execution finished.\n{"="*50}\n\n')
    except FileNotFoundError:
        cwd = os.getcwd()
        result = find_all(exec_file, cwd)
        if len(result) == 0:
            print(f'File "{exec_file}" not found, try again.')
            print(f'\n\n\n{"="*50}\n{exec_file} execution finished.\n{"="*50}\n\n')
        else:
            exec(open(result[0]).read())


while True:
    exec_file = str(input('Digit the file name: '))
    if exec_file[-3:] != '.py' and exec_file != '':
        exec_file += '.py'
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    if exec_file != '':
        execute_file(exec_file)
