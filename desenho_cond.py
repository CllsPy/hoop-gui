import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import random
import os


class Desenho_Condutividade:
    def __init__(self, estilo):
        self.graphs = []
        self.estilo = estilo

        sns.set_palette('Paired')
        sns.set_style("whitegrid")
        plt.rcParams['font.size'] = 8
        plt.rcParams['figure.figsize'] = (8, 4)

    def desenha(self, objH, modelo, stats=None,  direcao=None, tresh_hold=None):
        if self.estilo == False: self.estilo = 'fixar_fracao'
        elif direcao == False: direcao = 'K11'

        if objH.analise_tipo == 'condutividade':
            objH.modH = modelo
            
            label = f'Modelo: {objH.modH.tipo}'

            self.K = []
            self.xk = []


            if len(objH.matH) == 2:
                _range = int(objH.fi * 100) if objH.fi * 100 > 0 else 100

                for i in range(0, _range):
                    Fi = i / 100
                    if self.estilo == 'fixar_fracao':
                        self.fixar_fi(objH, modelo, Fi, direcao)
                        plt.title('Condutividade')
                        plt.xlabel('Fração Volumétrica')
                        plt.ylabel(direcao)

            if self.estilo=="fixar_fracao":

                sns.lineplot(x = self.xk, y = self.K, label=label)
                sns.despine(left=True)
                plt.show()
                self.graphs.append((self.xk, self.K, label))

            # este loop é destinado a plotar modelo de três fases
            elif len(objH.matH) == 3:
                    _range = int(objH.fi * 100) if objH.fi * 100 > 0 else 100

                    for i in range(0, _range):
                        Fi = i / 100

                        if self.estilo == 'fixar_fracao_3':
                            self.fixar_fi_nfases(objH, modelo, Fi, direcao)
                            plt.title('Módulo E. Homogeinizado vs. FI')
                            plt.xlabel('Fração Volumétrica de Inclusão')
                            plt.ylabel('Módulo de Elásticidade Homogeinizado')

                    if self.estilo == "fixar_fracao_3":
                        sns.lineplot(x=self.xk, y=self.K, label=label)
                        sns.despine(left=True)
                        plt.show()
                        self.graphs.append((self.xk, self.K, label))


    def fixar_fi_nfases(self, objH, modelo, Fi, direcao):
        if direcao == 'K11': direcao_K = objH.modH.K11
        elif direcao == 'K22': direcao_K = objH.modH.K22
        else: direcao_K = objH.modH.K33

        fiC, fmC = (Fi, Fi - 1)
        objH.analH.fi, objH.analH.fr, objH.analH.fm = (fiC, objH.analH.fr, fmC)
        objH.calc()

        self.K.append(direcao_K)
        self.xk.append(Fi)

    def fixar_fi(self, objH, modelo, Fi, direcao):
        if direcao == 'K11': direcao_K = objH.modH.K11
        elif direcao == 'K22': direcao_K = objH.modH.K22
        else: direcao_K = objH.modH.K33

        objH.analH.fi, objH.analH.fm = (Fi, Fi - 1)
        objH.calc()
        self.K.append(direcao_K)
        self.xk.append(Fi)

    def juntar_grafs(self, objH, stats=False, direcao=False, tresh_hold=None):
        direcao = direcao.upper()

        plt.title('Condutividade')
        plt.xlabel('Fração Volumétrica')
        plt.ylabel(direcao)

        i = 0
        for graph in self.graphs:
            i += 1
            marcadores = ['o', 's', '^', '*', 'x', 'D', 'p', 'h',
                          '+', '|', '.', ',', '1', '2', '3', '4',
                          '<', '>', 'v']

            xk, K, label = graph
            plt.plot(xk, K, label=label,  marker=marcadores[i], markersize=1)
            plt.legend()
            sns.despine(left=True)
            plt.ylim(tresh_hold)
          
        



