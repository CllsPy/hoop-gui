import streamlit as st
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
from homogenizacao import Homogenizacao
from desenho_mec import DesenhoMecanico
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

h1 = Homogenizacao()

st.title("WebApp Hoop - Mecânico")
d = DesenhoMecanico(estilo='fixar_fracao')

h1.tipo = "global"
h1.analise_tipo = 'mecanica'
h1.geo = 'esfera'

fi = st.slider("Escolha a fração", 0, 100, 25)
h1.fi = fi/100

# Campos das variáveis
col1, col2 = st.columns(2)

with col1:
	Em = st.number_input("(E) Material 1: ", min_value=0)
	vm = st.number_input("(v) Material 1: ", min_value=0.0)

with col2: 
	Ei = st.number_input("(E) Material 2: ", min_value=0)
	vi = st.number_input("(v) Material 2: ", min_value=0.0)


h1.Em = Em
h1.vm = vm
h1.vi = vi 
h1.Ei = Ei

h1.set_analise()  

m1 = Mecanico() 
m1.E = h1.Em
m1.v = h1.vm
m1.geo = h1.analH.geo

m2 = Mecanico() 
m2.E = h1.Ei
m2.v = h1.vi
m2.geo = h1.analH.geo

h1.matH.append(m1)
h1.matH.append(m2)


if st.button("Computar"):

	d.desenha(h1, modelo=GSC())
	d.desenha(h1, modelo=SelfConsistent())
	d.desenha(h1, modelo=MoriTanaka())
	d.desenha(h1, modelo=DiluteSuspension())
	d.desenha(h1, modelo=Reuss())
	d.desenha(h1, modelo=Voigt())

	fig, ax = plt.subplots()
	ax = d.juntar_grafs(h1)
	
	st.pyplot(ax)

else:
	error = "Use valores válido!"
	st.write(error)
