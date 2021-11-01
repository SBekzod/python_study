# import numpy
# A = numpy.array([[2, 25, 3], [34, 34, 54]])
# print(A)

import pytz
import datetime

country = 'Europe/Moscow'
tz_to_display = pytz.timezone(country)

local_time = datetime.datetime.now(tz=tz_to_display)
print('In {0} now, the time is: {1}'.format(country, local_time))
print('In {0} now, the time is: {1}'.format('Greenwich', datetime.datetime.utcnow()))


