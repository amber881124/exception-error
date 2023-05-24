# num = input('請輸入一個數字： ')

# try: # 捕捉所有錯誤
#     # 放有可能發生錯誤的程式碼
#     int(num)
# except:
#     print('caught an error')

# print('program can still run')

# # 請輸入一個數字： q
# # caught an error
# # program can still run


try:
    with open('file.txt','r') as f:
        for line in f:
            int(line.strip())
except FileNotFoundError as err:
    print(err)
    # [Errno 2] No such file or directory: 'file.txt'
except ValueError as err:
    print(err)
    # invalid literal for int() with base 10: '嗨'






