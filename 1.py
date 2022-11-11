#Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
#N может быть любой длины.
#N = 132:132 + 132132 + 132132132 = 132264396


 number = list(number)

 N = ''
 for i in number:
     N += i

 NN = N + N
 NNN = NN + N

 Ansver = int(N) + int(NN) + int(NNN)
 print(Ansver)
