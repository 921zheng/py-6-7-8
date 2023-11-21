alphebet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(plain_text,shift_amount,cipher_direction):
    new_text=""
    for char in plain_text:
        if char in alphebet:
          if cipher_direction=="encode":
            new_text+=alphebet[alphebet.index(char)+shift_amount]
          else:
             new_text+=alphebet[alphebet.index(char)-shift_amount] 
        else:
            new_text+=char
    print(f"{new_text}")
    

should_continue=True

while should_continue:

    direction=input("type 'encode'to encrypt, type 'decode' to decrypt:\n")

    text=input("type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))

    shift=shift%26


    caesar(plain_text=text,shift_amount=shift,cipher_direction=direction)
     
    result=input("continue or not? 'y' or 'n'")
    if result=="n":
        should_continue =False
        print("Goodbye")
  
