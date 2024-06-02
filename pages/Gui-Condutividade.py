import streamlit as st

import matplotlib.pyplot as plt
from homogenizacao import Homogenizacao
from mecanico import Mecanico
from condutividade import Condutividade
from voigt import Voigt
from hashin_inf import Hashin_Inf
from hashin_sup import Hashin_Sup
from reuss import Reuss
from dilute import DiluteSuspension
from couto import Counto
from moritanaka import MoriTanaka
from selfconsistent import SelfConsistent
from gsc import GSC
from d_f import DifferentialScheme
from maxwelleucken import MaxwellEucken
from campbell import Campbell
from hamilton import Hamilton
from popovic import Popovic
from desenho_cond import Desenho_Condutividade

h1 = Homogenizacao()
d = Desenho_Condutividade(estilo="fixar_fracao")

h1.tipo = "global"
h1.analise_tipo = 'condutividade'
h1.geo = 'esfera'

fi = st.slider("Escolha a fração", 0, 100, 25)
h1.fi = fi/100

h1.fi = fi
#h1.fr =  0.1
#h1.fm = 0.5

col1, col2 = st.columns(2)

with col1:
	k11 = st.number_input("(K11) Material 1: ", min_value=0.0)
	k22 = st.number_input("(K22) Material 1: ", min_value=0.0)
	k33 = st.number_input("(K33) Material 1: ", min_value=0.0)

	m1 = Condutividade() # modelo material
	m1.k11 = 0.31
	m1.k22 = 0.51
	m1.k33 = 0.91

with col2: 
	k11 = st.number_input("(K11) Material 2: ", min_value=0.0)
	k22 = st.number_input("(K22) Material 2: ", min_value=0.0)
	k33 = st.number_input("(K33) Material 2: ", min_value=0.0)
	
	m2 = Condutividade() # modelo material
	m2.k11 = 0.21
	m2.k22 = 0.11
	m2.k33 = 0.41
	

h1.set_analise()

h1.matH.append(m1)
h1.matH.append(m2)

if st.button("Computar"):

	d.desenha(h1, modelo=GSC())
	d.desenha(h1, modelo=SelfConsistent())
	d.desenha(h1, modelo=MoriTanaka())
	d.desenha(h1, modelo=DiluteSuspension())

	fig, ax = plt.subplots()
	ax = d.juntar_grafs(h1, direcao='K11')

	st.pyplot(ax)


else:
	error = "Use valores válido!"
	st.write(error)
