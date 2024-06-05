def welcom_speech(t):
    '''
    input: t - template(string)
    output:return None,used as just built-in function print()
    
    '''
    print(f'''
    добро пожадовать в игру - hangman 2000
    ваша задача угадать загаданое слово за несколько попыток,
    иначе вас ждёт расплата!
    заганое слово состоит из {len(t)} букв {t}
    ''')
    

def get_word(w):
    '''
    input: w - list with strings (words)
    output: for now: first element in list as string
    '''
    return w[0]

def start_template(w):
    '''
    input: w - string (word)
    output: replace all chars in string to '_'
            replaced chars as string with length w == t        
    '''
    how_many = len(w)
    t=[]
    for i in range(how_many+1):
        t.append('_')
    return t
        
def list_to_string_convert(t):
    '''
    input: t- template (list)
    outputi s- list converted to string
    '''
    string = ''
    for i in t:
        string += i
    return string 
        
def list_to_string_convert_v2(t):
    '''
    input: t- template (list)
    outputi s- list converted to string
    '''
    s = ''
    return s.join(t)

def user_input():
    '''
    output:return str,build-in input() function
    '''
    
    return input('ведите букву:')

def build_template(t,w,g=''):
    '''
    input:t - temlate(list), w - word(string),g - guess(string)
    output:t - template(list) with replaced characters in template
                if character in word == guess:
                    'sharacter'
                else:
                    '_'
    '''
    
    for i in range(len(w)):
        for u in w:
             if g == w[i]:
                 t[i] = w[i]
    return t
        
def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play = get_word(word)
    template = star_template(word_in_play)
    welcom_speech(list_to_string_conwert(tempale))

    while progress:
        user_guess = user_input()
        template = build_template(template,word_in_play,user_guess)

    
