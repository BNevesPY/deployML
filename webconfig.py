import streamlit as st
from st_functions import st_button, load_css
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class PgSettings():
    def __init__(self):
        self.pgtitle = 'AI world for Industrial Place'
        self.pgIcon = ':wave:'
        self.pgLayout = 'wide'
        self.pgHeader = ' Welcome to AI world for Industrial solutions '
        self.pgsubheader = 'The AI working for you'

        pass


class PageSessions():
    def __init__(self):
        self.icon_size = 20
        self.aboutHeader = '# Bruno Neves'
        self.aboutSubheader = '## Electrical Enginier, Machine Learning Developer'
        self.aboutDescription_1 = 'Com fortes conhecimentos matematicos e físicos, desenvolvi a capacidade de integração de sistemas de machine learning na industria.'
        self.aboutDescription_2 = 'Desde 2010 desenvolvo AI para o sector agricola, Real State e Energético.'
        self.aboutDescription_3 = 'Em 2020 devido à evolucao das tecnicas de programacao, e oportinudade de trabalho no sector solar.'
        self.aboutDescription_4 = 'O meu método de trabalho consiste em acompanhar, interpretar e executar o processo produtivo, de forma a perceber problemas mecânicos, eléctricos, humanos e logísticos.'
        self.aboutDescription_5 = "Após esta abordagem, desenvolver as regras do processo e as AI's que leve à boa obtenção de resultados."
        self.aboutDescription_6 = 'Com a identificacao dos problemas do estágio anterior começo na criação do(s) algoritmos, em extreita parceria com o cliente, porque ninguém com o cliente entende melhor o processo produtivo.'
        self.aboutDescription_7 = 'Entendo não existirem modelos estáticos, no mundo da AI o sucesso de hoje é o insucesso de amanha, a monitorização e manutenção dos sistemas é o que leva ao sucesso constante.'
        self.aboutDescription_8 = 'Casos de sucesso: Tire você mesmo essa conclusão experimentando os meus trial algorithmos.'
        self.personallabels = "Focado", "dedicado", "Coenctividade"
        self.personallsizes = [40, 40, 20]
        self.personalexplode = (0.1, 0.1, 0.1)
        self.cientificallabels = "Infrared", "Mecanical", "Electrical", "MultiSpectral"
        self.cientificalsizes = [35, 10, 40, 15]
        self.cientificalexplode = (0.2, 0.2, 0.2, 0.2)
        self.devlabels = "Python", "Pytorch", "AWS", "LLM", "AZURE"
        self.devsizes = [30, 30, 13, 20, 2]
        self.devexplode = (0.3, 0.3, 0.3, 0.3, 0.3)
        pass

    def plotpie(self, sizes, explode, labels):
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        return fig1

    def aboutMe(self):
        #        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        #        sizes = [15, 30, 45, 10]
        #        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        #

        #        df = pd.DataFrame(np.random.randint(1,10,size=(10, 3)),columns=['Apple', 'Microsoft', 'Google'])
        col1, col2 = st.columns([0.2, 0.8])
        personalsk, cientificSk, DevSk = st.columns(3)
        with st.container():

            col1.image('mywebpage/FotoPerfil.jpeg', width=400)
            col2.markdown(self.aboutHeader)
            col2.markdown(self.aboutSubheader)
            col2.write(self.aboutDescription_1)
            col2.write(self.aboutDescription_2)
            col2.write(self.aboutDescription_3)
            col2.write(self.aboutDescription_4)
            col2.write(self.aboutDescription_5)
            col2.write(self.aboutDescription_6)
            col2.write(self.aboutDescription_7)
            col2.write(self.aboutDescription_8)
            # image('mywebpage/FotoPerfil.jpeg', width=400)
            with st.container():
                personalsk.markdown('## Personal ')
                personalsk.pyplot(self.plotpie(
                    self.personallsizes, self.personalexplode, self.personallabels))
                cientificSk.markdown('## Scientifical')
                cientificSk.pyplot(self.plotpie(
                    self.cientificalsizes, self.cientificalexplode, self.cientificallabels))
                DevSk.markdown('## Developer')
                DevSk.pyplot(self.plotpie(
                    self.devsizes, self.devexplode, self.devlabels))

    def contactMe(self):
        with st.container():
            st.write('---')
            st.header('Get in Touch with me')
            st.write('##')

            contact_form = '''
            <form action="https://formsubmit.co/nevesbmhenr@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your Name" required>
             <input type="email" name="email" placeholder="Your Email" required>
             <textarea name="message" placeholder="Your message" required></textarea>
             <button type="submit">Send</button>
            </form>
            '''
            left_col, right_col = st.columns(2)
            with left_col:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_col:
                st.empty()

    def portolio(self):
        st.markdown('### Portofilo')
        pass

    def algoritmos(self):
        load_css()
        st.markdown('#### Solar on Roof')
        st_button('box', 'https://8ca635a078173001fa.gradio.live',
                  'Materials Detection', self.icon_size)
        st_button('box', 'https://92fb842ffbf13f135c.gradio.live',
                  'Micros', self.icon_size)
        st_button('box', 'https://25c8de66cc823db36b.gradio.live',
                  'Stickers', self.icon_size)
        st_button('box', 'https://67a60842dbb6e77235.gradio.live',
                  'Tails', self.icon_size)
        st.markdown('#### Electrical')
        st_button('box', 'https://661d24c4d13d8bd157.gradio.live',
                  'Check box connections', self.icon_size)
        st.markdown('#### Solar Test')
        st_button('box', 'https://65021eb872b6c67bc4.gradio.live',
                  'Solar Cells Detect', self.icon_size)
        st_button('box', 'https://792ba614ccba479214.gradio.live',
                  'Cientifical Judgement', self.icon_size)
        st_button('box', 'https://d08d28a84154bfda15.gradio.live',
                  'TUV Judgement', self.icon_size)
        st.markdown('#### Food')
        st_button('box', 'https://d503c024a18d98ae89.gradio.live',
                  'Food', self.icon_size)
    pass


class Sidebar():
    def __init__(self):
        self.texto = 'BN@NL24'
        pass

    def vertical(self):
        st.sidebar.caption(self.texto)
        Home = st.sidebar.button('Home')
        about = st.sidebar.button('Sobre mim')
        Portfolio = st.sidebar.button('Portfolio')
        Algoritmos = st.sidebar.button('Algoritmos')
        datascience = st.sidebar.button('Análise de dados')
        if about:
            return 0
#            PageSessions().aboutMe()
        elif Portfolio:
            return 1
        elif Algoritmos:
            return 2
