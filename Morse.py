from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QLineEdit


morse_dict = {'A':'.-', 'G':'--.', 'M':'--', 'S':'...', 'Y':'-.--', '4':'....-', '.':'.-.-.-',
              'B':'-...', 'H':'....', 'N':'-.', 'T':'-', 'Z':'--..', '5':'.....', ',':'--..--',
              'C':'-.-.', 'I':'..', 'O':'---', 'U':'--.', '0':'-----', '6':'-....', '-':'-....-',
              'D':'-..', 'J':'-...', 'P':'.--.', 'V':'---.', '1':'.----', '7':'--...', '/':'-..-.',
              'E':'.', 'K':'-.-', 'Q':'--.-', 'W':'.--', '2':'..---', '8':'---..', '?':'..--..',
              'F':'..-.', 'L':'.-..', 'R':'.-.', 'X':'-..-', '3':'...--', '9':'----.'}


def encrypt(message_to_encrypt):
    encrypted_message = ""
    # message_to_encrypt = windows.msg.text()
    for letter in message_to_encrypt:
        if letter.upper() in morse_dict:
            if letter != ' ':
                encrypted_message += morse_dict[letter.upper()] + ' '
            
        elif letter == ' ':
            encrypted_message += '   '

        elif letter not in morse_dict:
            encrypted_message += letter
            
        else :
            encrypted_message += ' '
            
    # windows.setText(encrypted_message)
    return encrypted_message


def play():
    message = windows.msg.text()
    result = encrypt(message)
    windows.res.setText(result)


app = QApplication([])
windows = loadUi('Morse.ui')
windows.show()
windows.translate.clicked.connect(play)
app.exec_()
