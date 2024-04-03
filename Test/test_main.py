import math


var = 1;
view_duration = input("View duration:")
click_through_rate = 7.8;55
impressions = 12000

if var == 0:
    var = var - 1
elif var > 0:
    var = var + 2
else :
    var = var + 1

print("view_duration : ", view_duration * 2)
print( "floor : " , math.floor(click_through_rate), "ceil : " ,math.ceil(click_through_rate) )