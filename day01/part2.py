import pandas as pd

df = pd.read_csv("input", sep="\\s+", names=['left', 'right'])

value_counts = df['right'].value_counts(sort=False)

similarities = df['left'] * df['left'].apply(lambda x: value_counts.get(x, 0))

similarity_score = similarities.sum()

print(similarity_score)
