# create a function to find the index of the character
# this solution I will use while loop just to try another way
# and you can make simple solution in another way but this dor training

# solution:

s = "mman"

def find_index(string, sub):
    try:
        index=0
        i = string[index]
        while i in string:
            if i == sub:
                print(index)
                break
            
            elif i == s[-1]and i != sub:
                print(-1)
                break
                
            index+=1
            i = string[index]
                    
    except:
      pass    

find_index(s, "a")
