import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.axis("off")

# Define boxes: (x, y, width, height, color, text, rotation, fontsize)
boxes = [
    (0, 3, 2, 1, "#792b1c", "Fuck it\nwe ball", 0, 16),
    (2, 3, 1.8, 1, "#edc967", "We are so\nfucking back", 45, 16),
    (3, 3.75, 1, 0.25, "#fff478", "LETS FUCKING\nGOOOOOOOO", 0, 8),
    (0, 2, 2, 1, "#e5974f", "It is\nwhat it is", 45, 18),
    (2, 2, 2, 1, "#6bbd6f", "We vibing", 0, 20),
    (0, 0, 2, 2, "#8baecc", "It's so\nover", 0, 18),
    (0, 0, 0.75, 0.75, "#6f8da0", "Mom would\nbe sad", 0, 8),
]

for x, y, w, h, color, text, rotation, fontsize in boxes:
    ax.add_patch(Rectangle((x, y), w, h, color=color))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fontsize, rotation=rotation, color="black")

# Add axis labels
ax.text(-0.5, 2, "LOW\nENERGY", va="center", ha="center", rotation=90, fontsize=10)
ax.text(-0.5, 3.5, "HIGH\nENERGY", va="center", ha="center", rotation=90, fontsize=10)
ax.text(1, -0.5, "UNPLEASANT", va="center", ha="center", fontsize=10)
ax.text(3, -0.5, "PLEASANT", va="center", ha="center", fontsize=10)

# Title
plt.title("THE MOOD METER", fontsize=16, pad=20)

plt.tight_layout()
plt.savefig("mood_meter.png")
plt.show()
