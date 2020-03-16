import random

class Cartas:
    def __init__(self,cartas):
        self.cartas=cartas

    def embaralhar_cartas(self,cartas):
        num_cartas=13
        cartas_embaralhadas=[]
        for i in range(0,num_cartas):
            a = random.choice(cartas)
            cartas.remove(a)
            cartas_embaralhadas.append(a)
        return cartas_embaralhadas

    def conversao_cartas(self,carta):
        if carta == 'Q' or carta == 'J' or carta == 'K' or carta== 'A':
            return 10
        return carta

class Jogador:
    def __init__(self,cartas_viradas):
        self.cartas_viradas=cartas_viradas

    def virar_carta(self, cartas_embaralhadas):
        cartas_viradas = []
        pegar_carta = cartas_embaralhadas[0]
        cartas_viradas.append(pegar_carta)
        cartas_embaralhadas.pop(0)
        return cartas_viradas

class Mesa:
    # def __init__(self,jogador,cartas):
    #     self.jogador = Jogador
    #     self.cartas = Cartas(['a'])

    def Pegar_carta(self,jogador):
        pass

    def Jogo(self,cartas,jogador,cartas_embaralhadas):

        continuar_jogo = True
        contador = 0
        cartas_escolhidas = jogador.cartas_viradas

        while continuar_jogo:
            continua = True
            cartas_do_jogador = jogador.virar_carta(cartas_embaralhadas)
            print(f"Você pegou a carta {cartas_do_jogador} ")

            cartas_do_jogador_int = (cartas.conversao_cartas(cartas_do_jogador[0]))
            cartas_escolhidas.append(int(cartas_do_jogador_int))

            if cartas_escolhidas[0] == 'A':
                contador += 11
            else:
                contador += int(cartas_do_jogador_int)
            print(f'Cartas na mão: {cartas_escolhidas}')
            print(f"A soma da suas cartas vale: {contador}")


            if contador == 21:
                print("Parabens, você ganhou o jogo")
                break
            if contador > 21:
                print("Voce perdeu o jogo")
                break
            else:
                x=input("Pegar mais uma carta? (y/n): ")
                if x == 'y' or x=="Y":
                    continue
                if x =='n' or x=="N":
                    print("n")
                    break
                else:
                    while x != 'y' or x != 'n':
                        print('insira y ou n')
                        x = input("Pegar mais uma carta? y/n ")
                        if x == 'y' or x=="Y":
                            break
                        if x =='n' or x=="N":
                            continuar_jogo = False
                            print("perdeu")
                            break

jogador=Jogador([])
cartas=Cartas(['2','3','4','5','6','7','8','9','10','A','J','Q','K'])
mesa = Mesa
cartas_baralho=cartas.cartas
cartas_escolhidas = jogador.cartas_viradas
cartas_embaralhadas = cartas.embaralhar_cartas(cartas_baralho)



mesa.Jogo(mesa,cartas,jogador,cartas_embaralhadas)