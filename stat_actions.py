from datetime import datetime
from dateutil.relativedelta import relativedelta
from matplotlib import pyplot
import numpy
# pip install python-dateutil


def get_all_stats(cursor, when):
    when = when.lower()
    if (when[0] == 'w'):
        cursor.execute(
            "SELECT * FROM detections WHERE idobelyeg >= %(nowminusaweek)s", {"nowminusaweek": (datetime.today() - relativedelta(weeks=1))})
        result = cursor.fetchall()
    elif (when[0] == 'm'):
        cursor.execute("SELECT * FROM detections WHERE idobelyeg >= %(nowminusamonth)s", {
            "nowminusamonth": (datetime.today() - relativedelta(months=1))})
        result = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM detections WHERE idobelyeg >= %(nowminusayear)s", {
            "nowminusayear": (datetime.today() - relativedelta(years=1))})
        result = cursor.fetchall()
    return result


def create_bar_chart(entries, type):
    # belépések száma, szektorok neve
    sectors = ['A', 'B', 'C', 'D']
    x = numpy.arange(len(sectors))
    width = 0.5
    fig, ax = pyplot.subplots()
    rects1 = ax.bar(x, entries, width)

    ax.set_ylabel(f'{type} belépések száma')
    ax.set_xlabel('Szektorok')
    ax.set_xticks(x, sectors)
    ax.set_title(f'{type} belépések szektoronként')
    ax.bar_label(rects1, padding=1)
    fig.canvas.manager.set_window_title(f'{type} belépések szektoronként')
    fig.tight_layout()
    pyplot.locator_params(axis='y', integer=True)
    path = ('./charts/successful_entries_by_sector.png' if (type ==
            'Sikeres') else './charts/unsuccessful_entries_by_sector.png')
    pyplot.savefig(path)


def create_line_chart(dates, entries, type):
    x = numpy.arange(len(entries))
    fig, ax = pyplot.subplots()
    pyplot.plot(dates, entries)
    ax.set_ylabel(f'{type} belépések száma')
    ax.set_xlabel('Belépési dátumok')
    ax.set_title(f'{type} belépések dátumra lebontva')
    fig.canvas.manager.set_window_title(f'{type} belépések dátumra lebontva')
    fig.tight_layout()
    ax.grid()
    for index in range(len(dates)):
        ax.text(dates[index], entries[index], entries[index], size=10)
    pyplot.locator_params(axis='y', integer=True)
    path = ('./charts/successful_entries_by_date.png' if (type ==
            'Sikeres') else './charts/unsuccessful_entries_by_date.png')
    pyplot.savefig(path)


def create_charts(stats):
    # Bar chart - successful and unsuccessful entries per sector
    # Line chart - entries by date
    bar_successful_entries = [0, 0, 0, 0]
    bar_unsuccessful_entries = [0, 0, 0, 0]
    line_successful_entries = []
    line_unsuccessful_entries = []
    line_dates = []
    for (id, sector, timestamp, successful) in stats:
        bar_place = ord(sector) - ord('A')
        curr_date = timestamp.strftime("%Y-%m-%d")
        if (curr_date not in line_dates):
            line_dates.append(curr_date)
            line_successful_entries.append(0)
            line_unsuccessful_entries.append(0)
        line_place = line_dates.index(curr_date)
        if (successful):
            bar_successful_entries[bar_place] += 1
            line_successful_entries[line_place] += 1
        else:
            bar_unsuccessful_entries[bar_place] += 1
            line_unsuccessful_entries[line_place] += 1
    create_bar_chart(bar_successful_entries, 'Sikeres')
    create_bar_chart(bar_unsuccessful_entries, 'Sikertelen')
    create_line_chart(line_dates, line_successful_entries, 'Sikeres')
    create_line_chart(line_dates, line_unsuccessful_entries, 'Sikertelen')

    print('Az elkészült diagramok megtalálhatók a ./charts könyvtárban')
