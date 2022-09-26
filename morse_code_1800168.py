# Coding Challenge 2
# Name: Jilliane Manansala
# Student No: 1800168

# A Morse code encoder/decoder

MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), 
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)

def print_intro():
    """Prints an introduction of the Morse Code encoder/decoder for the user"""
    print('Welcome to Wolmorse')
    print('This program encodes and decodes Morse code')


def get_input():
    """
    Prompts the user if they would like to encode or decode
        •Ensures user provides a valid response by utilising while loop
        •Uses if/else statements to return users input back to main to execute relevant function

    Keyword:
        response (str): User's response of whether they want to encode or decode
        encode_message (str): prompts user what message they would like to encode
        decode_message (str): prompts user what message they would like to decode

    Returns:
        variables: tuple consisting of keywords to use with relevant functions
    """
    response = input('Would you like to encode (e) or decode (d): ')
    while response != 'e' and response != 'd':
        response = input('Invalid Mode\nWould you like to encode (e) or decode (d): ')
    if response == 'e':
        encode_message = input('What message would you like to encode: ')
        return response, encode_message.upper()
    else:
        decode_message = input('What message would you like to decode: ')
        return response, decode_message.upper()


def encode(message):
    """
    Takes user's message and prints the message into morse code
        •Ensured message is capitalised to match the element in the MORSE_CODE tuple
        •Uses for loop to run through each individual letter in message
        •Use of .append() to add matching morse code to list
        •Uses enumerate to find both index and element whilst traversing through the tuple MORSE_CODE

    Parameters:
        message (str): Message in text format to encode into morse code
    """
    words = list(message.upper())
    sentence = []
    for x in words:
        if x == ' ':
            sentence.append(' ')
        else:
            for i, element in enumerate(MORSE_CODE):
                if element[1] == x:
                    sentence.append(element[0])
                else:
                    pass
    encoded_list = ' '.join(sentence)
    return encoded_list


def decode(message):
    """
    Takes user's morse code message and prints decoded message into text format
        •Use of variables to split message into list of words, then list of characters
        •Uses enumerate to find both index and element whilst traversing through the tuple MORSE_CODE
        •Much like encode() uses combination of list and append() in conjunction with join() to formulate sentences
    Parameters:
        message (str): Message in morse code format to decode into text

    Returns:
        formed_sentence (str): plain string value with decoded message
    """
    words = message.split('   ')  #sentence to words i.e. ['.... . .-.. .-.. ---','.-- --- .-. .-.. -..']
    sentence = []  # Use to list the words that were joined back together
    for word in words:
        characters = word.split(' ')  # splits to each character in words i.e. ['....','.','.-..','.-..','---']
        each_character = []  # when done completed word should go here as a list of each letter in word
        for x in characters:  # will look at each element i.e '....'
            for i, element in enumerate(MORSE_CODE):
                if element[0] == x:
                    each_character.append(element[1])
                else:
                    pass
        each_word = ''.join(each_character)
        sentence.append(each_word)
    formed_sentence = ' '.join(sentence)
    return formed_sentence

# ---------- Challenge Functions (Optional) ----------
def process_lines(filename, mode):
    """
    Opens filename traverses through each line in text file encoding/decoding and adding to list

    Parameters:
        filename (str): name of file to encode/decode
        mode (str): mode for what to do with file encode/decode

    Returns:
        lines (list): list with each element corresponding to new line in file
    """
    lines = []
    if mode == 'e':
        empty_str = ''
        input_file = open(filename, 'r')
        line = input_file.readline().strip('\n')
        while line != empty_str:
            lines.append(encode(line))
            line = input_file.readline().strip('\n')
        input_file.close()
    elif mode == 'd':
        empty_str = ''
        input_file = open(filename, 'r')
        line = input_file.readline().strip('\n')
        while line != empty_str:
            lines.append(decode(line))
            line = input_file.readline().strip('\n')
        input_file.close()
    return lines


