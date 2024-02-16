"""""
abdkodr bra dars bghon


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
    y = n % 2020
    x = (n-y)//2020-y
    if y >= 0 and x >= 0 and (x*2020 + y*2021 == n):
        print("YES")
    else:
        print("NO")
