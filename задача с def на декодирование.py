def decode(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    number = 0
    for w in range(len(s)):
        if s[w] == ' ':
            answer += ' '
        for i in range(len(alphabet)):
            if alphabet[i] == s[w]:
                answer += alphabet[-i + -1 ]
                           
    return answer
                    
    

print(decode('hello'))
print(decode('try to decode this'))
print(decode(''))
