from flask import Flask
from fileDB import  FileDB

app = Flask(__name__)
db = FileDB()

def read_cntr():
  ctr_file = open('file_src/country.csv', encoding="utf8")
  lines = ctr_file.readlines()
  dict = {}
  for line in lines:
    splitted = line.split(';')
    dict[splitted[2].strip()] = splitted[1].strip()
  db.set_cntr(dict)


def read_match(filename, tourID):
  match_file = open(filename, encoding="utf8")
  lines = match_file.readlines()
  dict = {}
  names = lines[0].split(';')
  results = lines[1].split(';')
  idx = 0
  for name in names:
    res_tab = results[idx].strip().split(':')
    dict[name.strip()] = ( int(res_tab[0].strip()), int(res_tab[1].strip()))
    idx += 1
  mtch_tuple = (tourID, dict)
  db.add_match_list(mtch_tuple)

if __name__ == "__main__":
  read_cntr()
  read_match('file_src/match_WM2018.csv', 'WM18')
  app.run()


