def encode(text,shift):
    
    encode=""
    for i in text:
        encode+=chr(ord(i)+shift)
    return encode
def decode(text,shift):
    decode=""
    for i in text:
        decode+=chr(ord(i)-shift)
    return decode
while True:
    print(" 1 Encode \n 2 Decode \n 3 Exit")
    ch=int(input())
    if(ch==1):    
        text=input("Enter the Text")
        shift=int(input("Enter the shift Key"))
        print(encode(text,shift))
    if(ch==2):    
        text=input("Enter the Text")
        shift=int(input("Enter the shift Key"))
        print(decode(text,shift))
    if(ch==3):
        break

    