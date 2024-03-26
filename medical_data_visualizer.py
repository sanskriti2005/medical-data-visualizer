import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
    #made a function to calculate the BMI
def BMI_calc(height, weight):
    height_conv = height / 100
    BMI = weight/ (height_conv ** 2)
    return BMI 

    #using the BMI_calc function, a column for the BMI is added to the dataframe
df['BMI']= df.apply(lambda row: BMI_calc(row['height'], row['weight']), axis = 1)

    # the BMI column is used to create the overweight column with binary values
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0 )

    # the BMI column is then dropped from the dataframe
df.drop(['BMI'], axis = 1, inplace = True)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x:0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    value =  ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    df_long = pd.melt(df, id_vars = 'cardio', value_vars = value, var_name='variable', value_name='value')


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.)
    df_grouped = df_long.groupby(['cardio','variable','value']).size().reset_index(name='total')

    # Draw the catplot with 'sns.catplot()'
    df_cat = sns.catplot(x = 'variable', hue='value', col='cardio', data = df_long, kind = 'count')
    df_cat.set_ylabels('total')

    # Get the figure for the output
    fig = df_cat.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
        #cleaned rows where the dystolic pressure is higher than the systolic pressure
    df_cleanedrows1 = df[df[ap_lo] <= df['ap_hi']]


        #calculating the quantiles for the 'height' column
    height_2_5 = df['height'].quantile(0.025)
    height_97_5 = df['height'].quantile(0.975)
        #cleaning the data that is incorrect from the 'height' column
    df_cleanedrows2 = df_cleanedrows1[(df_cleanedrows1['height'] >= height_2_5) & (df_cleanedrows1['height'] <= height_97_5)]

        #calculating the quantiles for the 'weight' column
    weight_2_5 = df['weight'].quantile(0.025)
    weight_97_5 = df['weight'].quantile(0.975)
        #cleaning the data that is incorrect from the 'weight' column
    df_cleanedrows3 = df_cleanedrows2[(df_cleanedrows2['weight'] >= weight_2_5) & (df_cleanedrows2['weight'] <= weight_97_5)]


    df_heat = df_cleanedrows3

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
