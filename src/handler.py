from datetime import datetime, timedelta

next_order_deltas = [
    [3, 7],  # monday can order for thursday and next monday
    [2, 6],  # tuesday can order for thursday and next monday
    [5, 8],  # wednesday can order for next monday and next thursday
    [4, 7],  # thursday can order for next monday and next thursday
    [3, 6],  # friday can order for next monday and next thursday
    [2, 5],  # saturday can order for next monday and next thursday
    [4, 8]  # sunday can order for next thursday and next the following monday
]

day_string = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]


def calculate(today):
    next_delivery_days = [
        today + timedelta(days=d) for d in next_order_deltas[today.weekday()]]

    return ['{}, {}/{}'.format(day_string[d.weekday()], d.month, d.day) for d in next_delivery_days]


def handle(event, context):
    return calculate(datetime.today())
