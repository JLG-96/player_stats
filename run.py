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
        print("Invalid input! Please ensure matches, goals, assists and man of the matches are numbers.")
