import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Transcribed data from the image into a DataFrame
data = {
    "Workload Characterization": [
        "Sim Instruction (Count)",
        "Sim Ops (Count)",
        "Host Instruction Rate (Count/Second)"
    ],
    "Blackscholes-A-M_2_L": [137609035, 254523771, 242714],
    "Bodytrack-A-M_2_L": [746854929, 1264292337, 159509],
    "Raytrace-A-M_2_L": [1019148207, 1713617509, 144862],
    "Ferret-A-M_2_L": [1843516103, 3219243548, 154685]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Titles for each subplot
titles = [
    'Simulation Instruction Count',
    'Simulation Operations Count',
    'Host Instruction Rate'
]

# Defining the color palette
colors = plt.cm.viridis(np.linspace(0.3, 0.7, len(df.columns) - 1))

# Function to format large tick values
def reformat_large_tick_values(tick_val, pos):
    if tick_val >= 1e9:  # For values 1 billion or higher
        val = int(tick_val) // 1e9
        return f'{val}B'
    elif tick_val >= 1e6:  # For values 1 million or higher
        val = int(tick_val) // 1e6
        return f'{val}M'
    elif tick_val >= 1e3:  # For values 1 thousand or higher
        val = int(tick_val) // 1e3
        return f'{val}K'
    else:
        return int(tick_val)

# Plotting each metric in a subplot
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(df.columns[1:], df.iloc[0, 1:], color=colors)
ax1.set_title(titles[0], fontsize=16)
ax1.set_ylabel('Count', fontsize=14)
ax1.set_xticks(range(len(df.columns[1:])))
ax1.set_xticklabels(df.columns[1:], rotation=45, ha='right', fontsize=12)
# Adding data labels on the bars
for j, value in enumerate(df.iloc[0, 1:]):
    ax1.text(j, value, f'{reformat_large_tick_values(value, None)}', ha='center', va='bottom', fontsize=12)
# Use a formatter for the y axis
ax1.yaxis.set_major_formatter(plt.FuncFormatter(reformat_large_tick_values))
# Adjust layout to prevent overlap
plt.tight_layout()
# Show the plot
plt.show()

# Simulation Operations Count
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(df.columns[1:], df.iloc[1, 1:], color=colors)
ax2.set_title(titles[1], fontsize=16)
ax2.set_ylabel('Count', fontsize=14)
ax2.set_xticks(range(len(df.columns[1:])))
ax2.set_xticklabels(df.columns[1:], rotation=45, ha='right', fontsize=12)
# Adding data labels on the bars
for j, value in enumerate(df.iloc[1, 1:]):
    ax2.text(j, value, f'{reformat_large_tick_values(value, None)}', ha='center', va='bottom', fontsize=12)
# Use a formatter for the y axis
ax2.yaxis.set_major_formatter(plt.FuncFormatter(reformat_large_tick_values))
# Adjust layout to prevent overlap
plt.tight_layout()
# Show the plot
plt.show()

# Host Instruction Rate
fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.bar(df.columns[1:], df.iloc[2, 1:], color=colors)
ax3.set_title(titles[2], fontsize=16)
ax3.set_ylabel('Count/Second', fontsize=14)
ax3.set_xticks(range(len(df.columns[1:])))
ax3.set_xticklabels(df.columns[1:], rotation=45, ha='right', fontsize=12)
# Adding data labels on the bars
for j, value in enumerate(df.iloc[2, 1:]):
    ax3.text(j, value, f'{reformat_large_tick_values(value, None)}', ha='center', va='bottom', fontsize=12)
# Use a formatter for the y axis
ax3.yaxis.set_major_formatter(plt.FuncFormatter(reformat_large_tick_values))
# Adjust layout to prevent overlap
plt.tight_layout()
# Show the plot
plt.show()
