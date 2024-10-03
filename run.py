import pandas as pd # pandas imported as using data sets
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('CPD-player-stats')


class PlayerStats: 
    def __init__(self, sheet_worksheet): 
        # Create DataFrame to store player statistics with columns
        self.stats = pd.DataFrame(columns = ['Player', 'Matches', 'Goals', 'Assists', 'Yellow Cards', 'Red Cards']
        )
        self.sheet_worksheet = sheet_worksheet

# Add new players stats 
    def add_player(self, player_name, matches, goals, assists, yellow_cards, red_cards):
        try:
            new_data = {'Player': player_name, 'Matches': int(matches), 'Goals': int(goals), 'Assists': int(assists), 'Yellow Cards': int(yellow_cards), 'Red Cards': int(red_cards)}
            self.stats = pd.concat([self.stats, pd.DataFrame([new_data])], ignore_index=True)
            print(f"{player_name}'s data added successfully!")

            # Append the player stats to Google Sheet
            row = [player_name, matches, goals, assists, yellow_cards, red_cards]
            self.sheet_worksheet.append_row(row)
            print("Data being added to Google Sheet.")

        except ValueError:
            # to prevent invalid input 
            print("Invalid input! Please ensure matches, goals, assists, yellow cards and red cards are numbers.")


# to display player stats from Google Sheet
    def display_stats(self):

        # Retrieve values from google sheet
        sheet_data = self.sheet_worksheet.get_all_values()

        stats_df = pd.DataFrame(sheet_data[1:], columns=sheet_data[0])


        if not stats_df.empty: 
            print(stats_df.to_string(index=False))
        else:
            print("No player data is available.")

# to get a specific player's stats by name 
    def get_player_stats(self, player_name):
        # Retrieve all player stats from google sheet
        sheet_data = self.sheet_worksheet.get_all_values()

        stats_df = pd.DataFrame(sheet_data[1:], columns=sheet_data[0])

        # Filter for the specific player
        player_data = stats_df[stats_df['Player'].str.lower() == player_name.lower()] # Case-insensitive match

        if not player_data.empty:
            print(player_data.to_string(index=False))
        else:
            print(f"No stats found for {player_name}.")

    # Method to get the top players for the different stats

    def get_top_players(self):
        sheet_data = self.sheet_worksheet.get_all_values()
        stats_df = pd.DataFrame(sheet_data[1:], columns=sheet_data[0])

        if stats_df.empty:
            print("There is no top player for this category.")
            return

        # Convert values to integers for easy comparison
        stats_df[['Matches', 'Goals', 'Assists', 'Yellow Cards', 'Red Cards']] = stats_df[['Matches', 'Goals', 'Assists', 'Yellow Cards', 'Red Cards']].apply(pd.to_numeric)

        # Function to find top players
        def find_top_players(column_name):
            max_value = stats_df[column_name].max()
            if max_value == 0:
                return "No top player for this category."
            top_players = stats_df[stats_df[column_name] == max_value]['Player'].tolist()
            return ', '.join(top_players) if top_players else "No top player for this category"
        
        # Get the top player(s) for each statistic
        top_matches = find_top_players('Matches')
        top_goals = find_top_players('Goals')
        top_assists = find_top_players('Assists')
        top_yellow_cards = find_top_players('Yellow Cards')
        top_red_cards = find_top_players('Red Cards')


        print("\nTop Players: ")
        print(f"Most Matches Played: {top_matches}")
        print(f"Most Goals Scored: {top_goals}")
        print(f"Most Assists Made: {top_assists}")
        print(f"Most Yellow Cards: {top_yellow_cards}")
        print(f"Most Red Cards: {top_red_cards}")




# Main function to run the programme 

def main():
    stats_worksheet = SHEET.worksheet('stats')
    tracker = PlayerStats(stats_worksheet)

    while True:
        # Display main options 
        print("\nCPD Yr Wyddgrug Stats Tracker")
        print("1. Add player stats")
        print("2. Display all stats")
        print("3. Get player stats")
        print("4. Get top players")
        print("5. Exit")

        choice = input("Enter your choice: ") # Get user choice

        if choice == '1':
            # Add new player stats 
            name = input("Enter player name: ")
            matches = input("Enter matches played: ")
            goals = input("Enter goals scored: ")
            assists = input("Enter assists made: ")
            yellow_cards = input("Enter yellow cards received: ")
            red_cards = input("Enter red cards received: ")

            # Add player data
            tracker.add_player(name, matches, goals, assists, yellow_cards, red_cards)

        elif choice == '2':
            # Display all player stats
            tracker.display_stats()
        
        elif choice == '3':
            # Retrieve specific player stats 
            name = input("Enter player name: ")
            tracker.get_player_stats(name)

        elif choice == '4':
            # Display top players for each stat
            tracker.get_top_players()

        elif choice == '5':
            # Exit the programme 
            print("Exiting the tracker.")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main() # Run main function