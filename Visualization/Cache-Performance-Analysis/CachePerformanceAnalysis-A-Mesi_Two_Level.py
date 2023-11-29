import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data from the simulation stats.txt file
data = {
    'Cache': ['L1 Data Cache', 'L1 Instruction Cache', 'L2 Cache']*4,
    'Program': ['Blackscholes']*3 + ['Bodytrack']*3 + ['Raytrace']*3 + ['Ferret']*3,
    'Hits': [
        23600244, 104356877, 251420, # Blackscholes
        77060600, 449087019, 6736909, # Bodytrack
        224259941, 801118947, 686112, # Raytrace
        354042535, 1386347161, 10440158 # Ferret
    ],
    'Misses': [
        128565, 13768, 30896, # Blackscholes
        3889043, 547683, 2816863, # Bodytrack
        685823, 173547, 1074928, # Raytrace
        8394120, 634712, 5323457 # Ferret
    ],
    'Accesses': [
        23728809, 104370645, 282316, # Blackscholes
        80949643, 449634702, 9553772, # Bodytrack
        224945764, 801292494, 1761040, # Raytrace
        362436655, 1386981873, 15763615 # Ferret
    ],
    'Hit Rate': [
        0.994581903, 0.999868086, 0.890562349, # Blackscholes
        0.951957256, 0.998781938, 0.705156979, # Bodytrack
        0.996951163, 0.999783416, 0.389606142, # Raytrace
        0.97683976, 0.999542379, 0.662294658 # Ferret
    ],
    'Miss Rate': [
        0.005418097, 0.000131914, 0.109437651, # Blackscholes
        0.048042744, 0.001218062, 0.294843021, # Bodytrack
        0.003048837, 0.000216584, 0.610393858, # Raytrace
        0.02316024, 0.000457621, 0.337705342 # Ferret
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
