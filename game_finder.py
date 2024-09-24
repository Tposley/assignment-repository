from collections import defaultdict
from datetime import datetime

def find_qualified_games(game_data, true_shooting_cutoff, player_count):
    # Dictionary to hold counts of qualified players per game
    qualified_players_count = defaultdict(int)
    game_dates = {}

    for entry in game_data:
        # Calculate total points for the player
        points = (entry['fieldGoal2Made'] * 2) + (entry['fieldGoal3Made'] * 3) + entry['freeThrowMade']
        field_goal_attempts = entry['fieldGoal2Attempted'] + entry['fieldGoal3Attempted']
        free_throw_attempts = entry['freeThrowAttempted']

        # Calculate TS%
        if field_goal_attempts + 0.44 * free_throw_attempts > 0:
            ts_percentage = points / (2 * (field_goal_attempts + 0.44 * free_throw_attempts))
        else:
            ts_percentage = 0

        # Check if the TS% meets the cutoff
        if ts_percentage >= true_shooting_cutoff:
            qualified_players_count[entry['gameID']] += 1
            game_dates[entry['gameID']] = entry['gameDate']

    # Filter games with enough qualified players
    qualified_game_ids = [
        game_id for game_id, count in qualified_players_count.items() if count >= player_count
    ]

    # Sort games by date (most recent first)
    qualified_game_ids.sort(key=lambda game_id: datetime.strptime(game_dates[game_id], '%m/%d/%Y'), reverse=True)

    return qualified_game_ids