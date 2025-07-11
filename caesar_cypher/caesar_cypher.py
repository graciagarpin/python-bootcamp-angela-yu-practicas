from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ""
    if encode_or_decode == 'decode':
        shift_amount = shift_amount * -1
    for text_letter in original_text:
        if text_letter not in alphabet:
            output_text += text_letter
        else:
            shifted_position = alphabet.index(text_letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {output_text}")

# TODO-2: restart the cypher program

caesar(direction, text, shift)