import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data from the simulation stats.txt file
data = {
    'Cache': ['L1 Data Cache', 'L1 Instruction Cache', 'L2 Cache']*4,
    'Program': ['Blackscholes']*3 + ['Bodytrack']*3 + ['Raytrace']*3 + ['Ferret']*3,
    'Hits': [23328608, 104301193, 592448,
             76054857, 443919929, 7457387,
             205869677, 731265176, 616494,
             347467941, 1417376028, 10130569],
    'Misses': [393333, 13806, 54946,
               3981567, 881483, 2975733,
               633174, 187153, 1052479,
               7254196, 478823, 4882118],
    'Accesses': [23721941, 104314999, 647394,
                 80036424, 444801412, 10433120,
                 206502851, 731452329, 1668973,
                 354722137, 1417854851, 15012687],
    'Hit Rate': [0.983419021, 0.999867651, 0.915127419,
                 0.950253062, 0.998018255, 0.714780142,
                 0.996933824, 0.999744135, 0.369385245,
                 0.979549638, 0.999662291, 0.67480052],
    'Miss Rate': [0.016580979, 0.000132349, 0.084872581,
                  0.049746938, 0.001981745, 0.285219858,
                  0.003066176, 0.000255865, 0.630614755,
                  0.020450362, 0.000337709, 0.32519948]
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
