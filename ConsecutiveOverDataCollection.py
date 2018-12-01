import pandas as pd
import yaml
import numpy as np
import os


def get_data():

    runs_matrix = []
    wickets_matrix=[]
    path = 'C:/Users/Shihab/Dropbox/6thSemester/604-AI/odis';

    for filename in os.listdir(path):

        runs_by_overs = np.array([])
        wickets_by_overs = np.array([])

        runs_by_overs_second_innings = np.array([])
        wickets_by_overs_second_innings = np.array([])

        print(filename + ":")
        with open(path + '/' + filename, 'r') as f:
            doc = yaml.load(f)
            venue = doc["info"]["venue"]
            date = doc["info"]["dates"][0]
            team1 = doc["info"]["teams"][0]
            team2 = doc["info"]["teams"][1]

            team1Runs = 0
            team1Wickets = 0
            team1BallsPlayed = 0

            previous_ball=0

            data = doc["innings"][0]['1st innings']['deliveries']

            count=0
            score_matrix= np.array([])
            matrix=np.array([])

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

                    if previous_ball!=team1BallsPlayed and team1BallsPlayed>0 and team1BallsPlayed<=300 and team1BallsPlayed%6 ==0:

                        count=count+1
                        oversgone= team1BallsPlayed/6;
                        runs_by_overs = np.append(runs_by_overs, team1Runs);
                        wickets_by_overs = np.append(wickets_by_overs, team1Wickets);
                        #print(team1BallsPlayed," ",runs_by_overs)

                    previous_ball= team1BallsPlayed


            #Second Innings
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

                        if previous_ball != team2BallsPlayed and team2BallsPlayed > 0 and team2BallsPlayed <= 300 and team2BallsPlayed % 6 == 0:
                            count = count + 1
                            oversgone = team2BallsPlayed / 6;
                            runs_by_overs_second_innings = np.append(runs_by_overs_second_innings, team2Runs);
                            wickets_by_overs_second_innings = np.append(wickets_by_overs_second_innings, team2Wickets);
                            # print(team1BallsPlayed," ",runs_by_overs)

                        previous_ball = team2BallsPlayed


        # print(len(runs_by_overs))


        #First innings runs matrix
        if len(runs_by_overs)<50:
            totalOversPlayed= len(runs_by_overs)
            runs_at_finish= runs_by_overs[totalOversPlayed-1]


            for x in range (totalOversPlayed,50):
                runs_by_overs=np.append(runs_by_overs,runs_at_finish)

        #First innings wickets matrix
        if len(wickets_by_overs)<50:
            totalOversPlayed= len(wickets_by_overs)
            wickets_at_finish= wickets_by_overs[totalOversPlayed-1]


            for x in range (totalOversPlayed,50):
                wickets_by_overs=np.append(wickets_by_overs,wickets_at_finish)

        #print(len(runs_by_overs_second_innings))

        #Second innings runs matrix
        if len(runs_by_overs_second_innings) != 0 and len(runs_by_overs_second_innings) < 50:
            totalOversPlayed_second_innings = len(runs_by_overs_second_innings)
            runs_at_finish_second_innings = runs_by_overs_second_innings[totalOversPlayed_second_innings - 1]

            for x in range(totalOversPlayed_second_innings, 50):
                runs_by_overs_second_innings = np.append(runs_by_overs_second_innings, runs_at_finish_second_innings)


        #Second innings wickets matrix
        if len(wickets_by_overs_second_innings) != 0 and len(wickets_by_overs_second_innings) < 50:
            totalOversPlayed_second_innings = len(wickets_by_overs_second_innings)
            wickets_at_finish_second_innings = wickets_by_overs_second_innings[totalOversPlayed_second_innings - 1]

            for x in range(totalOversPlayed_second_innings, 50):
                wickets_by_overs_second_innings = np.append(wickets_by_overs_second_innings, wickets_at_finish_second_innings)

        runs_by_overs=np.concatenate((runs_by_overs[:0], [team1], runs_by_overs[0:]))
        wickets_by_overs=np.concatenate((wickets_by_overs[:0], [team1], wickets_by_overs[0:]))


        if len(runs_by_overs_second_innings>0):
            #runs_by_overs_second_innings=np.concatenate((runs_by_overs_second_innings[:0], [team1], runs_by_overs_second_innings[0:]))
            runs_by_overs_second_innings=np.concatenate((runs_by_overs_second_innings[:0], [team2], runs_by_overs_second_innings[0:]))

        if len(wickets_by_overs_second_innings > 0):
            wickets_by_overs_second_innings = np.concatenate(
                (wickets_by_overs_second_innings[:0], [team2], wickets_by_overs_second_innings[0:]))

        #print('wickets_by_overs:', len(wickets_by_overs), len(wickets_by_overs_second_innings) )


        if len(runs_matrix) == 0:
            runs_matrix = np.array(runs_by_overs)
            if len(runs_by_overs_second_innings)>0:
                runs_matrix_second_innings = np.array(runs_by_overs_second_innings)

        else:
            runs_matrix = np.vstack([runs_matrix, np.array(runs_by_overs)])
            if len(runs_by_overs_second_innings) >0:
                runs_matrix_second_innings = np.vstack([runs_matrix_second_innings, np.array(runs_by_overs_second_innings)])

        if len(wickets_matrix) == 0:
            wickets_matrix = np.array(wickets_by_overs)
            if len(wickets_by_overs_second_innings)>0:
                wickets_matrix_second_innings = np.array(wickets_by_overs_second_innings)

        else:
            wickets_matrix = np.vstack([wickets_matrix, np.array(wickets_by_overs)])
            if len(wickets_by_overs_second_innings) >0:
                wickets_matrix_second_innings = np.vstack([wickets_matrix_second_innings, np.array(wickets_by_overs_second_innings)])


        #print(wickets_matrix)



        #print(runs_by_overs[50])

    # print(len(runs_matrix[1]))
    # print(len(runs_matrix_second_innings[1]))
    # print(len(runs_matrix))
    #
    # print(runs_matrix_second_innings)

    print(wickets_matrix)
    #print(len(wickets_matrix_second_innings))

    runs_matrix=np.concatenate([runs_matrix, runs_matrix_second_innings] )

    #print(wickets_matrix)
    #print("////////////////////////")
    #print(wickets_matrix_second_innings)

    wickets_matrix= np.concatenate([wickets_matrix, wickets_matrix_second_innings])

    # print(wickets_matrix)
    #
    # print("Runs matrix: ",len(runs_matrix))
    # print("Wickets matrix: ",len(wickets_matrix))


    pd.DataFrame(runs_matrix).to_csv("RunsPerOvers.csv", sep=',')
    pd.DataFrame(wickets_matrix).to_csv("WicketsPerOvers.csv", sep=',')




get_data()