# -*- coding: utf-8 -*-
import random
def quiz():
    print ('Welcome to the cool quiz')
    qlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    money = 0
    wrong = False
    while (wrong == False and len(qlist)!=0):
        q1 = ('What is the fastest car in the world?')
        q2 = ('How dense is Jupiters largest moon?')
        q3 = ('Which of these is not a real war?')
        q4 = ('Which country did the cappuccino originate from?')
        q5 = ('Which English king signed the Magna Carta?')
        q6 = ('Who was the first NHL player to be drafted from Slovenia?')
        q7 = ('On what island was Jurrasic Park located?')
        q8 = ('In what century was the original Star Trek set?')
        q9 = ("Who was John McCain's ruuning mate in the 2008 election?")
        q10 = ('What is the fourth tallest building east of the Mississippi?')
        q11 = ('What was John F. Kennedys middle name?')
        q12 = ('What is the name of the largest known star?')
        q13 = ('What queen was the last ruler of Hawaii before the U.S. annexation?')
        q14 = ('What is the meaning of life?')
        q15 = ('What is the average mass of a pulsar?')
        question = random.choice(qlist)
        if question == 1:
            qlist.remove(1)
            print q1
            print ('A: Bugatti Veyron')
            print ('B: Lamborghini Aventador')
            print ('C: Koenigsegg Agara R')
            print ('D: Pagani Huayra')
            guess = raw_input('Answer?: ')
            if guess == 'c' or guess == 'C':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 2:
            qlist.remove(2)
            print q2
            print ('A: 2.24g/cubic cm')
            print ('B: 6.32g/cubic cm')
            print ('C: 1.94g/cubic cm')
            print ('D: 2.67g/cubic cm')
            guess = raw_input('Answer?: ')
            if guess == 'c' or guess == 'C':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 3:
            qlist.remove(3)
            print q3
            print ('A: Indo-Pakistan war')
            print ('B: The Pig war')
            print ('C: The Toledo war')
            print ('D: The niger-chad conflic')
            guess = raw_input('Answer?: ')
            if guess == 'd' or guess == 'D':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 4:
            qlist.remove(4)
            print q4
            print ('A: Italy')
            print ('B: France')
            print ('C: Germany')
            print ('D: Switzerland')
            guess = raw_input('Answer?: ')
            if guess == 'a' or guess == 'A':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 5:
            qlist.remove(5)
            print q5
            print ('A: Henry VIII')
            print ('B: John')
            print ('C: Henry VI')
            print ('D: Henry VII')
            guess = raw_input('Answer?: ')
            if guess == 'b' or guess == 'B':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 6:
            qlist.remove(6)
            print q6
            print ('A: Wayne Gretsky')
            print ('B: Anze Kopitar')
            print ('C: Leonard Niche')
            print ('D: Connor McDavid')
            guess = raw_input('Answer?: ')
            if guess == 'b' or guess == 'B':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 7:
            qlist.remove(7)
            print q7
            print ('A: Maui')
            print ('B: Tahiti')
            print ('C: Isla Nublar')
            print ('D: Isla Contoy')
            guess = raw_input('Answer?: ')
            if guess == 'c' or guess == 'C':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 8:
            qlist.remove(8)
            print q8
            print ('A: 27th')
            print ('B: 31st')
            print ('C: 25th')
            print ('D: 23rd')
            guess = raw_input('Answer?: ')
            if guess == 'd' or guess == 'D':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 9:
            qlist.remove(9)
            print q9
            print ('A: Mitt Romney')
            print ('B: Dick Chaney')
            print ('C: Joe Biden')
            print ('D: Sarah Palin')
            guess = raw_input('Answer?: ')
            if guess == 'd' or guess == 'D':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 10:
            qlist.remove(10)
            print q10
            print ('A: Trump International Hotel and Tower')
            print ('B: One world trade center')
            print ('C: Empire state building')
            print ('D: Willis tower')
            guess = raw_input('Answer?: ')
            if guess == 'a' or guess == 'A':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 11:
            qlist.remove(11)
            print q11
            print ('A: Felix')
            print ('B: Fitzgerald')
            print ('C: Ferdinand')
            print ('D: Frank')
            guess = raw_input('Answer?: ')
            if guess == 'b' or guess == 'B':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 12:
            qlist.remove(12)
            print q12
            print ('A: Felix')
            print ('B: VY Canis Majoris')
            print ('C: Betelgeuse')
            print ('D: UY Scuti')
            guess = raw_input('Answer?: ')
            if guess == 'd' or guess == 'D':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 13:
            qlist.remove(13)
            print q13
            print ('A: Queen Naluai')
            print ('B: Queen Kealoha')
            print ('C: Queen Liliʻuokalani')
            print ('D: Queen Vitoria')
            guess = raw_input('Answer?: ')
            if guess == 'c' or guess == 'C':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 14:
            qlist.remove(14)
            print q14
            print ('A: To have offspring')
            print ('B: 42')
            print ('C: To find love ')
            print ('D: To be successful')
            guess = raw_input('Answer?: ')
            if guess == 'b' or guess == 'B':
                print ('Correct!')
                money += 500
            else:
                wrong = True
        if question == 15:
            qlist.remove(15)
            print q15
            print ('A: 999999999kg')
            print ('B: 1.4 times the sun')
            print ('C: 2.2 times the moon ')
            print ('D: 987036473209kg')
            guess = raw_input('Answer?: ')
            if guess == 'b' or guess == 'B':
                print ('Correct!')
                money += 500
            else:
                wrong = True
    if wrong == True:
        print ('Game over!')
        return money/2
    if len(qlist) == 0:
        print ('You Won!')
        print ('Play again?')
        again = raw_input('?: ')
    if again == 'yes' or again =='Yes':
        print ('Would you like hard or easy questions?')
        choice = raw_input('?: ')
    else:
        print ('bye bye')
        return money
    if choice == 'hard' or choice == 'Hard':
        quizhard()
    if choice == 'easy' or choice == 'Easy':
        quizeasy()          
