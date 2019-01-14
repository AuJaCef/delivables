#Caesar cipher
#Austin Cefaratti 1/2/19
#does a Caesar cipher

def main():
    print("This program can encode and decode caesar ciphers")
    #recieve test from the user
    textStr = input("Enter a regular sentence: ").lower()
    Key = 0
    Key = eval(input("What do you want the key value to be?: "))
    x = ""
    for ch in textStr:
        #ch = ord(ch) + Key
        #ch = chr(ch)
        x = x + chr(ord(ch)+Key)
    print(x)
    give = x
    q = ""
    print("Returning original text")
    for bh in give:
        q = q + chr(ord(bh)-Key)
    print(q)
        
    
    
    




main()
