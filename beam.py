import numpy as np

moments = []
Zs = []
matrix = []
L = float(input("Beam Length : "))
q = float(input("Beam Load q : "))
EI = float(input("Beam stiffness : "))
n = float(input("Number of beam parts : "))

h = L/n

print()
print("Calculating Moments..")
for i in range(0,int(n)-1):
    X = float(input("Enter X" + str(i) + ":"))
    moments.append((0.5*q*L*X) - (0.5*q*(X**2)))

print("Calculating Z..")
for i in range(0,int(n)-1):
    Zs.append((-h**2 * moments[i]) / EI)

print("Building the system of equations..")
matrix.append([-2,1,0])
matrix.append([1,-2,1])
matrix.append([0,1,-2])

print(Zs)
print("Solution")
A = np.array(matrix)
b = np.array(Zs)
z = np.linalg.solve(A,b)
print(z)

