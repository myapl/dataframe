from datetime import datetime, timedelta

def get_file_data(filename):
    chunks = filename.split('-')
    file_datetime = filename[-14:-4]
    start_date = datetime.strptime(file_datetime, "%Y-%m-%d")
    return (chunks[0], start_date)

def get_interval(date_start, interval):
    date_end = date_start + timedelta(minutes=interval)
    date_file_finish = date_start + timedelta(days=1)
    timestamp_start = int(date_start.timestamp() * 1e3)
    timestamp_end = int(date_end.timestamp() * 1e3)
    timestamp_file_finish = int(date_file_finish.timestamp() * 1e3)
    return (timestamp_start, timestamp_end, timestamp_file_finish)

def get_precision(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0