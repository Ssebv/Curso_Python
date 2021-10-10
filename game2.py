import random
import os

def run():
    IMAGES = ['''
    +---+
        |
        |
        |
       ===
''','''
    +---+
    O   |
        |
        |
       ===
''','''
    +---+
    O   |
    |   |
        |
       ===
''','''
    +---+
    O   |
    |\  |
        |
       ===
''','''
    +---+
    O   |
   /|\  |
        |
       ===
''','''
    +---+
    O   |
   /|\  |
     \  |
       ===
''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===
'''],
    
    
    DB=[
        'C',
        'Python',
        'Dart',
        'JavaScrip'
        
    ]
    
    word = random.choice(DB)
    spaces = ['_'] * len(word)
    attemps = 6
    
    
    
    while True:
        os.system('clear')# Limpiar pantalla
        for character in spaces:
            print(character, end= " ")
        print( 
            IMAGES[attemps])
        letter= input('Elige una letra: ').upper()
        
        found = False   
        for idx, character in enumerate(word): #idx = indices
            if character ==letter:
                spaces[idx] = letter
                found = True
                
            if found== False :
                attemps -=1
                
            if '_' in spaces:
                os.system('clear')
                print('Ganaste!!!')
                print()
                break
                
            if attemps == 0:
                os.system('clear')
                print('Perdiste :c')
                print()
                break
                
                
                

if __name__== "__main__":
    run()
    