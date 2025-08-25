l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
percentage = {
    0:	8.2,  1:	1.5,  2:	2.8,  3:	4.3,  4:	12.7,  5:	2.2,  6:	2.0,  7:	6.1,  8:	7.0,  9:	0.15,  10:	0.77,  11:	4.0,  12:	2.4,  13:	6.7,  14:	7.5,  15:	1.9,  16:	0.095,  17:	6.0,  18:	6.3,  19: 9.1,  20: 2.8,  21: 0.98,  22:	2.4,  23:	0.15,  24:	2.0,  25:	0.074
}
code = input("Enter the word to be decoded: ")
a=1
c=(1000*len(code))
e=0
f = "Some error occurred"
while a<=26:
  l1=[]
  b=0
  d=""
  for char in code:
    try:
      d=d+l[l.index(char)+a]
    except:
      d=d+char
  for char in d:
    try:
      l1.append(int(l.index(char)%26))
    except:
      z=0

  for y in range(0,26,1):
    b=b+(abs(((l1.count(y)/len(l1))*100)-percentage[y]))
  if c>b:
    c = b
    f = d
    e = a
  a=a+1
print(f)
print("The word was shifted by: ",(26-e))