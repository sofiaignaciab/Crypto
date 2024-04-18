import sys

def caesarCipher(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = ""

    for letter in text:
        if letter in alphabet:
            possition = alphabet.find(letter)
            new_position = (possition + shift) % len(alphabet)
            new_letter = alphabet[new_position]
            message += new_letter
        else:
            message += letter
    return message

if __name__ == "__main__":
    text = sys.argv[1]
    shift = int(sys.argv[2])

    message = caesarCipher(text, shift)

    print(f"{message}")
