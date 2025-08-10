class Notebook:
    def __init__(self, tamanho, cor, marca, memoria, preço): #CLASSE DEFINE O QUE TODOS OS ELEMENTOS PERTENCENTES A ELA VÃO TER COMO CARACTERISTICAS 
        self.tamanho= tamanho
        self.cor= cor
        self.marca= marca
        self.memoria= memoria
        self.preço= preço
    
    def promocao(self):
        print("ELE ESTÁ EM PROMOÇÃO")

notebook_1= Notebook(43,"azul", "lenovo", 1000, 2000)

print(notebook_1.marca)

if notebook_1.marca=="lenovo" and notebook_1.preço<=2000:
    print("mil e quintos para hoje")



