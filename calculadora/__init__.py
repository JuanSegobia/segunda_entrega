# Esto podria estar en otro archivo ya que no esta relacionado a la calculadora, pero lo pongo aca para no
# tener mas de un archivo con metodos.

def clear_names(names):
    names = names.replace(" ","")
    split_names = names.split(",")
    cleared_names = [name.lower() for name in split_names]
    return cleared_names

def players_stats_in_structure (names, goals, goals_avoided,assists):
    keys = clear_names(names)
    players_stats = {name: [goals, no_goals, assists] for name, goals, no_goals, assists in zip(keys, goals, goals_avoided, assists)}
    return players_stats

def get_top_scorer (player_stats):
    name_top_scorer = max(player_stats, key=lambda x: player_stats[x][0])
    return name_top_scorer, player_stats[name_top_scorer][0]

def most_influential_player(player_stats):
    most_influential = max(player_stats, key=lambda x: player_stats[x][0] * 1.5 + player_stats[x][1] * 1.25 + player_stats[x][2])
    return most_influential