# Выжимка

## Очистка данных
*Удаление пунктуации*
```python
import re
def clean(line):
    new_line=re.sub(r'\W+', ' ', line).lower()
    return new_line
```
*Удаление пустых ячеек*
```python
import pandas as pd
# 1 вариант
df = pd.read_csv('movie_scores.csv')
for column in df.columns.tolist():
    df = df[df[column].notnull()]
# 2 вариант
df.dropna()
# заполнение пустых ячеек средним значением
df.fillna(df.mean())
# интерполяция
series.interpolate()
```
*Удаление пустых ячеек*
```python
import pandas as pd
df = pd.read_csv('movie_scores.csv')
for column in df.columns.tolist():
    df = df[df[column].notnull()]
```
