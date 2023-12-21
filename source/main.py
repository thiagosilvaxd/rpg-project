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
    [ 2 ] tentar um chute nas pernas ''')

if escolha == "1":
    print('Você tenta fugir, mas, está muito fraco, então a criatura misteriosa o pega')
    print('Você perdeu')
if escolha == "2":
    print('Você arrisca um chute nas pernas da criatura e por muita sorte, consegue derruba-lo e rapidamente foge da cabana para a floresta mais próxima.')
    print('Você fugiu, mas, percebeu que não poderia enfrentar tal criatura novamente.')
    print('Você se esconde na floresta e tenta sobreviver....')
    print()
    sleep(2)
    print('Após vários dias desde o incidente com a criatura, você finalmente sai da floresta e acha um pequeno vilarejo')
    print('Você adentra no vilarejo e caminha pelo local, tal localidade transparece um sentimento de aconchego e paz')
    print()
    print()    
    sleep(2)
    print('Após vários dias desde o incidente com a criatura, você finalmente sai da floresta e acha um pequeno vilarejo')
    print('Você adentra no vilarejo e caminha pelo local, tal localidade transparece um sentimento de aconchego e paz')
    print()
    print(''' Depois de conversar com o prefeito do vilarejo, você procura um local pra passar a noite....
      Chega em uma tarverna e, então, pede abrigo ao dono.
      "São 50 moedas de cobre a noite e a comida" - diz o dono
      
      Você explica sua situação ao dono da taverna, contando sobre a criatura e como perdeu seus pertences para tal.

      "Entendo, mas, mesmo assim não tem nada que eu possa fazer"

      Você então se oferece para trabalhar na taverca, como troca pela estadia e comida.
      O dono meio relutante, aceita tal oferta. ''')
    print()    
    sleep(2)
    print('''Sua primeira noite começa muito bem, o bar está cheio e animado.
      
      "Desce mais uma" = grita os clientes do bar.
      
      Tudo parecia correr bem, naquela noite. ''')
    print('''Até que chega um grupo de valentões do vilarejo.
      Todo mundo fica em silêncio enquanto eles passam até o balcão.

      "Ai dono dessa espelunca, me desce uma cerveja" - Grita rindo o lider do bando.
      O dono entrega a cerveja e sai para limpar os copos.
      
      "bleh!, que cerveja horrivel!" - grita lider do bando.
      
      Então enfurecido, ele quebra o copo e ameaça o dono da taverna.

      "Você ousa me dar essa porcaria para beber?" - grita enquanto agarra o dono da taverna". ''')
    print(f'{personagem} então, saindo da cozinha da taverna, avista o dono sendo ameaçado e rapidamente tira o dono das mãos do valentão')
    print('"O que você pensa que está fazendo seu verme?" - grita o lider enfurecido.')
    print(f'Sem pensar duas vezes o lider do bando, saca sua clava e parte pra cima do {personagem}')
    print('Sem muitos opções só lhe resta lutar')
    sleep(1)
    opção = input('''
   [ 1 ] atacar na cabeça
   [ 2 ] atacar nas pernas
   [ 3 ] atacar os braços ''')
    if opção == "1":
      print('Você tenta acertar a cabeça dele, mas, ele bloqueia com a clava e te derruba')
      print('Ele ataca você na cabeça com a clava')
      print('VOCÊ MORREU!')
    if opção == "2":
       print('Você acerta um chute nas pernas e consegue desiquilibra-lo, mas, devido ao seu tamanho, ele não cai e te ataca')
       print('Ele consegue te acertar, mas, você desvia por pouco, nisso, você fica muito ferido e morre')
       print('VOCÊ MORREU!')
    if opção == "3":
       print('Você acerta seus braços com um chute e consegue derrubar a clava dele, mas, ele vem pra cima com as mãos e limpa e vocês trocam socos')
       print('Ambos trocam vários socos, até que um dos dois finalmente cai no chão')
       sleep(2)
       print('Só sobrou você em pé!!!')
       print('o bando de valentões então levam seu chefe e ficam resmungando que aquilo não ia ficar assim.')
       print('O dono da taverna agradece você por salva-lo e todos no bar comemoram !')
    

 