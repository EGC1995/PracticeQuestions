def one_away(s,t):


    if(s[len(s)-1] == t[len(t)-1]):
        return one_away(s[0:len(s)], t[0:len(t)])
    else:
        return one_away(s[0:len(s)], t) || one_away(s, t[0:len(t)])
