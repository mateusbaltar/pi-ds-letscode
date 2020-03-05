class Colaborador:
    
    def __init__(self, matricula, nome, salario, cargo):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def __repr__(self):
        return f'Matrícula: {self.matricula} | Funcionário: {self.nome} | Cargo: {self.cargo} | Salário: {self.salario}'
        
    
class Organograma:
    
    def __init__(self, func= None, sub1 = None, sub2 = None):
        self.func = func
        self.sub1 = sub1
        self.sub2 = sub2
    
    def __repr__(self):
        return (f'{self.func.nome}')
    
    def salarios(self):
        
        dicionario = {self.func.nome: self.func.salario}
        
        if self.sub1 != None: 
            dicionario.update(self.sub1.salarios())

        if self.sub2 != None:
            dicionario.update(self.sub2.salarios())

        return dicionario  

colaborador_1 = Colaborador(1, 'Colab1', 100, 'Diretor')
colaborador_2 = Colaborador(2, 'Colab2', 200, 'Gerente')
colaborador_3 = Colaborador(3, 'Colab3', 300, 'Desenvolvedor')
colaborador_4 = Colaborador(4, 'Colab4', 400, 'Desenvolvedor')

Empresa = Organograma(func= colaborador_1, 
                      sub1 = Organograma(func = colaborador_2,
                                        sub1 = Organograma(func = colaborador_3), sub2 = Organograma(func = colaborador_4)))

print(Empresa.salarios())