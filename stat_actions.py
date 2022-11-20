from datetime import datetime
from dateutil.relativedelta import relativedelta
# pip install python-dateutil


def get_stats(cursor, when):
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


# ide valami terminal data visualization library
# pl.: bashplotlib, prettytable, colorama(colors)
# másik opció, hogy agy külön file-t generálunk statnak, és azt megnyitja a program
# pl.: matplotlib, seaborn(matplotlib továbbhúzva), bokeh, plotly
def display_stats(stats):
    for (id, sector, timestamp, successful) in stats:
        print(id, sector, timestamp, successful)
