#QUES.
#Take as input S, a number in the form of a string.
#Assume that values of a=1, b=2, c=3, d=4, ...., z=26. Write a recursive function to print all possible codes for the string.

#Ex.: For “1123” possible codes are:
#aabc
#aaw
#alc
#kbc
#kw


#ANS.
s=input()
d={1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h',9: 'i',
   10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q',
   18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
def encode(s):
    if len(s)==0:
        return [""]
    if len(s)==1:
        return [d[int(s[0])]]
    r1=encodeHelper(s[0],s[1:])
    r2=encodeHelper(s[:2],s[2:])
    return r1+r2
def encodeHelper(elem,remaining):
    if int(elem)>26:
        return []
    result=[]
    letter=d[int(elem)]
    combList=encode(remaining)
    for comb in combList:
        result.append(letter+comb)
    return result
r=encode(s)
for v in r:
    print(v)
