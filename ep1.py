# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Lucca Nazari da Silva e Souza, luccanss@al.insper.edu.br
# - aluno B: Luca Cazzolato Machado, lucacm@al.insper.edu.br



from pprint import pprint
import json
from random import randint
import time
import sys

#Váriaveis:
atributos_jogador = {
        "hit points": 100,
        "pontos de ataque": 12,
    }

vida_jogador = atributos_jogador["hit points"]
ataque_jogador = atributos_jogador["pontos de ataque"]
defesa_jogador = atributos_jogador["pontos de defesa"]


inventario_jogador = ["carteirinha do insper"]
#adaga = 10 atk points
#escudo = 10 atk points
#poção de vida = restore 100 hit points


#Funções:

def carregar_cenarios():
    with open("Dicionario_Cenarios_EP1.json",'r') as cenario:
        conteudo_cenario = cenario.read()
    cenarios = json.loads(conteudo_cenario)

    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def carregar_monstros():
    monstros = [ 
        {
            "nome": "Bibliotecaria",
            "fala": "Ora ora se não é um forasteiro perdido procurando alguns livros.",
            "premio": "adaga",
            "status": {
                "hit points": 15,
                "pontos de ataque": 5
                }
            },
        {
            "nome": "Veterano",
            "fala": "Hahahaha, eu cursei anoooos de INSPER, acha mesmo que pode me derrotar?????",
            "premio": "chave ss",
            "status": {
                "hit points": 10,
                "pontos de ataque": 2
                }
            },
        {
            "nome": "Fumante",
            "fala": "Cof... Cof... Se você veio pedir um trago, pode ir se preparando pra levar um pe na bunda",
            "premio": "poção de vida",
            "status": {
                "hit points": 5,
                "pontos de ataque": 10
                }
            },
        {
            "nome": "Daniel Guzzo",
            "fala": "Você veio ao FAB LAB, pois bem QUERO UM PROTÓTIPO!",
            "premio": "poção de vida",
            "status": {
                "hit points": 50,
                "pontos de ataque": 20
                }
            },
        {
            "nome": "Paulina",
            "fala": "Iterar e Graficar...",
            "premio": "tapete deslizante",
            "status": {
                "hit points": 65,
                "pontos de ataque": 15
                }
            }
        ]
    return monstros

def carregar_combate():
    monstros = carregar_monstros()
    combate = {
        "luta 0": {
                "titulo": "Parece que uma luta lhe espera! E alguém lhe impede de prosseguir:",
                "nome": monstros[0]["nome"],
                "fala": monstros[0]["fala"],
                "status_monstro": monstros[0]["status"],
                "opcoes": "lutar ou fugir? "
        },
        "luta 1": {
                "titulo": "Parece que uma luta lhe espera! E alguém lhe impede de prosseguir:",
                "nome": monstros[1]["nome"],
                "fala": monstros[1]["fala"],
                "status_monstro": monstros[1]["status"],
                "opcoes": "lutar ou fugir? "
            
        },
        "luta 2": {
                "titulo": "Parece que uma luta lhe espera! E alguém lhe impede de prosseguir:",
                "nome": monstros[2]["nome"],
                "fala": monstros[2]["fala"],
                "status_monstro": monstros[2]["status"],
                "opcoes": "lutar ou fugir? "
            
        },
        "luta 3": {
                "titulo": "Parece que uma luta lhe espera! E alguém lhe impede de prosseguir:",
                "nome": monstros[3]["nome"],
                "fala": monstros[3]["fala"],
                "status_monstro": monstros[3]["status"],
                "opcoes": "lutar ou fugir? "
            
        },
        "luta 4": {
                "titulo": "Parece que uma luta lhe espera! E alguém lhe impede de prosseguir:",
                "nome": monstros[4]["nome"],
                "fala": monstros[4]["fala"],
                "status_monstro": monstros[4]["status"],
                "opcoes": "lutar ou fugir? " 
            
            
        }
    }
    return combate


