from random import sample
from time import sleep

sorteio = sample(range(0, 60), 6)
l1 = []

print("")
print("\033[1;33m----- MEGA SENA SIMULADOR  -----\033[m")
print("\033[1;90m-------------------------------\033[m")
print("\033[1;30mVocê precisa escolher 6 dezenas entre 01 e 60.\033[m")

while True:
    dezena1 = input("Primeira dezena: ")

    if len(dezena1) != 2:
        print('\033[1;31mDezenas possuem 2 algarismos. Digite novamente!\033[m')
    elif (int(dezena1) > int(60)):
        print('\033[1;31mAs dezenas precisam ser entre 01 e 60\033[m')
        dezena1 = input("Primeira dezena: ")
    else:
        break

while True:
    print("\033[1;90m-------------------------------\033[m")
    dezena2 = input("Segunda dezena: ")
    if len(dezena2) != 2:
        print('\033[1;31mDezenas possuem 2 algarismos. Digite novamente.\033[m')
    elif (int(dezena2) > int(60)):
        print('\033[1;31mAs dezenas precisam ser entre 01 e 60. Digite novamente.\033[m')
    else:
        break

while True:
    print("\033[1;90m-------------------------------\033[m")
    dezena3 = input("Terceira dezena: ")
    if len(dezena3) != 2:
        print('\033[1;31mDezenas possuem 2 algarismos. Digite novamente!\033[m')
    elif (int(dezena3) > int(60)):
        print('\033[1;31mAs dezenas precisam ser entre 01 e 60. Digite novamente!\033[m')
    else:
        break

while True:
    print("\033[1;90m-------------------------------\033[m")
    dezena4 = input("Quarta dezena: ")
    if len(dezena4) != 2:
        print('\033[1;31mDezenas possuem 2 algarismos. Digite novamente:\033[m')
    elif (int(dezena4) > int(60)):
        print('\033[1;31mAs dezenas precisam ser entre 01 e 60. Digite novamente!\033[m')
    else:
        break

while True:
    print("\033[1;90m-------------------------------\033[m")
    dezena5 = input("Quinta dezena: ")
    if len(dezena5) != 2:
        print('\033[1;31mDezenas possuem 2 algarismos. Digite novamente!\033[m')
    elif (int(dezena5) > int(60)):
        print('\033[1;31mAs dezenas precisam ser entre 01 e 60. Digite novamente!\033[1;31m')
    else:
        break

while True:
    print("\033[1;90m-------------------------------\033[m")
    dezena6 = input("Sexta dezena: ")
    print("\033[1;90m-------------------------------\033[m")
    if len(dezena6) != 2:
        print('\033[1;31mDezenas possuem 2 algarismos. Digite novamente!\033[m')
    elif (int(dezena6) > int(60)):
        print('\033[1;31mAs dezenas precisam ser entre 01 e 60. Digite novamente!\033[m')
    else:
        break

escolhidos = [int(dezena1), int(dezena2), int(dezena3), int(dezena4), int(dezena5), int(dezena6)]
sleep(1)
print("Aguarde...")
sleep(3)
print("\033[1;90m-------------------------------\033[m")
print("\033[1;30mOs números sorteados foram: \033[m \033[1;33m", sorteio)
print("\033[1;90m-------------------------------\033[m")
print("\033[1;30mVocê escolheu:\033[m \033[1;33m", escolhidos)
print("\033[1;90m-------------------------------\033[m")

def findDuplicate(self, nums):
    hare = nums[0]
    tortoise = nums[0]
    while True:
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]
        if hare == tortoise:
            break
    ptr = nums[0]
    while ptr != tortoise:
        ptr = nums[ptr]
        tortoise = nums[tortoise]
    return ptr

def L3():
    for i in sorteio:
        if i in escolhidos:
            l1.append(i)
    return l1

if L3() == []:
    print('\033[1;31mNão foi dessa vez!\033[m')
else:
    print("\033[1;30mO numeros em comum foram: \033[m \033[1;33m", l1)

if (len(l1) == 1):
    print("\033[1;33mVocê acertou 1 dezena!\033[m")
    print("\033[1;96mPrêmio: R$ 1000,00\033[m")
elif (len(l1) == 2):
    print("\033[1;33mVocê acertou 2 dezenas!\033[m")
    print("\033[1;96mPrêmio: R$ 2000,00\033[m")
elif (len(l1) == 3):
    print("\033[mVocê acertou 3 dezenas!\033[m")
    print("\033[1;96mPrêmio: R$ 3000,00\033[m")
elif (len(l1) == 4):
    print("\033[mVocê acertou 4 dezenas!\033[m")
    print("\033[1;96mPrêmio: R$ 4000,00\033[m")
elif (len(l1) == 5):
    print("\033[mVocê acertou 5 dezenas!\033[m")
    print("\033[1;96mPrêmio: R$ 5000,00\033[m")
elif (len(l1) == 6):
    print("\033[1;96mParabéns! Você ganhou o prêmio máximo!\033[m")
    print("\033[1;96mValor: R$ 1.000.000\033[m")