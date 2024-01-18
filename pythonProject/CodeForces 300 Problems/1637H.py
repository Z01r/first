"""""
author ZoirKimsanov
         __                              ___   __        .ama     ,
      ,d888a                          ,d88888888888ba.  ,88"I)   d
     a88']8i                         a88".8"8)   `"8888:88  " _a8'
   .d8P' PP                        .d8P'.8  d)      "8:88:baad8P'
  ,d8P' ,ama,   .aa,  .ama.g ,mmm  d8P' 8  .8'        88):888P'
 ,d88' d8[ "8..a8"88 ,8I"88[ I88' d88   ]IaI"        d8[
 a88' ]P "bm8mP8'(8'.8I  8[      d88'    `"         .88
,88I ]P[  .I'.8     88' ,8' I[  ,88P ,ama    ,ama,  d8[  .ama.g
[88' I8, .I' ]8,  ,88B ,d8 aI   (88',88"8)  d8[ "8. 88 ,8I"88[
]88  `8888"  '8888" "88P"8m"    I88 88[ 8[ ]P "bm8m88[.8I  8[
]88,          _,,aaaaaa,_       I88 8"  8 ]P[  .I' 88 88' ,8' I[
`888a,.  ,aadd88888888888bma.   )88,  ,]I I8, .I' )88a8B ,d8 aI
  "888888PP"'        `8""""""8   "888PP'  `8888"  `88P"88P"8m"
"""

import sys

I = lambda: [*map(int, sys.stdin.readline().split())]


class BIT:
    def __init__(self, n):
        self.n = n + 5
        self.arr = [0] * self.n

    def add(self, index):
        while index < self.n:
            self.arr[index] += 1
            index += index & (-index)

    def query(self, index):
        s = 0
        while index > 0:
            s += self.arr[index];
            index -= index & (-index)
        return s


t, = I()
for _ in range(t):
    n, = I()
    p = I()
    invs = 0
    bit = BIT(n)
    for i in range(n - 1, -1, -1):
        invs += bit.query(p[i])
        bit.add(p[i])
    c = [0] * n
    for i in range(n):
        c[i] = i + 2 - 2 * p[i]
    c.sort(reverse=True)
    s = 0
    out = [invs]
    for i in range(n):
        s += c[i]
        out.append(invs - s - i * (i + 1) // 2)
    print(*out)
