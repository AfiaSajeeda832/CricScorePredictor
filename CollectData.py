import pandas as pd
import yaml
import numpy as np
import os

def get_data():

    new_matrix=[]
    matrix = []

    row = ['team1', 'team2', 'venue','date','toss', 'winnerTeam','team1RunRate','team1Runs', 'team1Wickets', 'team1BallsPlayed',
           'team2RunRate','team2Runs', 'team2Wickets', 'team2BallsPlayed']

    matrix = np.array(row)

    path='C:/Users/Shihab/Dropbox/6thSemester/604-AI/odis';

    for filename in os.listdir(path):

        print(filename+":")
        with open(path+'/' + filename, 'r') as f:
            doc = yaml.load(f)
            venue= doc["info"]["venue"]
            date= doc["info"]["dates"][0]
            #print(date)
            team1= doc["info"]["teams"][0]
            team2= doc["info"]["teams"][1]
            #print(team1+" played against "+ team2)

            toss= doc["info"]["toss"]["winner"]
            #print("Toss winner: "+ toss)

            outcome = doc["info"]["outcome"]
            #print(outcome)

            winnerTeam=""
            for key, value in outcome.items():
                #print(key)
                if key =='by':
                    continue
                if 'winner' not in key:
                    winnerTeam="no result"
                else:
                    winnerTeam=value;

            #print(winnerTeam)

            '''
            if doc["info"]["outcome"]["winner"] in doc :
                print("Hudai")
                winnerTeam= doc["info"]["outcome"]["winner"]
            else:
                winnerTeam= "none"

            print(winnerTeam)
            
            
            print("Second Innings:")
            data2 = None
            if len(doc["innings"]) > 1:
                data2 = doc["innings"][1]['2nd innings']['deliveries']

            for datum in data2:
                print(datum)
            
            data = doc["innings"][0]['1st innings']['deliveries']

            for datum in data:
                print(datum)

            '''


            '''
            
            '''
            team1Runs = 0
            team1Wickets = 0
            team1BallsPlayed = 0

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

            overs= team1BallsPlayed/6
            team1RunRate= team1Runs/overs

            #runRate2= team1Runs*6/team1BallsPlayed
            #print(team1Runs)
            #print(team1Wickets)
            #print(overs)
            #print(runRate)
            #print(runRate2)

            #print("Second Innings:")
            data2 = None
            if len(doc["innings"]) > 1:
                data2 = doc["innings"][1]['2nd innings']['deliveries']

            team2Runs = 0
            team2Wickets = 0
            team2BallsPlayed = 0

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

                oversTeam2 = team2BallsPlayed / 6
                team2RunRate = team2Runs / oversTeam2


            row = [team1 , team2,venue,date,toss, winnerTeam,team1RunRate, team1Runs, team1Wickets, team1BallsPlayed,
                   team2RunRate, team2Runs, team2Wickets, team2BallsPlayed]

            if len(matrix) == 0:
                matrix = np.array(row)
            else:
                matrix = np.vstack([matrix, np.array(row)])

            #print(matrix)

    pd.DataFrame(matrix).to_csv("MatchDetails.csv", sep=',')

    print("Finish")

get_data()