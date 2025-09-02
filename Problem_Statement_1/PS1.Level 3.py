#Made the level 3 without the bonus part to decode without keyword
l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
     "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
     "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
     "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
     "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
f = int(input("Enter 0 to encode a word or enter 1 to decode an encoded word: "))
match f:
    case 0:
        a = input("Enter the word to be encoded: ")
        b = input("Enter the word used to determine the shift: ")
        c = []
        d = ""
        e = 0
        for char in b:
            try:
                c.append(int(l.index(char) % 26))
            except:
                print("Some error occured")
        for char in a:
            try:
                d = d + l[l.index(char) + c[e % len(c)]]
                e = e + 1
            except:
                d = d + char

        import base64

        bytes1 = base64.b64encode(d.encode('utf-8'))
        output = bytes1.decode('utf-8')
        print(output)

    case 1:
        import base64

        word = input("Enter the word to be decoded: ")
        bytes1 = base64.b64decode(word.encode('utf-8'))
        a = bytes1.decode('utf-8')
        b = input("Enter the keyword used to code the word: ")

        c = []
        d = ""
        e = 0

        for char in b:
            try:
                c.append(int(l.index(char) % 26))
            except:
                print("Some error occured")
        for char in a:
            try:
                d = d + l[l.index(char) + (26 - c[e % len(c)])]
                e = e + 1
            except:
                d = d + char
        print(d)
