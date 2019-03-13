#!/usr/bin/env python
# coding: utf-8

# # Python Data Structures - Predict Solution

# Below is the proposed model solution for the Predict deliverable of Python Data Structures. We will start by transforming the raw data as we did in the tutorial: Manipulating Dataframes.

# ## Transform Data

# ### Import Data

# In[1]:


import pandas as pd

# Load data - pass 'Name' as our index column
load_df = pd.read_csv('football_players.csv', index_col='Name').sample(frac=1)

# Create dataframe called df
df = pd.DataFrame(load_df)


# ### Create Position Type Column

# In[2]:


def position_type(s):
    
    """"This function converts the individual positions (abbreviations) and classfies it
    as either a forward, midfielder, back or goal keeper"""
    
    if (s[-2] == 'T') | (s[-2] == 'W'):
        return 'Forward'
    elif s[-2] == 'M':
        return 'Midfielder'
    elif s[-2] == 'B':
        return 'Back'
    else:
        return 'GoalKeeper'

# Create position type column
df['Preferred Positions Type'] = df['Preferred Positions'].apply(position_type)


# ### Transform Attribute Columns to Floats

# In[3]:


# Select all attribute columns
cols = ['Overall', 'Acceleration', 'Aggression',
       'Agility', 'Balance', 'Ball control', 'Composure', 'Crossing', 'Curve',
       'Dribbling', 'Finishing', 'Free kick accuracy', 'GK diving',
       'GK handling', 'GK kicking', 'GK positioning', 'GK reflexes',
       'Heading accuracy', 'Interceptions', 'Jumping', 'Long passing',
       'Long shots', 'Marking', 'Penalties', 'Positioning', 'Reactions',
       'Short passing', 'Shot power', 'Sliding tackle', 'Sprint speed',
       'Stamina', 'Standing tackle', 'Strength', 'Vision', 'Volleys']

def to_float(x):    
    "Transforms attribute columns to type float"
    
    if type(x) is int:
        return float(x)
    else:
        return float(x[0:2])

df[cols] = df[cols].applymap(to_float)


# ## Function 1
# 
# Build an algorithm that identifies the nth ranked (rank) defender in the world - sorted by 'Overall' then 'Name' (both descending order)
# * Under a certain age (max_age)

# In[4]:


def best_defender_1(rank, max_age):
    
    "Returns a string of the nth ranked defender under a certain age"
    
    # create filters
    filter_1 = df['Preferred Positions Type'] == 'Back'   
    filter_2 = df['Age'] < max_age  
    
    # filter dataframe
    defenders = df[(filter_1) & (filter_2)].reset_index() 
    
    # return defender (as a string) sorted on 'Overall' and 'Name'
    return defenders.sort_values(by=['Overall','Name'], ascending=False).iloc[rank-1]['Name']


# In[5]:


best_defender_1(10, 35)


# ## Function 2
# 
# Build an algorithm that identifies the nth ranked (rank) defender in the world - sorted by 'Overall' then 'Name' (both descending order)
# * Under a certain age (max_age)
# * Has an aggression score below a certain level (max_aggression)
# * Has a stamina score above a certain level (min_stamina)

# In[6]:


def best_defender_2(rank, max_age, max_aggression, min_stamina):
    
    "Returns a string of the nth ranked defender under certain age, with a max aggression and a min stamina"
    
    # create filters
    filter_1 = df['Preferred Positions Type'] == 'Back'   
    filter_2 = df['Age'] < max_age                       
    filter_3 = df['Aggression'] < max_aggression          
    filter_4 = df['Stamina'] > min_stamina 
    
    # filter dataframe
    defenders = df[(filter_1) & (filter_2) & (filter_3) & (filter_4)].reset_index()
    
    # return defender (as a string) sorted on 'Overall'
    return defenders.sort_values(by=['Overall', 'Name'], ascending=False).iloc[rank-1]['Name']


# In[7]:


best_defender_2(11, 35, 80, 60)


# ## Function 3
# 
# Build an algorithm that identifies the nth ranked (rank) defender in the world - sorted by 'Overall' then 'Name' (both descending order)
# * Under a certain age
# * Does not play for a certain team (team)

# In[8]:


def best_defender_3(rank, max_age, team):
    
    "Returns a string of the nth ranked defender under certain age, excluding a certain country"
    
    # create filters
    filter_1 = df['Preferred Positions Type'] == 'Back'
    filter_2 = df['Age'] < max_age
    filter_3 = df['Nationality'] != team
    
    # filter dataframe
    defenders = df[(filter_1) & (filter_2) & (filter_3)].reset_index()
    
    # return defender (as a string) sorted on 'Overall' and 'Name'
    return defenders.sort_values(by=['Overall', 'Name'], ascending=False).iloc[rank-1]['Name']


# In[9]:


best_defender_3(10, 30, 'Argentina')


# ## Function 4
# 
# Build an algorithm that identifies the nth ranked (rank) attacker in the world - sorted by 'Overall' then 'Name' (both descending order)
# * With specified attribute (attribute_name) above a threshold (min_attribute_score)

# In[10]:


def best_attacker_1(rank, attribute_name, min_attribute_score):
    
    "Returns a string of nth ranked attacker with specified attribute above a threshold"
    
    # create filters
    filter_1 = df['Preferred Positions Type'] == 'Forward'
    filter_2 = df[attribute_name] > min_attribute_score
    
    # filter dataframe
    attackers = df[(filter_1) & (filter_2)].reset_index()
    
    # return attacker (as a string) sorted on 'Overall' and 'Name'
    return attackers.sort_values(by=['Overall', 'Name'], ascending=False).iloc[rank-1]['Name']


