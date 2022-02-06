# Выжимка

## Очистка данных

```python
import re
import pandas as pd

df = pd.read_csv('movie_scores.csv')

# Удаление пунктуации
def clean(line):
    new_line=re.sub(r'\W+', ' ', line).lower()
    return new_line

# Удаление пустых ячеек
df.dropna()

# Заполнение пустых ячеек средним значением
df.fillna(df.mean())

# интерполяция
series = df['Column']
series.interpolate()
```
