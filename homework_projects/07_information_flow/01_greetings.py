def main():
  name : str = input("What's your name? ")
  print(greet(name))

def greet(name):
    return "Hi Nice to meet you " + name + ".Have a great day !"
	
if __name__ == '__main__':
    main()