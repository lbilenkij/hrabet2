from Tournament import Tournament


class Controler:
    def __init__(self, db):
        self.db = db
        self.tour_list = []
        for tour in db.get_tour_id():
            self.tour_list.append([tour, Tournament(tour, db)])

    def get_tournament_table(self):
        result = []
        for id, obj in self.tour_list:
            match_no = obj.get_match_no()
            goals = obj.get_total_goals()
            stats = obj.get_tour_stats()
            result.append([id, match_no , obj.get_player_no(), goals, round(goals/match_no, 2), stats[0], stats[1], stats[2], stats[3]])
            tst = obj.get_results_common()
            tst_result = obj.get_all_bets()

        return  result

    def get_player_list(self):
        result = []
        player_set = set()
        for id, obj in self.tour_list:
            for player in obj.get_player_names():
                player_set.add(player)

        for player in player_set:
            sum = 0
            sum_vanilla = 0
            tour = { }
            player_stats = [0,0,0]
            for id, obj in self.tour_list:
                tour[id] = obj.get_tour_points_with_bonus(player)
                sum_vanilla += obj.get_tour_points_no_bonus_joker(player)
                tmp_stats = obj.get_player_stats(player)
                player_stats[0] += tmp_stats[0]
                player_stats[1] += tmp_stats[1]
                player_stats[2] += tmp_stats[2]
                sum += tour[id]
            result.append([player,tour, sum, sum_vanilla, player_stats[0], player_stats[1], player_stats[2]])
        return sorted(result, key=lambda l:l[2], reverse=True)

    def get_all_match_points(self):
        result = []

        players = self.get_player_list()
        for pl in players:
            sum = 0
            res = {}
            res['player'] = pl[0]
            res['value'] = []
            for id, obj in self.tour_list:
                for i in range(0, (obj.get_match_no())):
                    sum += obj.get_point_for_match(pl[0], i)
                    res['value'].append(sum)
                sum += obj.get_bonus_for_player(pl[0])
                res['value'].append(sum)

            result.append(res)
        return result

    def get_all_match_list(self):
        result = []
        for id, obj in self.tour_list:
            match = obj.get_match_list()
            match.append('BONUS'+id)
            result = result + match
        return result




