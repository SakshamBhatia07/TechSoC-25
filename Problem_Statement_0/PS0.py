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
    print(sin(a))
  elif(b=="cos"):
    print(cos(a))
  elif(b=="tan"):
    print(tan(a))


b = input("Enter the operator: ")
if(b=="+" or b=="-" or b=="/" or b=="*" or b=="**" or b=="^"):
  a = float(input("Enter 1st number: "))
  c = float(input("Enter 2nd number: "))
  Calculator(b,a,c)
elif(b=="sqrt" or b=="ln" or b=="log10" or b=="exp" or b=="sin" or b=="cos" or b=="tan"):
  a = float(input("Enter 1st number: "))
  Calculator(b,a)
