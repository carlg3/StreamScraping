# Problemi: se lo eseguo come .exe da CMD, senza cliccarci due volte su, dà errore perché secondo lui non passo il giusto path a chromedriver
# 
import os.path, sys
# import chromedriver_binary # togli il commento se usi il .py
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


DISCONNECTED_MSG = 'Unable to evaluate script: disconnected: not connected to DevTools\n'

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def main():
    
    print("Una volta aperta la pagina di Chrome: \n 1. Ordina per Data i video su Stream \n 2. Scendi giù finchè non finiscono i video \n 3. Chiudi la pagina \nOra potrai trovare i link ordinati per Data nella stessa cartella del .py\n")
    print("Incolla l'url al gruppo di video su Stream: ")
    url = input()
    print("Preso!")

    '''
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    '''
    
    application_path_nr = os.path.dirname(__file__)
    application_path = resource_path(os.path.dirname(__file__))
    chrome_path = os.path.join(application_path, 'selenium','webdriver','chromedriver.exe')

    try:
        if getattr(sys, 'frozen', False): 
          # executed as a bundled exe, the driver is in the extracted folder
          driver = webdriver.Chrome(chrome_path)
        else:
          # executed as a simple script, the driver should be in `PATH`
          driver = webdriver.Chrome()
    except selenium.common.exceptions.WebDriverException:
        print("Sembra che non hai Chrome installato!")
    
    driver.get(url)
    
    while True:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        try:
            ris = driver.get_log('driver')[-1]['message'] 
        except IndexError:
            ris = ''
            pass
        if ris == DISCONNECTED_MSG:
            print ('OK')
            break
    sleep(1)

    src = soup.find_all(attrs={"class":"c-hyperlink c-caption-1 video-list-item-title no-hover"})
    src1 = BeautifulSoup(str(src), 'lxml')
    urls = []

    for a in src1.find_all('a', href=True):
        urls.append(a['href'])

    nome_txt = 'lista_link.txt'
    percorso_txt = os.path.join(application_path_nr,nome_txt)
    with open(percorso_txt, "w+") as o:
        for links in urls:
            o.write('https://web.microsoftstream.com'+str(links))
            o.write('\n')
    o.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("OK. ciao.")