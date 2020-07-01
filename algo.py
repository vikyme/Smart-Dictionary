# Ratcliff/Obershelp Pattern Recognition Algorithm analyses two strings to check how similar/different they are.
# Its main application is Spell Check (when user mistypes, recommends similar words)
# This algorithm uses longest common substring in O(M*N) time recursively to find the matching score b/w two strings
# 0-> No Overlapping, 1-> Perfect Matching of strings. ( 0 <= Score <= 1 ) 
from collections import deque
def LongestCommonSubstring(s1,s2):
    #length of longest common substring
    ans=0
    #length of string s1 & s2 
    l1=len(s1)
    l2=len(s2)
    # matrix arr stores longest common suffix of substrings with Ist row and column always zero
    arr=[]
    row=0
    #end point of longest common substring
    end=0
    for i in range(2):
        temp=[]
        for j in range(l2+1):
            temp.append(0)
        arr.append(temp)
        
    for i in range(l1+1):
        for j in range(l2+1):
            
            # building matrix arr in bottom-up method to find lcs
            if (i==0 or j==0):
                arr[row][j]=0
            elif (s1[i-1]==s2[j-1]):
                #print(i,j)
                arr[row][j]=1+arr[1-row][j-1]
                if (ans<arr[row][j]):
                    ans=arr[row][j]
                    end=i-1
            else:
                arr[row][j]=0
        row=1-row
        #switch current and previous rows
    if ans==0:
        return (-1)
    # Case if there is zero overlapping
    r=[ans, end-ans+1,end,s1[end-ans+1:end+1]]
    return (r)
    # returns length, start index, end index 
        
#print(LongestCommonSubstring("dictionary", "dictonary"))   

# Ratcliff/Obershelp Pattern Recognition Algorithm Implementation
# First, LCS is found b/w str1 & str2 which is called an Anchor. Increment the matches by length of LCS, 
# recursively repeat the same process for left & right substrings of LCS. Apply the forrmula after the loop finishes,
# divide the matches by sum of length of input strings to get their Matching Score.
 
def Rat_Ober_Pattern_Recognition(str1, str2):
    # Inbuilt Stack Data Structure 
    stack=deque()
    # push given strings into stack
    stack.append(str1)
    stack.append(str2)
    # matching score of strings intialized with 0 represents (zero matching) & 1 represents (perfect matching)
    match=0.0
    while(stack):
        s1=stack.pop()
        s2=stack.pop()
        # Comparing both strings to find longest common substring
        #print(s1,s2)
        ans=LongestCommonSubstring(s1,s2)
        #print(ans)
        # Ignoring the case with zero overlapping
        if (ans!=-1):
            #print(ans, match)
            # ans matrix contains length, start index, end index of LCS
            for i in range(len(s2)):
                if s2[i:i+ans[0]]==ans[3]:
                    ans[2]=i
                    break
            #print(ans)
            match+=2*ans[0]
            # check if start not equal to end for adding string from 0 index & last index respectively
            if (ans[1]!=0 and ans[2]!=0):
                stack.append(s1[0:ans[1]])
                stack.append(s2[0:ans[2]])
            if (ans[0]+ans[1]!=len(s1) and ans[0]+ans[2]!=len(s2)):
                stack.append(s1[ans[0]+ans[1]:len(s1)])
                stack.append(s2[ans[0]+ans[1]:len(s2)])
    l=len(str1)+len(str2)
    return(match/l)

#print(Rat_Ober_Pattern_Recognition("mousse","sensuous"))                