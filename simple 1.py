while True:
    print ('Tjenixen, välkommen till mitt feta spel om mig själv!')

    ans = input('Är du redo bish? (ja/nee): ')
    score = 0
    total_q = 5
    if ans.lower() == 'ja':
        ans = input('1. Vad har jag för ögonfärg?')
        if ans.lower() == 'blå':
           score += 1
           print ('RÄTT SVAR')
        else:
            print ('fel för fan')


        ans = input('2. Vilket är mitt favoritband')
        if ans.lower() == 'gunsnroses':
           score += 1
           print ('RÄTT SVAR')
        else:
            print ('fel för fan')

        ans = input('3. Vilket är mitt favoritämne i skolan')
        if ans.lower() == 'fysik':
           score += 1
           print ('RÄTT SVAR')
        else:
            print ('Men vad fan')


        ans = input('4. Vilket är min favorit spelserie?')
        if ans.lower()  == 'zelda':
           score += 1
           print ('RÄTT SVAR')
        else:
            print ('FEL JU!')

        ans = input('5. Vilket instrument kan jag förtom gitarr?')
        if ans.lower()  == 'bas':
           score += 1
           print ('rätt!')
        else:
            print ('Kunde du inte den?')

    print ('Du har spelat färdigt, du fick ', score, " questions correct.")
    mark = (score/total_q) * 100

    print ("Poäng: ", mark)
    print ('godkänt är 50%')
    print('Hare gött')

    ans = input('En gång till? (ja/nee): ')
    if ans.lower() == 'nee': break

