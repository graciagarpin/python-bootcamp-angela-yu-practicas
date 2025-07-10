alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# PART 1: ENCODE
# TODO1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text, shift_amount):

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    encrypted_text = ""
    for text_letter in original_text:
        print(text_letter)
        for alphabet_letter in alphabet: # cogemos la letra "h" de la palabra "hi" y el shift = 1
            if text_letter == alphabet_letter:
                index_letter = alphabet.index(text_letter)
                # index = 7
                print(index_letter)
                index_encoded_letter = index_letter + shift_amount
                print(index_encoded_letter)
                print(alphabet[index_encoded_letter])
                encrypted_text += alphabet[index_encoded_letter]

    else:
        print("salida")

    return print(encrypted_text)
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text, shift)