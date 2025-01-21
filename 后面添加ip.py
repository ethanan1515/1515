# 读取 ip.txt 和 账号.txt 的内容
with open('ip.txt', 'r') as ip_file:
    ip_lines = ip_file.readlines()

with open('账号.txt', 'r') as account_file:
    account_lines = account_file.readlines()

# 检查两文件的行数是否一致
if len(ip_lines) != len(account_lines):
    print("错误：ip.txt 和 账号.txt 的行数不一致！")
else:
    # 将 ip.txt 的内容加到 账号.txt 的每一行末尾
    with open('账号.txt', 'w') as account_file:
        for account_line, ip_line in zip(account_lines, ip_lines):
            # 去掉 ip_line 和 account_line 末尾的换行符，并加上空格分隔
            new_line = account_line.strip() + ' ' + ip_line.strip() + '\n'
            account_file.write(new_line)

    print("文件处理完毕！")
