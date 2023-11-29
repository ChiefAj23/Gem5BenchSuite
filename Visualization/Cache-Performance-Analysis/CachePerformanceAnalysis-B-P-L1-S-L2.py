import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data from the simulation stats.txt file
data = {
    'Cache': ['L1 Data Cache', 'L1 Instruction Cache', 'L2 Cache']*4,
    'Program': ['Blackscholes']*3 + ['Bodytrack']*3 + ['Raytrace']*3 + ['Ferret']*3,
    'Hits': [23619581, 104400728, 228757, 101626401,
            566534708, 8228805, 206150686, 734515833,
            622715, 345413355, 1398278583, 9870900],
    'Misses': [120565, 8545, 21376, 4344974, 1069825,
            1958802, 630979, 158547, 986326, 7471206,
            481755, 4769344],
    'Accesses': [23740146, 104409273, 250133, 105971375,
                567604533, 10187607, 206781665, 734674380,
                1609041, 352884561, 1398760338, 14640244],
    'Hit Rate': [0.994921472, 0.999918159, 0.914541464, 0.958998607,
                0.998115193, 0.807726977, 0.996948574, 0.999784194,
                0.387010026, 0.978828187, 0.999655584, 0.674230566],
    'Miss Rate': [0.005078528, 0.0000818414, 0.085458536, 0.041001393,
                0.001884807, 0.192273023, 0.003051426, 0.000215806,
                0.612989974, 0.021171813, 0.000344416, 0.325769434]
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
