import sys
#Fucntions :
# File I/O fuctions
def add_credit() :
    c1 = open("credit_file.txt", "a")
    value = input()
    c1.write('%d \n' %value)
    c1.close()
def view_credit() :
    v1 =  open("credit_file.txt", "r")
    for money in v1 :
        print money
#Credit Function
def credit() :
    print 'Choose an option :'
    print '1. Add to a new file'
    print '2. Add to previous file'
    print '3. Exit'
    credit_input = input()
    if (credit_input == 1) :
        #print 'Open a new file here'
        add_credit()
    elif (credit_input == 2) :
        print 'Open a previous file with append mode'
    elif (credit_input == 3) :
        sys.exit()
    else :
        print 'Invalid Input!!'

#Debit Functions
def add_debit() :
    c1 = open("debit_file.txt", "a")
    value = input()
    c1.write('%d \n' %value)
    c1.close()
def view_debit() :
    v1 =  open("debit_file.txt", "r")
    for money in v1 :
        print money
def debit() :
    print 'Choose an option :'
    print '1. Add to a new file'
    print '2. Add to previous file'
    print '3. Exit'
    debit_input = input()
    if (debit_input == 1) :
        add_debit()
    elif (debit_input == 2) :
        view_debit()
    elif (debit_input == 3) :
        sys.exit()
    else :
        print 'Invalid Input!!'

#Modify Function
def modify_c() :
    print 'Choose an option'
    print '1. View Previous Records'
    print '2. Delete a record file'
    print '3. Exit'

    modify_input =  input()
    if (modify_input == 1) :
        view_credit()
    elif (modify_input == 2) :
        print 'Deleted a file'
    elif (modify_input == 3) :
        sys.exit()
    else :
        print 'Invalid Input!!'

def modify_d() :
    print 'Choose an option'
    print '1. View Previous Records'
    print '2. Delete a record file'
    print '3. Exit'

    modify_input =  input()
    if (modify_input == 1) :
        view_debit()
    elif (modify_input == 2) :
        print 'Deleted a file'
    elif (modify_input == 3) :
        sys.exit()
    else :
        print 'Invalid Input!!

#Main Function Starts Here!!...

print 'Welcome to Expense Records Manager'
print 'Choose an option :'
print '1. Credit'
print '2. Debit'
print '3. View/Modify prev. Credit records'
print '4. View/Modify prev. Debit records'
print '5. Exit application'

user_input = input()
print 'Option Selected = %d' %user_input

if (user_input == 1) :
    credit()
    #print 'Credit Function called'
elif (user_input == 2) :
    debit()
    #print 'Debit Function called'
elif (user_input == 3) :
    modify_c()
    #print 'Modify Function called'
elif (user_input == 4) :
    modify_d()
elif (user_input == 5) :
    sys.exit()
else :
    print 'Invalid Input!!'
