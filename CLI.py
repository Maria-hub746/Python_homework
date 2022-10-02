

CONTACTS = {} #Key( Name ): Value( Phone )

def corrector(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except KeyError:
            print('This contact does not exist')
        except IndexError:
            print("Give me name and phone please")
    return wrapper

@corrector
def hello(argument):
    argument = input('How can I help you?: ')
    comand = argument.split(' ')[0]

    if comand not in INFORMATION:
        print('Wrong comand')
    INFORMATION[comand](argument)  

@corrector
def add(argument):
    name = argument.split(' ')[1]
    phone = argument.split(' ')[2]
    if name not in CONTACTS:
        CONTACTS[name] = phone
        print('New contact added')
    else:
        print('This contact already exists')

@corrector
def change(argument):
    name = argument.split(' ')[1]
    phone = argument.split(' ')[2]
    if name in CONTACTS:
        CONTACTS[name] = phone
        print('Contact changed')
    else:
        raise KeyError

@corrector
def find_phone(argument):
    name = argument.split(' ')[1]
    phone = f'{name} : +{CONTACTS[name]}'
    print(phone)


def show_all(argument):
    for keys in CONTACTS:
        show = f'{keys} : +{CONTACTS.get(keys)}'
        print(show)


def finish_work(argument):
    print('Good bye!')
    quit()


INFORMATION = {
    'hello' : hello,
    'add' : add,
    'change' : change,
    'phone' : find_phone,
    'show all' : show_all,
    "good bye" : finish_work,
    "close": finish_work,
    "exit": finish_work,
}

def main():
    while True:
        go = input('Enter your comand: ')
        go = go.lower()
        if go == 'show all' or go == 'good bye':
            comand1 = go.split(' ')[0]
            comand2 = go.split(' ')[1]
            comand = f'{comand1} {comand2}'
        else:
            comand = go.split(' ')[0]

        if comand not in INFORMATION:
            print('Wrong comand')
            continue
        INFORMATION[comand](go)  


main()