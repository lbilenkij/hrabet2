class FileDataReader:
    def __init__(self):
        self.tour_match = {}
        self.country = {}
        self.bets = {}
        # read match lis and results
        self.read_match_list('file_src/match_EURO16.csv', 'ME16')
        self.read_match_list('file_src/match_WM2018.csv', 'WM18')
        # self.read_match_list('file_src/match_EURO20.csv', 'ME20')
        self.read_cntr()
        self.read_bets('file_src/betsEUR2016.csv', 'ME16')
        self.read_bets('file_src/betsMS2018.csv', 'WM18')
        # self.read_bets('file_src/betsEUR2020.csv', 'ME20')

    def read_match_list(self, filename, tourID):
        match_file = open(filename, encoding="utf8")
        lines = match_file.readlines()
        dict = {}
        names = lines[0].split(';')
        results = lines[1].split(';')
        idx = 0
        for name in names:
            res_tab = results[idx].strip().split(':')
            dict[name.strip()] = (int(res_tab[0].strip()), int(res_tab[1].strip()))
            idx += 1
        self.tour_match[tourID] = dict

    def read_cntr(self):
        ctr_file = open('file_src/country.csv', encoding="utf8")
        lines = ctr_file.readlines()
        for line in lines:
            splitted = line.split(';')
            self.country[splitted[2].strip()] = splitted[1].strip()

    def read_bets(self, filename, tourID):
        bets_file = open(filename, encoding='utf8')
        lines = bets_file.readlines()
        self.bets[tourID] = {}
        for line in lines:
            lcl_dict = {}
            lcl_player = []
            lcl_result = []

            splitted = line.split(';')
            bonus_start = splitted[1].find('(')+1
            bonus_end = splitted[1].find(')')
            bonus = splitted[1][bonus_start:bonus_end]
            if bonus != '':
                lcl_player.append(int(splitted[1][bonus_start:bonus_end]))
            else:
                lcl_player.append(0)
            for res in splitted[2:]:
                result = []
                if res[0] == "-":
                    lcl_result.append([-1, -1, False, 0])
                    continue

                # home score
                result.append(int(res[0]))
                # away score
                result.append(int(res[2]))
                # joker TRue/False
                try:
                    if res[5].isdigit():
                        joker = True
                    else:
                        joker = False
                except IndexError:
                    joker = False
                result.append(joker)
                #points

                if joker:
                    result.append(int(res[4])*int(res[5]))
                else:
                    result.append(int(res[4]))
                lcl_result.append(result)
            lcl_player.append(lcl_result)
            self.bets[tourID][splitted[0].strip()] = lcl_player

    def get_match_list(self):
        return self.tour_match

    def get_country(self):
        return self.country

    def get_bets(self):
        return self.bets


class FileDB:
    def __init__(self):
        self.reader = FileDataReader()
        self.match_results = self.reader.get_match_list()
        self.cntr_data = self.reader.get_country()
        self.bets = self.reader.get_bets()

    def get_country_name(self, id):
        return self.cntr_data[id]

    def get_tour_id(self):
        return self.match_results.keys()

    def get_results(self, tourID):
        return self.match_results[tourID]

    def get_bets(self, tourID):
        return self.bets[tourID]
