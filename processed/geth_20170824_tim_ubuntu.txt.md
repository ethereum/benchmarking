```
Name                                         Gascost         Time (ns)       MGas/S    Gasprice for 10MGas/S  Gas/Ideal percent      VS Ecdsa
-----------------------------------------  ---------  ----------------  -----------  -----------------------  -------------------  ----------
PrecompiledEcrecover/                           3000  205110              14.6263                   2051.1    146.26 %                   1
PrecompiledSha256/128                            108     815             132.515                       8.15   1325.15 %                  0.11
PrecompiledRipeMD/128                           1080    2468             437.601                      24.68   4376.01 %                  0.03
PrecompiledIdentity/128                           27      22.4          1205.36                        0.224  12053.57 %                 0.01
PrecompiledModExp/eip_example1                  2611   44204              59.0671                    442.04   590.67 %                   0.25
PrecompiledModExp/eip_example2                  2611   10144             257.394                     101.44   2573.94 %                  0.06
PrecompiledModExp/nagydani-1-square               40    3490              11.4613                     34.9    114.61 %                   1.28
PrecompiledModExp/nagydani-1-qube                 40    4393               9.10539                    43.93   91.05 %                    1.61
PrecompiledModExp/nagydani-1-pow0x10001          655   17256              37.9578                    172.56   379.58 %                   0.39
PrecompiledModExp/nagydani-2-square              133    5438              24.4575                     54.38   244.58 %                   0.6
PrecompiledModExp/nagydani-2-qube                133    7905              16.8248                     79.05   168.25 %                   0.87
PrecompiledModExp/nagydani-2-pow0x10001         2129   36893              57.7074                    368.93   577.07 %                   0.25
PrecompiledModExp/nagydani-3-square              378    9818              38.5007                     98.18   385.01 %                   0.38
PrecompiledModExp/nagydani-3-qube                378   16213              23.3146                    162.13   233.15 %                   0.63
PrecompiledModExp/nagydani-3-pow0x10001         6062   93514              64.8245                    935.14   648.25 %                   0.23
PrecompiledModExp/nagydani-4-square             1116   22544              49.5032                    225.44   495.03 %                   0.3
PrecompiledModExp/nagydani-4-qube               1116   45107              24.7412                    451.07   247.41 %                   0.59
PrecompiledModExp/nagydani-4-pow0x10001        17858  271090              65.8748                   2710.9    658.75 %                   0.22
PrecompiledModExp/nagydani-5-square             3573   60317              59.237                     603.17   592.37 %                   0.25
PrecompiledModExp/nagydani-5-qube               3573  128073              27.8982                   1280.73   278.98 %                   0.52
PrecompiledModExp/nagydani-5-pow0x10001        57180  857053              66.717                    8570.53   667.17 %                   0.22
PrecompiledBn256Add/chfast1                      500   61410               8.142                     614.1    81.42 %                    1.8
PrecompiledBn256Add/chfast2                      500   65268               7.66072                   652.68   76.61 %                    1.91
PrecompiledBn256Add/cdetrio1                     500    2098             238.322                      20.98   2383.22 %                  0.06
PrecompiledBn256Add/cdetrio2                     500    2149             232.666                      21.49   2326.66 %                  0.06
PrecompiledBn256Add/cdetrio3                     500    2123             235.516                      21.23   2355.16 %                  0.06
PrecompiledBn256Add/cdetrio4                     500    2159             231.589                      21.59   2315.89 %                  0.06
PrecompiledBn256Add/cdetrio5                     500    2106             237.417                      21.06   2374.17 %                  0.06
PrecompiledBn256Add/cdetrio6                     500    2330             214.592                      23.3    2145.92 %                  0.07
PrecompiledBn256Add/cdetrio7                     500    2315             215.983                      23.15   2159.83 %                  0.07
PrecompiledBn256Add/cdetrio8                     500    2367             211.238                      23.67   2112.38 %                  0.07
PrecompiledBn256Add/cdetrio9                     500    2297             217.675                      22.97   2176.75 %                  0.07
PrecompiledBn256Add/cdetrio10                    500    2283             219.01                       22.83   2190.10 %                  0.07
PrecompiledBn256Add/cdetrio11                    500    9778              51.1352                     97.78   511.35 %                   0.29
PrecompiledBn256Add/cdetrio12                    500    9792              51.0621                     97.92   510.62 %                   0.29
PrecompiledBn256Add/cdetrio13                    500   60059               8.32515                   600.59   83.25 %                    1.76
PrecompiledBn256Add/cdetrio14                    500    9778              51.1352                     97.78   511.35 %                   0.29
PrecompiledBn256ScalarMul/chfast1               2000  648306               3.08496                  6483.06   30.85 %                    4.74
PrecompiledBn256ScalarMul/chfast2               2000       2.52246e+06     0.792876                25224.6    7.93 %                    18.45
PrecompiledBn256ScalarMul/chfast3               2000       2.50564e+06     0.798199                25056.4    7.98 %                    18.32
PrecompiledBn256Pairing/jeff1                 260000       2.63287e+07     9.87515                263287      98.75 %                    1.48
PrecompiledBn256Pairing/jeff2                 260000       2.59834e+07    10.0064                 259834      100.06 %                   1.46
PrecompiledBn256Pairing/jeff3                 260000       2.59959e+07    10.0016                 259959      100.02 %                   1.46
PrecompiledBn256Pairing/jeff4                 340000       3.31864e+07    10.2452                 331864      102.45 %                   1.43
PrecompiledBn256Pairing/jeff5                 340000       3.32826e+07    10.2155                 332826      102.16 %                   1.43
PrecompiledBn256Pairing/jeff6                 260000       2.60602e+07     9.97691                260602      99.77 %                    1.47
PrecompiledBn256Pairing/empty_data            100000       2.13641e+06    46.8075                  21364.1    468.07 %                   0.31
PrecompiledBn256Pairing/one_point             180000       1.80948e+07     9.94763                180948      99.48 %                    1.47
PrecompiledBn256Pairing/two_point_match_2     260000       1.5636e+07     16.6283                 156360      166.28 %                   0.88
PrecompiledBn256Pairing/two_point_match_3     260000       2.51824e+07    10.3247                 251824      103.25 %                   1.42
PrecompiledBn256Pairing/two_point_match_4     260000       2.52498e+07    10.2971                 252498      102.97 %                   1.42
PrecompiledBn256Pairing/ten_point_match_1     900000       6.83181e+07    13.1737                 683181      131.74 %                   1.11
PrecompiledBn256Pairing/ten_point_match_2     900000       8.0069e+07     11.2403                 800690      112.40 %                   1.3
PrecompiledBn256Pairing/ten_point_match_3     260000       2.5351e+07     10.256                  253510      102.56 %                   1.43
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gas/Ideal percent` shows how the gas should be adjusted, in order to reach 10 MGas/second
* `VS Ecdsa` shows a factor by which the gascost should be multiplied, in order to reach the same G/S as `ecRecover`
    
