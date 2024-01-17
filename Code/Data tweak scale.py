#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# In[2]:


sample = pd.read_csv("top_songs_per_genre.csv")


# In[3]:


sample.info()


# In[6]:


# Selecting numerical columns for scaling
numerical_columns = sample.select_dtypes(include=['int64', 'float64']).columns

# Columns to exclude
exclude_columns = ['duration_ms', 'key', 'mode', 'time_signature']

# Filtering out the columns to be excluded
selected_columns = [col for col in numerical_columns if col not in exclude_columns]

# Creating a new DataFrame with selected columns
df_selected = sample[selected_columns].copy()

# Standardizing numerical features using MinMaxScaler
scaler = MinMaxScaler()
df_selected[selected_columns] = scaler.fit_transform(df_selected[selected_columns])

# Combining the non-numerical columns with the standardized numerical columns
final_df = pd.concat([sample[['genre', 'artist_name', 'track_name', 'track_id']], df_selected], axis=1)

# Save the final DataFrame to a CSV file
final_df.to_csv('Spotify_ft.csv', index=False)


# In[ ]:




