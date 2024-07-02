import time
# init = time.time()
# for x in range(50000):
#     print(x)

# print(time.time()-init)

print(4)
# t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) #the case for the formatted time matters %M is for minutes
print(formatted_time)
time.sleep(3)
print(5) # this will print after 3 seconds