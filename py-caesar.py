alphebet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(plain_text,shift_amount,cipher_direction):
    new_text=""
    for letter in plain_text:
        if cipher_direction=="encode":
            new_text+=alphebet[alphebet.index(letter)+shift_amount]
        else:
            new_text+=alphebet[alphebet.index(letter)-shift_amount]
    print(f"{new_text}")
    




direction=input("type 'encode'to encrypt, type 'decode' to decrypt:\n")

text=input("type your message:\n").lower()
shift=int(input("Type the shift number:\n"))


caesar(plain_text=text,shift_amount=shift,cipher_direction=direction)
   
