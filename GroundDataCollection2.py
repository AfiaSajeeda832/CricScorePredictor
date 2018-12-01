import pandas as pd
import yaml
import numpy as np
import os


def get_data():
    new_matrix = []
    matrix = []
    '''
    row = ['team1', 'team2', 'venue', 'date', 'toss', 'winnerTeam', 'team1RunRate', 'team1Runs', 'team1Wickets',
           'team1BallsPlayed',
           'team2RunRate', 'team2Runs', 'team2Wickets', 'team2BallsPlayed']

    matrix = np.array(row)
    '''

    row = ['team', 'Run/10', 'Wicket/10 ', 'Run/20', 'Wicket/20 ', 'Run/30', 'Wicket/30 ', 'Run/40', 'Wicket/40 ',
           'Team Total Run', 'Team Total Wicket',
           ]
    matrix= np.array(row)

    path = 'C:/Users/Shihab/Dropbox/6thSemester/604-AI/odis';

    for filename in os.listdir(path):

        print(filename + ":")
        with open(path + '/' + filename, 'r') as f:
            doc = yaml.load(f)
            venue = doc["info"]["venue"]
            date = doc["info"]["dates"][0]
            #print(date)
            team1 = doc["info"]["teams"][0]
            team2 = doc["info"]["teams"][1]
            # print(team1+" played against "+ team2)

            #toss = doc["info"]["toss"]["winner"]
            # print("Toss winner: "+ toss)

            team1Runs = 0
            team1Wickets = 0
            team1BallsPlayed = 0
            team1Run=[0,0,0,0]
            team1Wicket=[0,0,0,0]

            data = doc["innings"][0]['1st innings']['deliveries']

            for datum in data:
                for key, value in datum.items():
                    team1Runs += int(value['runs']['total'])
                    if 'wicket' in value:
                        team1Wickets += 1

                    if 'extras' not in value:
                        team1BallsPlayed += 1
                    elif 'legbyes' in value['extras'] \
                            or 'byes' in value['extras']:
                        team1BallsPlayed += 1

                    #runs in first 10 overs
                    if team1BallsPlayed<=60 :
                        team1Run[0]=team1Runs
                        team1Run[1] = team1Runs
                        team1Run[2] = team1Runs
                        team1Run[3] = team1Runs

                        team1Wicket[0] = team1Wickets
                        team1Wicket[1] = team1Wickets
                        team1Wicket[2] = team1Wickets
                        team1Wicket[3] = team1Wickets
                    #runs in first 20 overs
                    if team1BallsPlayed>60 and team1BallsPlayed<=120:
                        team1Run[1]= team1Runs
                        team1Run[2] = team1Runs
                        team1Run[3] = team1Runs

                        team1Wicket[1] = team1Wickets
                        team1Wicket[2] = team1Wickets
                        team1Wicket[3] = team1Wickets

                    # runs in first 30 overs
                    if team1BallsPlayed > 120 and team1BallsPlayed <= 180:
                        team1Run[2] = team1Runs
                        team1Run[3] = team1Runs

                        team1Wicket[2] = team1Wickets
                        team1Wicket[3] = team1Wickets

                    # runs in first 40 overs
                    if team1BallsPlayed > 180 and team1BallsPlayed <= 240:
                        team1Run[3] = team1Runs
                        team1Wicket[3] = team1Wickets

            #overs = team1BallsPlayed / 6
            #team1RunRate = team1Runs / overs

            # runRate2= team1Runs*6/team1BallsPlayed
            # print(team1Runs)
            # print(team1Wickets)
            # print(overs)
            # print(runRate)
            # print(runRate2)

            # print(team1Run[0])
            # print(team1Run[1])
            # print(team1Run[2])
            # print(team1Run[3])
            # print(team1Runs)

    #
    #         print("Second Innings:")
            data2 = None
            if len(doc["innings"]) > 1:
                data2 = doc["innings"][1]['2nd innings']['deliveries']

            team2Runs = 0
            team2Wickets = 0
            team2BallsPlayed = 0
            team2Run=[0,0,0,0]
            team2Wicket=[0,0,0,0]

            if data2 is not None:
                for datum in data2:
                    for key, value in datum.items():
                        team2Runs += int(value['runs']['total'])
                        if 'wicket' in value:
                            team2Wickets += 1

                        if 'extras' not in value:
                            team2BallsPlayed += 1
                        elif 'legbyes' in value['extras'] \
                                or 'byes' in value['extras']:
                            team2BallsPlayed += 1

                        # runs in first 10 overs
                        if team2BallsPlayed <= 60:
                            team2Run[0] = team2Runs
                            team2Run[1] = team2Runs
                            team2Run[2] = team2Runs
                            team2Run[3] = team2Runs

                            team2Wicket[0] = team2Wickets
                            team2Wicket[1] = team2Wickets
                            team2Wicket[2] = team2Wickets
                            team2Wicket[3] = team2Wickets
                        # runs in first 20 overs
                        if team2BallsPlayed > 60 and team2BallsPlayed <= 120:
                            team2Run[1] = team2Runs
                            team2Run[2] = team2Runs
                            team2Run[3] = team2Runs

                            team2Wicket[1] = team2Wickets
                            team2Wicket[2] = team2Wickets
                            team2Wicket[3] = team2Wickets

                        # runs in first 30 overs
                        if team2BallsPlayed > 120 and team2BallsPlayed <= 180:
                            team2Run[2] = team2Runs
                            team2Run[3] = team2Runs

                            team2Wicket[2] = team2Wickets
                            team2Wicket[3] = team2Wickets

                        # runs in first 40 overs
                        if team2BallsPlayed > 180 and team2BallsPlayed <= 240:
                            team2Run[3] = team2Runs
                            team2Wicket[3] = team2Wickets

                oversTeam2 = team2BallsPlayed / 6
                team2RunRate = team2Runs / oversTeam2


            row = [team1,team1Run[0],team1Wicket[0],team1Run[1],team1Wicket[1],team1Run[2],team1Wicket[2],team1Run[3],team1Wicket[3],
                   team1Runs,team1Wickets
                   ]
            row2=[team2,team2Run[0],team2Wicket[0],team2Run[1],team2Wicket[1],team2Run[2],team2Wicket[2],team2Run[3],team2Wicket[3],
                   team2Runs,team2Wickets
            ]

            if len(matrix) == 0:
                matrix = np.array(row)
                matrix = np.array(row2)

            else:
                matrix = np.vstack([matrix, np.array(row)])
                matrix = np.vstack([matrix, np.array(row2)])


            #print(matrix)

    pd.DataFrame(matrix).to_csv("MatchInOvers.csv", sep=',')

    print("Finish")


get_data()