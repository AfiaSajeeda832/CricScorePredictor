import pandas as pd
import numpy as np
import RandomForest
import KNN
import LinearRegressionAlgorithm
import DecisionTree
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import math




def getTeamAverage(team):
    #print(team)
    df = pd.read_csv('TeamAverage.csv').as_matrix()
    #print(df)

    data = np.where(df[:, 1] == team)
    team_matrix = df[data]
    team_matrix = np.array(team_matrix)

    #print(team_matrix)

    score = team_matrix[:, [2]]

    score= score[0][0]
    #print(score)
    score=float(score)

    return score

def getGroundAverage(ground):
    df = pd.read_csv('GroundDetails.csv').as_matrix()
    # print(df)

    data = np.where(df[:, 1] == ground)
    team_matrix = df[data]
    team_matrix = np.array(team_matrix)

    # print(team_matrix)

    ground_score = team_matrix[:, [2]]

    ground_score = ground_score[0][0]
    # print(score)
    score = float(ground_score)

    return ground_score

    # df = pd.read_csv('MatchDetails.csv').as_matrix()
    # row = np.where(df[:,3] == "Brisbane Cricket Ground, Woolloongabba")
    # team_matrix = df[row]
    # score_2d = team_matrix[:,[8,12]]
    # score_2d = score_2d.astype(np.int64)
    # mean_first_team = np.mean(score_2d[:,0])
    # print(mean_first_team)
    # mean_second_team = np.mean(score_2d[:,1])
    # print(mean_second_team)
    #print(score_2d[:,0])
    #print(team_matrix)

    #df2= df[:, "team1"]
    #print(df)


def generate_file(team, team_average, ground_average, overs):

    df= pd.read_csv('RunsPerOvers.csv').as_matrix()
    df2= pd.read_csv('WicketsPerOvers.csv').as_matrix()


    #Get the Runs
    data = np.where(df[:, 1] == team)
    run_matrix = df[data]
    run_matrix= np.array(run_matrix)

    #get the wickets
    data2 = np.where(df2[:, 1] == team)
    wickets_matrix = df2[data2]
    wickets_matrix = np.array(wickets_matrix)
    #print(team_matrix)


    runs_at_matrix=[]
    for row in run_matrix:
        runs= row[overs+1]
        totalRuns = row[50 + 1]
        runsRow = [runs, totalRuns]

        if len(runs_at_matrix) == 0:
            runs_at_matrix = np.array(runsRow)
        else:
            runs_at_matrix = np.vstack([runs_at_matrix, np.array(runsRow)])


    #print(runs_at_matrix)

    wickets_at_matrix = []

    for row in wickets_matrix:
        wickets = row[overs + 1]
        totalWickets = row[50 + 1]
        fileRow = [wickets, totalWickets]

        if len(wickets_at_matrix) == 0:
            wickets_at_matrix = np.array(fileRow)
        else:
            wickets_at_matrix = np.vstack([wickets_at_matrix, np.array(fileRow)])

    #print(wickets_at_matrix)

    #print(runs_at_matrix.ndim, runs_at_matrix.shape)
    #print(wickets_at_matrix.ndim, wickets_at_matrix.shape)

    match_matrix= np.concatenate([runs_at_matrix,wickets_at_matrix], axis=1)

    #print(match_matrix.shape)

    #print(match_matrix)

    #print(wickets_matrix)

    matrix=[]

    for row in match_matrix :

        runs= row[0]
        totalRuns=row[1]
        wickets= row[2]
        totalWickets= row[3]

        #print(overs," ",runs)
       #print("total: ",totalRuns)

        fileRow= [team_average, ground_average, runs,wickets, totalRuns, totalWickets]
        # i=i+1
        # print(i)
        # print(row)

        if len(matrix) == 0:
            matrix = np.array(fileRow)
        else:
            matrix = np.vstack([matrix, np.array(fileRow)])

    #
    pd.DataFrame(matrix, columns=['team_average', 'ground_average', 'runs','wickets', 'totalRuns', 'totalWickets']).to_csv("TestFile.csv", sep=',')
    print("Test File Created!!")

def predict_score(team,teamAverage,groundAverage,runs,wickets):
    fileName = 'TestFile.csv'
    matrix = pd.read_csv(fileName).as_matrix()

    X_train_matrix, X_test_matrix = train_test_split(matrix, test_size=0.2)

    X_train_matrix = np.delete(X_train_matrix, 0, 1)  # Get Rid of the first column
    X_test_matrix = np.delete(X_test_matrix, 0, 1)  # Get Rid of the first column

    X_train = pd.DataFrame(X_train_matrix,
                           columns=['team_average', 'ground_average', 'runs', 'wickets', 'totalRuns', 'totalwickets'])

    X_test = pd.DataFrame(X_test_matrix,
                          columns=['team_average', 'ground_average', 'runs', 'wickets', 'totalRuns', 'totalwickets'])

    X = X_train[['team_average', 'ground_average', 'runs', 'wickets']]
    Y = X_train[['totalRuns', 'totalwickets']]

    lin = LinearRegression()
    lin.fit(X, Y)

    X_test = [[teamAverage, groundAverage, runs, wickets]]
    score = lin.predict(X_test)

    print(score)

    run= score[0][0]
    if (run+.5)<math.ceil(run):
        run= math.floor(run)
    elif (run+.5)> math.ceil(run):
        run= math.ceil(run)
        #print("Dhuksi")

    wickets= score[0][1]
    if (wickets +.5)< math.ceil(wickets):
        wickets = math.floor(wickets)
    else:
        wickets = math.ceil(wickets)

    print(run," ", wickets)


def main1():
    team= input("Team Name:")
    ground= input("Ground Name:")
    oversGone= int(input("Overs Gone:") )

    runs= int( input("Run:") )
    wickets= int( input("Wickets:") )


    teamAverage= getTeamAverage(team)

    groundAverage= getGroundAverage(ground)

    generate_file(team, teamAverage,groundAverage,oversGone)

    predict_score(team,teamAverage,groundAverage,runs,wickets)


def mainProgram():
    team = input("Team Name:")
    ground = input("Ground Name:")
    oversGone = int(input("Overs Gone:"))
    #runs = int(input("Run:"))
    #wickets = int(input("Wickets:"))
    teamAverage = getTeamAverage(team)
    # print(teamAverage)
    groundAverage = getGroundAverage(ground)



    generate_file(team, teamAverage, groundAverage, oversGone)

    print("Using Linear Legression: ")
    LinearRegressionAlgorithm.predict_score_using_lr()

    print("Using KNN: ")
    KNN.predict_score_using_knn()

    print("Using Random Regressor: ")
    RandomForest.random_regressor()

    print("Using Decision Tree: ")
    DecisionTree.decision_tree()


mainProgram()

#main1()

