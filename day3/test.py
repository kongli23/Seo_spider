str_1 = input('您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？')
if str_1 == '需要':
    num = int(input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询\n'))
    if num ==1:
        print('请您自己去取款窗口取款\n')
    if num ==2:
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        money = int(input('请问您需要兑换多少金加隆呢？\n'))
        print('好的，我知道了，您需要兑换（'+str(money)+'）金加隆。')
        print('那么，您需要付给我（'+str(money*51.3)+'）人民币。')
    if num==3:
        print('这个问题推荐您去咨询窗口')
else:
    print('好的，再见。')
