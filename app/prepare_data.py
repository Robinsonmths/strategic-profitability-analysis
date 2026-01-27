import pandas as pd
#%%
#carregando dados
df = pd.read_csv(r'C:\Users\MATHEUS\Desktop\PROGRAMAÇÃO\PROJETOS\VENDAS\data\superstore.csv')
# Agrupar por Category e somar o Real Profit
summary = df.groupby('Category')['Profit'].sum().reset_index()
# Agrupando a categoria por valor maior para menor
summary_sorted = summary.sort_values(by='Profit',ascending=False)
#vendo as peimriras linhas 
print(summary_sorted)