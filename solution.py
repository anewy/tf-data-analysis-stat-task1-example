import pandas as pd
import numpy as np


chat_id = 381099717 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x_median = np.median(x)
    t = 29
    a = (2 * x_median) / (t ** 2)
    return a # Ваш ответ

#def solution(x: np.array, n: int) -> tuple:
    # Вычисляем среднее значение пройденного расстояния, медиана лучше подходит для распределния Лапласа
    #x_median = np.median(x)
    #t = 29
    #a = (2 * x_median) / (t ** 2)
    
    # Вычисляем MSE на выборке размера n
   # mu, scale = 10, 1
   # x_sample = np.random.laplace(mu, scale, n)
   # a_sample = 2 * x_sample / (t ** 2)
   # mse = np.mean((a_sample - a) ** 2)
    
   # return a, mse
#checkers = [0.00000126, 3.40e-7, 1.18e-7]
#for n, c in zip([10,100,1000],checkers):
#    print(n,solution(x_creation(n),n)[1],c, solution(x_creation(n),n)[1]<=c, sep='   ')
#OUT:
#10   2.850580532878075e-06   1.26e-06   False
#100   8.947294938577117e-06   3.4e-07   False
#1000   1.108588462916965e-05   1.18e-07   False
