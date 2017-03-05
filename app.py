from flask import Flask
from flask import render_template
from testcursos import Consumer
import json

my_consumer = Consumer()

app = Flask(__name__)


@app.route("/inicio")
def inicio():
	titulos_soft_deve = my_consumer.coursera_soft_deve()
	titulos_music_art = my_consumer.coursera_music_art()
	titulos_web_deve = my_consumer.coursera_web_deve()
	titulos_desing_prod = my_consumer.coursera_desing_prod()
	titulos_machine_lear = my_consumer.coursera_machine_lear()
	titulos_perso_deve = my_consumer.coursera_perso_deve()
	return render_template('inicio.html',sdeve=titulos_soft_deve, music = titulos_music_art, webs = titulos_web_deve, desing = titulos_desing_prod, machine_lear=titulos_machine_lear , perso_deve = titulos_perso_deve )


if __name__ == "__main__":
    app.run()