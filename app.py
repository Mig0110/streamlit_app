import random
import streamlit as st

presentacion = '''

***************JUEGO DE NICO 👨‍💻********************
*********Piedra Papel Tijeras***********
         🧻  🪨   ✂️

'''

st.write(presentacion)
#user_option = input('Por favor elija Piedra, papel o tijeras : ')
st.header ('Primera App Phyton: ')
options = ['piedra','papel','tijeras']

st.selectbox("Por favor elija una opciòn", options)
user_option=st.selectbox

random_options = (random.randint(0,2))
computer_option = options[random_options]
# st.write(computer_option)

'''
piedra y piedra empate
piedra gana tijeras
papel gana a piedra

papel y papel empate
papel gana a piedra
tijeras gana a papel


tijeras y tijeras empate
tijeras gana a papel
piedra gana a tijeras

'''

st.write(f"Eleccion usuario 👨‍🦰: {user_option}")
st.write(f"Eleccion computador 🤖: {computer_option}")


if user_option.lower() == computer_option:
    st.write("!!Empate!! ")

elif user_option == "piedra":
    if computer_option=="tijeras":
        st.write("Usuario Gana Piedra rompe tijeras")
    else :
        st.write("Computador Gana papel tapa a piedra ☹️")

elif user_option == "papel":
    if computer_option == "tijeras":
        st.write("Computador gana tijeras corta a papel☹️")
    else :
        st.write("Usuario Gana papel tapa a piedra") 

elif user_option == "tijeras":
    if computer_option == "piedra":
        st.write("Computador gana piedra rompe tijeras ☹️")
    else :
        st.write("Usuario Gana tijeras corta papel")

