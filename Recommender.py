#!usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats.stats import pearsonr

movie_user_preferences={'Jill': {'Avenger: Age of Ultron': 7.0,
  'Django Unchained': 6.5,
  'Gone Girl': 9.0,
  'Kill the Messenger': 8.0},
 'Julia': {'Avenger: Age of Ultron': 10.0,
  'Django Unchained': 6.0,
  'Gone Girl': 6.5,
  'Kill the Messenger': 6.0,
  'Zoolander': 6.5},
 'Max': {'Avenger: Age of Ultron': 7.0,
  'Django Unchained': 7.0,
  'Gone Girl': 10.0,
  'Horrible Bosses 2': 6.0,
  'Kill the Messenger': 5.0,
  'Zoolander': 10.0},
 'Robert': {'Avenger: Age of Ultron': 8.0,
  'Django Unchained': 7.0,
  'Horrible Bosses 2': 5.0,
  'Kill the Messenger': 9.0,
  'Zoolander': 9.0},
 'Sam': {'Avenger: Age of Ultron': 10.0,
  'Django Unchained': 7.5,
  'Gone Girl': 6.0,
  'Horrible Bosses 2': 3.0,
  'Kill the Messenger': 5.5,
  'Zoolander': 7.0},
 'Toby': {'Avenger: Age of Ultron': 8.5,
  'Django Unchained': 9.0,
  'Zoolander': 2.0},
 'William': {'Avenger: Age of Ultron': 6.0,
  'Django Unchained': 8.0,
  'Gone Girl': 7.0,
  'Horrible Bosses 2': 4.0,
  'Kill the Messenger': 6.5,
  'Zoolander': 4.0}}

# Printing a user's rating of one of the movies 
print movie_user_preferences['William']['Gone Girl']

# Understanding Euclidean distances
## creating a data frame of user who have rated both Avengers and Django
data = []
for i in movie_user_preferences.keys():
  try:
    data.append((i
      ,movie_user_preferences[i]['Django Unchained']
      ,movie_user_preferences[i]['Avenger: Age of Ultron']))
  except:
    pass

df = pd.DataFrame(data = data, columns = ['user', 'django', 'avenger'])
print df

plt.scatter(df.django, df.avenger)
plt.xlabel('Django')
plt.ylabel('Avengers')
for i, txt in enumerate(df.user):
  plt.annotate(txt, (df.django[i], df.avenger[i]))
plt.show()

# Euclidean distance between Jill and Toby
jill_toby_euclidean = sqrt(pow(8.5 - 7, 2) + pow(9 - 6.5, 2))
print jill_toby_euclidean

# Euclidean distance between Robert and Max
robert_max_euclidean = sqrt(pow(8 - 7, 2) + pow(7 - 7, 2))
print robert_max_euclidean

# Similarity score based on euclidean distance (Jill and Toby)
print 1/(1 + jill_toby_euclidean)

# Similarity score based on euclidean distance (Robert and Max)
print 1/(1 + robert_max_euclidean)
