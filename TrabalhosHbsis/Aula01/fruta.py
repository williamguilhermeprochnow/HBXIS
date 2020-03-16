import random
lista = ['banana','jabuticaba','pitanga','mirtilo','morango','abacaxi','cereja']


class Forca:
    def __init__(self):
        self.fruta = random.choice(lista)
        self.letra = ''
        self.quantidade_de_letra = len(self.fruta)

    def escolher_letra(self):
        lista_letras_citadas = []
        tentativas = 0
        print(f'Aquantidade de letra que tem na palvra selcionada é: {self.quantidade_de_letra}')
        self.letra = input('Digite uma letra: ')
        for i in range(len(self.fruta)):
            if self.letra in lista_letras_citadas:
                print('ESTÁ LETRA JA FOI CITADA! Digite outra letra...')
                self.letra = ''
                continue
            lista_letras_citadas.append(self.letra)
            if self.letra in self.fruta:
                print('Continue...')
                self.letra = input('ESCOLHA A PRÓXIMA LETRA: ')
                continue
            else:
                print('VOCÊ ERROU A LETRA OU...')
                tentativas += 1
                if tentativas == 15:
                    print(f'Você perdeu :(')
                    print(f'A palavra era {self.fruta}')
                    exit()
        print()

f = Forca()
f.escolher_letra()
