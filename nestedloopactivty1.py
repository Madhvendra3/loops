string = input("enter word: ")
chara = input("enter a character/letter: ")
i=0
count=0
while(i< len(string)):

    if(string[i]==chara):
        count =count+1
    i=i+1

print("the total number of times ",chara,"has occured in the word is: ",count)     