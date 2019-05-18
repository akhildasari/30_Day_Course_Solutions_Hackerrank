#!/bin/python3

import sys


meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())
    
tip=meal_cost*tip_percent/100
tax=meal_cost*tax_percent/100
total=round(meal_cost+tip+tax)
    
print(str(total))
