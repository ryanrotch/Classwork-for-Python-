# write a python netsed loop to print out
# all the prime numbers between 2-100

for number in range(2,100):
   
        for num in range(2,number):
             if(number%num)==0:

               break

        else:
              print(number)
