# Q:find out the angle of the clock hands, given the hour and minute

# A: the idea is to view 360 degree, referencing from 0/12 mark as a straight line. Any movement 
# of the hand, independently from each other, can be used to calculate the angle by using 
# percentage. For example, there are 60 minutes in the whole clock circle. The minute to which
# the minute hand is point to is used to compute percentage and equate to the degree. Say it's
# 15 minute, we do 15 / 60 * 360 = 90 degree. 
# 
# Same idea with hour except that we need to wrap hour at 12 mark because there are 24 hours in 
# a day but hand moves around twice. Also, the the minutes contributes to the actual hour degree
# in the bound of hour angle width (i.e. hour many angles between hour i and i+1, which is 
# 360 / 12 = 30).
#
# Once the two independent angles of hour and minute are obtained, it's easy to calculate
# the degree by subtracting the greater with lesser. The result can be used as if we don't care
# where we measure the angle from (e.g. invert or outvert). If we do care only the invert,
# we simply choose the smaller angle of the result and (360 - result).
#
# use this web-base clock to observe/verify result
# http://www.oswego.org/ocsd-web/games/ClassClock/clockres.html

# how many angles between hour i and i+1
hour_angle_width = 360 / 12

# calcualte the minute angle
def find_minute_angle(minute):
   return (minute / 60 * 360) % 360

# calculate the hour angle with minute taken into account
def find_hour_angle(hour, minute):
   only_hour_angle = (hour % 12) / 12 * 360
   minute_offset_angle = hour_angle_width * (minute / 60)
   return (only_hour_angle + minute_offset_angle) % 360

# now we calculate the clock angle. This version return the invert angle
def find_clock_hands_angle(hour, minute):
   hour_angle = find_hour_angle(hour, minute)
   minute_angle = find_minute_angle(minute)
   raw_angle = max(hour_angle, minute_angle) - min(hour_angle, minute_angle)
   return min(raw_angle, 360-raw_angle)
   

