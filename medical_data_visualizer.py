import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
def BMI_calc(height, weight):
    height_conv = height / 100
    BMI = weight/ (height_conv ** 2)
    return BMI 

df['BMI']= df.apply(lambda row: BMI_calc(row['height'], row['weight']), axis = 1)
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0 )
df.drop(['BMI'], axis = 1, inplace = True)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x:0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    value = ['cholesterol', 'gluc','smoke', 'alco','active','overweight']
    df_long = pd.melt(df, id_vars = 'cardio', value_vars = value, var_name='variable', value_name='value')


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.)
    df_grouped = df_long.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Draw the catplot with 'sns.catplot()'
    df_cat = sns.catplot(x = 'variable', hue='value', col='cardio', data = df_grouped, kind = 'count')
    df_cat.set_ylabels('total')

    # Get the figure for the output
    fig = df_cat.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
