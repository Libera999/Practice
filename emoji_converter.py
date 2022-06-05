def emoji_converter(message):

    list_w = message.split(' ')
    emojis = {
        ":)": "😊",  # "\U0001F600",
        ":(": "😒",  # "\U0001F612",
        ":))": "😂"  # "\U0001F605"
    }
    new_message = ''
    for w in list_w:
        new_message += emojis.get(w, w)+' '
    return new_message


line = input('Input message using emoji >')
new_l = emoji_converter(line)
print(new_l)
