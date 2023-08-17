# beginner Project: ToDo, HangMan => soz topish oyini

# https://www.fiverr.com/  => zakas olib ishlavchi sayt nomi

from random import choice
from colorama import Fore  # textni oziga rang berish uchun ushbu funksiya ishlatiladi
from os import system  # clear qlib keturadi

# doskaning holati: gorizantal, vertical, dioganal
# 0 1 2
# 3 4 5
# 6 7 8



def finished(arr):
    # gorizantal holatlar
    for i in range(0,7,3):  # 0 dan 6 gacha boradi 3 ta qadam bilan
        if arr[0] == arr[i+1] and arr[1] == arr[i+2]:
            return True
    # vertical holatlar
    for i in range(3):
        if arr[i] == arr[i+3] and arr[i] == arr[i+6]:
            return True
    # dioganal holatlar
    if arr[0] == arr[4] and arr[4] == arr[8]:
        return True
    if arr[2] == arr[4] and[4] == arr[6]:
        return True
    return False


def show(arr):
    system('cls') # 'systemclsearscreen' => toliq nomi cls ni
    # print("+---"*3+ '+')
    print(Fore.WHITE,end='')
    print(*"++++", sep='---') # 4ta plusni oldidagi yulduzcha ajratib chqarb un ishl.di
    for i in range(9):
        color = Fore.RED if 'X'==arr[i] else Fore.GREEN if arr[i]=='0' else Fore.YELLOW
        print('|', color + arr[i], end=' ')
        print(Fore.WHITE, end='')
        if i%3==2:
            print('|')
            print(*"++++", sep='---')



def start():
    var = list(map(str,range(1, 10))) # game board  - o'yin doskasi
    comp_board = list(range(9))  # 0 1 2 3 4 5 6 7 8 9
    for i in range(4): # 0,,1,2,3,4....
        show(var)
        place = int(input('Choose: '))-1
        # var[place] ='X0'[i%2] # => x > juft indexda, 0 esa toq indexdagi sonlar uchun yani i ni 2 ga bolganda qoldiq nolga teng bolsa => "X" qoldiq nolga teng bolmasa "0" sonlari bilan toldriladi
        var[place] = 'X'
        if finished(var):
            show(var)
            return 'Player'
        comp_board.remove(place)
        place2 = choice(comp_board) # 1
        var[place2] = '0'
        if finished(var):
            show(var)
            return 'Computer'
        comp_board.remove(place2)
    place = int(input('Choose: '))-1
    var[place] = 'X'
    show(var)
    if finished(var):
        return 'Player'
    return 'Draw'


if __name__ == "__main__":
    winner = start()
    print('Game Over: '+winner if winner=='Draw' else "The winner is " + winner)



# uyga vazifa: 

