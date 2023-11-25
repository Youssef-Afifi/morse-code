
# dictionary english to morse code
dictionary = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# function that converts english to morse code
def eng_to_morse(eng_text):
    #initialize an empty string to store morse code
    morse_code = ''
    for char in eng_text:

    #add single space after every character and double space after word

        if char == ' ':
            morse_code += '  '
        else:
            # adding morse code to final result
            morse_code += dictionary[char.upper()] + '  '

    return morse_code


#function that translates morse to english
def morse_to_eng(morse_text):
    morse_text += " "
    decipher = ""
    citext = ""
    space_count = 0

    for char in morse_text:
        # checks for space
        if char != " ":
            space_count = 0
            # storing single character
            citext += char
        else:
            # if space == 1, new character. if space == 2, new word
            space_count += 1

            if space_count == 2:
                decipher += " "
            else:
                for key, value in dictionary.items():
                    if citext == value:
                        decipher += key

                citext = ""

    return decipher


    


#gives user choice of encryption or decryption
def run_function():
    lang = input("Encryption or decryption? (e/d): ").lower()

    #process user's choice
    if lang == "e":
        # if e is chosen, ask user for message and display the encrypted text
        message = input("Enter text to be encrypted: ")
        result = eng_to_morse(message.upper())
        print("Encrypted Message:", result)
    elif lang == "d":
        # if d is chosen, ask user for message and display the decrypted text
        message = input("Enter Morse code to be decrypted: ")
        result = morse_to_eng(message)
        print("Decrypted Message:", result)
    else:
        print("Invalid input. Please enter 'e' for encryption or 'd' for decryption.")

run_function()








      

      
      
      















 










            
    










