import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2296c00a2e4265232a4ee4d989cb7ef8"
# Your Auth Token from twilio.com/console
auth_token  = "4a0aab32281011dd0fedb7f683e251b4"
client = Client(account_sid, auth_token)

# ABRIR OS 6 ARQUIOS EM EXCEL
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5563992150818",
            from_="+12187890698",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'    )
        print(message.sid)

# PARA CADA ARQUIVO:


# VERIFICAR SE ALGUM VALOR NA COLUNA VENDAS DAQUELE ARQUIVO É MAIOR QUE 55.000

# SE FOR MAIOR DO QUE 55.000 -> ENVIA UM SMS COM O NOME, O MÊS E AS VENDAS DO VENDEDOR

# CASO NÃO SEJA MAIOR DO QUE 55.000 NÃO QUERO FAZER NADA