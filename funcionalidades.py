from modulos import *

class Funcs():
    def limpa_tela(self):
        self.ent_ticker.delete(0, END)
        entries = [self.ent_rest1, self.ent_rest2, self.ent_rest3, self.ent_rest4,
                   self.ent_rest5, self.ent_rest6, self.ent_rest7, self.ent_rest8,
                   self.ent_rest9, self.ent_rest10, self.ent_rest11, self.ent_rest12,
                   self.ent_rest13, self.ent_rest14, self.ent_rest15, self.ent_rest16]
        for entry in entries:
            entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('tickers.bd');
        print("Conectando ao Banco de Dados")
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close();
        print("Desconectando do Banco de Dados")

    def monta_tabela(self):
        self.conecta_bd()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickers(
            TICKER VARCHAR(10),
            PRECO FLOAT,
            PL FLOAT,
            ROIC FLOAT,
            DY FLOAT            
        );
        """
                            )
        self.conn.commit();
        print("Banco de Dados Criado")
        self.desconecta_bd()

    def limpar_bd(self):
        self.conecta_bd()
        self.cursor.execute("""
            DELETE FROM tickers
        """
                            );
        self.conn.commit();
        print("Banco de Dados Criado")
        self.desconecta_bd()

    # ATUALIZANDO DADOS
    def webscrap_statusinvest(self):
        driver = webdriver.Chrome()
        driver.get("https://statusinvest.com.br/acoes/busca-avancada")
        time.sleep(3)
        botao_buscar = driver.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]').click()
        time.sleep(1.5)
        botao_buscar = driver.find_element(By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a').click()
        time.sleep(2)
        messagebox.showinfo("Concluído", "Os dados foram atualizados!")
        driver.quit()

    def delete_file_in_folder(self, file_name):
        pasta = os.path.join(os.path.expanduser("~"), "Downloads")
        file_path = os.path.join(pasta, file_name)  # Obtém o caminho completo do arquivo
        if os.path.exists(file_path):  # Verifica se o arquivo existe na pasta
            os.remove(file_path)  # Exclui o arquivo

    def verifica_arquivo_pasta(self, arquivo):
        pasta = os.path.join(os.path.expanduser("~"), "Downloads")
        caminho_arquivo = os.path.join(pasta, arquivo)  # Cria o caminho completo do arquivo
        if os.path.isfile(caminho_arquivo):  # Verifica se o caminho aponta para um arquivo existente
            return True
        else:
            return False

    def atualiza_csv_statusinvest(self):
        if self.verifica_arquivo_pasta('statusinvest-busca-avancada.csv') == True:
            self.delete_file_in_folder('statusinvest-busca-avancada.csv')
        self.webscrap_statusinvest()
        self.verifica_arquivo_pasta('statusinvest-busca-avancada.csv')
        print('Arquivo Atualizado!')

    def create_ranks(self, df):
        df = self.classificar_coluna(df, 'P/L')
        df = self.classificar_coluna(df, 'EV/EBIT')
        df = self.classificar_coluna(df, 'ROE', ascending=True)
        df = self.classificar_coluna(df, 'ROIC', ascending=True)
        return df

    # FUNCOES DE SUPORTE
    def classificar_coluna(self, df, coluna, ascending=False):
        df[f'Rank_{coluna}'] = df[coluna].rank(ascending=ascending)
        return df

    def transform_brazil_to_us_dataframe(self, df):
        df = df.applymap(lambda x: x.replace('.', '').replace(',', '.') if isinstance(x, str) else x)
        return df

    def obtem_restr(self):
        self.rest1 = float("-inf") if self.ent_rest1.get() == "" else float(self.ent_rest1.get())
        self.rest2 = float("inf") if self.ent_rest2.get() == "" else float(self.ent_rest2.get())
        self.rest3 = float("-inf") if self.ent_rest3.get() == "" else float(self.ent_rest3.get())
        self.rest4 = float("inf") if self.ent_rest4.get() == "" else float(self.ent_rest4.get())
        self.rest5 = float("-inf") if self.ent_rest5.get() == "" else float(self.ent_rest5.get())
        self.rest6 = float("inf") if self.ent_rest6.get() == "" else float(self.ent_rest6.get())
        self.rest7 = float("-inf") if self.ent_rest7.get() == "" else float(self.ent_rest7.get())
        self.rest8 = float("inf") if self.ent_rest8.get() == "" else float(self.ent_rest8.get())
        self.rest9 = float("-inf") if self.ent_rest9.get() == "" else float(self.ent_rest9.get())
        self.rest10 = float("inf") if self.ent_rest10.get() == "" else float(self.ent_rest10.get())
        self.rest11 = float("-inf") if self.ent_rest11.get() == "" else float(self.ent_rest11.get())
        self.rest12 = float("inf") if self.ent_rest12.get() == "" else float(self.ent_rest12.get())
        self.rest13 = float("-inf") if self.ent_rest13.get() == "" else float(self.ent_rest13.get())
        self.rest14 = float("inf") if self.ent_rest14.get() == "" else float(self.ent_rest14.get())
        self.rest15 = float("-inf") if self.ent_rest15.get() == "" else float(self.ent_rest15.get())
        self.rest16 = float("inf") if self.ent_rest16.get() == "" else float(self.ent_rest16.get())
        self.rest17 = self.v1.get()

    def select_lista(self):
        self.lista_tickers.delete(*self.lista_tickers.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT TICKER, PRECO, PL, ROIC, DY FROM tickers
        """)
        for i in lista:
            self.lista_tickers.insert("", END, values=i)
        self.desconecta_bd()

    def limpa_lista_tickers(self):
        self.limpar_bd()
        self.lista_tickers.delete(*self.lista_tickers.get_children())

    # FUNCOES DE DF
    def joel_greenblat(self, df, restricao_liquidez=False):
        # Cria a coluna de pontuacao baseada na formula magica de Joel Greenblat
        df_JG = df.copy()
        df_JG = df_JG[(df_JG['P/L'] > 0) & (df_JG['EV/EBIT'] > 0) & (df_JG['ROIC'] > 10)]
        if restricao_liquidez == True:
            df_JG = df_JG[df_JG[' LIQUIDEZ MEDIA DIARIA'] > df_JG[' LIQUIDEZ MEDIA DIARIA'].quantile(0.25)]
        df_JG['Joel_Greenblat'] = df_JG['Rank_ROIC'] + df_JG['Rank_EV/EBIT']

        # Separa as colunas e ordena os valores de acordo com o ranking da formula magica
        df_JG = df_JG.sort_values('Joel_Greenblat', ascending=False)

        # Remove tickers da mesma empresa
        df_JG['EMPRESA'] = df_JG['TICKER'].str[:4]
        df_JG.drop_duplicates(subset=['EMPRESA'], inplace=True, keep='first')
        df_JG.drop('EMPRESA', axis=1, inplace=True)
        # df_JG.reset_index(inplace=True, drop=True)
        # df_JG.drop('index', axis=1, inplace=True)
        return df_JG

    def read_clean_statusinvest_dataset(self, nan_off=True):
        arquivo = os.path.join(os.path.expanduser("~"), "Downloads")
        df = pd.read_csv(f'{arquivo}//statusinvest-busca-avancada.csv', sep=';')
        if nan_off == True:
            df.dropna(
                subset=['P/L', 'DY', 'P/VP', 'ROE', 'ROIC', 'EV/EBIT', 'DIVIDA LIQUIDA / EBIT', 'DIV. LIQ. / PATRI.'],
                inplace=True)
        df = self.transform_brazil_to_us_dataframe(df)
        colunas_com_excecao = [coluna for coluna in df.columns if coluna != 'TICKER']
        df[colunas_com_excecao] = df[colunas_com_excecao].astype('float')
        # df.set_index('TICKER', inplace=True)
        df.reset_index(inplace=True, drop=True)
        return df

    def df_restrictions(self, df, pl_min=float('-inf'), pl_max=float('inf'), evebit_min=float('-inf'),
                        evebit_max=float('inf'),
                        dy_min=float('-inf'), dy_max=float('inf'), pvp_min=float('-inf'), pvp_max=float('inf'),
                        roe_min=float('-inf'), roe_max=float('inf'), roic_min=float('-inf'), roic_max=float('inf'),
                        div_ebit_min=float('-inf'), div_ebit_max=float('inf'), div_pat_min=float('-inf'),
                        div_pat_max=float('inf'), liq_off=False):
        if liq_off == True:
            df = df[df[' LIQUIDEZ MEDIA DIARIA'] > df[' LIQUIDEZ MEDIA DIARIA'].quantile(0.25)]
        df = df[(df['P/L'] > pl_min) &
                (df['P/L'] < pl_max) &
                (df['EV/EBIT'] > evebit_min) &
                (df['EV/EBIT'] < evebit_max) &
                (df['DY'] > dy_min) &
                (df['DY'] < dy_max) &
                (df['P/VP'] > pvp_min) &
                (df['P/VP'] < pvp_max) &
                (df['ROE'] > roe_min) &
                (df['ROE'] < roe_max) &
                (df['ROIC'] > roic_min) &
                (df['ROIC'] < roic_max) &
                (df['DIVIDA LIQUIDA / EBIT'] > div_ebit_min) &
                (df['DIVIDA LIQUIDA / EBIT'] < div_ebit_max) &
                (df['DIV. LIQ. / PATRI.'] > div_pat_min) &
                (df['DIV. LIQ. / PATRI.'] < div_pat_max)]
        df.reset_index(inplace=True, drop=True)
        return df

    # FUNCOES DE INSERÇÃO
    def inserir_df(self):
        self.limpa_lista_tickers()
        self.obtem_restr()
        df = self.read_clean_statusinvest_dataset()
        df.rename(columns={'P/L': 'PL'}, inplace=True)
        df = df[['TICKER', 'PRECO', 'PL', 'DY', 'ROIC']]

        self.conecta_bd()
        # for index, row in df.iterrows():
        #    self.cursor.execute("""INSERT INTO tickers (TICKER, PRECO, PL, ROIC, DY) VALUES (?, ?, ?, ?, ?)""",
        #              (row['TICKER'], row['PRECO'], row['PL'], row['ROIC'], row['DY']))

        df.to_sql('tickers', self.conn, if_exists='replace')
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def inserir_magic_formula(self):
        self.limpa_lista_tickers()
        self.obtem_restr()
        df = self.joel_greenblat(self.create_ranks(self.read_clean_statusinvest_dataset()),
                                 restricao_liquidez=self.rest17)
        df.rename(columns={'P/L': 'PL'}, inplace=True)
        df = df[['TICKER', 'PRECO', 'PL', 'DY', 'ROIC']]
        self.conecta_bd()
        # for index, row in df.iterrows():
        #    self.cursor.execute("""INSERT INTO tickers (TICKER, PRECO, PL, ROIC, DY) VALUES (?, ?, ?, ?, ?)""",
        #              (row['TICKER'], row['PRECO'], row['PL'], row['ROIC'], row['DY']))
        df.to_sql('tickers', self.conn, if_exists='replace')
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
        messagebox.showinfo("Concluído", "Este é o ranking de ações da Fórmula Mágica (ROIC e EV/Ebit).")

    def inserir_com_restricoes(self):
        self.limpa_lista_tickers()
        self.obtem_restr()
        df = self.df_restrictions(self.read_clean_statusinvest_dataset(), pl_min=self.rest1, pl_max=self.rest2,
                                  evebit_min=self.rest3,
                                  evebit_max=self.rest4, dy_min=self.rest5, dy_max=self.rest6, pvp_min=self.rest7,
                                  pvp_max=self.rest8,
                                  roe_min=self.rest9, roe_max=self.rest10, roic_min=self.rest11, roic_max=self.rest12,
                                  div_ebit_min=self.rest13,
                                  div_ebit_max=self.rest14, div_pat_min=self.rest15, div_pat_max=self.rest16,
                                  liq_off=self.rest17)
        df.rename(columns={'P/L': 'PL'}, inplace=True)
        df = df[['TICKER', 'PRECO', 'PL', 'DY', 'ROIC']]
        self.conecta_bd()
        # for index, row in df.iterrows():
        #    self.cursor.execute("""INSERT INTO tickers (TICKER, PRECO, PL, ROIC, DY) VALUES (?, ?, ?, ?, ?)""",
        #              (row['TICKER'], row['PRECO'], row['PL'], row['ROIC'], row['DY']))
        df.to_sql('tickers', self.conn, if_exists='replace')
        self.desconecta_bd()
        self.select_lista()

    def buscar_ticker(self):
        self.conecta_bd()
        self.lista_tickers.delete(*self.lista_tickers.get_children())

        self.ent_ticker.insert(END, '%')
        nome = self.ent_ticker.get()
        self.cursor.execute("""SELECT TICKER, PRECO, PL, ROIC, DY FROM tickers
                                WHERE TICKER LIKE '%s'""" % nome)
        buscaticker = self.cursor.fetchall()
        for i in buscaticker:
            self.lista_tickers.insert("", END, values=i)
        self.ent_ticker.delete(0, END)
        self.desconecta_bd()

    def get_crypto_price(self):
        c = CurrencyRates()
        exchange = ccxt.binance()
        exchange_rate = c.get_rate('BRL', 'USD')

        bitcoin_price_usd = exchange.fetch_ticker('BTC/USDT')['last']
        bitcoin_price_brl = bitcoin_price_usd / exchange_rate

        ethereum_price_usd = exchange.fetch_ticker('ETH/USDT')['last']
        ethereum_price_brl = ethereum_price_usd / exchange_rate

        self.crypto_price.delete('1.0', 'end')
        self.crypto_price.insert('1.1',
                                 f'     BITCOIN PRICE: R${bitcoin_price_brl:,.2f}         ETHEREUM PRICE: R${ethereum_price_brl:,.2f}')
        self.root.after(20000, self.get_crypto_price)