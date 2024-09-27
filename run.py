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


# Main function to run the programme 

def main():
    tracker = PlayerStats()

    while True:
        # Display main options 
        print("\nFootball Stats Tracker")
        print("1. Add player stats")
        print("2. Display all stats")
        print("3. Get player stats")
        print("4. Exit")

        choice = input("Enter your choice: ") #Get user choice

        if choice == '1':
            # Add new player stats 
            name = input("Enter player name: ")
            matches = input("Enter matches played: ")
            goals = input("Enter goals scored: ")
            assists = input("Enter assists made: ")
            man_of_the_matches = input("Enter man of the matches earned: ")

        elif choice == '2':
            # Display all player stats
            tracker.display.stats()
        
        elif choice == '3':
            # Retrieve specific player stats 
            name = input("Enter player name: ")
            tracker.get_player_stats(name)

        elif choice == '4':
            # Exit the programme 
            print("Exiting the tracker.")
            break

        else:
            print("Invalid choice! Please select a valid option.")
            