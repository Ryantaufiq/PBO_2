class Matematika:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c=0):
        return a + b + c
mat = Matematika()
B = mat.add(6, 3, 9)
print(B)
mut = Matematika()
C = mut.add(5,2)
print(C)