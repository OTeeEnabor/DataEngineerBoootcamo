# Create a function that finds the top 5 nearest datapoints for a
# given datapoint with features(temperature and humidity) and uses them
# to estimate the occupancy value.?

import pandas as pd
import numpy as np
import os

path_to_raw_file = "Temp_hum_data.txt"


# check if datafile exists before processing
def process_data(path_to_raw_file):
    if not os.path.exists(path_to_raw_file):
        raise FileNotFoundError("Datafile missing in specified path")
    else:
        try:
            with open(path_to_raw_file, "r") as f:
                data = f.read()

            rawdata = data.split("\n")
            colnames = rawdata[0].split("\t")
            datapoints = rawdata[1:]

            # format for processing with proper names
            datarows = []
            for f in range(len(datapoints)):
                datarows.append(datapoints[f].split(" "))
            return pd.DataFrame(datarows, columns=colnames, dtype=float)

        except Exception as e:
            print(f"Datafile not processed! \n{e}")



def compute_euclid_dist(arr1, arr2):
    """
    computes eucledian distances.
    Args:
        arr1 (np.array): array to provide x-values.
        arr2 (np.array): array to provide y-values.
    Returns:
        distances (list): eucledian distances.
    """
    if (len(arr1)==0 or len(arr2)==0):
        raise ValueError("At least one array is empty")
    else:
        try:
            tot = np.sum((arr1 - arr2)**2, axis=0)
            return np.sqrt(tot)
        except Exception as e:
            print(f"Unexpected error occured: \n{e}")


def knn_algo(new_datapt, df, n_neighbors=5):
    """Get the 5 nearest points to the new data point.
    Args
    ----
        new_datapt (tupple):  a datapoint for which to find the top5 neighbors
        dataframe (df): a pandas processed dataframe
        n_neighbors (int): optional, the number of nearest neighbors
    Returns
    -------
        None
    """
    tmp = df["Temperature"].values
    hum = df["Humidity"].values
    dtypes = [float, int]

    # The datapoint should be of length 2. check before proceeding
    if type(new_datapt) not in [list, tuple] or len(new_datapt)!=2:
        raise ValueError("New datapoint can only be a list/tuple of lenght 2")

    # check for dtypes before proceeding
    if type(new_datapt[0]) in dtypes and type(new_datapt[0]) in dtypes:

        d = compute_euclid_dist(np.array([tmp, hum]),  np.array(new_datapt))

        indices = np.argsort(d)
        top5_indices = indices[:n_neighbors]

        return df.iloc[top5_indices, 0:2]
    else:
        raise TypeError("Mixed datatypes in new_datapoint.")


#-------------------------------------------------

df = process_data(path_to_raw_file)
print(knn_algo((9,3), df))
