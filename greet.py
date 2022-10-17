def greet(name):
    def hello():
        print(f'hello,{name}')
    return hello
    greet('vishal')   