
from sklearn import datasets, linear_model
import numpy as np

def capm1(x,y):
    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(x, y)

    # Make predictions using the testing set
    pred = regr.predict(x)
    return pred


def multi_capm(x,y,days):
    # split data in to windows
    # perform capm on each window
    # concatenate
    length = len(x)
    max_windows = int(length / days)
    print(max_windows)

   # y_pred = [[]]
    start = 0 * days
    end = start + days
    print('start', start, 'end', end)
    x_slice = x[start:end]
    y_slice = y[start:end]
    x_train = x_slice[np.newaxis, :]
    y_train = y_slice[np.newaxis, :]
    y_pred = capm1(x_train, y_train)

    for i in range(1, max_windows):
        start = i * days
        end = start + days
        x_slice = x[start:end]
        y_slice = y[start:end]
        x_train = x_slice[np.newaxis, :]
        y_train = y_slice[np.newaxis, :]
        y_pred_slice = capm1(x_train,y_train)
        y_pred = np.concatenate((y_pred, y_pred_slice))

    return y_pred
