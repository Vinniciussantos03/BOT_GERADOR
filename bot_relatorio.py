from src.model.relatorio import gerar_relatorio
import logging
import traceback
import os
import pyautogui as p

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='log.txt', filemode='w', datefmt='%d/%m/%Y %H:%M:%S', encoding='utf-8')

try:
    logging.info('inicio do bot')
    print('inicio do bot')
    os.startfile(rf"C:\Conces\vec\vec.exe")
    p.sleep(1)
    gerar_relatorio()

except Exception:
    error = traceback.format_exc()
    logging.error(error)

finally:
    print('fim do bot')
    logging.info('Tarefa Concluida')
    # os.system("taskkill /im vec.exe")