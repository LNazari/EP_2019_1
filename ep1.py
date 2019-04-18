# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Fulano da Silva, fulanos@insper.edu.br
# - aluno B: Sicrano de Almeida, sicranoa1@insper.edu.br
import json
import random as randint
#x= bool(randint(0,1))
#pocao_de_vida=100 de vida 
#if pocao_de_vida= "algum lugar do jogo"
    #vida_jogador=100
#print('opa, voce encontrou uma pocao de vida, sua vida voltou aos 100.')
    
vidas= {'vida_jogador': 100,
        'adaga':15,
        'bibliotecaria': 15,
        'monstrinho': 30,
        'monstrao': 60 }


def carregar_inventário():
    with open("Dicionario inventario ep1.json","r") as itens:
        conteudo_itens = itens.read()
    inventario = json.loads(conteudo_itens)
    return inventario




def carregar_cenarios():
    
    with open('Dicionario vida ep1.json','r') as cenario:
        conteudo_cenario = cenario.read()
    cenarios = json.loads(conteudo_cenario)

    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def main():
    print("------------------")
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        titulo= cenario_atual['titulo']
        print(titulo)
        print("-"*len(titulo))
        print()
        print(cenario_atual["descricao"])
        print()
        
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("Escolha sua opção:")
            print()
            for k,v in cenario_atual["opcoes"].items():
                print("{0}: {1}".format(k,v))
            escolha = input("O que você quer fazer? ")
            print()

            if escolha in opcoes:
                
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")



# Programa principal.
if __name__ == "__main__":
    main()
