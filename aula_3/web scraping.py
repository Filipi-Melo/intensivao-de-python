import pandas as pd
from selenium.webdriver import Chrome

#navegador.get("https://www.google.com.br/")
#navegador.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("")
#press('enter')

#Dolar
navegador = Chrome()
navegador.get("https://www.google.com/search?q=cota%C3%A7ao+do+dolar&oq=cota%C3%A7ao+do+dolar&aqs=chrome..69i57.412j0j1&sourceid=chrome&ie=UTF-8")

dolar = navegador.find_element("xpath",'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute('data-value')
print('\nCotações:')
print('- Dolar: R$ '+ dolar)

#Euro
navegador.get("https://www.google.com/search?q=cota%C3%A7%C3%A3o+euro&ei=V1XYY_c-sdnWxA_rz7AI&oq=cota%C3%A7ao+do+dolar&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgcIABCwAxBDMhIILhDHARDRAxDIAxCwAxBDGAEyFQguEMcBENEDENQCEMgDELADEEMYATIVCC4QxwEQ0QMQ1AIQyAMQsAMQQxgBSgQIQRgASgQIRhgAUABYAGCoEGgBcAF4AIABAIgBAJIBAJgBAMgBDMABAdoBBAgBGAg&sclient=gws-wiz-serp")
euro = navegador.find_element("xpath",'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute('data-value')
print('- Euro: R$ '+ euro)
#Ouro
navegador.get("https://dolarhoje.com/ouro-hoje/")
ouro = navegador.find_element("xpath",'//*[@id="nacional"]').get_attribute('value').replace(",",".")
print('- Grama do Ouro: R$ '+ouro)
navegador.quit()

tabela = pd.read_excel('./Produtos.xlsx')
print('\nTabela antes:\n',tabela)

tabela.loc[tabela['Moeda']=='Dólar','Cotação']=float(dolar)
tabela.loc[tabela['Moeda']=='Euro','Cotação']=float(euro)
tabela.loc[tabela['Moeda']=='Ouro','Cotação']=float(ouro)
print('\nTabela em números: \n',tabela)

tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']
print('\nTabela nova:\n',tabela)

#tabela['Preço de Venda']=tabela['Preço de Venda'].map("R${:.2f}".format)

tabela.to_excel("./Produtos Novo.xlsx",index=False)