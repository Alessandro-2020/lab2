def shifrovka (word, key):
        result = ''
        for l,k in zip(word, key):
                new_l = ord(l.upper())+(ord(k.upper())-ord("A"))+1
                if new_l>90:
                    new_l-=26
                    
                result += chr(new_l)
        return result
def deshifrovka (word, key):
    result = ''
    for l,k in zip(word, key):
            new_l = ord(l.upper())-(ord(k.upper())-ord("A"))-1
            if new_l<65:
                new_l+=26
                    
            result += chr(new_l)
    return result
def kluch(word, key):
        size_word = len(word)
        while len(key) < size_word:
                key += key
        return key
def kluch2(word, key2):
        size_word = len(word)
        while len(key2) < size_word:
                key2 += key2
        return key2
a = input('0=шифровка, 1=расшифровка:')
w = open('word.txt')
for line in w:
    word=line
k1 = open('key.txt')
for line in k1:
    key=line
k2 = open('key2.txt')
for line in k2:
    key2=line
new_key = kluch(word, key)
new_key2 = kluch2(word, key2)
itog = open('shifr.txt', 'w')
i =(shifrovka (word, new_key), shifrovka(word, new_key2))
if a=="0":          
          for index in i:
                itog.write(index + '\n')
          itog.close()
else:        
          for index in i3:
                itog.write(index + '\n')
          itog.close()
