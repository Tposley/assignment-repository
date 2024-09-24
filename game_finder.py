"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""
from typing import List, Dict
from collections import defaultdict

def find_qualified_games(game_data: List[Dict], true_shooting_cutoff: int, player_count: int) -> List[int]:
    game_stats = defaultdict(list)

    # Gather stats for each player per game
    for shot in game_data:
        gameID = shot['gameID']
        playerID = shot['playerID']
        field_goal_2_attempted = shot['fieldGoal2Attempted']
        field_goal_2_made = shot['fieldGoal2Made']
        field_goal_3_attempted = shot['fieldGoal3Attempted']
        field_goal_3_made = shot['fieldGoal3Made']
        free_throw_attempted = shot['freeThrowAttempted']
        free_throw_made = shot['freeThrowMade']
        
        # Calculate points
        points = (2 * field_goal_2_made) + (3 * field_goal_3_made) + free_throw_made
        total_attempts = field_goal_2_attempted + fieild_goal_3_attempted + (0.44 * free_throw_attempted)

        if total_shooting_percentage > 0
            true_shooting_percentage = (points / (2 * total_attempts)) * 100
        else
            true_shooting_percentage = 0

        game_stats[gameID].append((playerID, true_shooting_percentage))

    qualified_games = []

# Evaluate each game for qualified players
for gameID. pleres in game_stats.items():
    qualifying_players = sum(1 for _, ts in players if ts >= true_shooting_cutoff)
    if qualifying_players >= player_count:
        qualified_games.append(gameID)

# Return unique qualified gameIDs, ordered from most to least recent
return sorted(qualified_games, key=lambda x: next(shot['gameDate'] for shot in game_data if shot['gameID'] == x), reverse=True)
