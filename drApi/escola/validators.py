from validate_docbr import CPF

def validate_cpf(cpf):     
    numero_cpf = CPF()
    return numero_cpf.validate(cpf) 
    
def validate_nome(nome):
    return  nome.isalpha()

def validate_rg(rg):   
    return len(rg) == 9