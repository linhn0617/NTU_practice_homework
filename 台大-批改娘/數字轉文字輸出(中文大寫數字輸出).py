def num_to_chinese(number):
    if 1 <= number <= 99999:
        chinese_numbers = ["壹", "貳", "參", "肆", "伍", "陸", "柒", "捌", "玖"]
        units = ["", "拾", "佰", "仟", "萬"]

        num_str = str(number)
        length = len(num_str)
        result = ""

        for i in range(length):
            digit = int(num_str[i])
            if digit != 0:
                result += chinese_numbers[digit - 1] + units[length - i - 1]
            elif i < length - 1 and int(num_str[i + 1]) != 0:
                result += "零"

        if result.startswith("壹拾"):
            result = result[1:]
        if result.endswith("壹拾"):
            result = result[:-1]

        return result + "元整"
    else:
        return "out of range"
n= int(input())
if 1 <= n <= 99999:
    result = num_to_chinese(n)
    print(result)
else:
    print("out of range")
