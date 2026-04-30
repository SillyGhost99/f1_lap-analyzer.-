import pandas as pd
import matplotlib.pyplot as plt

# Sample F1 lap data (replace with real CSV from FastF1 or ergast.com later)
data = {
    'driver': ['VER', 'LEC', 'NOR', 'PIA', 'HAM', 'VER', 'LEC', 'NOR'],
    'lap_time': [84.567, 84.892, 85.123, 85.456, 85.789, 84.623, 84.910, 85.089],
    'team': ['Red Bull', 'Ferrari', 'McLaren', 'Alpine', 'Mercedes', 'Red Bull', 'Ferrari', 'McLaren']
}
df = pd.DataFrame(data)

# Find fastest lap per driver (groupby + min)
fastest = df.loc[df.groupby('driver')['lap_time'].idxmin()]

# Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(fastest['driver'], fastest['lap_time'], color=['#FF2800', '#DC0000', '#FF7700', '#009E49', '#00D2BE'])
plt.title('Fastest Lap Times by Driver (Sample Data)')
plt.ylabel('Lap Time (seconds)')
plt.xlabel('Driver')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('fastest_laps.png')  # Saves plot for README
plt.show()

print(fastest)  # Prints table to console
