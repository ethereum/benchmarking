```
Name                                         Gascost         Time (ns)     MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
-----------------------------------------  ---------  ----------------  ---------  -----------------------  -----------------------
PrecompiledEcrecover/                           3000  159077              18.8588                 1590.77               3000
PrecompiledSha256/128                            108     639             169.014                     6.39                 12.0508
PrecompiledRipeMD/128                           1080    2030             532.02                     20.3                  38.2833
PrecompiledIdentity/128                           27      17.2          1569.77                      0.172                 0.324371
PrecompiledModExp/eip_example1                 13056   34735             375.874                   347.35                655.06
PrecompiledModExp/eip_example2                 13056    7713            1692.73                     77.13                145.458
PrecompiledModExp/nagydani-1-square              204    2590              78.7645                   25.9                  48.8443
PrecompiledModExp/nagydani-1-qube                204    3357              60.7685                   33.57                 63.309
PrecompiledModExp/nagydani-1-pow0x10001         3276   13991             234.151                   139.91                263.853
PrecompiledModExp/nagydani-2-square              665    4215             157.77                     42.15                 79.4898
PrecompiledModExp/nagydani-2-qube                665    6248             106.434                    62.48                117.83
PrecompiledModExp/nagydani-2-pow0x10001        10649   31272             340.528                   312.72                589.752
PrecompiledModExp/nagydani-3-square             1894    7558             250.595                    75.58                142.535
PrecompiledModExp/nagydani-3-qube               1894   12706             149.063                   127.06                239.62
PrecompiledModExp/nagydani-3-pow0x10001        30310   78718             385.045                   787.18               1484.53
PrecompiledModExp/nagydani-4-square             5580   18090             308.458                   180.9                 341.156
PrecompiledModExp/nagydani-4-qube               5580   36116             154.502                   361.16                681.104
PrecompiledModExp/nagydani-4-pow0x10001        89292  207740             429.826                  2077.4                3917.73
PrecompiledModExp/nagydani-5-square            17868   45934             388.993                   459.34                866.26
PrecompiledModExp/nagydani-5-qube              17868   99434             179.697                   994.34               1875.21
PrecompiledModExp/nagydani-5-pow0x10001       285900  659933             433.226                  6599.33              12445.5
PrecompiledBn256Add/chfast1                      500   14068              35.5417                  140.68                265.305
PrecompiledBn256Add/chfast2                      500   14136              35.3707                  141.36                266.588
PrecompiledBn256Add/cdetrio1                     500    1032             484.496                    10.32                 19.4623
PrecompiledBn256Add/cdetrio2                     500    1110             450.45                     11.1                  20.9333
PrecompiledBn256Add/cdetrio3                     500    1189             420.521                    11.89                 22.4231
PrecompiledBn256Add/cdetrio4                     500    1135             440.529                    11.35                 21.4047
PrecompiledBn256Add/cdetrio5                     500    1199             417.014                    11.99                 22.6117
PrecompiledBn256Add/cdetrio6                     500    1417             352.858                    14.17                 26.7229
PrecompiledBn256Add/cdetrio7                     500    1495             334.448                    14.95                 28.1939
PrecompiledBn256Add/cdetrio8                     500    1552             322.165                    15.52                 29.2688
PrecompiledBn256Add/cdetrio9                     500    1611             310.366                    16.11                 30.3815
PrecompiledBn256Add/cdetrio10                    500    1440             347.222                    14.4                  27.1567
PrecompiledBn256Add/cdetrio11                    500   14456              34.5877                  144.56                272.623
PrecompiledBn256Add/cdetrio12                    500   14485              34.5185                  144.85                273.17
PrecompiledBn256Add/cdetrio13                    500   14315              34.9284                  143.15                269.964
PrecompiledBn256Add/cdetrio14                    500    2164             231.054                    21.64                 40.8104
PrecompiledBn256ScalarMul/chfast1              40000   97875             408.685                   978.75               1845.8
PrecompiledBn256ScalarMul/chfast2              40000  105280             379.939                  1052.8                1985.45
PrecompiledBn256ScalarMul/chfast3              40000  101911             392.499                  1019.11               1921.92
PrecompiledBn256ScalarMul/cdetrio1             40000  108458             368.806                  1084.58               2045.39
PrecompiledBn256ScalarMul/cdetrio6             40000  107855             370.868                  1078.55               2034.01
PrecompiledBn256ScalarMul/cdetrio11            40000  108114             369.98                   1081.14               2038.9
PrecompiledBn256Pairing/jeff1                 260000       3.2591e+06     79.7766                32591                 61462.7
PrecompiledBn256Pairing/jeff2                 260000       3.20302e+06    81.1735                32030.2               60405
PrecompiledBn256Pairing/jeff3                 260000       3.23077e+06    80.4762                32307.7               60928.4
PrecompiledBn256Pairing/jeff4                 340000       4.32009e+06    78.7021                43200.9               81471.7
PrecompiledBn256Pairing/jeff5                 340000       4.31471e+06    78.8003                43147.1               81370.2
PrecompiledBn256Pairing/jeff6                 260000       3.25083e+06    79.9796                32508.3               61306.7
PrecompiledBn256Pairing/empty_data            100000       1.02727e+06    97.3457                10272.7               19373
PrecompiledBn256Pairing/one_point             180000       2.13090e+06    84.4712                21309.1               40186.3
PrecompiledBn256Pairing/two_point_match_2     260000       3.18384e+06    81.6623                31838.4               60043.5
PrecompiledBn256Pairing/two_point_match_3     260000       3.18156e+06    81.7208                31815.6               60000.5
PrecompiledBn256Pairing/two_point_match_4     260000       3.22249e+06    80.6828                32224.9               60772.3
PrecompiledBn256Pairing/ten_point_match_1     900000       1.17622e+07    76.5164               117622                221821
PrecompiledBn256Pairing/ten_point_match_2     900000       1.1861e+07     75.8787               118610                223685
PrecompiledBn256Pairing/ten_point_match_3     260000       3.18667e+06    81.5899                31866.7               60096.7
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gasprice for ECDSA eq` shows what the gasprice should have been, in order to have the same cost/cycle as ecRecover
    
