import random

misses = 0


def hangman():

    misses = 0
    end = 0
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    a = int(input('Enter number 1: '))
    b = int(input('Enter number 2: '))
    while b == a or b<0:
        print('Number 2 cannot be equal to Number 1 or negative')
        b = int(input('Enter number  2: '))
    wlist, l = [], []
    wordl = []
    if a > b:
        a, b = b, a
    r = random.randint(b-a, b+a)
    print(r)
    wl = int(input('Enter the letter count chosen: '))
    while type(wl) != int:
        wl = int(input('Enter the letter count chosen: '))
    for i in range(r):
        word = input('Enter word: ')
        while len(word) != wl:
            print('Word is not of chosen length')
            word = input('Enter word: ')
        else:
            l.append(word)

    w = random.choice(l)
    print('The random word chosen is of length: ', wl)
    for i in range(wl):
        wlist.append(w[i])
        wordl.append('_')

    def new_word(ch):
        global misses
        global end
        if ch not in alpha:
            print('You have already guessed this letter')
        else:
            if ch in w:
                print(ch, 'is in the word')
                for i in range(len(wlist)):
                    if wlist[i] == ch:
                        wordl[i] = ch
            else:
                print('That letter is not in the word')
                misses += 1
                print(misses)
            alpha.remove(ch)
        w_res = ''
        for i in wordl:
            w_res += i
        if misses == 1:
            print('''
            
           
           
            
            
    _________''')
        elif misses == 2:
            print('''
            
            
            
            
            
    ____|____''')
        elif misses == 3:
            print('''
    
    
    
    
        |
    ____|____''')
        elif misses == 4:
            print('''
    
    
    
        |
        |
    ____|____''')
        elif misses == 5:
            print('''
    
    
        |
        |
        |
    ____|____''')
        elif misses == 6:
            print('''
    
        |
        |
        |
        |
    ____|____''')
        elif misses == 7:
            print('''
        _____
        |
        |
        |
        |
    ____|____''')
        elif misses == 8:
            print('''
       _____
       |    |
       |
       |
       |
    ___|____''')
        elif misses == 9:
            print('''
       _____
       |    |
       |    o
       |
       |
    ___|____''')
        elif misses == 10:
            print('''
       _____
       |    |
       |    o
       |    |
       |
    ___|____''')
        elif misses == 11:
            print('''
       _____
       |    |
       |   \o
       |    |
       |
    ___|____''')
        elif misses == 12:
            print('''
       _____
       |    |
       |   \o/
       |    |
       |
    ___|____''')
        elif misses == 13:
            print('''
       _____
       |    |
       |   \o/
       |    |
       |   /
    ___|____''')
        elif misses == 14:
            print('''
       _____
       |    |
       |   \o/
       |    |
       |   / \\
    ___|____''')
            end = 1
        print('The word now is', w_res)
        return w_res

    c = 0
    print('The word you are trying to guess is:', '_'*wl)
    while True:
        if end == 1:
            print('You lost...')
            print('The word was:', w)
            break
        ch = input('Enter a character: ')
        if ch.isalpha() == True:
            p = new_word(ch[0])
            if '_' not in p:
                print('Congratulations! You got the word!!!')
                break
            c += 1
        else:
            print('Enter a valid answer')

hangman()