def jogador(inventario):
    vida_jogador = 100
    ataque_jogador = 12

    inventario_jogador = inventario

    for l in inventario:
        if "adaga" in inventario_jogador:
            ataque_jogador += 10


    return vida_jogador, ataque_jogador

def luta(i):
    monstros= carregar_monstros()
    x,y = jogador(inventario)
    vida_monstros = monstros[i]["status"]["hit points"]
    vida_jogador = x
    ataque_jogador = y
    ataque_monstro = monstros[i]["status"]["pontos de ataque"]

    contador_da_vez= randint(1,2)
    
    while vida_monstros >0 and vida_jogador>0:
        if contador_da_vez%2 == 0: #vez do jogador
            print("Sua vez de atacar")
            print()
            print("Você causou {0} de dano".format(ataque_jogador))
            vida_monstros= vida_monstros + defesa_monstros - ataque_jogador
            if vida_monstros < 0:
                vida_monstros = 0
                print("O monstro morreu")
            print ("A vida do monstro ficou: {0}".format(vida_monstros))
            print()
   
        elif contador_da_vez%2 !=0:
            print("É a vez do monstro de atacar")
            print()
            print("O monstro causou {0} de dano".format(ataque_monstro))
            vida_jogador= vida_jogador + defesa_jogador - ataque_monstro
            if carregar_atributos(atributos_jogador, inventario_jogador, i)["hit points"] < 0:
                carregar_atributos(atributos_jogador, inventario_jogador, i)["hit points"] = 0
                print("Voce morreu")
                game_over = True
            print("Após o ataque do monstro, sua vida ficou: {0}".format(vida_jogador))
            print()
            
            
        contador_da_vez+=1
    return vida_jogador




