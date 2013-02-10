#-------------------------------------------------------------------------------
# Name:        mean_Calculator
# Purpose:      Calculates the average of all 5-digit numbers that can be formed
#               by each of the digits 1, 3, 5, 7, 8.
#
# Author:      marc
#
# Created:     20/01/2013
# Copyright:   (c) marc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import time
def main():
    i = 0
    j = 0
    k = 0
    m = 0
    n = 0
    Sum = 0
    N = 0

    a = [1,3,5,7,8]

    start = time.time()

    for i in a: #ten-thousands place
        for j in a: #thousands place

            if j != i:
                for k in a: #hundreds place
                    if k not in [i,j]:
                        for m in a: #tens place
                            if m not in [i,j,k]:
                                for n in a: #ones place
                                    if n not in [i,j,k,m]:
                                        Sum += 10000*i + 1000*j + 100*k + 10*m + n #sum all numbers
                                        N+=1
    avg = Sum / N

    stop = time.time()
    print('The average is... ' + str(round(avg,1)))
    print('Amount of time spent calculating: ' + str(round(stop - start,8)) + ' s')

if __name__ == '__main__':
    main()
