import random
import time
text = ('''
        :xKNWWN0d,
    .ckNNNNNNNNNNNXx;
  .dXXXXXXXXXXXkxxOXXXl
 ,KXXXXXXXXX0;.;;;,.cKXO.                 :d.     KN.
'KKKKKKKKKKK..d   .x :KKO.      ';::;   ;;KXl;;.  0X. .;;.   '::;.  .;'    ,;.  ':::;;'   ,::;.   ;'.;:;.
d000000000O,  o.  'l c000c     kKl..'   ''OK:''.  OK.c0d.  .Ox'.:Kx  kK.  :Ko  OO..:Kx. ,0o..lKc  0Kx;,O0
 .,cdO000o     .,,..l0000l     'okkdc.    x0.     k0x0l    l0xoooxx. .Ok '0x   dO:,oO;  k0doooxo  OO   d0
      ...'.    ,oxkOOOOOO:     .. .lOo    dO,     xO.;ko.  ,ko.  ..   .koxx.  .ko''.    cO:.  .   kk   oO
.l:'.     ,;.lkkkkkkkkkkd      ;:cc:,      ;:c:.  ;:  .::.  .,:c::'    :xd.   .dd:::od.  .;:c::.  ::   ,:
 .dxxo...';,dxxxxxxxxxxo.                                           .,:d:     'dc...co.
   :dxxlccoxxxxxxxxxxd,                                              ..         .....
     ':oddddddddddo:.
        .:loddoc;.       
''')
print(text)
print('[?] How many codes do you want?')
sayi = input('>')
if  sayi.isdigit() == False:
    print('[!] Software ran into a problem. Exiting in 5 seconds.')
    time.sleep(5)
elif int(sayi) < 1:
    print('[!] Software ran into a problem. Exiting in 5 seconds.')
    time.sleep(5)
else:
    start = time.time()
    with open("codes.txt","w") as f:
        for i in range(int(sayi)):
            kod = '-'.join(''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(5)) for _ in range(3))
            print(kod)
            print(kod, file=f)
    end = time.time()
    sure = str((end - start))[:5]
    print(f'[!] Successfully generated {sayi} codes in {sure} seconds and created a file named "codes.txt". Press ENTER to exit.')
    input()