def main():
    jogador = input("Diga seu nome aventureiro: ")
    print()
    print("Olá {0}, seus atributos são {1} e você começa com sua carteirinha do Insper em seu inventário".format(jogador, atributos_jogador))
    print()
    pronto= input("voce esta pronto?: ")
    print("Vamos comecar")
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
    combate = carregar_combate()
    monstros = carregar_monstros()
    
    contador_biblioteca=0
    contador_aquarios=0
    contador_fumodromo=0
    contador_fablab=0
    contador_objeto=0

    game_over = False
    while not game_over:

        if atributos_jogador["hit points"]==0: #alterar pra conceito de vida (hit points + defesa)
            break
        cenario_atual = cenarios[nome_cenario_atual]
        cenario_anterior= nome_cenario_atual

        titulo= cenario_atual['titulo']
        print()
        print(titulo)
        print("-"*len(titulo))
        print()
        print(cenario_atual["descricao"])
        print()
        print("Seu inventário:", inventario_jogador)
        
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
            
            cenario_anterior= nome_cenario_atual
            nome_cenario_atual=escolha
            
            if escolha not in opcoes:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                

            if contador_biblioteca==0 or contador_aquarios==0 or contador_fablab==0 or contador_fumodromo==0 or contador_objeto==0:
                if escolha == "biblioteca" and contador_biblioteca==0:
                    print(combate["luta 0"]["titulo"])
                    print()
                    print(combate["luta 0"]["nome"])
                    print()
                    print(combate["luta 0"]["fala"])
                    print(combate["luta 0"]["nome"], ":", combate["luta 0"]["status_monstro"])
                    print(jogador, ":", atributos_jogador)
                    choice = input("O que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(luta(0))
                        print()
                        print("Parece que esse monstro deixou um prêmio para você:", monstros[0]["premio"])
                        print("Este item adiciona 10 pontos de ataque ao seu avatar")
                        inventario_jogador.append(monstros[0]["premio"])
                        contador_biblioteca+=1  
                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                
                elif escolha== "aquarios" and contador_aquarios==0:
                    print(combate["luta 1"]["titulo"])
                    print()
                    print(combate["luta 1"]["nome"])
                    print()
                    print(combate["luta 1"]["fala"])
                    print(combate["luta 1"]["nome"], ":", combate["luta 1"]["status_monstro"])
                    print(jogador, ":", carregar_atributos(atributos_jogador, inventario_jogador, i))
                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(luta(1))
                        print()
                        print("Parece que esse monstro deixou um prêmio para você:", monstros[1]["premio"])
                        print("Este item lhe permite acesso à sala secreta")
                        inventario_jogador.append(monstros[1]["premio"])                       
                        contador_aquarios+=1  
                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                        
                elif escolha == "fumodromo" and contador_fumodromo==0:
                    print(combate["luta 2"]["titulo"])
                    print()
                    print(combate["luta 2"]["nome"])
                    print()
                    print(combate["luta 2"]["fala"])
                    print(combate["luta 2"]["nome"], ":", combate["luta 2"]["status_monstro"])
                    print(jogador, ":", carregar_atributos(atributos_jogador, inventario_jogador, i))
                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(luta(2))
                        print()
                        print("Parece que esse monstro deixou um prêmio para você:", monstros[2]["premio"])
                        print("Este item recupera sua vida em 100 hit points")
                        inventario_jogador.append(monstros[2]["premio"])                       
                        contador_fumodromo+=1  
                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                        
                elif escolha == "fablab" and contador_fablab==0:
                    print(combate["luta 3"]["titulo"])
                    print()
                    print(combate["luta 3"]["nome"])
                    print()
                    print(combate["luta 3"]["fala"])
                    print(combate["luta 3"]["nome"], ":", combate["luta 3"]["status_monstro"])
                    print(jogador, ":", carregar_atributos(atributos_jogador, inventario_jogador, i))
                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(luta(3))
                        print()
                        print("Parece que esse monstro deixou um prêmio para você:", monstros[3]["premio"])
                        print("Este item permite você ter acesso ao toboga multidimensional")
                        inventario_jogador.append(monstros[3]["premio"])                      
                        contador_fablab+=1  
                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True              
                elif escolha == "objeto" and contador_objeto==0:
                    print(combate["luta 4"]["titulo"])
                    print()
                    print(combate["luta 4"]["nome"])
                    print()
                    print(combate["luta 4"]["fala"])
                    print(combate["luta 4"]["nome"], ":", combate["luta 4"]["status_monstro"])
                    print(jogador, ":", carregar_atributos(atributos_jogador, inventario_jogador, i))
                    choice = input("o que deseja fazer: 'lutar' ou 'fugir'? ")
                    if choice == "lutar":
                        print(luta(4))
                        print()
                        print("Parece que esse monstro deixou um prêmio para você:", monstros[4]["premio"])
                        print("Este item permite você ter acesso para usar o toboga multidimensional para todos lugares")
                        inventario_jogador.append(monstros[0]["premio"])                       
                        contador_objeto+=1  
                    elif choice == "fugir":
                        nome_cenario_atual = cenario_anterior
                        print()
                        print("Você voltou para o cenário anterior")
                        print()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                    
                

                        
                 
            
            
            
            
            
            else:
                if escolha in opcoes:
                    if escolha == "objeto" and "tapete deslizante" in inventario:
                        nome_cenario_atual=escolha
                    
            
    morte = "Voce morreu!\n"
    for l in morte:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)

                

# Programa principal.
if __name__ == "__main__":
    main()

#ideias, para acessar a sala real do andrew somente pelo toboga e ai comecaria a boss fight final
#para acessar o toboga ele precisa dos seguintes itens em seu inventario = tapete deslizante
#quando usar o toboga para chegar a sala real do andrew vai ser feito uma condicao para ver se ele tem os itens necessarios
#se ele tiver a luta começa e ai ele pode escolher se quer usar pocao de vida ou nao
#o andar professor serve somente para recreação e o jogador pode encontrar itens la, como: poção de vida.