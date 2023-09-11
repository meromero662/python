# Anslagstavlans tre poster
POST_1 = ''
POST_2 = ''
POST_3 = ''

while True:
    # Rensa terminalfönstret genom att skriva ut många tomma rader
    print("\n" * 100)

    # Skriv ut instruktioner
    print('.: basicBILLBOARD :.')
    print('********************')
    print('P1:', POST_1)
    print('P2:', POST_2)
    print('P3:', POST_3)
    print('--------------------')
    print('c | Ändra post')
    print('e | Stäng program')
    print('--------------------')

    # Hämta kommando från användaren
    choice = input('meny > ')

    # Utför operationer för inmatat kommando
    if choice == 'c':
        post_num = input('Vilken post vill du ändra (P1, P2, P3)? ')
        if post_num == 'P1':
            POST_1 = input('Skriv in den nya texten för P1: ')
        elif post_num == 'P2':
            POST_2 = input('Skriv in den nya texten för P2: ')
        elif post_num == 'P3':
            POST_3 = input('Skriv in den nya texten för P3: ')
        else:
            print('Ogiltig post!')
    elif choice == 'e':
        print('Programmet avslutas.')
        break
    else:
        print('Ogiltigt kommando!')

    # Pausa exekvering och vänta på användarens bekräftelse innan nästa iteration
    input('Tryck enter för att fortsätta ... ')
