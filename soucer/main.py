from time import sleep

print('''
      Olá, essa é uma história de um herói que após sobreviver a uma terrivel guerra perdeu sua memória...
      Gravemente ferido devido a guerra com os guerreiros do vazio, ele descansa em uma cabana...
      finalmente depois de um longo tempo, ele acorda assustado, pois, não se lembra de nada...''')
sleep(2)
print()
print('''Aos poucos você vai se recordando de quem você é....
      Então você se lembra que seu nome é...''')

personagem = input('Qual é o seu nome? ')

print(f' "Você se chama {personagem}" - disse uma voz ao fundo da cabana...') 
print(''' " Quem está ai? " - você grita assustado e percebe que suas mãos estão cobertas de sangue.
      "ha, ha, ha" - ri um ser misterioso enquanto se levanta e vai em sua direção.
      rapidamente você se levanta e tenta sacar sua espada, mas, percebe que não está mais com você, e só lhe restam duas opções.''')
print()
sleep(2)

escolha = input('''Qual opção seguir? 
    [ 1 ] fugir           
    [ 2 ] tentar um chute nas pernas''')

if escolha == "1":
    print('Você tenta fugir, mas, está muito fraco, então a criatura misteriosa o pega')
    print('Você perdeu')
elif escolha == "2":
    print('Você arrisca um chute nas pernas da criatura e por muita sorte, consegue derruba-lo e rapidamente foge da cabana para a floresta mais próxima.')
    print('Você fugiu, mas, percebeu que não poderia enfrentar tal criatura novamente.')
    

 