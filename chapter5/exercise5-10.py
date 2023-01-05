current_users = ['YB','lhl','ZSH','YH','MY']

#低效的方式：制作一个新的，完全大写的表
all_upper_users = []
for cuser in current_users:
    all_upper_users.append(cuser.upper());
new_users = ['Yb', 'LHL', 'ZSH', 'TMC', 'HXY']

#然后再来碰一碰
for new_user in new_users:
    if new_user.upper() in all_upper_users:
        print("Please enter a different user name.")
    else:
        print("This user name is not used.")
