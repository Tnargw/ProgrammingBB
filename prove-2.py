

print('Please enter the following to create your own story:')

print('')

adjective = input('Adjective: ')
animal = input('Animal: ')
verb = input('Verb: ')
exclamation = input('Exclamation: ')
verb2 = input('Verb: ')
verb3 = input('Verb: ')
time = input('Unit of time: ')
verb4 = input('Verb: ')
celeb = input('Name of a Celebrity: ')
utensil = input('Kitchen utensil: ')

print('')

print('Your story is:')

print('')

print('The other day, I was really in trouble. It all started when I saw a very')
print(adjective , animal , verb  , 'down the hallway. "' + exclamation.capitalize() + '!" I yelled. But all')
print('I could think to do was to ' + verb2 + ' over and over. Miraculously,')
print('that caused it to stop, but not before it tried to ' + verb3)
print('right in front of my family.')
print('that was all I could remember when i woke up ' + time + ' later. my head ' + verb4 + ' as I tried to focus my eyes.' )
print('As my eyes finally focused i saw standing over me ' + celeb + ' holding a ' + utensil + ' menacingly')
print('It was then i realized the' + '\033[31m' + ' blood' + '\033[39m' + ' on my hands was not my own.')



print()

print('\033[39m') #to reset font color.