import pandas as pd
import numpy as np
from scipy.spatial import distance


def getOccupancy(dataset, testInput):
    """
    This function finds the top 5 nearest (euclidean) datapoints for a given datapoint with features
    (temperature and humidity) and uses the distances to estimate the occupancy value.
    :argument: datset- A Pandas Dataframe (temperature, humidity, occupancy)
    :argument: testInput -A list containing int values for temperature and humidity respectively
    :return: occupancy value (int)
    """
    # separate features (temperature and humidity) from output
    # check if dataset argument is pandas dataframe
    if isinstance(dataset, pd.DataFrame):
        # Dataset Structure -> column 1 : Temperature, column 2 : Humidity
        X = dataset.drop('Occupancy',axis= 1) # create features df by removing occupancy column
        # column 1: occupancy
        #y = dataset.drop(['Temperature', 'Humidity'] , axis=1) # create output df by removing temperature and humidity column
        
        # check if the testInput is a list
        if isinstance(testInput,list):
            # if it is a list, continue to calculation
            
            # temperature Input testInput[0], Humidity Input testInput[1]
        
            # calculate euclidean distance

            #point 1  dataset
            # convert temperature column to a list
            temperature = (X['Temperature'].to_numpy()).tolist()
            # convert humidity column to a list
            humidity = (X['Humidity'].to_numpy()).tolist()
            
            # using a list comprehension, calculate the euclidian distance between the input datapoint and
            # datapoints in dataset
            
            euclidean_list =[distance.euclidean((temperature[i],humidity[i]),(testInput[0],testInput[1])) for i in range(len(temperature))]
            # add euclidean list to dataset
            dataset['distance'] = np.array(euclidean_list)
            #print(dataset)

            # sort dataset by euclidean list
            sortedDataset= dataset.sort_values(by='distance',ascending=True)
            print(sortedDataset)
            # get the occupancy value of the 5 closest datapoints
            sortedOccupancyList = (sortedDataset['Occupancy'].to_numpy()).tolist()[:5]
            # Retreive the most common occupancy value from the sortedOccupancyList
            calOccupancy = (max(set(sortedOccupancyList), key=sortedOccupancyList.count))
            return calOccupancy
        else:
            raise ValueError("Not a list")
    # if not a dataframe raise a Value Error letting the user know not a Dataframe
    else:
        raise ValueError("Not a Pandas DataFrame")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv('Temp_hum_data.txt',sep=" ")
    #print(df.head())
    datapoint = [20,18]
    print(f" The estimated occupancy for the test input is {getOccupancy(df,datapoint)}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
