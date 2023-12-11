#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd

def calculate_distance_matrix(csv_filename):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_filename)

    # Create a nested dictionary to store distances
    distances = {}
    for _, row in df.iterrows():
        if row['id_start'] not in distances:
            distances[row['id_start']] = {}
        distances[row['id_start']][row['id_end']] = float(row['distance'])

        if row['id_end'] not in distances:
            distances[row['id_end']] = {}
        distances[row['id_end']][row['id_start']] = float(row['distance'])

    # Create a DataFrame from the nested dictionary
    result_df = pd.DataFrame(distances).fillna(0)

    # Ensure the matrix is symmetric
    result_df = result_df.add(result_df.T, fill_value=0)

    return result_df

# Example usage
result_dataframe = calculate_distance_matrix('dataset-3.csv')
print(result_dataframe)


# In[ ]:




