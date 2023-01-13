import math
def Log2(x):
  return (math.log10(x) /math.log10(2));
 
def isPowerOfTwo(N):
  return (math.ceil(Log2(test)) == math.floor(Log2(test)));
  
again = True
while again == True:
  flag = False
  flag1 = False
  maximum = 0
  minimum = 100000000
  meanfinder = 0
  currentITmax = 0
  meanITfinder = 0
  meanIThelper = 0
  pow2total = 0
  while flag == False:
    min = input("What will be your minimum value to test? ")
    max = input("What will be your maximum value to test? ")
    if max.isdigit() == False or min.isdigit()==False:
        print("One of your inputs is not an integer! Try again.")
        flag = False
    else:
      max = int(max)
      min = int(min)
      if min>max:
        print("Minimum is greater than maximum. This is not possible.")
        flag = False
      else:
        print("Parsing Data...")
        flag = True
        break
  
  for i in range(min,max):
    test = i
    iteration = 0
    meanIThelper=0
    pow2test = False
    while test != 1:
      if test % 2 == 1:
        test = test*3+1
        iteration = iteration+1
      else:
        test = test/2
        iteration = iteration+1
      if test>currentITmax:
        currentITmax = test
      if test>meanIThelper:
        meanIThelper=test
      if pow2test==False and isPowerOfTwo(test):
        pow2test=True
        pow2total=pow2total+1
        
      
    meanfinder=iteration+meanfinder
    if iteration>maximum:
      maximum = iteration
      maxnumber = i
    if iteration<minimum:
      minimum = iteration
      minnumber = i
    meanITfinder=meanIThelper+meanITfinder
  print("minimum amount of iterations before 1:")
  print(minnumber,"With",minimum,"iterations")