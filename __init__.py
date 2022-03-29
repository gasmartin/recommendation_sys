import streamlit as st

from recommendation import recommend


def space(num_lines=1):
    for _ in range(num_lines):
        st.write("")


st.set_page_config(layout='centered', page_icon='🕹️', page_title='Nintendo Switch Games Recommendation System')

st.title('🕹️ Nintendo Switch Games Recommendation System')

space(2)

form = st.form('user_form')

name = form.text_input('For which player do you wanna suggest a game?')

space(1)

suggest = form.form_submit_button('Suggest now!')

if suggest:
    suggestions = recommend(name.strip())

    if not suggestions:
        st.write("""
            ### This person has already played all games registered on the system. 
            ### There is no suggestion for this monster!
        """)
    else:
        for s in suggestions:
            st.write(f'### {s}')
