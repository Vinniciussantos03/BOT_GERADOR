import pyautogui as p
import time
import logging      
import traceback
import os
import datetime 
from datetime import datetime,timedelta


credenciais = open('C:/Users/vinicius.ribeiro/Documents/Desafios/credenciais.txt', 'r')
lista = credenciais.readlines()
login = lista[0][:-1]
senha = lista[1][:]

hoje = datetime.now()
ontem = hoje - timedelta(days=1)
data_formatada = ontem.strftime('%d/%m/%y')



def gerar_relatorio():

    try:

        usuario = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_usuario.png', confidence = 0.50)
        
        if usuario is not None:


            print("Encontrei o usuario")
            p.moveTo(usuario)
            p.sleep(1)
            p.click(usuario.x + 160, usuario.y)
            p.sleep(1)
            p.press('backspace', presses=20)
            p.sleep(1)
            p.typewrite(login)
        


        p.sleep(1)
        p.press('tab')
        p.sleep(1)
        p.typewrite(senha) #colocar senha
        p.sleep(1)


        botao_empresa = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_empresa.png', confidence = 0.70)
        
        if botao_empresa is not None:
            p.sleep(2)
            p.click(botao_empresa.x + 160, botao_empresa.y)
            p.sleep(2)
            p.scroll(400)
            p.sleep(2)

        
        jangada_automotive = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_jangada_automotive.png', confidence = 0.70)  

        if jangada_automotive is not None:
            p.sleep(1)
            p.click(jangada_automotive)
            p.sleep(1)
        
        else:
            logging.info('Nao encontrei a jangada automotive')


        botao_ok = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_ok.png', confidence = 0.90)
            
        if botao_ok is not None:
            p.sleep(1)
            p.click(botao_ok)
        else:
            logging.info('Nao encontrei o botao ok')

        p.sleep(2)


        print_relatorios = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_relatorios.png', confidence = 0.80)

        if print_relatorios is not None:
            p.sleep(1)
            p.click(print_relatorios)
            p.sleep(2)

        
        print_veiculos = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_veiculos.png', confidence = 0.90)

        if print_veiculos is not None:
            p.sleep(1)
            p.moveTo(print_veiculos)
            p.sleep(1) 
         
    
        print_previsao_de_entrega = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_previsao_de_entrega.png', confidence = 0.80)
        
        if print_previsao_de_entrega is not None:
            p.sleep(2)
            p.click(print_previsao_de_entrega)
            p.sleep(1)
        

        p.sleep(1)   

        print_data_incial = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_data_inicial.png', confidence = 0.80)

      

        if print_data_incial is not None:
            p.sleep(1)
            p.click(print_data_incial)
            p.click(print_data_incial.x + 75, print_data_incial.y, clicks=2)
            p.sleep(1)
            p.press('backspace')
            p.typewrite(data_formatada)
            p.sleep(1)
            p.press('tab')
            p.press('tab')
            p.press('backspace')
            p.typewrite(data_formatada)
            p.sleep(1)

        print_preview = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_preview.png', confidence = 0.80)

        if print_preview is not None:
            p.sleep(2)
            p.click(print_preview)  

        print_previsao = p.locateCenterOnScreen('C:\\Users\\vinicius.ribeiro\\Pictures\\PrintsDesafio\\print_previsao_veiculos.png', confidence = 0.80)
        
        while print_previsao == None:
            p.sleep(2)

            
            print_previsao = p.locateCenterOnScreen('C:\\Users\\vinicius.ribeiro\\Pictures\\PrintsDesafio\\print_previsao_veiculos.png', confidence = 0.90)
            
        
        

        
        print_zoom = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_zoom.png', confidence = 0.60)

        if print_zoom is not None:
            p.sleep(2)
            p.click(print_zoom.x + 75, print_zoom.y, clicks=2)
            p.sleep(1)
            p.press('backspace') 
            p.typewrite('80')
               

        p.sleep(1)
            
        print_horizontal = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_horizontal.png', confidence = 0.90)    

        if print_horizontal is not None:
            p.sleep(1)
            p.click(print_horizontal)

        p.sleep(1)    

        print_config = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_config.png', confidence = 0.80)

        if print_config is not None:
            p.sleep(1)
            p.click(print_config)    

        p.sleep(1)

        print_doro = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_doro_pdf.png', confidence = 0.80)    

        if print_doro is not None:
            p.click(print_doro)

    
            
        botao_ok = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_ok.png', confidence = 0.90)
            
        if botao_ok is not None:
            p.sleep(1)
            p.click(botao_ok)
      

        p.sleep(1)


        print_imprimir = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_imprimir.png', confidence = 0.80)

        if print_imprimir is not None:
            p.sleep(1)
            p.click(print_imprimir)
        else:
            logging.info('Nao encontrei o botao imprimir')

        #tratar imagem ok depois
        p.sleep(1)
        p.click(363,392)

        p.sleep(4)

        p.press('backspace')
        p.typewrite('relatorio_jangada_testes.pdf')

        print_criar = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_criar.png', confidence = 0.80)

        if print_criar is not None:
            p.sleep(1)
            p.click(print_criar)
            p.sleep(1)

        
        botao_substituir = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\print_substituir.png' , confidence = 0.90) 
        
        
        if botao_substituir is not None:
            p.sleep(3)
            p.click(778,390)   
  

        botao_fechar = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\botao_fechar.png' , confidence = 0.50)  

        if botao_fechar is not None:
            p.sleep(1)        
            p.click(1356,32)      

        botao_close = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\botao_vermelho_fechar.png' , confidence = 0.70)

        if botao_close is not None:
            p.sleep(3)       
            p.click(botao_close)


        botao_sair = p.locateCenterOnScreen(r'C:\Users\vinicius.ribeiro\Pictures\PrintsDesafio\botao_sair.png' , confidence = 0.50)

        if botao_sair is not None:
            
            p.sleep(2)
            p.click(botao_sair)      
    
    
    
    except Exception:
        error = traceback.format_exc()
        logging.error(error)
   
    finally:
        logging.info('Fim do bot')


        
    # if __name__ == '__main__':
    #     gerar_relatorio()




    





        
    


        
    
       
       



    
   