def write_lines(lines):
    """
    Opens up new file results.txt to write lines placed in parameters
        •Utilises while loop to print each line in list inside lines

    Parameter:
        lines (list): Contains the list of each line encoded from morse code or decoded from it

    """
    with open('results.txt','w') as output_file:
        k = 0
        while k < len(lines):
            index = lines[k]
            output_file.write(index + '\n')
            k+=1


def check_file_exists(filename):
    """
    Checks if file called upon exist

    Parameter:
        filename (str): name of file

    Returns:
        True statement if filename is found
        False if filename cannot be found
    """
    try:
        input_file = open(filename, 'r')
        input_file.close()
        return True

    except IOError:
        return False


def get_filename_input():
    """
    Prompts and returns users preferred mode of encoding or decoding, and the source of mode: file or console
        •Uses an empty list that utilises append() method to add desired outputs
        •Use of separate if statements with append() as opposed to nested to avoid repetition and longer code

    Variables:
        returning (list): The values that will be use to return output
        mode (str): Mode desired by user 'e' = encode, 'd' = decode
        method (str): Source of text to encode or decode from filename(f) or in console(c)
        message (str): Message user would like to encode or decode in console

    Returns:
        returning (list): Returns the list that contains the mode, message and/or filename \
        as a tuple instead of list
    """
    returning = []
    mode = input('Would you like to encode (e) or decode (d): ')
    while mode not in ['e', 'd']:
        mode = input('Invalid Mode\nWould you like to encode (e) or decode (d): ')
    if mode == 'e':
        returning.append(mode)
    else:
        returning.append(mode)
    method = input('Would you like to read from a file (f) or the console (c): ')
    while method not in ['f', 'c']:
        method = input('Invalid response\nWould you like to read from a file (f) or the console (c): ')
    if method == 'f':
        filename = input('Enter a filename: ')
        while not check_file_exists(filename):
            print('Invalid Filename')
            filename = input('Enter a filename: ')
        returning.append(None)
        returning.append(filename)
    if mode == 'e' and not method == 'f':
        message = input('What message would you like to encode: ')
        returning.append(message.upper())
        returning.append(None)
    elif mode == 'd' and not method == 'f':
        message = input('What message would you like to decode: ')
        while message.isalpha() or message.isdigit() or message.isalnum() :
            print('Invalid input please use Morse Code')
            message = input('What message would you like to decode: ')
        returning.append(message.upper())
        returning.append(None)
    return tuple(returning)

"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encode (e) or decode (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encode/decode.
    • Encode/decode the message as appropriate and print the output.
    • Prompt the user whether they would like to encode/decode another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.

Hints:
    • Use the tuple MORSE_CODE above to convert between plain text/Morse code
    • You can make use of str.split() to generate a list of Morse words and characters
      by using the spaces between words and characters as a separator.
    • You will also find str.join() useful for constructing a string from a list of strings.
    • You should use a loop to keep the programming running if the user says that would like to
      encode/decode another message after the first.
    • Your program should handle both uppercase and lowercase inputs. You can make use of str.upper()
      and str.lower() to convert a message to that case.
    • Check the assessment specification for code examples.
"""
def main():
    """
    Main function that executes whole program
        •Contains call to functions
        •Contains another function to ensure that a loop is created so user has option to always code another message

    """
    def more_input():
        mode, message, filename = get_filename_input()
        if mode == 'e'and filename is None:
            print(encode(message))
        elif mode =='d' and filename is None:
            print(decode(message))
        elif mode == 'e':
            write_lines(process_lines(filename,'e'))
            print('Output written to results.txt')
        elif mode == 'd':
            write_lines(process_lines(filename,'d'))
            print('Output written to results.txt')
        response = input('Would you like to encode/decode another message? (y/n): ')
        while response != 'y' and response != 'n':
            response = input('Invalid response\nWould you like to encode/decode another message? (y/n): ')
        if response == 'y':
            more_input()
        else:
            print('Thanks for using the program, goodbye!')
    print_intro()
    more_input()

# Program execution begins here
if __name__ == '__main__':
    main()
