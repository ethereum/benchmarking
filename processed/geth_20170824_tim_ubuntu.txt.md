```
Name                                         Gascost         Time (ns)       MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
-----------------------------------------  ---------  ----------------  -----------  -----------------------  -----------------------
PrecompiledEcrecover/                           3000  205110              14.6263                   2051.1             3000
PrecompiledSha256/128                            108     815             132.515                       8.15              11.9204
PrecompiledRipeMD/128                           1080    2468             437.601                      24.68              36.0977
PrecompiledIdentity/128                           27      22.4          1205.36                        0.224              0.327629
PrecompiledModExp/eip_example1                  2611   44204              59.0671                    442.04             646.541
PrecompiledModExp/eip_example2                  2611   10144             257.394                     101.44             148.369
PrecompiledModExp/nagydani-1-square               40    3490              11.4613                     34.9               51.0458
PrecompiledModExp/nagydani-1-qube                 40    4393               9.10539                    43.93              64.2533
PrecompiledModExp/nagydani-1-pow0x10001          655   17256              37.9578                    172.56             252.391
PrecompiledModExp/nagydani-2-square              133    5438              24.4575                     54.38              79.5378
PrecompiledModExp/nagydani-2-qube                133    7905              16.8248                     79.05             115.621
PrecompiledModExp/nagydani-2-pow0x10001         2129   36893              57.7074                    368.93             539.608
PrecompiledModExp/nagydani-3-square              378    9818              38.5007                     98.18             143.601
PrecompiledModExp/nagydani-3-qube                378   16213              23.3146                    162.13             237.136
PrecompiledModExp/nagydani-3-pow0x10001         6062   93514              64.8245                    935.14            1367.76
PrecompiledModExp/nagydani-4-square             1116   22544              49.5032                    225.44             329.735
PrecompiledModExp/nagydani-4-qube               1116   45107              24.7412                    451.07             659.748
PrecompiledModExp/nagydani-4-pow0x10001        17858  271090              65.8748                   2710.9             3965.04
PrecompiledModExp/nagydani-5-square             3573   60317              59.237                     603.17             882.214
PrecompiledModExp/nagydani-5-qube               3573  128073              27.8982                   1280.73            1873.23
PrecompiledModExp/nagydani-5-pow0x10001        57180  857053              66.717                    8570.53           12535.5
PrecompiledBn256Add/chfast1                      500   61410               8.142                     614.1              898.201
PrecompiledBn256Add/chfast2                      500   65268               7.66072                   652.68             954.629
PrecompiledBn256Add/cdetrio1                     500    2098             238.322                      20.98              30.686
PrecompiledBn256Add/cdetrio2                     500    2149             232.666                      21.49              31.4319
PrecompiledBn256Add/cdetrio3                     500    2123             235.516                      21.23              31.0516
PrecompiledBn256Add/cdetrio4                     500    2159             231.589                      21.59              31.5782
PrecompiledBn256Add/cdetrio5                     500    2106             237.417                      21.06              30.803
PrecompiledBn256Add/cdetrio6                     500    2330             214.592                      23.3               34.0793
PrecompiledBn256Add/cdetrio7                     500    2315             215.983                      23.15              33.8599
PrecompiledBn256Add/cdetrio8                     500    2367             211.238                      23.67              34.6204
PrecompiledBn256Add/cdetrio9                     500    2297             217.675                      22.97              33.5966
PrecompiledBn256Add/cdetrio10                    500    2283             219.01                       22.83              33.3918
PrecompiledBn256Add/cdetrio11                    500    9778              51.1352                     97.78             143.016
PrecompiledBn256Add/cdetrio12                    500    9792              51.0621                     97.92             143.221
PrecompiledBn256Add/cdetrio13                    500   60059               8.32515                   600.59             878.441
PrecompiledBn256Add/cdetrio14                    500    9778              51.1352                     97.78             143.016
PrecompiledBn256ScalarMul/chfast1               2000  648306               3.08496                  6483.06            9482.32
PrecompiledBn256ScalarMul/chfast2               2000       2.52246e+06     0.792876                25224.6            36894.3
PrecompiledBn256ScalarMul/chfast3               2000       2.50564e+06     0.798199                25056.4            36648.3
PrecompiledBn256Pairing/jeff1                 260000       2.63287e+07     9.87515                263287             385092
PrecompiledBn256Pairing/jeff2                 260000       2.59834e+07    10.0064                 259834             380041
PrecompiledBn256Pairing/jeff3                 260000       2.59959e+07    10.0016                 259959             380224
PrecompiledBn256Pairing/jeff4                 340000       3.31864e+07    10.2452                 331864             485395
PrecompiledBn256Pairing/jeff5                 340000       3.32826e+07    10.2155                 332826             486801
PrecompiledBn256Pairing/jeff6                 260000       2.60602e+07     9.97691                260602             381164
PrecompiledBn256Pairing/empty_data            100000       2.13641e+06    46.8075                  21364.1            31247.8
PrecompiledBn256Pairing/one_point             180000       1.80948e+07     9.94763                180948             264659
PrecompiledBn256Pairing/two_point_match_2     260000       1.5636e+07     16.6283                 156360             228697
PrecompiledBn256Pairing/two_point_match_3     260000       2.51824e+07    10.3247                 251824             368325
PrecompiledBn256Pairing/two_point_match_4     260000       2.52498e+07    10.2971                 252498             369311
PrecompiledBn256Pairing/ten_point_match_1     900000       6.83181e+07    13.1737                 683181             999241
PrecompiledBn256Pairing/ten_point_match_2     900000       8.0069e+07     11.2403                 800690                  1.17111e+06
PrecompiledBn256Pairing/ten_point_match_3     260000       2.5351e+07     10.256                  253510             370792
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gasprice for ECDSA eq` shows what the gasprice should have been, in order to have the same cost/cycle as ecRecover
    
