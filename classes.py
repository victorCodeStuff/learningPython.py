class Cattle:
    def __init__(self,name,sex,fatherName,species):
        self.name = name
        self.sex = sex
        self.fatherName = fatherName
        self.species = species
           
    def imprimir(Cattle):
        ##dados
        print(Cattle.name,Cattle.sex,Cattle.fatherName,Cattle.species)
        
Cattle = Cattle("Cattle Name: Rodolf","\nCattle Sex: Male","\nCattle Father's Name: Demetrian Titus","\nCattle Species: bovine")
        
Cattle.imprimir()