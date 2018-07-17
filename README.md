# Trajetória-orbital-de-massas
Resolução de equações de movimento para 3 massas em um campo gravitacional através do método de Runge–Kutta de 4ª ordem.


Consideremos três massas, M1, M2 e M3. Cada massa sentirá o campo gravitacional das outras duas, ou seja,
cada massa está em um campo gravitacional gerado por duas duas massas vizinhas.

O projeto consiste em dezudir as equações de movimento para as três massas através das leis de Newton,
onde o campo de força que atua em cada partícula consiste no sentido oposto do vetor gradiente do 
potencial gravitacional.

Em seguida as três equações de movimento das partículas é resolvida através do método de Runge-Kutta de 4ª
ordem, sendo assim, obtemos a posição da parícula para cada instante de tempo.

Para a execução do algoritmo, é necessário a instação dos pacotes numpy, pylab, e vpython.

O pacote vpython é utilizado para realizar simulações físicas, nesse projeto, utilizou-se para demonstrar
o movimento das três massas.

O pacote vpython está disponível em: http://vpython.org/
