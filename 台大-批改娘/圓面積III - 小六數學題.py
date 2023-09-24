#如下圖有兩個圓重疊，小圓半徑2公分，大圓半徑3公分，深灰色部分的面積和淺灰色部分的面積大約相差幾平方公分？
import math
math.pi
r1 = int(input())
r2 = int(input())
area1 = r1*r1*math.pi
area2 = r2*r2*math.pi
ans = area2-area1
print("%.2f"%(ans))
