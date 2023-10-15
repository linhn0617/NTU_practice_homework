dic =   {4:'鼠',5:'牛',6:'虎',7:'兔',8:'龍',9:'蛇',10:'馬',11:'羊',0:'猴',1:'雞',2:'狗',3:'豬'}
 
def Year_Checker(n,minguo = False):  #預設西元年(minguo)
    #n必須是整數(int)
    #minguo(代表民國年)
    if minguo == False:
        index = n % 12
        return dic[index]
    elif minguo == True:
        index = (n+1911) % 12
        return dic[index]
ans = [] 
AD_MINGUO = input()
while True:
    n = int(input())
    if n == -1:
        break
    else:
        if AD_MINGUO == "AD":
            ans.append(Year_Checker(n,False))
        elif AD_MINGUO == "Minguo":
            ans.append(Year_Checker(n,True))
for i in ans:
    print(i)