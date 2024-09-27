import pandas as pd # pandas imported as using data sets

class PlayerStats: 
    def __init__(self): 
        # Create DataFrae to store player statistics with columns
        self.stats = pd.DataFrame(columns = ['Player', 'Matches', 'Goals', 'Assists', 'Man of the Matches']
        )