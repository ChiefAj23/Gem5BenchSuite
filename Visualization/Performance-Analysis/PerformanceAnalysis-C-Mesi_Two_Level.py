import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Performance Analysis Data for Parsec Benchmark Suite using Cache [2,4] Assosiativity
performance_data = {
    'Parsec Configuration': ['Blackscholes-C', 'Bodytrack-C', 'Raytrace-C', 'Ferret-C'],
    'Sim Time (seconds)': [0.094665, 0.511476, 0.731022, 1.353612],
    'Sim Tics (Tick)': [
        94665478096,  # Blackscholes
        511476000000.0,  # Bodytrack
        731022000000.0,  # Raytrace
        1353610000000.0  # Ferret
    ],
    'Host Seconds (seconds)': [551.99, 4784.97, 7113.16, 13053.66],
    'Total Wallclock Time (minutes)': [9.53, 81.62, 119.29, 218.56]
}
# Create a DataFrame
performance_df = pd.DataFrame(performance_data)

# Improved plotting
colors = plt.cm.Dark2(np.linspace(0.5, 0.75, len(performance_df)))

# Separate plots for each metric
for i, column in enumerate(performance_df.columns[1:]):
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(performance_df['Parsec Configuration'], performance_df[column], color=colors)
    ax.set_title(column.replace('_', ' ').title())
    ax.set_xlabel('Parsec Configuration')
    ax.set_ylabel(column.split(' ')[0].title())
    ax.set_xticklabels(performance_df['Parsec Configuration'], rotation=45, ha='right')

    # Add data labels
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', color='black')

    plt.tight_layout()
    plt.show()
