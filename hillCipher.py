import numpy as np

def hill_cipher(k,d,A):
#------------get a key and massage and d 
# k=input("give a key matrix ")
    k=[[11,8],[3,7]]
    k=np.array(k)
# A=input("whats the massage?")
    A="let us fly"
    A=A.replace(" ","")
    d=2
# d=input("whats d ?")

#----------convert massage to a d block matrix
    A_matrix=[]
    for i in range(len(A)):
        A_matrix.append(ord(A[i])-97) 

    M=[A_matrix[i:i+2] for i in range(0,len(A_matrix),2)]
# B=[[0 for i in range(len(M))] for j in range(len(M[0]))]
# for i in range(len(M)):
#     for j in range(len(M[0])):
#         B[j][i]=M[i][j]

    M=np.array(M)
    M=M.T
    print(M)

#-------------multiply key matrix to massage in mod 26
    D=np.dot(k,M)
    for i in range(len(k)):
       for j in range(len(M[0])):
            D[i][j]=D[i][j]%26

#----------------- convert cipher text to a plaintext again
    C=[]
    for i in range(len(D[0])):
        for j in range(len(D)):
            C.append(D[j][i])
    for i in range(len(C)):
        C[i]=chr(C[i]+97)
    C=''.join(C)
    return C











    