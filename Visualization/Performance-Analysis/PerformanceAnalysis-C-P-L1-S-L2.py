import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Performance Analysis Data for Parsec Benchmark Suite using Cache [8,16] Associativity
performance_data = {
    'Parsec Configuration': ['Blackscholes-C', 'Bodytrack-C', 'Raytrace-C', 'Ferret-C'],
    'Sim Time (seconds)': [0.090274, 0.512825, 0.733517, 1.348978],
    'Sim Tics (Tick)': [90273541096, 5.12825e+11, 7.33517e+11, 1.34898e+12],
    'Host Seconds (seconds)': [570.77, 3768.93, 5457.75, 10984.78],
    'Total Wallclock Time (minutes)': [9.85, 80.07, 91.82, 183.53]
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
