# Testing yield
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i
        print('a')

generator = create_generator()
for i in generator:
    print(i)

# Don't run because generator was emptyed 
for i in generator:
    print(i)