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


# try:
#     with open('file.txt','r') as f:
#         for line in f:
#             int(line.strip())
# except FileNotFoundError as err:
#     print(err)
#     # [Errno 2] No such file or directory: 'file.txt'
# except ValueError as err:
#     print(err)
#     # invalid literal for int() with base 10: '嗨'
# else:
#     print('great! 都沒有發生錯誤')
# finally:
#     print('in finally')

# 沒有此檔案
# [Errno 2] No such file or directory: 'file.txt'
# in finally

# 檔案內容不能轉int
# invalid literal for int() with base 10: '嗨'
# in finally

# 沒有發生任何錯誤
# great! 都沒有發生錯誤
# in finally


i = 0
count_err = 0
while True:
    i += 1
    try:
        num = input('please enter a number: ')
        num = int(num)
        print(f'great! you entered {num}')
    except ValueError as err:
        count_err += 1
        if count_err < 3:
            print(f'已輸入錯誤{count_err}次')
            print(f'caught an ValueError : {err}')
        else:
            print('已輸入錯誤三次，不給輸入了')
            break
    # 鍵盤按ctrl+c強制終止會發生KeyboardInterrupt錯誤
    except KeyboardInterrupt:
        print(f'ctrl+c遊戲終止')
        break
    finally:
        print(f'這是第{i}次玩')

# please enter a number: 6
# great! you entered 6
# 這是第1次玩
# please enter a number: y
# 已輸入錯誤1次
# caught an ValueError : invalid literal for int() with base 10: 'y'
# 這是第2次玩
# please enter a number: 遊戲終止
# 這是第3次玩Z




