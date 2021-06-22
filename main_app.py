from flask import Flask
from flask import render_template
from fileDB import FileDB
from Controller import Controler
app = Flask(__name__)
db = FileDB()
controler = Controler(db)
@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/halloffame')
def show_hof():
    tour_list = controler.get_tournament_table()
    player_list = controler.get_player_list()
    return render_template('tournament_list.html', tour_list=tour_list, player=player_list)

if __name__ == "__main__":
  app.run()