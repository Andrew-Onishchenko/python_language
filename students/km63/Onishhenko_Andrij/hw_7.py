#task1-----------------------------------------------------------
 """
 ??????? ??????? ??????? ????????? ????????????? ????????. ???????? ??? ?????: ????? ?????? ? ????? ???????, 
 ? ??????? ????? ?????????? ??????? ? ????????? ???????. ???? ????? ????????? ?????????, ?? ????????? ???, 
 ? ???????? ?????? ????? ??????, ? ???? ?????? ????? ????? ?? ???, ? ???????? ?????? ????? ???????.
 
 ????????? ???????? ?? ???? ??????? ??????? n ? m, ????? n ????? ?? m ????? ? ??????. 
 """
 size = input().split()
 
 m=int(size[0])
 
 n=int(size[1])
 
 matrix = []
 
 for i in range(m):
 
     row = input().split()
 
     for i in range(len(row)):
 
         row[i] = int(row[i])
 
     matrix.append(row)
 
 for i in range(m):
 
     for j in range(n):
 
         if (i==0) and (j==0):
 
             x=i
 
             y=j
 
             max = matrix[0][0]
  
         elif matrix[i][j] > max:
 
             x=i
 
             y=j
 
             max=matrix[i][j]
 
 print (x, y, end=' ')
 #----------------------------------------------------------------
#task2-----------------------------------------------------------
"""
???? ???????? ????? n. ???????? ????????? ?????? ?? n?n ?????????, ???????? ??? ????????? "." 
(?????? ??????? ??????? ???????? ??????? ?? ?????? ???????). ????? ????????? ????????? "*" ??????? ?????? ???????, 
??????? ??????? ???????, ??????? ????????? ? ???????? ?????????. ? ?????????? ??????? ? ??????? ?????? ????????????
??????????? ?????????. ???????? ?????????? ?????? ?? ?????, ???????? ???????? ??????? ?????????. 
"""
 size=int(input())
 matrix = []
 matrix = ['.'] * size
 for i in range(size):
     matrix[i] = ['.'] * size
 for i in range(size):
     for j in range(size):
         if i==j:
             matrix[i][j] = '*' 
         elif (size-j) == (i+1):
             matrix[i][j] = '*'
         if size//2 == j:
             matrix[i][j] = '*'
         if size//2 == i:
             matrix[i][j] = '*'
 for i in range(size):
     for j in range(size):
         print(matrix[i][j], end=' ')
     print() 
 #----------------------------------------------------------------
 
 
 #task3-----------------------------------------------------------
 """
 ???? ??? ????? n ? m. ???????? ????????? ?????? ???????? n?m ? ????????? ??? ????????? "." ? "*" 
 ? ????????? ???????. ? ????? ??????? ???? ?????? ?????? ?????.
 
 """
 size = input().split()
 m=int(size[0])
 n=int(size[1])
 matrix = ['.'] * m
 for i in range(m):
     matrix[i] = ['.'] * n
 for i in range(m):
     for j in range(n):
         if (i+j)%2 == 1:
             matrix[i][j] = '*'
 for i in range(m):
     for j in range(n):
         print(matrix[i][j], end=' ')
     print()
 #----------------------------------------------------------------
 #task4-----------------------------------------------------------
 """
 ???? ????? n. ???????? ?????? ???????? n?n ? ????????? ??? ?? ?????????? ???????. ?? ??????? ????????? ?????? ???? ???????? ????? 0. 
 ?? ???? ??????????, ??????????? ? ???????, ????? 1. ?? ????????? ???? ?????????? ????? 2, ? ?.?. 
 """
 size = int(input())
 matrix = [0] * size
 for i in range(size):
     matrix[i] = [0] * size
 for x in range(1, size):
     for i in range(size-x):
         for j in range(size-x):
             if i == j:
                 matrix[i][j+x] = x
                 matrix[i+x][j] = x
 for i in range(size):
     for j in range(size):
         print(matrix[i][j], end=' ')
     print()
 #----------------------------------------------------------------
 
 #task5------------------------------------------------------------------------------------------------------------------------
 """
 ???? ????? n. ???????? ?????? ???????? n?n ? ????????? ??? ?? ?????????? ???????:
 
 ????? ?? ?????????, ?????? ?? ??????? ???????? ? ????? ?????? ???? ????? 1.
 
 ?????, ??????? ???? ???? ?????????, ????? 0.
 
 ?????, ??????? ???? ???? ?????????, ????? 2.
 
 ?????????? ?????? ???????? ?? ?????. ????? ? ?????? ?????????? ???? ????????. 
 """
 size = int(input())
 matrix = [0] * size
 for i in range(size):
     matrix[i] = [0] * (size-i-1) + [1] + [2] * i
 for i in range(size):
     for j in range(size):
         print(matrix[i][j], end=' ')
     print() 
 #----------------------------------------------------------------
 
 #task6------------------------------------------------------------
 """
??? ????????? ?????? ? ??? ?????: i ? j. ????????? ? ??????? ??????? ? ???????? i ? j ? ???????? ?????????.
 
 ????????? ???????? ?? ???? ??????? ??????? n ? m, ????? ???????? ???????, ????? ????? i ? j.
 
 ??????? ???????? ? ???? ??????? swap_columns(a, i, j). 
 """
 def swap_columns(matrix, i, j):
     for z in range (a):
         temp=matrix[z][i]
         matrix[z][i]=matrix[z][j]
         matrix[z][j]=temp
     return
 size = input().split()
 a=int(size[0])
 b=int(size[1])
 matrix = []
 for k in range(a):
     row = input().split()
     for k in range(len(row)):
         row[k] = int(row[k])
     matrix.append(row)
 size = input().split()
 i=int(size[0])
 j=int(size[1])
 swap_columns(matrix, i, j)
 for i in range(a):
     for j in range(b):
         print(matrix[i][j], end=' ')
     print()