import pandas as pd
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

# Plotting with improved aesthetics
fig, axes = plt.subplots(4, 1, figsize=(12, 18))

# Define colors for the plots
colors = ['skyblue', 'orange', 'green', 'red']

# Sim Time (seconds)
performance_df.plot(kind='bar', x='Parsec Configuration', y='Sim Time (seconds)', ax=axes[0], legend=False, color=colors[0])
axes[0].set_title('Simulation Time (seconds)', fontsize=14)
axes[0].set_ylabel('Seconds', fontsize=12)
axes[0].set_xticklabels(performance_df['Parsec Configuration'], rotation=45, ha='right')
axes[0].tick_params(axis='x', labelsize=10)
axes[0].tick_params(axis='y', labelsize=10)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Sim Tics (Tick)
performance_df.plot(kind='bar', x='Parsec Configuration', y='Sim Tics (Tick)', ax=axes[1], legend=False, color=colors[1])
axes[1].set_title('Simulation Tics (Tick)', fontsize=14)
axes[1].set_ylabel('Tics', fontsize=12)
axes[1].tick_params(axis='x', labelsize=10)
axes[1].tick_params(axis='y', labelsize=10)
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

# Host Seconds (seconds)
performance_df.plot(kind='bar', x='Parsec Configuration', y='Host Seconds (seconds)', ax=axes[2], legend=False, color=colors[2])
axes[2].set_title('Host Seconds (seconds)', fontsize=14)
axes[2].set_ylabel('Seconds', fontsize=12)
axes[2].tick_params(axis='x', labelsize=10)
axes[2].tick_params(axis='y', labelsize=10)
axes[2].grid(axis='y', linestyle='--', alpha=0.7)

# Total Wallclock Time (minutes)
performance_df.plot(kind='bar', x='Parsec Configuration', y='Total Wallclock Time (minutes)', ax=axes[3], legend=False, color=colors[3])
axes[3].set_title('Total Wallclock Time (minutes)', fontsize=14)
axes[3].set_ylabel('Minutes', fontsize=12)
axes[3].tick_params(axis='x', labelsize=10)
axes[3].tick_params(axis='y', labelsize=10)
axes[3].grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap and ensure labels are readable
fig.tight_layout()

# Show the plot
plt.show()
