# "Age","Gender","Impressions","Clicks","Signed_In"
# 36,0,3,0,1


#!/usr/bin/python
# Import required libraries
import sys

# Start a counter and store the textfile in memory
count = 0
lines = sys.stdin.readlines()
lines.pop(0)

total = maxAge = countAge = countImp = countClicks = 0
ageDistribution = {}

# For each line, find the sum of index 2 in the list.
for line in lines:
  (age, gender, impressions, clicks, signed_in) = map(int, line.strip().split(','))

  countAge    += age
  countClicks += clicks
  countImp    += impressions
  total       += 1

  ageDistribution[age] += 1

  if age > maxAge:
    maxAge = age

print "Impressions count", countImp
print "Avg age", countAge/total
print "CTR", countClicks/float(countImp)
print "Oldest Person", maxAge

print ageDistribution