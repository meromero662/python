# Anslagstavlans tre poster
POST_1 = ''
POST_2 = ''
POST_3 = ''

while True:
    # [ ] 1. Rensa terminalfönstret
    # Använd lämplig kommando för att rensa terminalfönstret
    import os
    os.system('cls')  # för Unix/Linux/Mac
    # os.system('cls')  # för Windows

    # [X] 2. Skriv ut instruktioner
    print('.: basicBILLBOARD :.')
    print('********************')
    print('P1:', POST_1)
    print('P2:', POST_2)
    print('P3:', POST_3)
    print('--------------------')
    print('c | Ändra post')
    print('e | Stäng program')
    print('--------------------')

    # [ ] 3. Hämta kommando från användaren
    command = input('meny > ')

    # [ ] 4. Utför operationer för inmatat kommando
    if command == 'c':
        post_number = input('Vilken post vill du ändra (P1, P2 eller P3)? ')
        if post_number in ['P1', 'P2', 'P3']:
            new_content = input(f'Ange nytt innehåll för {post_number}: ')
            if post_number == 'P1':
                POST_1 = new_content
            elif post_number == 'P2':
                POST_2 = new_content
            elif post_number == 'P3':
                POST_3 = new_content
        else:
            print('Ogiltig post!')

    elif command == 'e':
        print('Programmet stängs av.')
        break

    # [X] 5. Pausa exekvering
    input('Tryck enter för att fortsätta ...')
