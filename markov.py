# coding: utf-8

__author__ = "Paulo Sérgio dos Santos Araujo"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "paulo.araujo [at] splab.ufcg.edu.br"

def mm1k(K, lamda, mi, p0):
    p1 = p0 * lamda/mi 
    for i in range(0, K + 1):
        print("PK(%d) = %.12lf" % (i, p0))
        p2 = (p1 * (mi + lamda) - p0* lamda) / mi
        p0, p1 = p1, p2

mm1k(5, 0.5, 0.6, 1.0)