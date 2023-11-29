import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data from the simulation stats.txt file
data = {
    'Cache': ['L1 Data Cache', 'L1 Instruction Cache', 'L2 Cache']*4,
    'Program': ['Blackscholes']*3 + ['Bodytrack']*3 + ['Raytrace']*3 + ['Ferret']*3,
    'Hits': [
        23540193, 104202306, 219829,  # Blackscholes
        75793695, 442837526, 7958350,  # Bodytrack
        220114226, 783800879, 566627,  # Raytrace
        304016839, 1190796805, 9131299  # Ferret
    ],
    'Misses': [
        108065, 10996, 15209,  # Blackscholes
        3851346, 529330, 1342617,  # Bodytrack
        631027, 125101, 963054,  # Raytrace
        6039118, 418540, 4328065  # Ferret
    ],
    'Accesses': [
        23648258, 104213302, 235038,  # Blackscholes
        79645041, 443366856, 9300967,  # Bodytrack
        220745253, 783925980, 1529681,  # Raytrace
        310055957, 1191215345, 13459364  # Ferret
    ],
    'Hit Rate': [
        0.995430319, 0.999894486, 0.935291315,  # Blackscholes
        0.951643618, 0.998806113, 0.85564759,  # Bodytrack
        0.997141379, 0.999840417, 0.370421676,  # Raytrace
        0.98052249, 0.999648645, 0.678434657  # Ferret
    ],
    'Miss Rate': [
        0.004569681, 0.000105514, 0.064708685,  # Blackscholes
        0.048356382, 0.001193887, 0.14435241,  # Bodytrack
        0.002858621, 0.000159583, 0.629578324,  # Raytrace
        0.01947751, 0.000351355, 0.321565343  # Ferret
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
