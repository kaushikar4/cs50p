emoticon = "v.v"

def main():
    global emoticon
    say("is any one there?")
    emoticon = ":D"
    say("oh! hi there!")

def say(phrase):
    print(phrase +" "+ emoticon)

main()