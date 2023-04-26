from modulos import *
from funcionalidades import Funcs

root = Tk()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame_2()
        self.monta_tabela()
        self.select_lista()
        self.get_crypto_price()

        self.root.after(60000, self.get_crypto_price)

        root.mainloop()


    def tela(self):
        self.root.title("Application")
        self.root.configure(background='deepskyblue')
        self.root.geometry()
        self.root.geometry("1100x650")
        self.root.resizable(False, False)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bg='lightblue', bd=4, highlightbackground='white', highlightthickness=0.5)
        self.frame_1.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.34)
        self.frame_2 = Frame(self.root, bg='lightblue', bd=4, highlightbackground='white', highlightthickness=0.5)
        self.frame_2.place(relx=0.36, rely=0.01, relheight=0.98, relwidth=0.63)

    def widgets_frame1(self):
        self.botao_limpar = Button(self.frame_1, text='Limpar Tudo', font=('verdana', 11, 'bold'), command=self.limpa_lista_tickers)
        self.botao_limpar.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.07)

        self.lb_ticker = Label(self.frame_1, text='Ticker:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_ticker.place(relx=0.06, rely=0.102)
        self.ent_ticker = Entry(self.frame_1)
        self.ent_ticker.place(relx=0.225, rely=0.1, relwidth=0.23, relheight=0.04)

        self.botao_buscar = Button(self.frame_1, text='Buscar', font=('verdana', 11, 'bold'), command=self.buscar_ticker)
        self.botao_buscar.place(relx=0.52, rely=0.09, relwidth=0.46, relheight=0.07)

        self.botao_atualizar_dados = Button(self.frame_1, text='Atualizar Dados', bg='Skyblue2', font=('verdana', 11, 'bold'), command=self.atualiza_csv_statusinvest)
        self.botao_atualizar_dados.place(relx=0.02, rely=0.17, relwidth=0.96, relheight=0.07)

        self.botao_magic_formula = Button(self.frame_1, text='Magic Formula', font=('verdana', 11, 'bold'), command=self.inserir_magic_formula)
        self.botao_magic_formula.place(relx=0.02, rely=0.25, relwidth=0.96, relheight=0.07)

        self.crypto_price = Text(self.frame_2, font=('verdana', 12, 'bold'))
        self.crypto_price.place(relx=0.01, rely=0.01, relwidth=0.94, relheight=0.033)

        self.botao_restricoes = Button(self.frame_1, text='Gerar Lista com Restrições', font=('verdana', 11, 'bold'), command=self.inserir_com_restricoes)
        self.botao_restricoes.place(relx=0.02, rely=0.92, relwidth=0.96, relheight=0.07)

        self.v1 = IntVar()
        self.lb_liquidez = Label(self.frame_1, text='Remover Ações de Baixa Liquidez', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_liquidez.place(relx=0.15, rely=0.36)
        self.check_liquidez = Checkbutton(self.frame_1, background='lightblue', variable=self.v1, onvalue=1, offvalue=0)
        self.check_liquidez.place(relx=0.8, rely=0.36)

        #  RESTRICOES
        self.lb_rest1 = Label(self.frame_1, text='P/L Mín.:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest1.place(relx=0.002, rely=0.43)
        self.ent_rest1 = Entry(self.frame_1)
        self.ent_rest1.place(relx=0.24, rely=0.428, relwidth=0.23, relheight=0.04)

        self.lb_rest2 = Label(self.frame_1, text='P/L Máx.:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest2.place(relx=0.502, rely=0.43)
        self.ent_rest2 = Entry(self.frame_1)
        self.ent_rest2.place(relx=0.74, rely=0.428, relwidth=0.23, relheight=0.04)



        self.lb_rest3 = Label(self.frame_1, text='EV/Ebit Mín:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest3.place(relx=0.002, rely=0.49)
        self.ent_rest3 = Entry(self.frame_1)
        self.ent_rest3.place(relx=0.24, rely=0.488, relwidth=0.23, relheight=0.04)

        self.lb_rest4 = Label(self.frame_1, text='EV/Ebit Máx:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest4.place(relx=0.502, rely=0.49)
        self.ent_rest4 = Entry(self.frame_1)
        self.ent_rest4.place(relx=0.74, rely=0.488, relwidth=0.23, relheight=0.04)



        self.lb_rest5 = Label(self.frame_1, text='DY Mín:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest5.place(relx=0.002, rely=0.55)
        self.ent_rest5 = Entry(self.frame_1)
        self.ent_rest5.place(relx=0.24, rely=0.548, relwidth=0.23, relheight=0.04)

        self.lb_rest6 = Label(self.frame_1, text='DY Máx:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest6.place(relx=0.502, rely=0.55)
        self.ent_rest6 = Entry(self.frame_1)
        self.ent_rest6.place(relx=0.74, rely=0.548, relwidth=0.23, relheight=0.04)



        self.lb_rest7 = Label(self.frame_1, text='P/VP Mín:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest7.place(relx=0.002, rely=0.61)
        self.ent_rest7 = Entry(self.frame_1)
        self.ent_rest7.place(relx=0.24, rely=0.608, relwidth=0.23, relheight=0.04)

        self.lb_rest8 = Label(self.frame_1, text='P/VP Máx:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest8.place(relx=0.502, rely=0.61)
        self.ent_rest8 = Entry(self.frame_1)
        self.ent_rest8.place(relx=0.74, rely=0.608, relwidth=0.23, relheight=0.04)



        self.lb_rest9 = Label(self.frame_1, text='ROE Mín:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest9.place(relx=0.002, rely=0.67)
        self.ent_rest9 = Entry(self.frame_1)
        self.ent_rest9.place(relx=0.24, rely=0.668, relwidth=0.23, relheight=0.04)

        self.lb_rest10 = Label(self.frame_1, text='ROE Máx:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest10.place(relx=0.502, rely=0.67)
        self.ent_rest10 = Entry(self.frame_1)
        self.ent_rest10.place(relx=0.74, rely=0.668, relwidth=0.23, relheight=0.04)


        self.lb_rest11 = Label(self.frame_1, text='ROIC Mín:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest11.place(relx=0.002, rely=0.73)
        self.ent_rest11 = Entry(self.frame_1)
        self.ent_rest11.place(relx=0.24, rely=0.728, relwidth=0.23, relheight=0.04)

        self.lb_rest12 = Label(self.frame_1, text='ROIC Máx:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest12.place(relx=0.502, rely=0.73)
        self.ent_rest12 = Entry(self.frame_1)
        self.ent_rest12.place(relx=0.74, rely=0.728, relwidth=0.23, relheight=0.04)



        self.lb_rest13 = Label(self.frame_1, text='Div/Eb Mín:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest13.place(relx=0.002, rely=0.79)
        self.ent_rest13 = Entry(self.frame_1)
        self.ent_rest13.place(relx=0.24, rely=0.788, relwidth=0.23, relheight=0.04)

        self.lb_rest14 = Label(self.frame_1, text='Div/Eb Máx:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest14.place(relx=0.502, rely=0.79)
        self.ent_rest14 = Entry(self.frame_1)
        self.ent_rest14.place(relx=0.74, rely=0.788, relwidth=0.23, relheight=0.04)



        self.lb_rest15 = Label(self.frame_1, text='Div/PL Mín:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest15.place(relx=0.002, rely=0.85)
        self.ent_rest15 = Entry(self.frame_1)
        self.ent_rest15.place(relx=0.24, rely=0.848, relwidth=0.23, relheight=0.04)

        self.lb_rest16 = Label(self.frame_1, text='Div/PL Máx:', background='lightblue', font=('verdana', 8, 'bold'))
        self.lb_rest16.place(relx=0.502, rely=0.85)
        self.ent_rest16 = Entry(self.frame_1)
        self.ent_rest16.place(relx=0.74, rely=0.848, relwidth=0.23, relheight=0.04)

    def lista_frame_2(self):
        self.lista_tickers = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.lista_tickers.heading('#0', text='')
        self.lista_tickers.heading('#1', text='TICKER')
        self.lista_tickers.heading('#2', text='PREÇO')
        self.lista_tickers.heading('#3', text='P/L')
        self.lista_tickers.heading('#4', text='ROIC')
        self.lista_tickers.heading('#5', text='DY')

        self.lista_tickers.column('#0', width=1)
        self.lista_tickers.column('#1', width=50)
        self.lista_tickers.column('#2', width=50)
        self.lista_tickers.column('#3', width=50)
        self.lista_tickers.column('#4', width=50)
        self.lista_tickers.column('#5', width=50)

        self.lista_tickers.place(relx=0.01, rely=0.05, relheight=0.955, relwidth=0.95)

        self.scroll_lista = Scrollbar(self.frame_2, orient='vertical')
        self.scroll_lista.configure(command=self.lista_tickers.yview)
        self.lista_tickers.config(yscrollcommand=self.scroll_lista.set)
        self.scroll_lista.place(relx=0.96, rely=0.05, relheight=0.94, relwidth=0.03)

Application()