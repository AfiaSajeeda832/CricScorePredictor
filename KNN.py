
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import math
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def predict_score_using_knn():

    fileName = 'TestFile.csv'
    matrix = pd.read_csv(fileName).as_matrix()

    X_train_matrix, X_test_matrix = train_test_split(matrix, test_size=0.2)

    X_train_matrix = np.delete(X_train_matrix, 0, 1)  # Get Rid of the first column
    X_test_matrix = np.delete(X_test_matrix, 0, 1)  # Get Rid of the first column

    # for i in range (267):
    #     print(X_train[i])


    X_train = pd.DataFrame(X_train_matrix,
                           columns=['team_average', 'ground_average', 'runs', 'wickets', 'totalRuns', 'totalWickets'])

    X_test = pd.DataFrame(X_test_matrix,
                          columns=['team_average', 'ground_average', 'runs', 'wickets', 'totalRuns', 'totalWickets'])

    X = X_train[['team_average', 'ground_average', 'runs', 'wickets']]
    Y = X_train[['totalRuns', 'totalWickets']]



    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X, Y)

    X_test = X_test[['team_average', 'ground_average', 'runs', 'wickets']]

    score = classifier.predict(X_test)

    #print(len(score))
    #print(len(X_test))
    # print(X_test_matrix)

    real_run = np.array([])
    predicted_run = np.array([])

    real_wicket = np.array([])
    predicted_wicket = np.array([])

    for i in range(len(X_test)):
        real_run = np.append(real_run, np.array([X_test_matrix[i][4]]))
        predicted_run = np.append(predicted_run, np.array(score[i][0]))
        real_wicket = np.append(real_wicket, np.array([X_test_matrix[i][5]]))
        predicted_wicket = np.append(predicted_wicket, np.array(score[i][1]))

        # print(X_test_matrix[i][2],"/", X_test_matrix[i][3], "\t", X_test_matrix[i][4],"/", X_test_matrix[i][5] ," Score: ", score[i])

    #print("Real Run: ", real_run)
    #print("Predicted Run: ", predicted_run)
    # print(real_wicket)
    # print(predicted_wicket)

    get_rmse(real_run, predicted_run, real_wicket, predicted_wicket)





def get_rmse(real_run, predicted_run, real_wicket, predicted_wicket):
    run_mse = mean_squared_error(real_run, predicted_run)
    run_rmse = math.sqrt(run_mse)
    print('Run_rmse: ', run_rmse)

    # Wickets RMSE
    wicket_mse = mean_squared_error(real_wicket, predicted_wicket)
    wicket_rmse = math.sqrt(wicket_mse)
    print("Wickets_RMSE: ", wicket_rmse)
