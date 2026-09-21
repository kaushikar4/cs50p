def main():
    user_input = input("say something :")
    print(convert(user_input))

def convert(user_input):
    return user_input.replace(":)", "🙂").replace(":(", "🙁")


main()
