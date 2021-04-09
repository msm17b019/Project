'''
Author--Sujeet Kumar
Date--09/04/2021
Time--13:22

This program multiply two matrices.
'''
 
# m1 will multiply with m2....Note that m1*m2 is not equal to m2*m1 in matrix multiplication
m1=([[3,4,5],[4,5,2],[6,4,7]]) # Enter row-wise values in matrix 1
m2=([[2,4],[4,2],[3,3]]) # Enter row-wise values in matrix 2

#order of matrix 1 is a x b and matrix 2 is c x d. if b=c then only multiplication is possible.
#order of final matrix will be a x d.
m3=[[0,0],[0,0],[0,0]]

for i in range(0,len(m3)):
    for j in range(0,len(m3[0])):
        for k in range(0,len(m2)):
            m3[i][j]+=m1[i][k]*m2[k][j]  

for item in m3:
    print(item)  
    