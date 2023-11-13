ans = input().lower()
book_lst = []

while True:
    book = input()
    if book == "q":
        break
    book_lst.append(book)

if ans in book_lst:
    print("Yes", end=" ")
    print(book_lst.index(ans) + 1)
else:
    print("No", end=" ")
    print(len(book_lst))