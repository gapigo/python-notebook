import numpy as np
import copy

print('Write your linear system:')

def get_determinant(matrix):
    a = np.array(matrix)
    return np.linalg.det(a)

def set_default_vars():
    global exprs, coef_num, valid_coefs
    exprs = []
    coef_num = 0
    valid_coefs = []

def get_coefficients(expr):
    coefs = []
    for character in expr:
        if character.isalpha() and character not in coefs:
            coefs.append(character)
    return coefs

def unvalid_coefficients(expr, coefs):
    for character in expr: 
        if character.isalpha() and character not in coefs:
            return character
    return False

def has_repeated(coefs):
    for coef in coefs:
        if coefs.count(coef) > 1:
            return coef
    return False

def print_error(error):
    print(error)
    print('Digit all expressions again')
    print('----------------------')
    
def get_order_array(str_matrix):
    order_array = []
    for i in range(len(str_matrix)):
        if i == 0:
            for el in str_matrix[0]:
                for char in el:
                    if char.isalpha():
                        order_array.append(char)
    order_array.sort()
    return order_array

def organize_letters(str_matrix):
    
    for i in range(len(str_matrix)):
        for j in range(len(str_matrix[i])):
            str_matrix[i][j] = str_matrix[i][j].strip().replace(' ', '').replace(',', '.')
            
    order_array = get_order_array(str_matrix)
    
    for i, row in enumerate(str_matrix):
        new_row = ['' for i in order_array]  # get ['', '', ''...] excluding last term
        for j, el in enumerate(str_matrix[i]):
            if j != len(str_matrix[i]) - 1:
                correct_index = 0
                for k, sorted_el in enumerate(order_array):
                    if sorted_el in el:
                        correct_index = k
                        break
                new_row[correct_index] = str_matrix[i][j]
            else:
                new_row.append(str_matrix[i][j])
        str_matrix[i] = new_row
    return str_matrix

set_default_vars()
while True:
    expr = str(input('>> ')).strip().lower()
    coefficients = get_coefficients(expr)
    if has_repeated(coefficients):
        print_error('ERROR! Please agroup all coefficients.\nRight: 6a + b = 2\nWrong: 8a + b - 2a = 2')
    elif coef_num == 0:      
        coef_num = len(coefficients)
        exprs.append(expr)
        valid_coefs = coefficients
    elif coef_num < len(coefficients):
        print_error('ERROR! Insert the longest expression first, if it doesn\'t have all coefficients, put in the a + 0b + 3c = 5 form')
        
        set_default_vars()
    elif wrong_coef := unvalid_coefficients(expr, valid_coefs):
        print_error(f'ERROR! \'{wrong_coef}\' is not one of the expects coefficients detected in first line: {coefficients}')
        set_default_vars()
    else:
        exprs.append(expr)
        if len(exprs) == coef_num:
            break
str_matrix = []
for expr in exprs:
    initial_index = 0
    line = []
    for index, char in enumerate(expr):
        if char in '-+=':
            if expr[initial_index:index].strip() != "":
                line.append(expr[initial_index:index].strip())
                initial_index = index + 1 if char != '-' else index

        elif index == len(expr) - 1:
            if e := expr[initial_index:len(expr)]:
                line.append(e)
    str_matrix.append(line)


str_matrix = organize_letters(str_matrix)
num_matrix = []
ans_matrix = []

for i in range(len(str_matrix)):
    num_matrix.append([])
    for j in range(len(str_matrix[i])):
        str_num = ''
        for char in str_matrix[i][j]:
            str_num += str(char) if not char.isalpha() else ''
        if str_num == '':
            str_num = '1'
        elif str_num == '-':
            str_num = '-1'
        str_num = str_num.replace(' ', '')
        try:
            num_matrix[i].append(int(str_num))
        except ValueError:
            num_matrix[i].append(float(str_num).replace(',','.'))
    ans_matrix.append(num_matrix[i].pop(-1))

main_determinant = get_determinant(num_matrix)
determinants = []

for i in range(len(str_matrix)):
    aux_num_matrix = copy.deepcopy(num_matrix)
    for j in range(len(str_matrix)):
        aux_num_matrix[j][i] = ans_matrix[j]
    determinants.append(round(get_determinant(aux_num_matrix), 5))

for i, coef in enumerate(oa := get_order_array(str_matrix)):
    print(f'{coef} = {round(determinants[i]/main_determinant, 5)}', end=', ' if i != len(oa) - 1 else '')
