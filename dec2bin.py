####################################
#                                  #
#    CONVERT DECIMAL TO BINARY     #
#                                  #
# (C) 2019-10-07 PRZEMYSLAW ZBROCH #
#                                  #
####################################

binary = ' '
decstr = ' '
strcnt = 0

print()
print('This program converts any decimal number to binary')

while not decstr.isdigit():
    print()
    print('Decimal value: ', end = '')

    decstr = input()

    if decstr == '':
        continue
    if not decstr.isdigit():
        strcnt = strcnt + 1
        if strcnt < 10:
            print('Only integer numbers can be converted!')
        else:
            print('Words, letters, dots, spaces and other characters that are not numbers ARE NOT ACCEPTED!')
            print('PLEASE ENTER AN INTEGER NUMBER!')

if strcnt > 9:
    print('Now we\'re talking!')

decimal = int(decstr)

while decimal > 0:
    if len(binary) % 5 == 0:
        binary = ' ' + binary

    binary = str(decimal % 2) + binary
    decimal = decimal // 2

binary = binary[0:-1]

print(' Binary value:', binary)
print()