def quizeasy():
    print ('welcome to the five question easy quiz challenge!! You will start with all the money you earned but if you fail you lose it all!!!!!!')
    money = 7500
    qlist = [1,2,3,4,5]
    wrong = False
    while (wrong == False and len(qlist)!=0):
        question = random.choice(qlist)
        q1 = ('Who was the last democratic president?')
        q2 = ('What is the fifth planet from the sun?')
        q3 = ('What is the largest state by area?')
        q4 = ('Who was the first man on the moon?')
        q5 = ('What is the largest ocean?')
        if question == 1:
            qlist.remove(1)
            print q1
            print ('A: Bill Clinton')
            print ('B: Barrack Obama')
            print ('C: Donald Trump')
            print ('D: George W. Bush')
            guess = raw_input('Answer?: ')
            if guess == 'b' or guess == 'B':
                print ('Correct!')
            else:
                wrong = True
        if question == 2:
            qlist.remove(2)
            print q2
            print ('A: Earth')
            print ('B: Mars')
            print ('C: Saturn')
            print ('D: Jupiter')
            guess = raw_input('Answer?: ')
            if guess == 'd' or guess == 'D':
                print ('Correct!')
            else:
                wrong = True
        if question == 3:
            qlist.remove(3)
            print q3
            print ('A: Alaska')
            print ('B: Texas')
            print ('C: California')
            print ('D: Florida')
            guess = raw_input('Answer?: ')
            if guess == 'a' or guess == 'A':
                print ('Correct!')
            else:
                wrong = True
        if question == 4:
            qlist.remove(4)
            print q4
            print ('A: Buzz Aldrin')
            print ('B: Don Heanly')
            print ('C: Neil Armstrong')
            print ('D: Vladimir Taresenko')
            guess = raw_input('Answer?: ')
            if guess == 'c' or guess == 'C':
                print ('Correct!')
            else:
                wrong = True
        if question == 5:
            qlist.remove(5)
            print q5
            print ('A: Pacific')
            print ('B: Atlantic')
            print ('C: Indian')
            print ('D: Arctic')
            guess = raw_input('Answer?: ')
            if guess == 'a' or guess == 'A':
                print ('Correct!')
            else:
                wrong = True
    if wrong == True:
        print ('You lose all your money!!!!!!')
        return 0
    else:
        print ('You double your money!!!')
    return money*2
def quizhard():
    print ('welcome to the five question hard quiz challenge!! You will start with all the money you earned but if you fail you loose it all!!!!!!')
    money = 7500
    qlist = [1,2,3,4,5]
    wrong = False
    while (wrong == False and len(qlist)!=0):
        question = random.choice(qlist)
        q1 = ('What is the deepest crater on the moon?')
        q2 = ('What day did germany surrender in ww2?')
        q3 = ('Who is the current president of Azerbaijan')
        q4 = ('What country came in 12 for gold medal count at the 2010 winter olympics?')
        q5 = ('What nation has the highest rate of malaria?')
        if question == 5:
            qlist.remove(5)
            print q5
            print ('A: Uganda')
            print ('B: Guatamala')
            print ('C: Ecuador')
            print ('D: Congo')
            guess = raw_input('Answer?: ')
            if guess == 'a' or guess == 'A':
                print ('Correct!')
            else:
                wrong = True
        if question == 2:
            qlist.remove(2)
            print q2
            print ('A: August 25')
            print ('B: April 11')
            print ('C: July 17')
            print ('D: May 7')
            guess = raw_input('Answer?: ')
            if guess == 'd' or guess == 'D':
                print ('Correct!')
            else:
                wrong = True
        if question == 3:
            qlist.remove(3)
            print q3
            print ('A: Sunni Muslims')
            print ('B: Artur Rasizade')
            print ('C: Ilham Aliyev')
            print ('D: Mehriban Aliyeva')
            guess = raw_input('Answer?: ')
            if guess == 'c' or guess == 'C':
                print ('Correct!')
            else:
                wrong = True
        if question == 4:
            qlist.remove(4)
            print q4
            print ('A: Italy')
            print ('B: France')
            print ('C: Sweden')
            print ('D: Russia')
            guess = raw_input('Answer?: ')
            if guess == 'b' or guess == 'B':
                print ('Correct!')
            else:
                wrong = True
        if question == 1:
            qlist.remove(1)
            print q1
            print ('A: Sen 8')
            print ('B: Randolf crater')
            print ('C: Aitken basin')
            print ('D: Kerwan crater')
            guess = raw_input('Answer?: ')
            if guess == 'c' or guess == 'C':
                print ('Correct!')
            else:
                wrong = True
    if wrong == True:
        print ('You lose all your money!!!!!!')
        return 0
    if wrong == False:
        print ('You Double your money!!!')
        return money * 2 
        
    
        
        