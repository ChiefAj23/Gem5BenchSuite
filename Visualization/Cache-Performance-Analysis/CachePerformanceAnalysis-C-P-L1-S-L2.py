import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data from the simulation stats.txt file
data = {
    'Cache': ['L1 Data Cache', 'L1 Instruction Cache', 'L2 Cache']*4,
    'Program': ['Blackscholes']*3 + ['Bodytrack']*3 + ['Raytrace']*3 + ['Ferret']*3,
    'Hits': [
        23787270, 104913742, 215993, # Blackscholes
        101541961, 566673129, 7956230, # Bodytrack
        205057381, 730456300, 580226, # Raytrace
        306620444, 1232843962, 8138844 # Ferret
    ],
    'Misses': [
        108244, 9556, 15578, # Blackscholes
        4303508, 634541, 1300362, # Bodytrack
        619742, 148370, 973218, # Raytrace
        5723445, 527378, 5367715 # Ferret
    ],
    'Accesses': [
        23895514, 104923298, 231571, # Blackscholes
        105845469, 567307670, 9256592, # Bodytrack
        205677123, 730604670, 1553444, # Raytrace
        312343889, 1233371340, 13506559 # Ferret
    ],
    'Hit Rate': [
        0.995470112, 0.999908924, 0.932729055, # Blackscholes
        0.959341594, 0.998881487, 0.859520437, # Bodytrack
        0.996986821, 0.999796922, 0.373509441, # Raytrace
        0.981675822, 0.999572409, 0.602584567 # Ferret
    ],
    'Miss Rate': [
        0.004529888, 9.10761E-05, 0.067270945, # Blackscholes
        0.040658406, 0.001118513, 0.140479563, # Bodytrack
        0.003013179, 0.000203078, 0.626490559, # Raytrace
        0.018324178, 0.000427591, 0.397415433 # Ferret
    ]
}

# Function to plot a bar chart
def plot_bar_chart(dataframe, x, y, hue, title, y_label, y_scale=None, y_lim=None, rotation=45):
    plt.figure(figsize=(15, 10))
    sns.barplot(x=x, y=y, hue=hue, data=dataframe)
    plt.title(title)
    plt.ylabel(y_label)
    if y_scale:
        plt.yscale(y_scale)
    if y_lim:
        plt.ylim(y_lim)
    plt.xticks(rotation=rotation)
    plt.legend(title=hue, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Convert to a DataFrame
df = pd.DataFrame(data)

# Separate dataframes for hits/misses and rates for easier plotting
df_hits_misses = df[['Cache', 'Program', 'Hits', 'Misses']].melt(id_vars=['Cache', 'Program'], var_name='Type', value_name='Count')
df_rates = df[['Cache', 'Program', 'Hit Rate', 'Miss Rate']].melt(id_vars=['Cache', 'Program'], var_name='Type', value_name='Rate')

# Bar chart for Hits and Misses with Log Scale
plot_bar_chart(
    dataframe=df_hits_misses[df_hits_misses['Cache'] == 'L1 Data Cache'],
    x='Program',
    y='Count',
    hue='Type',
    title='L1 Data Cache Hits and Misses (Log Scale)',
    y_label='Count (Log Scale)',
    y_scale='log'
)

# Bar chart for Hit Rates
plot_bar_chart(
    dataframe=df_rates[df_rates['Type'] == 'Hit Rate'],
    x='Cache',
    y='Rate',
    hue='Program',
    title='Cache Hit Rates Across Programs',
    y_label='Hit Rate',
    y_lim=(0, 1)
)

# Bar chart for Miss Rates
plot_bar_chart(
    dataframe=df_rates[df_rates['Type'] == 'Miss Rate'],
    x='Cache',
    y='Rate',
    hue='Program',
    title='Cache Miss Rates Across Programs',
    y_label='Miss Rate',
    y_lim=(0, 1)
)
