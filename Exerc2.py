#Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
#Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
#Entrada
#Quatro números inteiros representando a hora de início e fim do jogo.
#Saída
#Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

horaInicio = int(input("Hora de inicio:"))
minutosInicio = int(input("Minuto de inicio:"))

horaFim = int(input("Hora do fim:"))
minutosFim = int(input("Minuto do fim:"))


minutosInicio += horaInicio*60
minutosFim += horaFim*60

tempo = minutosFim-minutosInicio
if tempo<=0:
  tempo += 24*60

horas = tempo//60
minutos = tempo%60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")