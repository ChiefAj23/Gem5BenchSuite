import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data from the simulation stats.txt file
data = {
    'Cache': ['L1 Data Cache', 'L1 Instruction Cache', 'L2 Cache']*4,
    'Program': ['Blackscholes']*3 + ['Bodytrack']*3 + ['Raytrace']*3 + ['Ferret']*3,
    'Hits': [
        23384468, 104542353, 220796,  # Blackscholes
        101799626, 567835663, 7494428,  # Bodytrack
        210956024, 751176283, 593034,  # Raytrace
        305587145, 1225752191, 9424362  # Ferret
    ],
    'Misses': [
        109207, 9192, 16271,  # Blackscholes
        4355995, 724940, 2003955,  # Bodytrack
        623589, 161173, 965211,  # Raytrace
        5844637, 419513, 4475233  # Ferret
    ],
    'Accesses': [
        23493675, 104551545, 237067,  # Blackscholes
        106155621, 568560603, 9498383,  # Bodytrack
        211579613, 783811352, 1558245,  # Raytrace
        311431782, 1226171704, 13899595  # Ferret
    ],
    'Hit Rate': [
        0.995351643, 0.999912082, 0.931365395,  # Blackscholes
        0.958965951, 0.998724956, 0.789021458,  # Bodytrack
        0.997052698, 0.958363618, 0.38057815,  # Raytrace
        0.98123301, 0.999657868, 0.67803141  # Ferret
    ],
    'Miss Rate': [
        0.004648357, 8.79184E-05, 0.068634605,  # Blackscholes
        0.041034049, 0.001275044, 0.210978542,  # Bodytrack
        0.002947302, 0.000205627, 0.61942185,  # Raytrace
        0.01876699, 0.000342132, 0.32196859  # Ferret
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
