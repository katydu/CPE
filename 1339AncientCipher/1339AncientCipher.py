if __name__ == "__main__":
    time = 0
    a,b,n,m = [0] * 26,[0] * 26,[0] * 26,[0] * 26
    while(time<2):
        FirstString = input("Enter First String:")
        SecondString = input("Enter Second String:")
        for i in range(len(FirstString)):
            a[ord(FirstString[i])-ord('A')] +=1
            b[ord(SecondString[i])-ord('A')] +=1
        for i in range(26):
            n[a[i]] +=1
            m[b[i]] +=1
        flag = True
        for i in range(len(FirstString)):
            if n[i] != m[i]:
                flag = False
                break
        if flag == True:
            print("Yes")
        else:
            print("No")
        time +=1