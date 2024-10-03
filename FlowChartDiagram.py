import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Create figure
fig, ax = plt.subplots(figsize=(6, 8))

# Define positions for each box
positions = {
    "START": (0.5, 0.9),
    "WATER FLOW": (0.5, 0.8),
    "LEAK DETECTION": (0.5, 0.7),
    "LEAK DETECTED (Yes)": (0.2, 0.6),
    "DATA PROCESSING (No)": (0.8, 0.6),
    "SEND ALERT TO USER": (0.2, 0.5),
    "TO DATABASE": (0.8, 0.5),
    "BILLING": (0.5, 0.4),
    "END": (0.5, 0.3)
}

# Add boxes and text
for label, pos in positions.items():
    ax.add_patch(FancyBboxPatch((pos[0]-0.2, pos[1]-0.05), 0.4, 0.1, boxstyle="round,pad=0.1", edgecolor="black", facecolor="white"))
    ax.text(pos[0], pos[1], label, ha='center', va='center', fontsize=12)

# Add arrows
ax.annotate('', xy=(0.5, 0.85), xytext=(0.5, 0.75), arrowprops=dict(facecolor='black', arrowstyle="->"))
ax.annotate('', xy=(0.5, 0.75), xytext=(0.5, 0.65), arrowprops=dict(facecolor='black', arrowstyle="->"))
ax.annotate('', xy=(0.5, 0.65), xytext=(0.3, 0.6), arrowprops=dict(facecolor='black', arrowstyle="->"))
ax.annotate('', xy=(0.5, 0.65), xytext=(0.7, 0.6), arrowprops=dict(facecolor='black', arrowstyle="->"))
ax.annotate('', xy=(0.2, 0.55), xytext=(0.2, 0.5), arrowprops=dict(facecolor='black', arrowstyle="->"))
ax.annotate('', xy=(0.8, 0.55), xytext=(0.8, 0.5), arrowprops=dict(facecolor='black', arrowstyle="->"))
ax.annotate('', xy=(0.5, 0.55), xytext=(0.5, 0.45), arrowprops=dict(facecolor='black', arrowstyle="->"))
ax.annotate('', xy=(0.5, 0.45), xytext=(0.5, 0.35), arrowprops=dict(facecolor='black', arrowstyle="->"))

# Turn off the axes
ax.axis('off')

# Display the flowchart
plt.tight_layout()
plt.show()
