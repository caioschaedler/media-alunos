'''tera uma lista de alunos com as notas de b1 e b2 um menu para selecionar a opção
1 - adiocionar aluno
2 - listar aluno
3 - remover aluno
4 - procurar aluno
5 - aprovados
6 - reprovados
7 - procurar por aluno
8 - media da turma b1
9 - media da turma b2
10 - media da turma geral
0 - sair
'''

alunos = {}

def menu():
    print('1 - adiocionar aluno')
    print('2 - listar aluno')
    print('3 - remover aluno')
    print('4 - procurar aluno')
    print('5 - aprovados')
    print('6 - reprovados')
    print("7 - procurar por aluno")
    print("8 - media da turma B1")
    print("9 - media da turma B2")
    print("10 - media da turma geral")
    print("11 - diário da turma")
    print('0 - sair')
    try:
        opt = int(input('digite a opção: '))
        return opt 
#    except KeyboardInterrupt:
#        print("deu pau no teclado")
#    except ValueError:
#        print("numero digitado errado")
    except Exception as e:
        print(f"opção inválida! {e}")
        return 9
#    finally:
#        print("mostra isso!")
        
def add_aluno():
    try:
        ra = input("digite o RA do aluno: ")
        nome = input("digite o nome do aluno: ")
        nota_b1 = float(input("digite a nota b1 do aluno:"))
        nota_b2 = float(input("digite a nota b2 do aluno: "))
        dados = {"nome": nome, 'b1':nota_b1, 'b2':nota_b2}
        alunos[ra] = dados
    except Exception as e:
        print(f"informação digitada errada! {e}")
    return 9

def listar_aluno():
    for ra, dados in alunos.items():
        print(f'RA: {ra} - nome: {dados['nome']} - B1: {dados['b1']} - B2{dados['b2']}')
        
    input("pressione qualquer tecla para continuar")

def remover_aluno():
    ra = input("digite o RA do aluno: ")
    if ra in alunos:
        aluno = alunos.pop(ra)
        print(f"O aluno: {aluno['aluno']} foi removido")
    else:
        print("aluno não encontrado !")
    input("pressione qualquer tecla para continuar")
    
def procurar_alunos():
    ra = input("digite o RA do aluno: ")
    if ra in alunos:
        dados = alunos[ra]
        print(f"RA: {ra} - nome:{dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']} ")
    else:
        print("aluno não encontrado!")
    input("pressione qualquer tecla para continuar")

def aprovados():
    for ra, dados in alunos.items():
        media = (dados['b1'] + dados['b2']) / 2
        if((dados["b1"] + dados["b2"]) / 2) < 7.0:
            aluno = f"RA: {ra} - "
            aluno += f"nome: {dados["nome"]} - "
            aluno += f"B1: {dados["b1"]} - "
            aluno += f"B2: {dados["b2"]} - "
            print(aluno)
            input("pressione qualquer tecla para continuar")

def reprovados():
    for ra, dados in alunos.items():
        if((dados["b1"] + dados["b2"]) / 2) > 6.9:
            aluno = f"RA: {ra} - "
            aluno += f"nome: {dados["nome"]} - "
            aluno += f"B1: {dados["b1"]} - "
            aluno += f"B2: {dados["b2"]} - "
            print(aluno)
            input("pressione qualquer tecla para continuar")
            
def procurar_nome():
    nome = input("Digite o nome do aluno: ") 
    nome = nome.upper
    for ra, dados in alunos.items():
        if (dados['nome'].upper() == nome):
            aluno = f"aluno encontrado - RA {ra} - "
            aluno += f"nome: {dados["nome"]} - "
            aluno += f"B1: {dados["b1"]} - "
            aluno += f"B2: {dados["b2"]} "
            print(aluno)
            break
    input("Pressione qualquer tecla para continuar") 

def media_b1():
    soma= 0 
    qtd = 0 
    for dados in alunos.values():
        soma += dados['b1']
        qtd += 1
    media = soma / qtd
    print(f"a media de B1 é : {media:.2f}")
    input("Pressione qualquer tecla para continuar")

def media_b2():
    soma= 0 
    qtd = 0 
    for dados in alunos.values():
        soma += dados['b2']
        qtd += 1
    media = soma / qtd
    print(f"a media de B2 é : {media:.2f}")
    input("Pressione qualquer tecla para continuar")
    
def media_geral():
    total = 0  
    soma = 0 
    for dados in alunos.items(): 
        total += (dados['b1'] + dados['b2']) 
        soma += 1 
    if soma > 0:
        media = total / (2 * soma)  
        print(f"Média geral da turma: {media}")
    input("Pressione qualquer tecla para continuar") 

def diario_turma():
    print("--------------------------------------------------------")
    print("                   Diario da turma                      ")
    print("--------------------------------------------------------")
    print("RA    Nome                      Nota B1  Nota B2   Média")
    print("--------------------------------------------------------")
    for ra, dados in alunos.items():
        nome = dados['nome'][:27].ljust(27)
        nota_b1 = f"{dados['b1']:.2f}".ljust(5)
        nota_b2 = f"{dados['b2']:.2f}".ljust(5)
        media = f"{(dados['b1'] + dados['b2']) / 2:.2f}".ljust(5)
        print(ra.ljust(6), nome, nota_b1, nota_b2, media)
    print("--------------------------------------------------------")
    print("                  Médias da Turma")
    print("--------------------------------------------------------")
    print("Média B1:".ljust(37), f"{calcular_media_b1():.2f}".ljust(5))
    print("Média B2:".ljust(37), f"{calcular_media_b2():.2f}".ljust(5))
    print("Média Geral:".ljust(37), f"{calcular_media_geral():.2f}".ljust(5))

def calcular_media_b1():
    total = 0
    qtd = 0
    for dados in alunos.values():
        total += dados['b1']
        qtd += 1
    if qtd == 0:
        return 0
    else:
        return total / qtd

def calcular_media_b2():
    total = 0
    qtd = 0
    for dados in alunos.values():
        total += dados['b2']
        qtd += 1
    if qtd == 0:
        return 0
    else:
        return total / qtd

def calcular_media_geral():
    total = 0
    qtd = 0
    for dados in alunos.values():
        total += (dados['b1'] + dados['b2']) / 2
        qtd += 1
    if qtd == 0:
        return 0
    else:
        return total / qtd

if __name__ == '__main__':
    while True:
        match menu():
            case 1:
                add_aluno()
            case 2:
                listar_aluno()
            case 3:
                remover_aluno()
            case 4:
                procurar_alunos()
            case 5:
                aprovados()
            case 6:
                reprovados()
            case 7:
                procurar_nome()
            case 8:
                media_b1()
            case 9:
                media_b2()
            case 10:
                media_geral()
            case 11:
                diario_turma()
            case 0:
                break
