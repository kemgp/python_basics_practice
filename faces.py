def main():
    message = input()
    print(emoji_converter(message))
 
 #Convert emoji   
def emoji_converter(text_emoji):
    smile_text = ":)"
    sad_text = ":("
    smile_emoji = "😊"
    sad_emoji = "😞"

    conv_emoji = text_emoji
    conv_emoji = conv_emoji.replace(smile_text, smile_emoji)
    conv_emoji = conv_emoji.replace(sad_text, sad_emoji)
    return conv_emoji

main()