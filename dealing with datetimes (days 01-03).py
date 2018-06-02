'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import re
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    m = re.search("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", line)
    return datetime.strptime(m.group(), '%Y-%m-%dT%H:%M:%S')
    # BETTER SOLUTION: No need to use search(re module). Better option is to select the timestamp by splitting the
    # string by whitespace and select the second item
    # timestamp = line.split()[1]
    # date_str = '%Y-%m-%dT%H:%M:%S'
    # return datetime.strptime(timestamp, date_str)


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    shutdowns = []
    for line in loglines:
        if re.search(SHUTDOWN_EVENT, line):
            shutdowns.append(convert_to_datetime(line))
    return max(shutdowns) - min(shutdowns)
    # BETTER SOLUTION: create the list in line
    # shutdown_entries = [line for line in loglines if SHUTDOWN_EVENT in line]
    # shutdown_times = [convert_to_datetime(event) for event in shutdown_entries]
    # return max(shutdown_times) - min(shutdown_times)