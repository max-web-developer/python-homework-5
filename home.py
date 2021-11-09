# hours = int(input("введите часы!: "))
# minutes = int(input("введите минуты!: "))
# n = 24
# if minutes >= 60:
#     print("минуты не должны превышать 60")
#     minutes = int(input("введите настоящее время! "))
# delta = int(input("введите дельту!: "))
# if 0 < hours + delta < 10 and minutes < 10 :
#     print('0' + str(hours + delta) + ':' + '0' + str(minutes))
# p =  hours-(hours//n*n) + delta 
# print(f"{p}:{minutes}")


# hours = int(input("введите часы!: "))
# minutes = int(input("введите минуты!: "))
# delta = float(input('введите разницу:'))
# result = '{0:02.0f}:{1:02.0f}'.format(*divmod(delta * 60, 60))
# if hours >= 0:
#     if hours < 24:
#         if minutes >= 0:
#             if minutes < 60:
#                 newHours = (hours + minutes) % 24
#                 if newHours < 10:
#                     newHours = "0" + str (newHours)
#                 if minutes < 10:
#                     minutes = "0" + str (minutes)  
#                 print(str(newHours)+ ':' +str(minutes)) 





             