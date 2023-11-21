import pandas as pd
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
