Python provides a `datetime` module which has a lot of functions to deal with dates, times, and timedeltas. For instance, you may want to create, manipulate and format dates and times.

To format dates, the `.strftime()` method is widely used. It's used to create a string representation of a `datetime/date/time` instance with a specific format. The method takes one argument: the format string which contains "format codes" that tell Python how to format the date.

```python 
from datetime import datetime
now = datetime.now() 
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S') 
print(formatted_date)
```
**Here are some commonly used format codes:**

- %Y : Full year. (e.g., 2022)
- %m : Month as a zero-padded decimal number.(01, 02, ..., 12)
- %d : Day of the month as a zero-padded decimal.(01, 02, ..., 31)
- %H : Hour in 24-hour format as a zero-padded decimal.(00, 01, ..., 23)
- %M : Minute as a zero-padded decimal.(00, 01, ..., 59)
- %S : Second as a zero-padded decimal.(00, 01, ..., 59)