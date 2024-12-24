import emoji

def main():
    input_str = input("Input: ")
    
    emojis_output = emoji.emojize(input_str,language="alias")
    
    print(f"output: {emojis_output}")
    
main()    