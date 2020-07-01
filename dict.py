import json
from algo import Rat_Ober_Pattern_Recognition

path="C:\\Users\\Vikas\\Desktop\\Project\\Dictionary\\dictionary_compact.json"
var=json.load(open(path))

# Comparator Function
def comp(a):
    return(a[1])
def mod(temp,str):
    index=0
    a=[]
    for i in range(5):
        if (temp[i][0][0]==str[0]):
            a.append(i)
    b=[]
    for i in range(5):
        if (i not in a):
            a.append(i)
    for i in range(5):
        b.append(temp[a[i]])
    return(b)


# suggestions method to apply Pattern Recognition to recommend similar words that exist in Dictionary
# Apply Ratcliff/Obershelp Pattern Recognition Algorithm over the dataset to calculate matcching scores
# and sort them in descending to order to recommend similar words existing in the dictionary
# i.e- lenhgt, jobb, dpllar, chhair, dinosor, accidentaly, acheive, reciept, plagerize

def suggestions(str):
    #list of keys
    key=list(var.keys())
    temp=[]
    for i in range(len(key)):
        temp.append([key[i],Rat_Ober_Pattern_Recognition(str,key[i])])
    temp.sort(key=comp,reverse=True)
    #print(temp[:5])
    if temp[0][1]>=0.8:
        print("\nInput Word does not exist in the directory. Here are the similar recommended words.")
        count=1
        temp=mod(temp[:5],str)
        for i in range(5):
            print(("{count})".format(count=count)),temp[i][0],end=" ")
            count+=1
        print("\n")
        print("Please enter corresponding integer index to continue (0 to return): ",end="")
        i=int(input())
        if i>=1 and i<=5:
            return(var[temp[i-1][0]])
        elif i==0:
            return(None)
        else:
            print("Invalid Input.")
    else:
        print("\nInput Word does not exist in the directory. Spell Check recommended.")

#suggestions("savve")

def get_meaning(str):           # returns meaning of word str
    if str in var:
        return(var[str])
    else:
        return(suggestions(str))

response="y"
# Keep running until user wishes to continue
while(response=="y" or response=="yes"):
    print("Enter Input Word: ",end="")
    word=input()                    # user input word to be searched in the dataset 
    word=word.lower()
    word_meaning=get_meaning(word)     # meaning of user input
    print()
    if word_meaning!=None:
        print(word_meaning)
    print("\nEnter 'Yes' or 'Y' to continue:",end="")
    response=input().lower()
    print()