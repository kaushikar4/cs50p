def greet(input):
    if "hello" in input:
        return "hello,these user"
    else:
        return "not sure what you mean"

greeting = greet("whats up?")
print(greeting)

