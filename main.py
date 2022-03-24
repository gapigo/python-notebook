import os

while True:
    exec_file = str(input('Digit the file name: '))
    if exec_file[-3:] != '.py':
        exec_file += '.py'
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        exec(open(f"./{exec_file}").read())
        print(f'\n\n\n{"="*50}\n{exec_file} execution finished.\n{"="*50}\n\n')
    except FileNotFoundError:
        print(f'File "{exec_file}" not found, try again.')


    
