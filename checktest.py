# checkTEST | (c) Copyright 2023 gamma.

import datetime as dt

data = dt.date.today()
path = str(data) + ".txt"

def CT(title: str, x: int, y: list, z: bool):
    # 初期化
    if z:
        f = open(path, 'w')
        f.write(f"< {title} の結果 >\n\n")
        f.close()

    print(f"\n< {title} の結果 >\n")
    n = 0
    total = 0
    more = 100 * x
    while n != x:
        print(str(y[n][0]) + " : " + str(y[n][1]) + " 点")            
        total += y[n][1]
        more -= y[n][1]
        
        if z:
            f = open(path, 'a')
            f.write(str(y[n][0]) + " : " + str(y[n][1]) + " 点\n")
            f.close()

        n += 1

    print(f"\n{x} 教科の合計 : {total} 点")
    print(f"満点まで : あと {more} 点\n")

    if z:
        f = open(path, 'a')
        f.write(f"\n{x} 教科の合計 : {total} 点\n")
        f.write(f"満点まで : あと {more} 点\n")
        f.close()