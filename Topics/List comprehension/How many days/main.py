seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
hour = 3600
day = 24 * hour
print([x // day for x in seconds])
