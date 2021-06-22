class Tournament:
    def __init__(self, id ,db):
        self.id = id
        self.db = db
        self.results = db.get_results(id)
        self.bets = db.get_bets(id)
    def get_match_no(self):
        return len(self.results.keys())
    def get_total_goals(self):
        sum = 0
        for result in self.results.values():
            sum += result[0]
            sum += result[1]
        return sum
    def get_results_common(self):
        dict = {}
        check = ''
        for result in self.results.values():
            if result[0] >= result[1]:
                check = str(result[0]) + '-' + str(result[1])
            else:
                check = str(result[1]) + '-' + str(result[0])
            if check in dict.keys():
                dict[check] += 1
            else:
                dict[check] = 1
        return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
    def get_all_bets(self):
        return self.bets
    def get_player_no(self):
        return len(self.bets)
    def get_tour_stats(self):
        # count winner
        all = self.get_player_no() * self.get_match_no()
        good_winner = 0
        good_goals = 0
        good_result = 0
        joker = 0
        joker_hit = 0
        for player in self.bets.values():
            for res in player[1]:

                if res[3] != 0:
                    good_winner += 1
                if res[2] == True:
                    joker += 1
                    if res[3] != 0:
                        joker_hit += 1
                    if res[3] == 6:
                        good_goals += 1
                    elif res[3] == 10:
                        good_goals += 1
                        good_result += 1
                else:
                    if res[3] == 3:
                        good_goals += 1
                    if res[3] == 5:
                        good_result +=1
        return [round(good_winner/all*100,2), round(good_goals/all*100,2), round(good_result/all*100,2), round(joker_hit/joker*100,2)]

    def get_player_names(self):
        result = []
        for player in self.bets.keys():
            result.append(player)
        return  result
    def get_tour_points_with_bonus(self, player):
        result = 0
        pl = self.bets.get(player)
        if pl:
            # bonus
            result += pl[0]
            for res in pl[1]:
                result += res[3]
        return result
    def get_tour_points_no_bonus_joker(self,player):
        result = 0
        pl = self.bets.get(player)
        if pl:
            for res in pl[1]:
                if res[2]:
                    if res[3] != 0:
                        result += res[3]/2
                else:
                    result += res[3]
        return int(result)
    def get_point_for_match(self,player, match_idx):
        pl = self.bets.get(player)
        if pl:
                return  pl[1][match_idx][3]
        else:
            return 0
    def get_match_list(self):
        return  list(self.results.keys())
    def get_bonus_for_player(self,player):
        pl = self.bets.get(player)
        if pl:
            return pl[0]
        else:
            return 0
