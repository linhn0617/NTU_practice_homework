#請撰寫一程式，印出二位同學的姓名、座號與分數：一行文字中的每個欄位請用tab間距隔開(\t)每行文字以換行結尾(\n)
#並請使用者可以自行輸入二位學生的姓名、座號、分數
name1 = input()
seat1 = int(input())
grade1 = int(input())
name2 = input()
seat2 = int(input())
grade2 = int(input())
print('姓名\t座號\t分數')
print(name1,seat1,grade1,sep='\t')
print(name2,seat2,grade2,sep='\t')
