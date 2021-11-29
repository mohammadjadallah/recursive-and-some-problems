'''
solve amazing problem:

Given a 2D array of mines, replace the question mark with the number of mines that immediately surround it.
This includes the diagonals, meaning it is possible for it to be surrounded by 8 mines maximum.
The key is as follows:

An empty space: "-"

A mine: "#"

Number showing number of mines surrounding it: "?"

sample:

         (["-","#","-"],
         ["-","?","-"],
         ["-","-","-"])

      
         (["-","#","#"],
         ["?","#",""],
         ["#","?","-"])

output:
       
         [["-","#","-"],
         ["-","1","-"],
         ["-","-","-"]]


        [["-","#","#"],
         ["3","#",""],
         ["#","2","-"]]

'''


tupli1 = (["-","#","-"],
         ["-","?","-"],
         ["-","-","-"])


tupli2 = (["-","#","-"],
         ["#","-","?"],
         ["#","#","-"])


tupli3 = (["-","#","#"],
         ["?","#",""],
         ["#","?","-"])

tupli4 = (["-","?","#"],
         ["?","#","?"],
         ["#","?","-"])

tupli5 = (["#","?","#"],
         ["#","#","?"],
         ["#","?","-"])


tupli6 = (["#","#","#"],
         ["#","?","#"],
         ["#","#","#"])


tupli7 = (["#","#","#"],
         ["#","#","#"],
         ["#","?","#"])


tupli8 = (["#","#","#"],
         ["#","#","?"],
         ["#","#","#"])



print()
result = [[],[],[]]
count = 0
liicount = []

def solveProblem(tp):
    global count, liicount
    for i in tp:
        if '?' in i:
           if tp[0][0] ==  '?':
               if tp[0][1] == '#':
                   count += 1

               if tp[1][0] == '#':
                   count += 1

               if tp[1][1] == '#':
                   count += 1

               liicount.append(count)


           if tp[0][1] == '?':
               count = 0
               if tp[0][0] == '#':
                   count += 1

               if tp[0][2] == '#':
                   count += 1

               if tp[1][0] == '#':
                   count += 1

               if tp[1][1] == '#':
                   count += 1

               if tp[1][2] == '#':
                   count += 1

               liicount.append(count)

           if tp[0][2] == '?':
               count = 0
               if tp[0][1] == '#':
                   count += 1

               if tp[1][1] == '#':
                   count += 1

               if tp[1][2] == '#':
                   count += 1

               liicount.append(count)

               # ========================================= 1

           if tp[1][0] == '?':
               count = 0
               if tp[0][0] == '#':
                   count += 1

               if tp[0][1] == '#':
                   count += 1

               if tp[1][1] == '#':
                   count += 1

               if tp[2][0] == '#':
                   count += 1

               if tp[2][1] == '#':
                   count += 1

               liicount.append(count)


           if tp[1][1] == '?':
               count = 0
               if tp[0][0] == '#':
                   count += 1

               if tp[0][1] == '#':
                   count += 1

               if tp[0][2] == '#':
                   count += 1

               if tp[1][0] == '#':
                   count += 1

               if tp[1][2] == '#':
                   count += 1

               if tp[2][0] == '#':
                   count += 1

               if tp[2][1] == '#':
                   count += 1

               if tp[2][2] == '#':
                   count += 1

               liicount.append(count)


           if tp[1][2] == '?':
               count = 0
               if tp[0][1] == '#':
                   count += 1

               if tp[0][2] == '#':
                   count += 1

               if tp[1][1] == '#':
                   count += 1

               if tp[2][1] == '#':
                   count += 1

               if tp[2][2] == '#':
                   count += 1

               liicount.append(count)

                   # ========================================= 2

           if tp[2][0] == '?':
                count = 0
                if tp[1][0] == '#':
                    count += 1

                if tp[1][1] == '#':
                    count += 1

                if tp[2][1] == '#':
                   count += 1

                liicount.append(count)


           if tp[2][1] == '?':
                count = 0
                if tp[1][0] == '#':
                    count += 1

                if tp[1][1] == '#':
                    count += 1

                if tp[1][2] == '#':
                    count += 1

                if tp[2][0] == '#':
                    count += 1

                if tp[2][2] == '#':
                    count += 1

                liicount.append(count)

           if tp[2][2] == '?':
                count = 0
                if tp[1][1] == '#':
                    count += 1

                if tp[1][2] == '#':
                    count += 1

                if tp[2][1] == '#':
                    count += 1

                liicount.append(count)

    def numOfQuest(numq):
        o = 0
        for i in numq:
            for g in i:
                if g == '?':
                    o += 1
                else:
                    pass
        return o
    liicount = [liicount[i] for i in range(numOfQuest(numq=tp))]


def replace_questionMark(tup):
    solveProblem(tup)
    y = 0
    m = 0
    for u in tup:
        for a in u:
            if a == '?':
                result[y].append(a.replace('?', str(liicount[m])))
                m += 1
            else: result[y].append(a)
        y += 1
    return result


if __name__ == '__main__':

    #print(replace_questionMark(tup=tupli1))

    #print(replace_questionMark(tup=tupli2))

    #print(replace_questionMark(tup=tupli3))

    #print(replace_questionMark(tup=tupli4))

    #print(replace_questionMark(tup=tupli5))

    #print(replace_questionMark(tup=tupli6))

    #print(replace_questionMark(tup=tupli7))

    print(replace_questionMark(tup=tupli8))
    
