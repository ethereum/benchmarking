```
Name                              Gascost         Time (ns)     MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
------------------------------  ---------  ----------------  ---------  -----------------------  -----------------------
ecrecover/                           3000   88110             34.0483                    881.1            3000
modexp/eip_example1                  2611  217802             11.988                    2178.02           7415.8
modexp/eip_example2                  2611   19047            137.082                     190.47            648.519
modexp/nagydani-1-square               40   16671              2.39938                   166.71            567.62
modexp/nagydani-1-qube                 40   18555              2.15575                   185.55            631.767
modexp/nagydani-1-pow0x10001          655   32145             20.3764                    321.45           1094.48
modexp/nagydani-2-square              133   37338              3.56205                   373.38           1271.3
modexp/nagydani-2-qube                133   39624              3.35655                   396.24           1349.13
modexp/nagydani-2-pow0x10001         2129   82141             25.9188                    821.41           2796.77
modexp/nagydani-3-square              378   90508              4.17643                   905.08           3081.65
modexp/nagydani-3-qube                378   99380              3.80358                   993.8            3383.72
modexp/nagydani-3-pow0x10001         6062  234354             25.8669                   2343.54           7979.37
modexp/nagydani-4-square             1116  229119              4.87083                  2291.19           7801.12
modexp/nagydani-4-qube               1116  258763              4.31283                  2587.63           8810.45
modexp/nagydani-4-pow0x10001        17858  692261             25.7966                   6922.61          23570.3
modexp/nagydani-5-square             3573  609520              5.86199                  6095.2           20753.1
modexp/nagydani-5-qube               3573  706821              5.05503                  7068.21          24066.1
modexp/nagydani-5-pow0x10001        57180       2.03342e+06   28.1201                  20334.2           69234.7
bn256Add/chfast1                      500   10521             47.524                     105.21            358.223
bn256Add/chfast2                      500   10469             47.7601                    104.69            356.452
bn256Add/cdetrio1                     500    2968            168.464                      29.68            101.055
bn256Add/cdetrio2                     500    2938            170.184                      29.38            100.034
bn256Add/cdetrio3                     500    2961            168.862                      29.61            100.817
bn256Add/cdetrio4                     500    2902            172.295                      29.02             98.8083
bn256Add/cdetrio5                     500    2942            169.952                      29.42            100.17
bn256Add/cdetrio6                     500    6234             80.2053                     62.34            212.257
bn256Add/cdetrio7                     500    6230             80.2568                     62.3             212.121
bn256Add/cdetrio8                     500    6654             75.1428                     66.54            226.558
bn256Add/cdetrio9                     500    7075             70.6714                     70.75            240.892
bn256Add/cdetrio10                    500    7137             70.0574                     71.37            243.003
bn256Add/cdetrio11                    500   10624             47.0633                    106.24            361.73
bn256Add/cdetrio12                    500   10755             46.49                      107.55            366.19
bn256Add/cdetrio13                    500   11879             42.0911                    118.79            404.46
bn256Add/cdetrio14                    500    8418             59.3965                     84.18            286.619
bn256ScalarMul/chfast1               2000  132643             15.0781                   1326.43           4516.28
bn256ScalarMul/chfast2               2000  561792              3.56004                  5617.92          19128.1
bn256ScalarMul/chfast3               2000  552138              3.62228                  5521.38          18799.4
bn256ScalarMul/cdetrio1              2000  889773              2.24776                  8897.73          30295.3
bn256ScalarMul/cdetrio2              2000  533102              3.75163                  5331.02          18151.2
bn256ScalarMul/cdetrio3              2000  153622             13.019                    1536.22           5230.58
bn256ScalarMul/cdetrio4              2000   11291            177.132                     112.91            384.44
bn256ScalarMul/cdetrio5              2000    5568            359.195                      55.68            189.581
bn256ScalarMul/cdetrio6              2000  925953              2.15994                  9259.53          31527.2
bn256ScalarMul/cdetrio7              2000  537926              3.71798                  5379.26          18315.5
bn256ScalarMul/cdetrio8              2000  152987             13.073                    1529.87           5208.95
bn256ScalarMul/cdetrio9              2000   10746            186.116                     107.46            365.884
bn256ScalarMul/cdetrio10             2000    5837            342.642                      58.37            198.74
bn256ScalarMul/cdetrio11             2000  893199              2.23914                  8931.99          30412
bn256ScalarMul/cdetrio12             2000  533286              3.75033                  5332.86          18157.5
bn256ScalarMul/cdetrio13             2000  154918             12.9101                   1549.18           5274.7
bn256ScalarMul/cdetrio14             2000   11947            167.406                     119.47            406.776
bn256ScalarMul/cdetrio15             2000    5998            333.444                      59.98            204.222
bn256Pairing/jeff1                 260000       1.67306e+07   15.5404                 167306            569650
bn256Pairing/jeff2                 260000       1.68075e+07   15.4693                 168075            572266
bn256Pairing/jeff3                 260000       1.6835e+07    15.444                  168350            573204
bn256Pairing/jeff4                 340000       2.08517e+07   16.3057                 208517            709964
bn256Pairing/jeff5                 340000       2.04393e+07   16.6346                 204393            695925
bn256Pairing/jeff6                 260000       1.48531e+07   17.5048                 148531            505724
bn256Pairing/empty_data            100000       3.02538e+06   33.0537                  30253.8          103009
bn256Pairing/one_point             180000       9.37954e+06   19.1907                  93795.4          319358
bn256Pairing/two_point_match_2     260000       1.57951e+07   16.4608                 157951            537797
bn256Pairing/two_point_match_3     260000       1.68278e+07   15.4506                 168278            572960
bn256Pairing/two_point_match_4     260000       1.68192e+07   15.4585                 168192            572667
bn256Pairing/ten_point_match_1     900000       5.90294e+07   15.2466                 590294                 2.00985e+06
bn256Pairing/ten_point_match_2     900000       6.50312e+07   13.8395                 650312                 2.21421e+06
bn256Pairing/ten_point_match_3     260000       1.51876e+07   17.1192                 151876            517112
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gasprice for ECDSA eq` shows what the gasprice should have been, in order to have the same cost/cycle as ecRecover
    
