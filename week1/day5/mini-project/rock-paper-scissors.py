from game import Game

if __name__ == "__main__":
    isplaying = True
    fun = Game()
    while isplaying:
        print('''
    Menu
      (g) play a new game
      (x) show score
      (q) to quit the game
''')
        choise = input(": ")
        if choise == 'g' :
            hand = int(input('choose (1) for rock (2) paper (3) for scissors : '))
            fun.play(hand)
        elif choise == 'x':
            print(f'games played {fun.history} games you won {fun.wins}, you lost {fun.losts} you drew {fun.draws}')
        elif choise == 'q':
            isplaying = False
            print("tanks for playing")
        else:
            print("wrong choise")
    