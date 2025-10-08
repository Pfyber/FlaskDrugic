from flask import Flask, render_template
import random
# pip install flask
# python app.py
app = Flask(__name__)
dijaki = ["Aljaž", "Bine", "Cene", "Darko"]


@app.route("/")
def hello_world():
    dijak = random.choice(dijaki)
    ocena = random.randint(1,5)
    return render_template("index.html", naslov = "Najboljša stran!❤️",
                            dijakHTML = dijak, ocenaHTML = ocena )

@app.route("/randomOseba")
def rndOseba():
    return "Page 2"


app.run(debug=True, port=7777 )


# napiši route /randomOseba
# ki zgenerira random ime, priimek, starost in kraj rojstva
# naslov in random številko naslova
# sezname generiraj z AI
# na koncu celoten HTML daj v AI 
# AI promprtaj naj naredi lep CSS za html file
