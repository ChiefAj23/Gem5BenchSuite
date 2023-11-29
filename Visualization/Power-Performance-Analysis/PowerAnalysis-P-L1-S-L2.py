import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data from the simulation stats.txt file
stats_data = {
    'Associativity Configuration': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C'],
    'Parsec Configuration': ['Blackscholes', 'Bodytrack', 'Raytrace', 'Ferret',
                             'Blackscholes', 'Bodytrack', 'Raytrace', 'Ferret',
                             'Blackscholes', 'Bodytrack', 'Raytrace', 'Ferret'],
    'Cache Associativity': [[2, 4], [2, 4], [2, 4], [2, 4], [4, 8], [4, 8], [4, 8], [4, 8], [8, 16], [8, 16], [8, 16], [8, 16]],
    'Average Power (mw)': [461.329111, 505.101617, 496.227008, 492.604799,
                           426.021113, 511.702805, 495.917521, 483.171388,
                           423.479573, 483.815412, 493.839784, 485.875951]
}

# Convert the corrected data into a DataFrame
df_data = pd.DataFrame(stats_data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Set the larger font size for better readability
sns.set_context("talk")

# Define a palette with distinct colors for each configuration
palette = sns.color_palette("viridis", n_colors=len(df_data['Associativity Configuration'].unique()))

# Create the bar plot with improved aesthetics
plt.figure(figsize=(16, 9))
barplot = sns.barplot(
    data=df_data,
    x='Parsec Configuration',
    y='Average Power (mw)',
    hue='Associativity Configuration',
    palette=palette
)

# Add annotations to each bar
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.1f'),
                     (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha = 'center', va = 'center',
                     xytext = (0, 9),
                     textcoords = 'offset points')

# Improve the title and labels with larger font sizes
plt.title('Average Power Consumption', fontsize=20)
plt.xlabel('Parsec Configuration', fontsize=18)
plt.ylabel('Average Power (mw)', fontsize=18)

# Rotate the x-axis labels for better visibility if needed
plt.xticks(rotation=45)

# Move the legend to the side of the graph
plt.legend(title='Associativity Config', bbox_to_anchor=(1.05, 1), loc='upper left')

# Improve the layout to fit everything nicely, accounting for the legend
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show the improved plot
plt.show()
