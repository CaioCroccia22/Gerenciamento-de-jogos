#Exercicio final do módulo
#Gerenciamento de jogadores e times
# -> Escreva um código em python que realize o gerenciamento de jogadores
#Siga os requisitos:
#1 - A opção de listar os times deve mostrar o indice , o nome e a quantindade de jogadores
#2 - A opção de adicionar um time deve pedir um nome para o time que será cadastrado
#3 - A opção de remover um time deve pedir o indice especifico do time que foi cadastrado
#4 - A opção de adicionar um jogador em um time deve pedir um indice do time que foi cadastrado
#5 - A opção de remover um jogador em um time deve pedir um indice do time que foi cadastrado e utilizar
#esse indice para remover o jogador cadastrado no time
#6 - A opção de listar os jogadores de um time deve ser informado o indice de um time
# e listar os jogadores que foram associados a ele.

Teams = {}
Team = {}

done = False

def plusTeam():
    name = input("Digite o nome do time:\n")
    players = input("Digite o números de jogadores\n")
    Team["name"] = name
    Team["players"] = players
    print(Team)
    Teams["Team"] = Team


def listTeam():
    


while done == False:
    print("Escolha umas das opções a seguir:\n")
    print("1 - Voce deseja adicionar algum time? \n")
    print("2 - Voce deseja remover algum time? \n")
    print("3 - Voce deseja listar os time? \n")
    print("4 - Voce deseja adicionar jogador do time? \n")
    print("6 - Voce deseja remover jogador do time? \n")
    print("7 - Voce deseja remover jogador do time? \n")
    number = int(input("Digite qual opção você deseja:\n"))
    if number == 1:
        plusTeam()
        done == True