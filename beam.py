import numpy as np

moments = []
Zs = []
matrix = []
Xs = []

L = float(input("Beam Length : "))
q = float(input("Beam Load q : "))
EI = float(input("Beam stiffness : "))
n = float(input("Number of beam parts : "))
h = L/n #interval

print()
print("Calculating Moments..")
Xs = [float(input("Enter X" + str(i) + ":")) for i in range(0,int(n)-1)]
moments = [(0.5*q*L*X) - (0.5*q*(X**2)) for X in Xs]

print("Calculating Z..")
Zs = [(-h**2 * moments[i]) / EI for i in range(0,int(n)-1)]

print("Building the system of equations..")
A = np.array([[-2,1,0],[1,-2,1],[0,1,-2]])
b = np.array(Zs)

print("Solution")
z = np.linalg.solve(A,b)
print(z)
