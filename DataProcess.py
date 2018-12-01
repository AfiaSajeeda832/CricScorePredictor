from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

def getGroundDetails():
    df = pd.read_csv('MatchDetails.csv').as_matrix()

    grounds=set()
    matrix=[]

    for row in df:
        row = row[3]
        grounds.add(row)
        #print(row)

    grounds.remove('venue')
    print(grounds)

    for ground in grounds:

        data = np.where(df[:, 3] == ground)
        team_matrix = df[data]
        score_2d = team_matrix[:, [8, 12]]
        score_2d = score_2d.astype(np.int64)
        mean_first_team = np.mean(score_2d[:, 0])
        #print(mean_first_team)
        mean_second_team = np.mean(score_2d[:, 1])
        #print(mean_second_team)

        #remove the ground
        #grounds.remove(ground)

        print(ground)
        print(mean_first_team)
        print(mean_second_team)

        row=[ground, mean_first_team, mean_second_team]

        if len(matrix) == 0:
            matrix = np.array(row)
        else:
            matrix = np.vstack([matrix, np.array(row)])

    pd.DataFrame(matrix).to_csv("GroundDetails.csv", sep=',')


def getTeamDetails():

    df = pd.read_csv('MatchInOvers.csv').as_matrix()

    #print(df)

    teams = set()
    matrix = []

    for row in df:
        row1 = row[1]
        #row2=row[2]
        teams.add(row1)
        #teams.add(row2)
        #print(row1)

        #teams.remove(team)

    teams.remove('team')
    #teams.remove('team2')
    print(teams)
    #print(teams.__len__())

    row = ['team', 'average_team_Score']
    matrix = np.array(row)

    for team in teams:

        data = np.where(df[:, 1] == team)
        team_matrix = df[data]
        team_matrix= np.array(team_matrix)


        score_2d = team_matrix[:,[10]]
        score_2d = score_2d.astype(np.int64)
        #print(score_2d)

        average_team_Score = np.mean(score_2d[:,0])
        print(team)
        print(average_team_Score)

        row = [team, average_team_Score]

        if len(matrix) == 0:
            matrix = np.array(row)
        else:
            matrix = np.vstack([matrix, np.array(row)])


    pd.DataFrame(matrix).to_csv("TeamAverage.csv", sep=',')


#getGroundDetails()
getTeamDetails()