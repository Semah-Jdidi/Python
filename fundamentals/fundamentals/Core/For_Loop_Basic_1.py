
#Basic - Print all integers from 0 to 150.
for i in range(0,151):
    print(i)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for y in range(5,1005,5):
    print (y)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(0,101):
    if (x % 10==0):
        print("Coding Dojo")
    elif (x % 5==0):
        print("Coding")
    else:
        print(x)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for count in range(0,500000,2):
    sum = sum + count
    
print(sum)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for num in range(2018,0,-4):
    print(num)