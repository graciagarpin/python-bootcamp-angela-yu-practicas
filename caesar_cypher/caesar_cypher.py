alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for text_letter in original_text:
        index_encoded_letter = alphabet.index(text_letter) + shift_amount
        index_encoded_letter %= len(alphabet)
        encrypted_text += alphabet[index_encoded_letter]
    return print(f"Here is the encoded result: {encrypted_text}")

def decrypt(original_text, shift_amount): # aa 2 --> yy
    decrypted_text = ""
    for text_letter in original_text:
        index_decoded_letter = alphabet.index(text_letter) - shift_amount
        index_decoded_letter %= len(alphabet)
        decrypted_text += alphabet[index_decoded_letter]
    return print(f"Here is the decoded result: {decrypted_text}")

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
# call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift

def caesar(cypher_direction, original_text, shift_amount):
    if cypher_direction == 'encode':
        encrypt(text, shift)
    elif cypher_direction == 'decode':
        decrypt(text, shift)
    else:
        print("Sorry, I cant understand you, please, type 'encode' to encrypt, or type 'decode' to decrypt")

caesar(direction, text, shift)
