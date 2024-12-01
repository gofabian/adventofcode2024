import pandas as pd

df = pd.read_csv("input", sep="\\s+", names=['left', 'right'])

df['left'] = sorted(df['left'])
df['right'] = sorted(df['right'])

distances = abs(df['left'] - df['right'])
total_distance = distances.sum()

print(total_distance)
