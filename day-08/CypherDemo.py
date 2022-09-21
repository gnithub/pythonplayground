alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(char, shift):
    print(f"Char is {char} with shift {shift}")
    if char == ' ':
        return char
    return alphabet[alphabet.index(char)+shift]


text=input("Input a text: ").lower()
shift=int(input("Input shift: "))

encrypted_text=""
for ch in text:
    encrypted_text += encode(ch, shift)

print(f"Encrypted word is {encrypted_text}")

