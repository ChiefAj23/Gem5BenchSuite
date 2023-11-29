import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Performance Analysis Data for Parsec Benchmark Suite using Cache [2,4] Assosiativity
performance_data = {
    'Parsec Configuration': ['Blackscholes-B', 'Bodytrack-B', 'Raytrace-B', 'Ferret-B'],
    'Sim Time (seconds)': [0.097871, 0.527896, 0.731214, 1.348016],
    'Sim Tics (Tick)': [
        97871327038,  # Blackscholes
        527896000000.0,  # Bodytrack
        731214000000.0,  # Raytrace
        1348020000000.0  # Ferret
    ],
    'Host Seconds (seconds)': [563.1, 4696.43, 7075.21, 13339.57],
    'Total Wallclock Time (minutes)': [9.74, 78.88, 118.6, 223.47]
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
