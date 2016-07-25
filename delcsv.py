'''
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
'''


from datetime import datetime
from csv import *
from math import exp, log, sqrt


# parameters #################################################################

train = '/Users/yihui/Downloads/ad-ml/kaggle-2014-criteo/train.new.txt'  # path to training file
test = '/Users/yihui/Downloads/ad-ml/kaggle-2014-criteo/train.csv'  # path to testing file

f_write = open(test,"w")
with open(train) as f:
    f_csv = reader(f,delimiter='\t')
    for row in f_csv:
        for i in range(len(row)):
            f_write.write(row[i])
            if i != len(row)-1:
                f_write.write(",")
        f_write.write('\n')

