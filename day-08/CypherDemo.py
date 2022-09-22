alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(char, shift):
    print(f"Char is {char} with shift {shift}")
    if char == ' ':
        return char
    return alphabet[alphabet.index(char)+shift]

def decode(char, shift):
    print(f"Char is {char} with shift {shift}")
    if char == ' ':
        return char
    return alphabet[alphabet.index(char)-shift]


text=input("Input a text: ").lower()
shift=int(input("Input shift: "))
direction=input("Direction : ")

final_text=""
if direction == "encode":
    for ch in text:
        final_text += encode(ch, shift)
elif direction == "decode":
    for ch in text:
        final_text += decode(ch, shift)

print(f"Final word is {final_text}")

