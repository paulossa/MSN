# coding: utf-8
import sys

__author__ = "Paulo Sérgio dos Santos Araujo"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "paulo.araujo@splab.ufcg.edu.br"

class Msn:
    """
    Essa classe feita para disciplina de Métodos de Software Númericos - UFCG 2018.2 
    se propõe a encontrar as raízes de uma certa equação definida por um usuário. 

    Parameters
    ----------
    eq : str        Equação a ser avaliada deve ser expressa em termos de 'x', pode usar funções de python. 
    tol : float     Tolerância da precisão do MSN.
    alg: string     String contendo qual algoritmo deve ser executado 'bisection' ou 'false_position'
    """
    def __init__(self, eq, tol, alg="false_position"):
        self.eq = eq
        self.tol = tol
        self.alg = alg

    def f(self, x):
        return eval(self.eq)

    def findRoots(self, a, b):
        """
        Encontra as raízes da função no intervalo A, B
        """
        if abs(b-a) >= self.tol and (self.f(a) * self.f(b) > 0):
            mid = (a + b) * .5
            self.findRoots(a, mid)
            self.findRoots(mid, b)
        else:
            iterNum = 1
            while abs(b - a) > self.tol :
                if self.alg == "bisection":         estimate = (a + b) * .5
                elif self.alg == "false_position":  estimate = (a*(self.f(b)) - b * (self.f(a))) / (self.f(b) - self.f(a))
                else:
                    print('Algoritmo não definido')
                    exit(0)
                if (self.f(a) * self.f(estimate) > 0):  a = estimate 
                else:                                   b = estimate
                iterNum += 1
            print(estimate) 
            print(iterNum) 

if __name__ == "__main__":
    msn = Msn(eq="-x**2 + 3", tol=0.01, alg="false_position")
    msn.findRoots(-2, 3) # -1.7320508075688774 e 1.7320508075688776

    msn2 = Msn(eq="-x**2 + 3", tol=0.01, alg="bisection") 
    msn2.findRoots(-2, 3) # -1.736328125 e 1.740234375