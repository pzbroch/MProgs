####################################
#                                  #
#    CONVERT BINARY TO DECIMAL     #
#                                  #
# (C) 2019-10-09 PRZEMYSLAW ZBROCH #
#                                  #
####################################

binchk = False
bincnt = 0

print()
print('This program converts any binary number to decimal')

while not binchk:
    print()
    print('Binary value: ', end = '')

    decimal = 0
    binstr = input()
    binpos = len(binstr)

    for x in binstr:
        binpos = binpos - 1
        if (x != '0') and (x != '1'):
            binchk = False
            bincnt = bincnt + 1
            if bincnt < 10:
                print('Only binary values are accepted!')
            else:
                print('Words, letters, dots, spaces and other characters that are not 1\'s or 0\'s ARE NOT ACCEPTED!')
                print('PLEASE ENTER A BINARY NUMBER!')
            break
        if x == '1':
            decimal = decimal + (2 ** binpos)
            binchk = True

print('Decimal value:', decimal)
