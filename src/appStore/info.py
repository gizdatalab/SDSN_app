import streamlit as st

def app():
    
    
    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center;  \
                      color: black;'> Policy Action Tracker</h2>", 
                      unsafe_allow_html=True)

    
    st.markdown("<div style='text-align: center; \
                    color: grey;'>The Policy Action Tracker is an open-source\
                         digital tool which aims to assist policy analysts and \
                          other users in extracting and filtering relevant \
                            information from policy documents.</div>",
                        unsafe_allow_html=True)
    footer = """
           <div class="footer-custom">
               Guidance & Feedback - <a href="https://www.linkedin.com/in/maren-bernlöhr-149891222" target="_blank">Maren Bernlöhr</a> |
               <a href="https://www.linkedin.com/in/manuelkuhm" target="_blank">Manuel Kuhm</a> |
               Developer - <a href="https://www.linkedin.com/in/erik-lehmann-giz/" target="_blank">Erik Lehmann</a>  |   
               <a href="https://www.linkedin.com/in/jonas-nothnagel-bb42b114b/" target="_blank">Jonas Nothnagel</a>   |
               <a href="https://www.linkedin.com/in/prashantpsingh/" target="_blank">Prashant Singh</a> |
               
           </div>
       """
    st.markdown(footer, unsafe_allow_html=True)

    c1, c2, c3 =  st.columns([8,1,12])
    with c1:
        st.image("docStore/img/ndc.png")
    with c3:
        st.markdown('<div style="text-align: justify;">The manual extraction \
        of relevant information from text documents is a \
    time-consuming task for any policy analyst. As the amount and length of \
    public policy documents in relation to sustainable development (such as \
    National Development Plans and Nationally Determined Contributions) \
    continuously increases, a major challenge for policy action tracking – the \
    evaluation of stated goals and targets and their actual implementation on \
    the ground – arises. Luckily, Artificial Intelligence (AI) and Natural \
    Language Processing (NLP) methods can help in shortening and easing this \
    task for policy analysts.</div><br>',
    unsafe_allow_html=True)

    intro = """
    <div style="text-align: justify;">
    For this purpose, the United Nations Sustainable Development Solutions \
    Network (SDSN) and the Deutsche Gesellschaft für Internationale \
    Zusammenarbeit (GIZ) GmbH are collaborated in the development \
    of this AI-powered open-source web application that helps find and extract \
    relevant information from public policy documents faster to facilitate \
    evidence-based decision-making processes in sustainable development and beyond.  
    This tool allows policy analysts and other users the possibility to rapidly \
    search for relevant information/paragraphs in the document according to the \
    user’s interest, classify the document’s content according to the Sustainable \
    Development Goals (SDGs), and compare climate-related policy documents and NDCs \
    across countries using open data from the German Institute of Development and \
    Sustainability’s (IDOS) NDC Explorer. 
    To understand the application's functionalities and learn more about ß
    the project, see the attached concept note. We hope you like our application 😊
    </div>
    <br>
    """
    st.markdown(intro, unsafe_allow_html=True)
    # st.image("docStore/img/paris.png")