import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Performance Analysis Data for Parsec Benchmark Suite using Cache [2,4] Assosiativity
performance_data = {
    'Parsec Configuration': ['Blackscholes-A', 'Bodytrack-A', 'Raytrace-A', 'Ferret-A'],
    'Sim Time (seconds)': [0.091374, 0.54707, 0.734004, 1.341934],
    'Sim Tics (Tick)': [9.1374426442e+10, 5.4707e+11, 7.34004e+11, 1.34193e+12],
    'Host Seconds (seconds)': [584.72, 2920.49, 5885.33, 10249.87],
    'Total Wallclock Time (minutes)': [10.08, 49.03, 98.64, 171.56]
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
