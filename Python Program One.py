Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #***************************************************************
#
#  Developer:         Renee White
#
#  Program #:         Program One
#
#  File Name:         Program1.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          9/9/19
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapters # 1-2
#
#  Description:
#     My First Program With Python
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():
    
    developerInfo()
    
    amount = 32500.00
    
    # Enter a statement here
    # Enter another statement here
    
    print('Annual Salary           = ', amount)
    print('When paid twice a month = ', twiceMonth)
    print('When paid bi-weekly     = ', biWeekly)
    
    # End of the main function 
    
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     <Put your full name here>')
    print('Course:   Programming Fundamentals I')
    print('Program:  One')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1
