import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import mean_squared_error
import math

def decision_tree():
    fileName= 'TestFile.csv'
    matrix = pd.read_csv(fileName).as_matrix()

    X_train_matrix, X_test_matrix= train_test_split(matrix, test_size=0.2)

    X_train_matrix= np.delete(X_train_matrix,0,1)  # Get Rid of the first column
    X_test_matrix= np.delete(X_test_matrix,0,1) #Get Rid of the first column

    X_train= pd.DataFrame(X_train_matrix, columns=['team_average', 'ground_average', 'runs', 'wickets', 'totalRuns', 'totalwickets'])

    X_test= pd.DataFrame(X_test_matrix, columns=['team_average', 'ground_average', 'runs', 'wickets', 'totalRuns', 'totalwickets'])

    X = X_train[['team_average', 'ground_average', 'runs', 'wickets']]
    Y = X_train[['totalRuns', 'totalwickets']]

    decision_regressor= DecisionTreeRegressor(random_state=50, max_depth = 10)
    decision_regressor.fit(X,Y)

    X_test = X_test[['team_average', 'ground_average', 'runs', 'wickets']]

    score=decision_regressor.predict(X_test)

    real_run=np.array([])
    predicted_run= np.array([])

    real_wicket=np.array([])
    predicted_wicket= np.array([])


    for i in range (len(X_test)):

        real_run= np.append(real_run, np.array( [X_test_matrix[i][4] ] ))
        predicted_run= np.append( predicted_run,np.array(score[i][0]) )
        real_wicket = np.append(real_wicket, np.array([X_test_matrix[i][5]]))
        predicted_wicket = np.append(predicted_wicket, np.array(score[i][1]))


    #print(real_run)
    #print(predicted_run)

    get_rmse(real_run, predicted_run, real_wicket, predicted_wicket)


def get_rmse(real_run, predicted_run, real_wicket, predicted_wicket):
    run_mse = mean_squared_error(real_run, predicted_run)
    run_rmse = math.sqrt(run_mse)
    print('Run_rmse: ', run_rmse)

    wicket_mse = mean_squared_error(real_wicket, predicted_wicket)
    wicket_rmse = math.sqrt(wicket_mse)
    print("Wickets_RMSE: ", wicket_rmse)
