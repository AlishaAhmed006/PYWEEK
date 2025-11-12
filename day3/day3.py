import pandas as pd
df=pd.read_csv("C:/Users/USER/Desktop/VS CODE/python-day1/venv/ipl-matches.csv")
print(df)
print(df.head())#first 5 rows
print(df.shape)#size
#showing every team
print(df["Team1"].unique())
#number of matches per season
print(df["Season"].value_counts())
#team winning most matches
print(df["WinningTeam"].value_counts().head(1))
#showing matches where mumbai indians were the winners
print(df[df["WinningTeam"]=="Mumbai Indians"])
#all matches in which a super over took place
print(df[df["SuperOver"]=="Y"])
#all matches played in Eden Garden
print(df[df["Venue"]=="Eden Gardens"])
#check if toss winner is match winner - in percentage
print(df[(df["TossWinner"]==df["WinningTeam"])].shape[0]/df.shape[0]*100)