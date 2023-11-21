import pandas as pd
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

# Plotting
fig, axes = plt.subplots(4, 1, figsize=(10, 12), tight_layout=False)
# Sim Time (seconds)
performance_df.plot(kind='bar', x='Parsec Configuration', y='Sim Time (seconds)', ax=axes[0], legend=False)
axes[0].set_title('Simulation Time (seconds)')
axes[0].set_ylabel('Seconds')
axes[0].set_xticklabels(performance_df['Parsec Configuration'], rotation=45, ha='right')

# Sim Tics (Tick)
performance_df.plot(kind='bar', x='Parsec Configuration', y='Sim Tics (Tick)', ax=axes[1], legend=False)
axes[1].set_title('Simulation Tics (Tick)')
axes[1].set_ylabel('Tics')

# Host Seconds (seconds)
performance_df.plot(kind='bar', x='Parsec Configuration', y='Host Seconds (seconds)', ax=axes[2], legend=False)
axes[2].set_title('Host Seconds (seconds)')
axes[2].set_ylabel('Seconds')

# Total Wallclock Time (minutes)
performance_df.plot(kind='bar', x='Parsec Configuration', y='Total Wallclock Time (minutes)', ax=axes[3], legend=False)
axes[3].set_title('Total Wallclock Time (minutes)')
axes[3].set_ylabel('Minutes')

# Show the plot
plt.show()
