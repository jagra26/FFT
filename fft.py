import cmath as cm
import numpy as np
import math as m
import matplotlib.pyplot as plt 
from cmath import exp, pi, sin, cos
def fft(x):
  N = len(x)
  if N == 1: return x
  else:
    Wn = exp(2*pi*complex(0,1)/N)
    W = 1 
    y1 = []
    y2= []
    yeven = []
    yodd = []
    for j in range(N):
      if j%2 == 0: 
        yeven.append(x[j])
      else:
        yodd.append(x[j])
    even = fft(yeven)
    odd =  fft(yodd)
    for j in range(min(len(even), len(odd))):
      y1.append(even[j] + W*odd[j])
      y2.append(even[j] - W*odd[j])
      W = W*Wn
    return y1+y2

m = 10 # define o número de amostras e o tamanho do sinal 
N = pow(2, m) # o tamanho do sinal é obrigatoriamente uma potência de 2 quando se usa a fft
fs = 1000 # frequência
T = 1/fs # periodo
time = []
i = 0
for x in range(0, N): # preenche o vetor de tempo
	time.append(i)
	i += T
sinal = []
sinal_real = []

for t in time:
  sinal.append(0.7*sin(2*pi*50*t)+ sin(2*pi*120*t)) # define um sinal complexo qualquer
for a in sinal:
  sinal_real.append(abs(a)) # transforma o sinal em real para plotar na escala do tempo
sinal_transformado = fft(sinal) # chama a transformada
amplitude = []
for x in range(0,N//2):
	amplitude.append(abs(sinal_transformado[x])) # preenche o vetor de amplitudes
frequencia = np.linspace(0.0, 1.0/(2.0*T), N/2) # preenche o vetor de frequências
# plotagem
plt.figure(1)
plt.plot(time, sinal_real)
plt.xlabel('Tempo(s)')
plt.ylabel('Sinal')
plt.title('Antes da transformada')
plt.figure(2)
plt.title('Após a transformada')
plt.xlabel('Frequência(Hz)')
plt.ylabel('Amplitude')
plt.plot(frequencia, amplitude)
plt.show()

''' Referências
https://www.mathworks.com/help/matlab/ref/fft.html
https://docs.python.org/3/library/cmath.html
https://matplotlib.org/tutorials/introductory/pyplot.html
http://people.scs.carleton.ca/~maheshwa/courses/5703COMP/16Fall/FFT_Report.pdf
https://rosettacode.org/wiki/Fast_Fourier_transform#Python
'''