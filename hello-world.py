while True:
     number = input("enter a positive number : ")   
     digits = len(number) # rakamlarin ussunu al
     summ = 0
     if not number.isdigit():
         print(number, "is an invalid entr. Do not use non-numeric, float or negative number. ")
     else:    

       for i in range(digits):
          summ += int(number[i]) ** digits
       if summ == int(number):
           print(number, "is an Armstrong number")
           break
       else:
           print(number, "is not an Armstrong number. ")        
           break 
