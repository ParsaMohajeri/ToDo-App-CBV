import random
from datetime import datetime, timedelta

start_date = datetime(2022, 1, 1, 0, 0, 0)
end_date = datetime(2026, 12, 31, 23, 59, 59)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
seconds_between_dates = time_between_dates.total_seconds()

random_seconds = random.randint(0, int(seconds_between_dates))

random_date = start_date + timedelta(seconds=random_seconds)

