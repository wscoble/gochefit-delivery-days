from handler import calculate
import pytest
from datetime import datetime, timedelta


@pytest.mark.parametrize('weekday,delivery_day_1,delivery_day_2', [
    (0, 'Thursday', 'Monday'),
    (1, 'Thursday', 'Monday'),
    (2, 'Monday', 'Thursday'),
    (3, 'Monday', 'Thursday'),
    (4, 'Monday', 'Thursday'),
    (5, 'Monday', 'Thursday'),
    (6, 'Thursday', 'Monday')
])
def test_correct_delivery_days_returned(weekday, delivery_day_1, delivery_day_2):
    today = datetime.today()
    today += timedelta((7 + weekday - today.weekday()) % 7)
    actual = calculate(today)
    # is the calculated today really the weekday we want?
    assert today.weekday() is weekday
    # is the first available delivery day the one we want?
    assert delivery_day_1 in actual[0]
    # is the second available delivery day the one we want?
    assert delivery_day_2 in actual[1]
