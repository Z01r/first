"""
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
t1 = input()
t2 = input()
h1 = int(t1[:2])
m1 = int(t1[3:])
h2 = int(t2[:2])
m2 = int(t2[3:])
ot1 = (h1 * 60) + m1
ot2 = (h2 * 60) + m2
r = ot1 + ((ot2 - ot1) // 2)
x = r // 60
v = r % 60
print("{:s}:{:s}".format(str(x // 10) + str(x % 10), str(v // 10) + str(v % 10)))
