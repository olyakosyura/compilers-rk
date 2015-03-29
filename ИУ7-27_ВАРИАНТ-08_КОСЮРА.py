def del_pair(i):
    b[i] = '#'
    b[h[i]] = '#'
    a[i] = a[i-1]
    a[h[i]] = a[h[i]+1]
      
        
 
f = open('brackets.in', 'r')
f1 = open('brackets.out','w')
line = f.readline()
n = len(line)
line = '#' + line + '#'
line1 = line
a = list(line)
b = list(line1)   
sch = -1
h = []
g = []
fl2 = 1
for i in range(0, n+1):
    h.append(0)
    if a[i] == '(':
        g.append(i)
        
    elif a[i] == ')':
        k = len(g)-1
        
        if h[g[k]] == 0:
            h.pop(int(g[k]))
            h.insert(int(g[k]),i)
        else:
            while h[g[k]] != 0:
                k=k-1
            h.pop(int(g[k]))
            h.insert(int(g[k]),i)

flag1 = 0
flag3 = 0
flag2 = 0
flag4 = 0
for i in range(0, n+1):
    if a[i] == '(':
        flag4=0
        for j in range(i,h[i]):
            if (a[j]=='+') or (a[j]=='-'):
                flag4=1
            
        if (flag4==1) and ((flag2==1) or (flag3==1)) and (a[i+1]!='('):
            continue
        if (flag3==1) and (flag4==1):
            flag2 = 0
            flag1 = 0
            flag3 = 0
            flag4=0
            continue
        del_pair(i)
        inew1 = i
        inew2 = h[i]
        if flag1 == 1:
            for q in range(inew1, inew2):
                if b[q] == '-':
                    b[q] = '+'
                    a[q] = '+'
                elif b[q] == '+':
                    b[q] = '-'
                    a[q] = '-'
        if flag2 == 1:
            for q in range(inew1, inew2):
                if b[q] == '/':
                    b[q] = '*'
                    a[q] = '*'
                elif b[q] == '*':
                    b[q] = '/'
                    a[q] = '/'
        flag2 = 0
        flag4 = 0
        flag3 = 0
        flag1 = 0
        continue
        if a[i-1] == '/':
            continue
        if (a[i-1] in ['+', '#', '(']) and (not(a[h[i]+1] in ['/', '*'])):
            if (flag3==1) and (flag4==1):
                flag2 = 0
                flag1 = 0
                flag3 = 0
                flag4=0
                continue
            del_pair(i)
            inew1 = i
            inew2 = h[i]
            if flag1 == 1:
                for q in range(inew1, inew2):
                    if b[q] == '-':
                        b[q] = '+'
                        a[q] = '+'
                    elif b[q] == '+':
                        b[q] = '-'
                        a[q] = '-'
            if flag2 == 1:
                for q in range(inew1, inew2):
                    if b[q] == '/':
                        b[q] = '*'
                        a[q] = '*'
                    elif b[q] == '*':
                        b[q] = '/'
                        a[q] = '/'
            flag2 = 0
            flag1 = 0
            flag3 = 0
            flag4=0
            continue
        fl = 1
        sch = -1
        for j in range(i, h[i] - 1):
            if ((a[j] == '+') or (a[j] == '-')) and (sch == -1):
                fl = 0
                break
            elif a[j] == '(':
                sch = sch + 1
            elif a[j] == ')':
                sch = sch - 1
            
        if fl==1:
            if (flag3==1) and (flag4==1):
                flag2 = 0
                flag1 = 0
                flag3 = 0
                flag4=0
                continue
            del_pair(i)
            inew1 = i
            inew2 = h[i]
            if flag1 == 1:
                for q in range(inew1, inew2):
                    if b[q] == '-':
                        b[q] = '+'
                        a[q] = '+'
                    elif b[q] == '+':
                        b[q] = '-'
                        a[q] = '-'
            if flag2 == 1:
                for q in range(inew1, inew2):
                    if b[q] == '/':
                        b[q] = '*'
                        a[q] = '*'
                    elif b[q] == '*':
                        b[q] = '/'
                        a[q] = '/'
                        
            flag2 = 0
            flag1 = 0
            flag3 = 0
            flag4 = 0

            continue
    elif (a[i] == '-') and (a[i+1] == '('):
        flag1 = 1
    elif (a[i] == '/') and (a[i+1] == '('):
        flag2 = 1
    elif (a[i] == '*') and (a[i+1] == '('):
        flag3 = 1
    elif ((a[i] == '-') or (a[i] == '+')):
        flag4 =1
    

while b.count('#') > 0:
    b.remove('#')


f1.write(''.join(b))

f.close()
f1.close()
