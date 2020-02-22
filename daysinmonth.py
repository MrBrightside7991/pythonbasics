# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:47:00 2020

@author: CEC
"""
def isYearLeap(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else:
        return True



#

def daysInMonth(year, month):
#
    if isYearLeap(year)==True:
        if month==2:
            return 29
        elif month==1:
            return 31
        elif month==11:
            return 30
    else:
        if month==2:
            return 28
        elif month==1:
            return 31
        elif month==11:
            return 30
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
