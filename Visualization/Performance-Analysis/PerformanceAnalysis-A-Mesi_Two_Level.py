import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Performance Analysis Data for Parsec Benchmark Suite using Cache [2,4] Associativity
performance_data = {
    'Parsec Configuration': ['Blackscholes-A', 'Bodytrack-A', 'Raytrace-A', 'Ferret-A'],
    'Sim Time (seconds)': [0.094543, 0.555863, 0.733304, 1.344864],
    'Sim Tics (Tick)': [
        94543302727,  # Blackscholes
        555863000000.0,  # Bodytrack
        733304000000.0,  # Raytrace
        1344864000000.0  # Ferret
    ],
    'Host Seconds (seconds)': [566.96, 4682.2, 7035.29, 11917.88],
    'Total Wallclock Time (minutes)': [9.81, 79.38, 121.6, 199.37]
}

# Create a DataFrame
performance_df = pd.DataFrame(performance_data)

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