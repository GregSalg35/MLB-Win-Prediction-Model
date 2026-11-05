import pandas as pd 

# read in batting data and get ready for querying
df = pd.read_csv("Batting_Final_Cleaned.csv")
df.to_csv("Batting_Final_Cleaned.csv", index=False, na_rep="NULL")


# read in teams csv file and get ready for querying
teamstats = pd.read_csv("Teams.csv")
teamstats.to_csv("TeamsCleaned.csv", index=False, na_rep="NULL")




