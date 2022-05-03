import pandas as pd
import numpy as np
from scipy.spatial import distance


def getOccupancy(dataset, testInput):
    """
    This function finds the top 5 nearest (euclidean) datapoints for a given datapoint with features
    (temperature and humidity) and uses the distances to estimate the occupancy value.
    :argument: dataset- A Pandas Dataframe (temperature, humidity, occupancy)
    :argument: testInput -A list containing int values for temperature and humidity respectively
    :return: occupancy value (int)
    """
    # separate features (temperature and humidity) from output
    # check if dataset argument is pandas dataframe
    if isinstance(dataset, pd.DataFrame):
        # if df with null values
        # Dataset Structure -> column 1 : Temperature, column 2 : Humidity
        # for this to work - we need the correct column names

        if 'Humidity' and 'Temperature' and 'Occupancy' in [dataset.columns]:

            X = dataset.drop('Occupancy', axis=1)  # create features df by removing occupancy column
            # column 1: occupancy
            # check if the testInput is a list
            if isinstance(testInput, list):
                # if it is a list, continue to calculation
                # if it is a list with 3 items or with strings

                # temperature Input testInput[0], Humidity Input testInput[1]
                # calculate euclidean distance
                # point 1  dataset

                # check for the correct input datatype
                if X['Temperature'].dtype == 'Object' or X['Humidity'].dtype == 'Object':

                    raise TypeError('Columns must be numeric')

                else:
                    if X['Humidity'].isnull().values.any() or X['Temperature'].isnull().values.any():
                        raise ValueError("Missing value in dataframe column.")
                    else:

                        # convert temperature column to a list
                        temperature = (X['Temperature'].to_numpy()).tolist()

                        # convert humidity column to a list
                        humidity = (X['Humidity'].to_numpy()).tolist()

                # check for the correct input type in the test input list
                if testInput[0] or testInput[1] is not (int, float):
                    raise TypeError('Only int or float as datatype will work as an input.')
                else:
                    # Using a list comprehension, calculate the Euclidean distance between the input datapoint and
                    # data points in dataset
                    euclidean_list = [distance.euclidean((temperature[i], humidity[i]), (testInput[0], testInput[1]))
                                      for i in range(len(temperature))]
                    # add euclidean list to dataset
                    dataset['distance'] = np.array(euclidean_list)

                # sort dataset by euclidean list
                sortedDataset = dataset.sort_values(by='distance', ascending=True)

                # get the occupancy value of the 5 closest data points -
                # for this to work there has to be at least 5 data points

                sortedOccupancyList = (sortedDataset['Occupancy'].to_numpy()).tolist()[:5]
                print(sortedOccupancyList)

                # Retrieve the most common occupancy value from the sortedOccupancyList
                calOccupancy = (max(set(sortedOccupancyList), key=sortedOccupancyList.count))

                return calOccupancy
            else:
                raise ValueError("Not a list")
            pass
        else:
            raise('Missing column!')
            # then proceed
    # if not a dataframe raise a Value Error letting the user know not a Dataframe
    else:
        raise ValueError("Not a Pandas DataFrame")


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     df = pd.read_csv('Temp_hum_data.txt',sep=" ")
#     #print(df.head())
#     datapoint = [20,18]
#     print(f" The estimated occupancy for the test input is {getOccupancy(df,datapoint)}")
#
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
