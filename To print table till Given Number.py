#To make a program to print Tables till the Input Number
#Taking input from the user
a=int(input('Enter the Number till which you want to find Tables'))
print('--'*50)
#Looping till the input number 
for i in range(2,a+1):
    print('Table of {} :'.format(i))
    print('--'*50)
    #Printing the table for i using loop
    for j in range(1,11):
        print('{} X {} = {}'.format(i,j,i*j))
    print('--'*50)
    