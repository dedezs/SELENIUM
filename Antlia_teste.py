import selenium
import time

driver = webdriver.Chrome()

url = driver.get('https://www.kabum.com.br/')
            
driver.maximize_window()
    
time.sleep(2)
    
barra_Pesquisa = driver.find_element_by_xpath('//*[@id="input-busca"]')
barra_Pesquisa.click()
barra_Pesquisa.send_keys('Processador')
    
botao_Enter = driver.find_element_by_xpath('//*[@id="barraBuscaKabum"]/div/form/button')
botao_Enter.click()
    
time.sleep(2)