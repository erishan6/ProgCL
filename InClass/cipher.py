import string

def decipher(s, perm):
    mydict = {}
    alphabets  = string.ascii_lowercase
    for i in range(26):
        mydict[perm[i]]=alphabets[i]
    keys = mydict.keys()
    res = ""
    for i in range(len(s)):
        if s[i]  in keys:
            res += mydict[s[i]]
        else:
            res += s[i]
    return res

if __name__ == '__main__':
    perm = "wnoegbjpkyxlfiuastqhvmcrzd"
    print(decipher("wnoeg", perm))
    print(decipher("rzd", perm))
    print(decipher("azhpui", perm))
    print(decipher("hpg ntuci bur yvfaq umgt hpg euj", perm))