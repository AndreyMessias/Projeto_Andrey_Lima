class ClasseA:
    def __init__(self):
        self.A1 = 0      # int
        self.A2 = 0.0    #float
    # Gets e Sets
    def get_A1(self): return self.A1
    def set_A1(self, valor): self.A1 = valor
    def get_A2(self): return self.A2
    def set_A2(self, valor): self.A2 = valor

    def MA1(self):
        print("MA1")

    def MA2(self):
        print("MA2")

    def MA3(self):
        print("Alteração a classe A partir do clone")