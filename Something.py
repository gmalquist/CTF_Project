print("Hi! Welcome to this program.")
why = input("Why are you here?")
if why == 'secrets':
    with open('./Others.txt', 'r') as file:
        print(file.read())
    with open('./Secrets.txt', 'r') as file:
        hi = file.readlines()
        for line in hi:
            print(line)
else:
    print('Not good enough.')