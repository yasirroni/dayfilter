# dayfilter

Filter time-series based on sun movement

## Usage

```python
from datetime import datetime

date_string = '2010-01-01-16:58:30.00000'
date_datetime = datetime.strptime(date_string, '%Y-%m-%d-%H:%M:%S.%f')

# WASHINGTON DC DULLES INT'L AR [STERLING - ISIS], VA. data
latitude = 38.98
longitude = -77.47
time_zone = -5

is_noon(date_datetime, latitude, longitude, time_zone)
```

## License

This project is licensed in MIT License, but depends on [`suntime` that use LGPL license](https://github.com/SatAgro/suntime/blob/master/LICENSE).
