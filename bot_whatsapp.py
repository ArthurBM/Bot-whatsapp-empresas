from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import textwrap
import time
from datetime import date
import traceback

def enter_wpp():
    return (Keys.SHIFT + Keys.ENTER) + Keys.SHIFT
def colar_wpp():
    return (Keys.CONTROL + "v") + Keys.CONTROL
class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('https://web.whatsapp.com')
        self.count_mensagens = 0
    
    def enviarMensagensLojas(self,nomes):
        time.sleep(20)
        for nome in nomes:
            try:
                primeiro_nome = ((nome.split())[0]).capitalize()
                icone_pesquisa = self.driver.find_element_by_xpath("//span[@data-icon='search']")
                icone_pesquisa.click()
                time.sleep(2)
                campo_pesquisa = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                campo_pesquisa.click()
                campo_pesquisa.send_keys(nome)
                time.sleep(2)
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{nome}'][@class='_3ko75 _5h6Y_ _3Whw5']")
                print(campo_grupo)
                campo_grupo.click()
                time.sleep(3)
                chat_box = self.driver.find_element_by_class_name('_3uMse')
                chat_box.click()
                mensagem = (
                    textwrap.dedent(
                        f"""
                        Olá {primeiro_nome}, tudo bem? Em comemoração ao dia Mundial do hambúrguer a MR HOPPY RUI BARBOSA está participando da campanha Cheeseburguer do bem.

                        Que tal poder comemorar esse dia e ainda ajudar o próximo? Isso será realidade, já que a cada unidade vendida do nosso novo Cheeseburguer, será DOADO uma outra unidade para um profissional de saúde, que estão na linha de frente na luta contra o covid-19

                        Vamos juntos se deliciar e fazer o bem?

                        Faça já o seu pedido por Whatsapp !
                        https://delivery.menew.com.br/mr-hoppy-rui-barbosa

                        Telefone:
                        30973109 (Com WhatsApp)
                        """
                    )
                )
                mensagem = mensagem.replace('\n', enter_wpp())
                
                chat_box.send_keys(mensagem)
                time.sleep(5)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                botao_enviar.click()
            except:
                print(f'Nome não encontrado: {nome}')
                with open("names_not_found.txt", "a") as myfile:
                    myfile.write(f"Pessoa não encontrada: {nome}")
                continue

    def enviarMensagensLojasImagem(self,nomes, image_path):
        time.sleep(15)
        for nome in nomes:
            try:
                primeiro_nome = ((nome.split())[0]).capitalize()
                icone_pesquisa = self.driver.find_element_by_xpath("//span[@data-icon='search']")
                icone_pesquisa.click()
                time.sleep(2)
                campo_pesquisa = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                campo_pesquisa.click()
                campo_pesquisa.send_keys(nome)
                time.sleep(2)
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{nome}'][@class='_3ko75 _5h6Y_ _3Whw5']")
                print(campo_grupo)
                campo_grupo.click()
                time.sleep(3)
                chat_box = self.driver.find_element_by_class_name('_3uMse')
                chat_box.click()
                mensagem = (
                    textwrap.dedent(
                        f"""
                        Olá {primeiro_nome}, tudo bem? Em comemoração ao dia Mundial do hambúrguer a MR HOPPY RUI BARBOSA está participando da campanha Cheeseburguer do bem.

                        Que tal poder comemorar esse dia e ainda ajudar o próximo? Isso será realidade, já que a cada unidade vendida do nosso novo Cheeseburguer, será DOADO uma outra unidade para um profissional de saúde, que estão na linha de frente na luta contra o covid-19

                        Vamos juntos se deliciar e fazer o bem?

                        Faça já o seu pedido por Whatsapp !
                        https://delivery.menew.com.br/mr-hoppy-rui-barbosa

                        Telefone:
                        30973109 (Com WhatsApp)
                        """
                    )
                )
                mensagem = mensagem.replace('\n', enter_wpp())
                
                chat_box.send_keys(mensagem)
                time.sleep(5)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                botao_enviar.click()

                time.sleep(2)
                icone_clip = self.driver.find_element_by_xpath("//div[@title='Anexar']")
                icone_clip.click()
                
                time.sleep(1)
                icone_imagem = self.driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                icone_imagem.send_keys(image_path)

                time.sleep(4)
                send_button = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
                send_button.click()
                

                time.sleep(3)
                self.count_mensagens += 1
            except Exception:
                traceback.print_exc()
                continue
            

    #O usuario seleciona manualmente a mensagem e o bot manda de uma vez
    def encaminharMensagens(self,sobrenome):
        time.sleep(20)
        botao_encaminhar = self.driver.find_element_by_xpath("//span[@data-icon='forward']")
        botao_encaminhar.click()
        chat_box = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/label/div/div[2]')
        chat_box.click()
        chat_box.send_keys(sobrenome)
        time.sleep(5)
        #scroll_box = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]')
        #self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll_box)
        links = self.driver.find_elements_by_class_name('_1mFmt')
        for clickable in links:
            if clickable != '':
                clickable.click()
                time.sleep(1)