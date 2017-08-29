```
Name                              Gascost         Time (ns)     MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
------------------------------  ---------  ----------------  ---------  -----------------------  -----------------------
ecrecover/                           3000   71227             42.1189                    712.27           3000
modexp/eip_example1                  2611  159543             16.3655                   1595.43           6719.77
modexp/eip_example2                  2611   13859            188.397                     138.59            583.725
modexp/nagydani-1-square               40   12487              3.20333                   124.87            525.938
modexp/nagydani-1-qube                 40   13026              3.07078                   130.26            548.64
modexp/nagydani-1-pow0x10001          655   23712             27.6231                    237.12            998.722
modexp/nagydani-2-square              133   27490              4.83812                   274.9            1157.85
modexp/nagydani-2-qube                133   30313              4.38756                   303.13           1276.75
modexp/nagydani-2-pow0x10001         2129   58725             36.2537                    587.25           2473.43
modexp/nagydani-3-square              378   70501              5.36163                   705.01           2969.42
modexp/nagydani-3-qube                378   76795              4.9222                    767.95           3234.52
modexp/nagydani-3-pow0x10001         6062  166532             36.4014                   1665.32           7014.14
modexp/nagydani-4-square             1116  180023              6.19921                  1800.23           7582.36
modexp/nagydani-4-qube               1116  196355              5.68358                  1963.55           8270.25
modexp/nagydani-4-pow0x10001        17858  493117             36.2145                   4931.17          20769.5
modexp/nagydani-5-square             3573  472713              7.5585                   4727.13          19910.1
modexp/nagydani-5-qube               3573  536074              6.66512                  5360.74          22578.8
modexp/nagydani-5-pow0x10001        57180       1.58318e+06   36.1173                  15831.8           66681.6
bn256Add/chfast1                      500    8527             58.6373                     85.27            359.148
bn256Add/chfast2                      500    8475             58.9971                     84.75            356.957
bn256Add/cdetrio1                     500    2358            212.044                      23.58             99.3163
bn256Add/cdetrio2                     500    2354            212.404                      23.54             99.1478
bn256Add/cdetrio3                     500    2359            211.954                      23.59             99.3584
bn256Add/cdetrio4                     500    2346            213.129                      23.46             98.8108
bn256Add/cdetrio5                     500    2354            212.404                      23.54             99.1478
bn256Add/cdetrio6                     500    5049             99.0295                     50.49            212.658
bn256Add/cdetrio7                     500    5088             98.2704                     50.88            214.301
bn256Add/cdetrio8                     500    5062             98.7752                     50.62            213.206
bn256Add/cdetrio9                     500    5053             98.9511                     50.53            212.827
bn256Add/cdetrio10                    500    5043             99.1473                     50.43            212.405
bn256Add/cdetrio11                    500    7564             66.1026                     75.64            318.587
bn256Add/cdetrio12                    500    7566             66.0851                     75.66            318.671
bn256Add/cdetrio13                    500    8476             58.9901                     84.76            356.999
bn256Add/cdetrio14                    500    6534             76.5228                     65.34            275.205
bn256ScalarMul/chfast1               2000  107330             18.6341                   1073.3            4520.62
bn256ScalarMul/chfast2               2000  433997              4.60833                  4339.97          18279.5
bn256ScalarMul/chfast3               2000  432094              4.62862                  4320.94          18199.3
bn256ScalarMul/cdetrio1              2000  701889              2.84945                  7018.89          29562.8
bn256ScalarMul/cdetrio2              2000  415061              4.81857                  4150.61          17481.9
bn256ScalarMul/cdetrio3              2000  120264             16.6301                   1202.64           5065.38
bn256ScalarMul/cdetrio4              2000    8953            223.389                      89.53            377.09
bn256ScalarMul/cdetrio5              2000    4541            440.432                      45.41            191.262
bn256ScalarMul/cdetrio6              2000  701845              2.84963                  7018.45          29560.9
bn256ScalarMul/cdetrio7              2000  415449              4.81407                  4154.49          17498.2
bn256ScalarMul/cdetrio8              2000  120511             16.596                    1205.11           5075.79
bn256ScalarMul/cdetrio9              2000    8923            224.14                       89.23            375.827
bn256ScalarMul/cdetrio10             2000    4499            444.543                      44.99            189.493
bn256ScalarMul/cdetrio11             2000  701702              2.85021                  7017.02          29554.9
bn256ScalarMul/cdetrio12             2000  415369              4.815                    4153.69          17494.9
bn256ScalarMul/cdetrio13             2000  120180             16.6417                   1201.8            5061.84
bn256ScalarMul/cdetrio14             2000    9008            222.025                      90.08            379.407
bn256ScalarMul/cdetrio15             2000    4537            440.82                       45.37            191.093
bn256Pairing/jeff1                 260000       1.12384e+07   23.135                  112384            473347
bn256Pairing/jeff2                 260000       1.12091e+07   23.1954                 112091            472115
bn256Pairing/jeff3                 260000       1.12459e+07   23.1196                 112459            473664
bn256Pairing/jeff4                 340000       1.54124e+07   22.0602                 154124            649153
bn256Pairing/jeff5                 340000       1.54326e+07   22.0313                 154326            650004
bn256Pairing/jeff6                 260000       1.12214e+07   23.17                   112214            472632
bn256Pairing/empty_data            100000       2.54697e+06   39.2624                  25469.7          107275
bn256Pairing/one_point             180000       7.04823e+06   25.5383                  70482.3          296864
bn256Pairing/two_point_match_2     260000       1.09196e+07   23.8103                 109196            459922
bn256Pairing/two_point_match_3     260000       1.12385e+07   23.1347                 112385            473355
bn256Pairing/two_point_match_4     260000       1.12034e+07   23.2072                 112034            471876
bn256Pairing/ten_point_match_1     900000       4.43926e+07   20.2737                 443926                 1.86977e+06
bn256Pairing/ten_point_match_2     900000       4.47169e+07   20.1266                 447169                 1.88342e+06
bn256Pairing/ten_point_match_3     260000       1.13238e+07   22.9605                 113238            476944
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gasprice for ECDSA eq` shows what the gasprice should have been, in order to have the same cost/cycle as ecRecover
    
