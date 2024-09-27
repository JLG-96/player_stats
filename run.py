import pandas as pd # pandas imported as using data sets

class PlayerStats: 
    def __init__(self): 
        # Create DataFrae to store player statistics with columns
        self.stats = pd.DataFrame(columns = ['Player', 'Matches', 'Goals', 'Assists', 'Man of the Matches']
        )

# Add new players stats 
def add_player(self, player_name, matches, goals, assists, man_of_the_matches):
    try: 
        new_data = {'Player': player_name, 'Matches': int(matches), 'Goals': int(goals), 'Assists': int(assists), 'Man of the matches': int(man_of_the_matches)}
        self.stats = self.stats.append(new_data, ignore_index=True)
        print(f"{player_name}'s data added successfully!")
    except ValueError:
        # to prevent invalid input 
        print("Invalid input! Please ensure matches, goals, assists and man of the matches are numbers.")


# to display player stats
def display_stats(self):
    if not self.stats.empty: 
        print(self.stats.to.string(index=False))
    else:
        print("No player data is available.")

# to get a specific player's stats by name 
def get_player_stats(self, player_name):
    player_data = self.stats[self.stats['Player'] == player_name]
    if not player_data.empty:
        print(player_data.to_string(index=False))
    else:
        print(f"No stats found for {player_name}.")
