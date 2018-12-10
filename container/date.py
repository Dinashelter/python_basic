# In this file, I will try to write something using list, which is one of the sequence in python
# what's interesting in python is that the index of a sequence can be negative
# for example: months[-1], the result will be Dec.

# Put months in the sequence
months = ["Jan.","Feb.","Mar.","Apr.","May","Jun.","Jul.","Aug.","Sep.","Oct.","Nov.","Dec."]

# Put all the endings from 1-31 to the sequence
dateEndings = ["st","nd","rd"] + 17 * ["th"] + ["st","nd","rd"] + 7 * ["th"] + ["st"];

# Also something interesting here, the period of a sequence
# At the very beginning, I thought year = int(date[0:3]) then I can get the result 2018
# But it turns to be 201, the second index here is the number right after the period
date = input("Please input 8-digit date, format year+month+day, e.g. 20180730: ")
year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8])

# Add some simple validations, about date there are lots of things to validate, so just for
# get it :)
if len(date) != 8:
    print("Wrong Format")
else:
    print(months[month - 1] + " " + str(day) + dateEndings[day - 1] + ", " + str(year))
