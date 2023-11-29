import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Performance Analysis Data for Parsec Benchmark Suite using Cache [4,8] Associativity
performance_data = {
    'Parsec Configuration': ['Blackscholes-B', 'Bodytrack-B', 'Raytrace-B', 'Ferret-B'],
    'Sim Time (seconds)': [0.091118, 0.52943, 0.732969, 1.345323],
    'Sim Tics (Tick)': [91117614844, 5.2943e+11, 7.32969e+11, 1.34532e+12],
    'Host Seconds (seconds)': [577.92, 3735.68, 7199.25, 10509.36],
    'Total Wallclock Time (minutes)': [10.63, 63.94, 120.83, 175.75]
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
