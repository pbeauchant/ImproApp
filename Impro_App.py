import streamlit as st
import numpy as np
import requests
import json

st.markdown("# L'impro App")


list_lieu = np.genfromtxt('lieu.csv', delimiter=',', dtype=str, encoding = 'utf8')
list_action = np.genfromtxt('action.csv', delimiter=',', dtype=str, encoding = 'utf8')
list_emotion = np.genfromtxt('emotion.csv', delimiter=',', dtype=str, encoding = 'utf8')
list_metier = np.genfromtxt('metier.csv', delimiter=',', dtype=str, encoding = 'utf8')
list_objet = np.genfromtxt('objet.csv', delimiter=',', dtype=str, encoding = 'utf8')

def display_gif(word1,word2):
    # set the apikey
    apikey = st.secrets["apikey"]
    image_holder = st.empty()

    # get the GIF's id and search used
    search_term = f"{word1} {word2}"

    r = requests.get(
        "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, 1))

    if r.status_code == 200:
        pass
        # move on
    else:
        pass
        # handle error
    myGif = json.loads(r.content)
    #st.json(myGif['results'][0]['media'][0])
    image_holder.image(myGif['results'][0]['media'][0]['gif']['url'])
    return

if st.button('5, 4, 3, 2, 1... IMPRO :'):
    metier = np.random.choice(list_metier,1)[0]
    lieu = np.random.choice(list_lieu,1)[0]
    action = np.random.choice(list_action,1)[0]
    objet = np.random.choice(list_objet,1)[0]
    #st.text(metier)
    st.markdown(f"Tu es **{metier}**, dans **{lieu}**")
    display_gif(metier,lieu)   
    st.markdown(f"Tu aimes **{action}**, avec **{objet}**")
    display_gif(action,objet)
