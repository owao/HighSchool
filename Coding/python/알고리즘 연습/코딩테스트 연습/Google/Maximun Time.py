s=input()
return_s=""

for i in range(5):
    if i==2:
        return_s += ':'
        continue
    if s[i]=='?':
        if i==0:
            if s[1] == '0' or s[1] == '1' or s[1] == '2' or s[1] == '3':
                return_s += '2'
            else:
                return_s += '1'
        if i==1:
            if return_s[0]== '2':
                return_s += '3'
            else:
                return_s += '9'
        if i==3:
            return_s += '5'
        if i==4:
            return_s += '9'
    else:
        return_s += s[i]

print(return_s)
