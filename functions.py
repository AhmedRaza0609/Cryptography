import streamlit as st

wordstxt = open('dictionary.txt', 'r').read()



upperscaling = [
'A','B','C','D','E','F','G','H','I','J','K','L',"M",'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'A','B','C','D','E','F','G','H','I','J','K','L',"M",'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
lowerscaling = [
'a','b','c','d','e','f','g','h','i','j','k','l',"m",'n','o','p','q','r','s','t','u','v','w','x','y','z',
'a','b','c','d','e','f','g','h','i','j','k','l',"m",'n','o','p','q','r','s','t','u','v','w','x','y','z',
]

atbash={
'A':'Z', 'B':'Y', 'C':'X', 'D':'W', 'E':'V', 'F':'U', 'G':'T', 'H':'S', 'I':'R', 'J':'Q', 'K':'P', 'L':'O', 'M':'N',
'N':'M', 'O':'L', 'P':'K', 'Q':'J', 'R':'I', 'S':'H', 'T':'G', 'U':'F', 'V':'E', 'W':'D', 'X':'C', 'Y':'B', 'Z':'A',
'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o', 'm':'n',
'n':'m', 'o':'l', 'p':'k', 'q':'j', 'r':'i', 's':'h', 't':'g', 'u':'f', 'v':'e', 'w':'d', 'x':'c', 'y':'b', 'z':'a',
}

AZen = {
'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7', 'H':'8', 'I':'9', 'J':'10', 'K':'11', 'L':'12', 'M':'13',
'N':'14', 'O':'15', 'P':'16', 'Q':'17', 'R':'18', 'S':'19', 'T':'20', 'U':'21', 'V':'22', 'W':'23', 'X':'24', 'Y':'25', 'Z':'26',

'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13',
'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26'
}

AZde = {
'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G', '8':'H', '9':'I', '10':'J', '11':'K', '12':'L', '13':'M',
'14':'N', '15':'O', '16':'P', '17':'Q', '18':'R', '19':'S', '20':'T', '21':'U', '22':'V', '23':'W', '24':'X', '25':'Y', '26':'Z',
}


def Atbash(txt):
    ans = ''
    for letter in txt:
        if letter in atbash:
            ans+=atbash[letter]
        else:
            ans += letter
    return ans

def Caeser(txt, method=None):
    if method == 'Encrypt':
        key = st.slider('Choose the key:', min_value=0, max_value=25)
        ans = ''
        for letter in txt:
            if letter in lowerscaling:
                ans+= lowerscaling[lowerscaling.index(letter)+key]
            elif letter in upperscaling:
                ans+= upperscaling[upperscaling.index(letter)+key]
            else:
                ans += letter
        return ans
    if method == 'Decrypt':
        keyorno = st.radio("Do you want to provide a key (Yes) or Let the Program decrypt on its own (No)",('Yes', 'No'))
        decrypted = ''
        if keyorno == 'Yes':
            decryptkey = st.slider('Choose the key:', min_value=0, max_value=25)
            for letter in txt:
                if letter in lowerscaling:
                    decrypted+= lowerscaling[lowerscaling.index(letter)-decryptkey]
                elif letter in upperscaling:
                    decrypted+= upperscaling[upperscaling.index(letter)-decryptkey]
                else:
                    decrypted += letter
            return decrypted
        if keyorno == 'No':
            highestcount = 0
            answer = ''
            for i in range(26):
                wordcount = 0
                decrypt = ''
                for letter in txt:
                    if letter in lowerscaling:
                        decrypt+= lowerscaling[lowerscaling.index(letter)-i]
                    elif letter in upperscaling:
                        decrypt+= upperscaling[upperscaling.index(letter)-i]
                    else:
                        decrypt += letter
                checker = decrypt.split()
                for word in checker:
                    if word in wordstxt:
                        wordcount += 1
                if wordcount > highestcount:
                    highindex = i
                    highestcount = wordcount
            for letter in txt:
                if letter in lowerscaling:
                    answer+= lowerscaling[lowerscaling.index(letter)-highindex]
                elif letter in upperscaling:
                    answer+= upperscaling[upperscaling.index(letter)-highindex]
                else:
                    answer += letter
            return answer.capitalize()




def A2Z(txt, method):
    if method == 'Encrypt':
        ans = ''
        for letter in txt:
            if letter in AZen:
                ans += AZen[letter]
            ans += ' '
        return ans
    if method == 'Decrypt':
        ans = ''
        nums = txt.split()
        for letter in nums:
            if letter in AZde:
                ans += AZde[letter]
            elif letter == '?':
                ans += ' '
        return ans
