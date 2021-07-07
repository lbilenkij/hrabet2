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
    all_chart_data = controler.get_all_match_points()
    match_list = controler.get_all_match_list()
    return render_template('tournament_list.html', tour_list=tour_list, player=player_list, all_chart_data=all_chart_data, match_list=match_list )
@app.route('/tour/<tourID>')
def show_tournament(tourID):
    return render_template('tournament.html', tourID = tourID )

if __name__ == "__main__":
  app.run()