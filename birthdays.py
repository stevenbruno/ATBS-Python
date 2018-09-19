birthdays = {'alice': 'Apr 1', 'bob': 'dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('no information exists for this name')
        print('what is their bday?')
        bday = input()
        birthdays[name] = bday
        print('bday database updated.')
