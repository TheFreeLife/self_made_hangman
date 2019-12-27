from random import randint  
picture = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''
    
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def word(): #이건 랜덤으로 단어를 얻는다.
    word = 'fire water night gun gum wtf car dirt trade nood rich world huge small big diamond'
    word = word.split()
    RandomNum = randint(0,len(word)-1)
    return word[RandomNum]

def guess(xWord):#여기서 단어를 입력받는다.
    while True:
        playerguess = input()
        if len(playerguess) != 1:
            print ("다시입력하세요")
        elif playerguess not in 'wqertyuiopasdfghjklzxcvbnm':
            print ('다시입력하세요')
        elif playerguess in xWord:
            print ('이미 한번 입력했네요')
        elif playerguess in SuccesChr:
            print('이미 정답 판정을 받은 글자네요.')
        else:
            return playerguess

    
def blank(word1): #여기서는 단어를 -로 바꾸어 보여준다.
    blankword = ''
    for i in range(len(word1)):
        blank_ = '-'
        blankword += blank_
    return blankword

isplaygame = True
while isplaygame:
    mainloop = True
    xWord = ''
    counted = 0
    HangmanImage = 0
    isWin = 0
    word1 = word()
    blank1 = blank(word1)
    GameIsDone = False
    again = False
    SuccesChr = ''
    print ('HANGMAN WORLD')
    print (picture[0])
    print ("비밀단어:{0}".format(blank1))
    print ('틀린단어:')
    while  mainloop:
        counted = 0  
        ok = guess(xWord)
        for i in range(len(word1)):
            if word1[i] in ok:
                if not blank1[i].isalpha():
                    blank1 = blank1[:i]+ok+blank1[i+1:]
                    counted = counted + 1
                    isWin = isWin + 1
                    SuccesChr += ok
                elif blank1[i].isalpha():
                    counted = counted + 1 

        if counted == 0:
            print('아뇨아뇨')
            xWord = xWord + ok
            HangmanImage = HangmanImage+1

        print ('HANGMAN WORLD')
        print (picture[HangmanImage])
        print ("비밀단어:{0}".format(blank1))
        print ('틀린단어:{0}'.format(xWord))
            
        if len(xWord) == 6:
            print ('패배~~')
            print ('정답은' + word1 +'입니다')
            again = input('다시 하시겠습니까?(no or yes)').lower().startswith('y')
            GameIsDone = True
        elif isWin == len(word1):
            print ('승리~~')
            again = input('다시 하시겠습니까?(no or yes)').lower().startswith('y')
            GameIsDone = True
        if GameIsDone:
            if again:
                mainloop = False
            else:
                mainloop= False
                isplaygame = False

    
        
        


        

    
    
