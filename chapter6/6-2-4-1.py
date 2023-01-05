aline_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: " + str(aline_0['x_position']))

#向右移动外星人
#剧外星人的移动速度决定将其移动多远
if aline_0['speed'] == 'slow':
    x_increment = 1
elif aline_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#新位置等于老位置加上增量
aline_0['x_position'] = aline_0['x_position'] + x_increment

print("New x-position: " + str(aline_0['x_position']))