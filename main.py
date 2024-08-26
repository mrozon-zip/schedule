import datetime as dt
import pandas as pd
from functions import flatten_extend


def schedule_dataframe(start, start2, rotations):
    dates = []
    cleaning = []
    trash = []

    delta = dt.timedelta(days=7)

    for i in range(rotations*12):
        friday = start + i * delta
        sunday = start2 + i * delta
        friday_formatted = friday.strftime('%d.%m')
        sunday_formatted = sunday.strftime('%d.%m')
        date = f"{friday_formatted}-{sunday_formatted}"
        dates.append(date)

    for j in range(rotations):
        # First part of the sequence: 1106 to 1112
        first_cleaning = [f'11{i:02}' for i in range(6, 13)]
        # Second part of the sequence: 1101 to 1105
        second_cleaning = [f'110{i}' for i in range(1, 6)]
        # Combine the two parts
        final_cleaning = first_cleaning + second_cleaning
        cleaning.append(final_cleaning)
        trash_iteration = [f"11{i:02}" for i in range(1,13)]
        trash.append(trash_iteration)

    cleaning = flatten_extend(cleaning)
    trash = flatten_extend(trash)

    data = {'dates': dates, 'trash': trash, 'cleaning': cleaning}

    df = pd.DataFrame(data)

    return df


if __name__ == '__main__':
    start = dt.date(2023, 8, 30)
    start2 = dt.date(2023, 9, 1)
    rotations = 20
    df = schedule_dataframe(start, start2, rotations)
    print(df.head())