n = int(input()) #giving the integer input in which we want to divide the peices of cake!
if 360%n == 0:
    a1 = 'y' 
else:
    a1 = 'n' 
if n <=360:
    a2 = 'y'
else:
    a2 = 'n' 
if n <= 26:
    a3 = 'y'
else:
    a3 = 'n' 
print(a1,a2,a3)
