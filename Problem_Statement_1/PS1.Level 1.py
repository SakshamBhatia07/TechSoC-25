l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# Shift of 3 has been considered for this code
b = input("Enter the word to be coded: ")
c=int(input("Enter 0 to code your word or 1 to decode your code: "))
match c:
  case 0:
    for char in b:
      try:
        print(l[l.index(char)+3],end="")
      except:
        print(char,end="")
  case 1:
    for char in b:
      try:
        print(l[l.index(char)+23],end="")
      except:
        print(char,end="")