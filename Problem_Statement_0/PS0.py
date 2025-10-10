def factorial(n):
  if( n == 0):
      return 1
  elif(n>0):
      return n * factorial(n-1)
def sin(a):
  z=0
  y=0
  while(z<=10):
    x=(((-1)**z)*(a**(2*z+1)))/factorial(2*z+1)
    y=y+x
    z=z+1
  print(y)

def cos(a):
  z=0
  y=0
  while(z<=10):
    x=(((-1)**(z))*(a**(2*z)))/factorial(2*z)
    y=y+x
    z=z+1
  print(y)

def Calculator(*num):
  if(b=="+"):
    print(a+c)
  elif(b=="-"):
    print(a-c)
  elif(b=="*"):
    print(a*c)
  elif(b=="/"):
    print(a/c)
  elif(b=="^" or b=="**"):
    print(a**c)
  elif(b=="sqrt"):
    print(a**(1/2))
  elif(b=="ln"):
    d=0.000000
    while(2.7182818284590**d<=a):
      d=d+0.000001
    print(d)
  elif(b=="log10"):
    d=0.000000
    while(10**d<=a):
      d=d+0.000001
    print(d)
  elif(b=="exp"):
    print(2.7182818284590**a)
  elif(b=="sin"):
    sin(a)
  elif(b=="cos"):
    cos(a)

b = str(input("Enter the operator: "))
if(b=="+" or b=="-" or b=="/" or b=="*" or b=="**" or b=="^"):
    a = float(input("Enter 1st number: "))
    c = float(input("Enter 2nd number: "))
    Calculator(b,a,c)
elif(b=="sqrt" or b=="ln" or b=="log10" or b=="exp" or b=="sin" or b=="cos"):
    a = float(input("Enter the number: "))
    Calculator(b,a)
else:
    print("Invalid Input!, enter a valid operator")