def welcom_speech(t):
    '''
    input: t - template(string)
    output:return None,used as just built-in function print()
    
    '''

    return t

def get_word(w):
    '''
    input: w - list with strings (words)
    output: for now: first element in list as string
    '''
    return w[0]

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
    pass
    
def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play = get_word(word)
    template = star_template(word_in_play)
    welcom_speech(list_to_string_conwert(tempale))
    
