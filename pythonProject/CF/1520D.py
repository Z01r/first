"""""
tandrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr


                                          .n=n=n, .
                                       .d=HHHHHHHdH
                                     d=HHHHHHH#HHHH
                                   .dHHHHHHHH##HHH^L
        .nnn, .oo^^^'           .'  `dHHHHHH#^##HHd'
    . nHP^^HH' .nndHHH#mni,   .o' .iIHHHhYH#  `##HH
   .Hd#'  m##HnHHHHHHHH##HHHhnnnndHHHHHHHhW    `#HH
   HHH#  m##HHHHHHHHHHH##HHHHHHHHHHHHHHHHHh,    W^P
  JHHH#  ###HHHHHHHHHHH#HHHHHHHHHHHHHHHHHHHH
  HHHH#   ###HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh
  HHHH#    ###HHHHHHHHH#HHHHHHHHHHHHHH#HHHHHH
`dHHH#'     `#H###HHHHH^#HHHHHHHHHHHHH#HHHHHP
           .dHH##HHHHH'  `^^YHHHHHHHHH##HHHH
             H###HHHP'           `###F W#HHHh
             ##HHHP'              ###    `^YHHn,
          .mdHHHHP                #HF       `YHH
          !HHHHH#L               .HH,         HH
           HHH^###               `HH'         HH
           HH' `#Hh               HP          HH
           HH    `Hh,            iH          .HP
           HH     `HHh           IH         FYH
           HH      `^HL          `Hh        LJ'
           YHh       dHh          HHh
            `H^i     [_.L         `='     =W.L.=
             HnHL
             `=='
"""""
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = dict()
    kol = 0
    for i in range(n):
        a[i] -= i + 1
        kol += b.get(a[i], 0)
        b[a[i]] = b.get(a[i], 0) + 1
    print(kol)