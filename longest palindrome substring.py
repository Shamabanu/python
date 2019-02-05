def longestPalindrome(M):
        tem = ""
        for i in range(len(M)):
            for j in range(len(M)-1,i-1,-1):
                if(M[i]==M[j]):
                    m=M[i:j+1]
                    if(m ==m[::-1]):
                        if(len(tem) <= len(m)):
                            tem = m
        return tem
M=str(input())
print(longestPalindrome(M))
