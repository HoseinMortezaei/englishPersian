def getit(n):
    n2=''
    for i in n:
        if i=='a':
            n2+='ش'
        elif i=='?':
            n2 += '؟'
        elif i=='’':
            n2+='گ'
        elif i=='b':
            n2+='ذ'
        elif i=='c':
            n2+='ز'
        elif i=='d':
            n2+='ی'
        elif i=='e':
            n2+='ث'
        elif i=='f':
            n2+='ب'
        elif i=='g':
            n2+='ل'
        elif i=='h':
            n2+='ا'
        elif i=='i':
            n2+='ه'
        elif i=='ك':
            n2+=';'
        elif i=='j':
            n2+='ت'
        elif i=='k':
            n2+='ن'
        elif i=='l':
            n2+='م'
        elif i=='s':
            n2+='س'
        elif i=='t':
            n2+='ف'
        elif i=='u':
            n2+='ع'
        elif i=='v':
            n2+='ر'
        elif i=='w':
            n2+='ص'
        elif i=='x':
            n2+='ط'
        elif i=='y':
            n2+='غ'
        elif i=='z':
            n2+='ظ'
        elif i=='A':
            n2+='َ'
        elif i=='B':
            n2+='إ'
        elif i=='C':
            n2+='ژ'
        elif i=='D':
            n2+='ِ'
        elif i=='E':
            n2+='ٍ'
        elif i=='F':
            n2+='ّ'
        elif i=='G':
            n2+='?'
        elif i=='H':
            n2+='آ'
        elif i=='I':
            n2+=']'
        elif i=='J':
            n2+='ـ'
        elif i=='K':
            n2+='«'
        elif i=='L':
            n2+='»'
        elif i=='S':
            n2+='ُ'
        elif i=='T':
            n2+='،'
        elif i=='U':
            n2+=','
        elif i=='V':
            n2+='ؤ'
        elif i=='W':
            n2+='ٌ'
        elif i=='X':
            n2+='ي'
        elif i=='Y':
            n2+='؛'
        elif i=='Z':
            n2+='ة'
        elif i=='m':
            n2+='ئ'
        elif i=='n':
            n2+='د'
        elif i=='o':
            n2+='خ'
        elif i=='p':
            n2+='ح'
        elif i=='q':
            n2+='ض'
        elif i=='r':
            n2+='ق'
        elif i=='M':
            n2+='ئ'
        elif i=='N':
            n2+='د'
        elif i=='O':
            n2+='خ'
        elif i=='P':
            n2+='ح'
        elif i=='Q':
            n2+='ض'
        elif i=='R':
            n2+='ريال'
        elif i=='\\':
            n2+='پ'
        elif i==',':
            n2+='و'
        elif i=='ا':
            n2+='h'
        elif i=='ب':
            n2+='f'
        elif i=='پ':
            n2+='\\'
        elif i=='ت':
            n2+='j'
        elif i=='ث':
            n2+='e'
        elif i=='ج':
            n2+='['
        elif i=='چ':
            n2+=']'
        elif i=='ح':
            n2+='p'
        elif i=='خ':
            n2+='o'
        elif i=='د':
            n2+='n'
        elif i=='ذ':
            n2+='b'
        elif i=='ر':
            n2+='v'
        elif i=='ز':
            n2+='c'
        elif i=='ژ':
            n2+='C'
        elif i=='س':
            n2+='s'
        elif i=='ش':
            n2+='a'
        elif i=='ص':
            n2+='w'
        elif i=='ض':
            n2+='q'
        elif i=='ط':
            n2+='x'
        elif i=='ظ':
            n2+='z'
        elif i=='ع':
            n2+='u'
        elif i=='غ':
            n2+='y'
        elif i=='ف':
            n2+='t'
        elif i=='ق':
            n2+='r'
        elif i=='ک':
            n2+=';'
        elif i=='گ':
            n2+="'"
        elif i=='ل':
            n2+='g'
        elif i=='م':
            n2+='l'
        elif i=='ن':
            n2+='k'
        elif i=='و':
            n2+=','
        elif i=='ه':
            n2+='i'
        elif i=='ی':
            n2+='d'
        elif i=='ئ':
            n2+='m'
        elif i=='ي':
            n2+='d'
        elif i==']':
            n2+='چ'
        elif i=="'":
            n2+='گ'
        elif i=='[':
            n2+='ج'
        elif i==';':
            n2+='ک'
        elif i=='ً':
            n2+='Q'
        elif i=='ٌ':
            n2+='W'
        elif i=='،':
            n2+='T'
        elif i=='؛':
            n2+='Y'
        elif i==',':
            n2+='U'
        elif i=='َ':
            n2+='A'
        elif i=='ُ':
            n2+='S'
        elif i=='ِ':
            n2+='D'
        elif i=='ّ':
            n2+='F'
        elif i=='ۀ':
            n2+='G'
        elif i=='آ':
            n2+='H'
        elif i=='«':
            n2+='K'
        elif i=='»':
            n2+='L'
        elif i=='ة':
            n2+='Z'
        elif i=='ي':
            n2+='X'
        elif i=='ژ':
            n2+='C'
        elif i=='ؤ':
            n2+='V'
        elif i=='إ':
            n2+='B'
        elif i=='أ':
            n2+='N'
        elif i=='ء':
            n2+='M'
        elif i=='؟':
            n2+=  '?'     
        else:
            n2+=i
    return n2