# In[11]:


best_attacker_1(10, 'Finishing', 80)


# ## Function 5
# 
# Build an algorithm that identifies the nth ranked (rank) attacker in the world - sorted by 'Overall' then 'Name' (both descending order)
# * With average of specified attributes (attribute_1_name, attribute_2_name) above a threshold (min_attributes_ave)

# In[12]:


def best_attacker_2(rank, attribute_1_name, attribute_2_name, min_attributes_ave):
    
    "Returns a string of the nth ranked attacker with average of specified attributes above a threshold"
    
    # create filters
    filter_1 = df['Preferred Positions Type'] == 'Forward'
    df['Attributes_ave'] = (df[attribute_1_name] + df[attribute_2_name]) / 2
    filter_2 = df['Attributes_ave'] > min_attributes_ave
    
    # filter dataframe
    attackers = df[(filter_1) & (filter_2)].reset_index()
    
    # return attacker (as a string) sorted on 'Overall' and 'Name'
    return attackers.sort_values(by=['Overall', 'Name'], ascending=False).iloc[rank-1]['Name']


# In[13]:


best_attacker_2(23, 'Finishing', 'Long shots', 80)


# ## Function 6
# 
# Build an algorithm that identifies the nth ranked (rank) attacker in the world - sorted by 'Overall' then 'Name' (both descending order)
# * With minimum of specified attributes (attribute_1_name, attribute_2_name) above a threshold (min_attributes_min)

# In[14]:


def best_attacker_3(rank, attribute_1_name, attribute_2_name, min_attributes_min):
    
    "Returns a string of the nth ranked attacker with min of specified attributes above a threshold"
    
    # create filters
    filter_1 = df['Preferred Positions Type'] == 'Forward'
    df['Attributes_min'] = df[[attribute_1_name, attribute_2_name]].min(axis=1)
    filter_2 = df['Attributes_min'] > min_attributes_min
    
    # filter dataframe
    attackers = df[(filter_1) & (filter_2)].reset_index()
    
    # return attacker (as a string) sorted on 'Overall' and 'Name'
    return attackers.sort_values(by=['Overall', 'Name'], ascending=False).iloc[rank-1]['Name']


# In[15]:


best_attacker_3(10, 'Finishing', 'Long shots', 70)


# ## Function 7
# 
# Build an algorithm that identifies the best n (no_defenders) defenders - sorted by 'Overall' then 'Name' (both descending order)
# * From a certain country (country)
# * Under a certain age (max_age)

# In[16]:


def best_team_1(country, no_defenders, max_age):
    
    "Returns a list of the top n defenders from specified country, under a certain age"
    
    # create filters
    filter_1 = df['Preferred Positions Type'] == 'Back'
    filter_2 = df['Age'] < max_age
    filter_3 = df['Nationality'] == country
    
    # filter dataframe
    defenders = df[(filter_1) & (filter_2) & (filter_3)].reset_index()
    
    # return defenders (as a list) sorted on 'Overall' and 'Name'
    return list(defenders.sort_values(by=['Overall', 'Name'], ascending=False).iloc[0:no_defenders]['Name'])


# In[17]:


best_team_1('England', 3, 30)


# ## Function 8
# 
# Build an algorithm that identifies the best n (no_attackers) attackers - sorted by 'Overall' then 'Name' (both descending order)
# * From a certain country (country)
# * With a specified attribute (attribute name) above a threshold (min_attribute_score)

# In[18]:


def best_team_2(country, no_attackers, attribute_name, min_attribute_score):
    
    "Returns a list of the top n attackers from specified country with a specified attribute above a threshold"
    
    # create filters
    filter_1 = df['Preferred Positions Type'] == 'Forward'
    filter_2 = df[attribute_name] > min_attribute_score
    filter_3 = df['Nationality'] == country
    
    # filter dataframe
    attackers = df[(filter_1) & (filter_2) & (filter_3)].reset_index()
    
    # return attackers (as a list) sorted on 'Overall' and 'Name'
    return list(attackers.sort_values(by=['Overall', 'Name'], ascending=False).iloc[0:no_attackers]['Name'])


# In[19]:


best_team_2('England', 3, 'Finishing', 80)


# ## Function 9
# 
# Build an algorithm that identifies the best team based on the team structure (no_attackers, no_defenders, no_midfielders, no_goalkeepers) - sorted by 'Overall' then 'Name' (both descending order)
# * From a certain country (country)

# In[20]:


def best_team_3(country, no_attackers, no_defenders, no_midfielders, no_goalkeepers):
    
    "Returns a list of the best team from a specifed country, given the playing structure"
    
    # create dictionary of positions mapped to no in structure
    positions = {'Forward':no_attackers, 'Back':no_defenders, 'Midfielder':no_midfielders, 'GoalKeeper':no_goalkeepers}
    
    # create empty list (to append later)
    team = []
    
    # loop through keys and values to select each position structure separately
    for k,v in positions.items():
        filter_1 = df['Nationality'] == country 
        filter_2 = df['Preferred Positions Type'] == k
        players = df[(filter_1) & (filter_2)].reset_index()
        team.extend(list(players.sort_values(by=['Overall', 'Name'], ascending=False).iloc[0:v]['Name']))
        
    # return team (as a list)    
    return team   


# In[21]:


best_team_3('Brazil', 3, 3, 4, 1)

