
def clear_names(names:str):
    names = names.replace(" ","")
    split_names = names.split(",")
    return split_names

def players_stats_in_structure (names:list, goals:int, goals_avoided:int, assists:int):
    keys = clear_names(names)
    players_stats = {name: (goals, no_goals, assists) for name, goals, no_goals, assists in tuple(zip(map(str.lower,keys), goals, goals_avoided, assists))}
    return players_stats

def get_top_scorer (player_stats:dict):
    name_top_scorer = max(player_stats, key=lambda x: player_stats[x][0])
    return name_top_scorer, player_stats[name_top_scorer][0]

def most_influential_player(player_stats:dict):
    most_influential = max(player_stats, key=lambda x: player_stats[x][0] * 1.5 + player_stats[x][1] * 1.25 + player_stats[x][2])
    return most_influential

def goals_per_match(goals:int, matches:int): 
    average = sum(goals) / matches
    return average

def top_scorer_average (top_scorer_goals:int, matches:int):
    average = top_scorer_goals / matches
    return average