#!/usr/bin/env python

import os
import re

for i in os.listdir():
    if os.path.isdir(i):
        for j in os.listdir(i):
            exp='^3_kman' #matches only starting with '3_kman'
            exp1= '^\d+[a-z]+' #matches 0ns.yaml
            exp2= '^[\d]+\_[a-z]+' #matches 0_ns.yaml'
            exp3= '.*\.yaml$' # to match with files starting with a-z
            if re.match(exp,j):
                continue
            elif re.match(exp1,j):
                print(j)
                k=j[1:]
                l='3_kman_'
                m= l + k
                os.system(f'mv {i}/{j} {i}/{m}')
            elif re.match(exp2,j):
                print(j)
                k=j[3:]
                l='3_kman_'
                m= l + k
                os.system(f'mv {i}/{j} {i}/{m}')
            elif re.match(exp3,j):
                print(j)
                k=j[0:]
                l='3_kman_'
                m= l + k
                os.system(f'mv {i}/{j} {i}/{m}')
