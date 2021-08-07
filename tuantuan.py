# -*- coding: utf-8 -*-


if __name__ == "__main__":
    board = ["TUAN", "tuan", "TUAN", "tuan"]
    ans = []
    ans.append(["".join(row) for row in board])
    board = ["LALA", "lala", "LALA", "lala"]
    ans.append(["".join(row) for row in board])
    print(ans)
