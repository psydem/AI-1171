import matplotlib.pyplot as plt

# Define the components of the architecture
components = [
    "Client Application",
    "Encryption Module",
    "Cloud Storage Service",
    "Key Management System",
    "Security Protocols",
    "Monitoring and Logging"
]

# Create a diagram using matplotlib
plt.figure(figsize=(10, 6))
plt.title("File Storage System Architecture")
plt.box(False)
plt.axis('off')

# Draw the components as rectangles
for i, component in enumerate(components):
    plt.text(0.5, 1 - (i + 0.5) / len(components), component,
             ha='center', va='center', bbox=dict(facecolor='lightblue', alpha=0.5, edgecolor='black'))

# Draw arrows to connect the components
for i in range(len(components) - 1):
    plt.arrow(0.5, 1 - (i + 1) / len(components), 0, -0.1,
              head_width=0.05, head_length=0.05, fc='black', ec='black')

plt.show()
