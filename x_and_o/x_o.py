def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end='')
        print()

def check_game_end(field):
    if check_win(field):
        return True

    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                return False
    return True

def check_win(field):
    if field[0][0] != '*' and field[0][0] == field[0][1] == field[0][2]:
        return True
    if field[1][0] != '*' and field[1][0] == field[1][1] == field[1][2]:
        return True
    if field[2][0] != '*' and field[2][0] == field[2][1] == field[2][2]:
        return True

    if field[0][0] != '*' and field[0][0] == field[1][0] == field[2][0]:
        return True
    if field[0][1] != '*' and field[0][1] == field[1][1] == field[2][1]:
        return True
    if field[0][2] != '*' and field[0][2] == field[1][2] == field[2][2]:
        return True

    if field[0][0] != '*' and field[0][0] == field[1][1] == field[2][2]:
        return True
    if field[0][2] != '*' and field[0][2] == field[1][1] == field[2][0]:
        return True

    return False


field = []
for i in range(3):
    field.append(['*'] * 3)

print_field(field)

current = 'x'

while not check_game_end(field):
    print ('ВВЕДИ СТРОКУ И СТОЛБЕЦ')
    print_field(field)
    row_number = int(input())
    column_number = int(input())

    field[row_number - 1][column_number - 1] = current

    if current == 'x':
        current = 'o'
    else:
        current = 'x'

print_field(field)

if current == 'x':
    print('выйграл нолик')
else:
    print('выйграл крестик')