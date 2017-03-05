from bs4 import BeautifulSoup
import requests
import json

class Consumer:
    def coursera_soft_deve(self):
        titulos_todos = []
        urlCoursera = "https://www.coursera.org/browse/computer-science/software-development"
        maxPages = 20
        counter = 0

        req = requests.get(urlCoursera)

        statusCode = req.status_code

        if statusCode == 200:


            html = BeautifulSoup(req.text)


            entradas = html.find_all('div',{'class':'offering-info flex-1'})


            for entrada in entradas:
                counter += 1
                titulo = entrada.find('h2', {'class' : 'color-primary-text headline-1-text flex-1'}).getText()
                    #autor = entrada.find('span', {'class' : 'autor'}).getText()
                    #fecha = entrada.find('span', {'class' : 'fecha'}).getText()
                titulos_todos.append(titulo)

                print titulo

            
            return titulos_todos

    def coursera_music_art(self):
        titulos_todos = []
        urlCoursera = "https://www.coursera.org/browse/arts-and-humanities/music-and-art"
        maxPages = 20
        counter = 0

        req = requests.get(urlCoursera)

        statusCode = req.status_code

        if statusCode == 200:


            html = BeautifulSoup(req.text)


            entradas = html.find_all('div',{'class':'offering-info flex-1'})


            for entrada in entradas:
                counter += 1
                titulo = entrada.find('h2', {'class' : 'color-primary-text headline-1-text flex-1'}).getText()
                    #autor = entrada.find('span', {'class' : 'autor'}).getText()
                    #fecha = entrada.find('span', {'class' : 'fecha'}).getText()
                titulos_todos.append(titulo)

                print titulo

            
            return titulos_todos



    def coursera_web_deve(self):
        titulos_todos = []
        urlCoursera = "https://www.coursera.org/browse/computer-science/mobile-and-web-development"
        maxPages = 20
        counter = 0

        req = requests.get(urlCoursera)

        statusCode = req.status_code

        if statusCode == 200:


            html = BeautifulSoup(req.text)


            entradas = html.find_all('div',{'class':'offering-info flex-1'})


            for entrada in entradas:
                counter += 1
                titulo = entrada.find('h2', {'class' : 'color-primary-text headline-1-text flex-1'}).getText()
                    #autor = entrada.find('span', {'class' : 'autor'}).getText()
                    #fecha = entrada.find('span', {'class' : 'fecha'}).getText()
                titulos_todos.append(titulo)

                print titulo

            
            return titulos_todos


    def coursera_desing_prod(self):
        titulos_todos = []
        urlCoursera = "https://www.coursera.org/browse/computer-science/design-and-product"
        maxPages = 20
        counter = 0

        req = requests.get(urlCoursera)

        statusCode = req.status_code

        if statusCode == 200:


            html = BeautifulSoup(req.text)


            entradas = html.find_all('div',{'class':'offering-info flex-1'})


            for entrada in entradas:
                counter += 1
                titulo = entrada.find('h2', {'class' : 'color-primary-text headline-1-text flex-1'}).getText()
                    #autor = entrada.find('span', {'class' : 'autor'}).getText()
                    #fecha = entrada.find('span', {'class' : 'fecha'}).getText()
                titulos_todos.append(titulo)

                print titulo

            
            return titulos_todos

    def coursera_machine_lear(self):
        titulos_todos = []
        urlCoursera = "https://www.coursera.org/browse/data-science/machine-learning"
        maxPages = 20
        counter = 0

        req = requests.get(urlCoursera)

        statusCode = req.status_code

        if statusCode == 200:


            html = BeautifulSoup(req.text)


            entradas = html.find_all('div',{'class':'offering-info flex-1'})


            for entrada in entradas:
                counter += 1
                titulo = entrada.find('h2', {'class' : 'color-primary-text headline-1-text flex-1'}).getText()
                    #autor = entrada.find('span', {'class' : 'autor'}).getText()
                    #fecha = entrada.find('span', {'class' : 'fecha'}).getText()
                titulos_todos.append(titulo)

                print titulo

            
            return titulos_todos

    def coursera_perso_deve(self):
        titulos_todos = []
        urlCoursera = "https://www.coursera.org/browse/personal-development"
        maxPages = 20
        counter = 0

        req = requests.get(urlCoursera)

        statusCode = req.status_code

        if statusCode == 200:


            html = BeautifulSoup(req.text)


            entradas = html.find_all('div',{'class':'offering-info flex-1'})


            for entrada in entradas:
                counter += 1
                titulo = entrada.find('h2', {'class' : 'color-primary-text headline-1-text flex-1'}).getText()
                    #autor = entrada.find('span', {'class' : 'autor'}).getText()
                    #fecha = entrada.find('span', {'class' : 'fecha'}).getText()
                titulos_todos.append(titulo)

                print titulo

            
            return titulos_todos