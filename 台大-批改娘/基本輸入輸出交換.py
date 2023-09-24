#請撰寫一程式，令使用者可以用鍵盤輸入任意的二個整數，再將它交換順序後由螢幕輸出
a = int(input())
b= int(input())
(a,b) = (b,a)
print(a)
print(b)
