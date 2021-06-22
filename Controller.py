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
            tst_result = obj.get_all()

        return  result

    def get_player_list(self):
        result = []
        player_set = set()
        for id, obj in self.tour_list:
            for player in obj.get_player_names():
                player_set.add(player)

        for player in player_set:
            tour = { }
            for id, obj in self.tour_list:
                tour[id] = obj.get_tour_points_with_bonus(player)
            result.append([player,tour])
        return  result
