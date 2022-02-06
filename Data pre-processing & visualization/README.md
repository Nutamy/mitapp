# Выжимка

## Очистка данных
*Удаление пунктуации*
```python
import re
def clean(line):
    new_line=re.sub(r'\W+', ' ', line).lower()
    return new_line
```
