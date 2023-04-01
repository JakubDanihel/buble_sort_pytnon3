import sys
import random

#vytvorenie nahodneho pola
A = [0]*5

for i in range(len(A)):
    A[i] = random.randint(0, 100)

print("Pole na utriedenie je: ", A)

#prejdenie cez cele pole elementov
for i in range(len(A)):

    #najdenie najmensieho elementu v neutriedenom poli
    min_val = i
    for j in range(i+1, len(A)):
        if A[min_val] > A[j]:
            min_val = j
    
    #vymen najmensi element s prvym elementom v poli
    A[i], A[min_val] = A[min_val], A[i]

#vypisanie pola
print("Utriedene pole: ", A)
