```
Name                                         Gascost         Time (ns)       MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
-----------------------------------------  ---------  ----------------  -----------  -----------------------  -----------------------
PrecompiledEcrecover/                           3000  171600              17.4825                   1716               3000
PrecompiledSha256/128                            108     675             160                           6.75              11.8007
PrecompiledRipeMD/128                           1080    2336             462.329                      23.36              40.8392
PrecompiledIdentity/128                           27      18.8          1436.17                        0.188              0.328671
PrecompiledModExp/eip_example1                  2611  140894              18.5317                   1408.94            2463.18
PrecompiledModExp/eip_example2                  2611    8229             317.293                      82.29             143.864
PrecompiledModExp/nagydani-1-square               40    3032              13.1926                     30.32              53.007
PrecompiledModExp/nagydani-1-qube                 40    3863              10.3546                     38.63              67.535
PrecompiledModExp/nagydani-1-pow0x10001          655   16787              39.0183                    167.87             293.479
PrecompiledModExp/nagydani-2-square              133    4851              27.417                      48.51              84.8077
PrecompiledModExp/nagydani-2-qube                133    7024              18.9351                     70.24             122.797
PrecompiledModExp/nagydani-2-pow0x10001         2129   35921              59.269                     359.21             627.99
PrecompiledModExp/nagydani-3-square              378    8929              42.334                      89.29             156.101
PrecompiledModExp/nagydani-3-qube                378   14808              25.5267                    148.08             258.881
PrecompiledModExp/nagydani-3-pow0x10001         6062   89075              68.055                     890.75            1557.26
PrecompiledModExp/nagydani-4-square             1116   21403              52.1422                    214.03             374.178
PrecompiledModExp/nagydani-4-qube               1116   42058              26.5348                    420.58             735.28
PrecompiledModExp/nagydani-4-pow0x10001        17858  264793              67.4414                   2647.93            4629.25
PrecompiledModExp/nagydani-5-square             3573   55296              64.6159                    552.96             966.713
PrecompiledModExp/nagydani-5-qube               3573  114431              31.2241                   1144.31            2000.54
PrecompiledModExp/nagydani-5-pow0x10001        57180  787085              72.6478                   7870.85           13760.2
PrecompiledBn256Add/chfast1                      500   71559               6.98724                   715.59            1251.03
PrecompiledBn256Add/chfast2                      500   76264               6.55617                   762.64            1333.29
PrecompiledBn256Add/cdetrio1                     500    1814             275.634                      18.14              31.7133
PrecompiledBn256Add/cdetrio2                     500    1818             275.028                      18.18              31.7832
PrecompiledBn256Add/cdetrio3                     500    1814             275.634                      18.14              31.7133
PrecompiledBn256Add/cdetrio4                     500    1844             271.15                       18.44              32.2378
PrecompiledBn256Add/cdetrio5                     500    1779             281.057                      17.79              31.1014
PrecompiledBn256Add/cdetrio6                     500    1917             260.824                      19.17              33.514
PrecompiledBn256Add/cdetrio7                     500    1954             255.885                      19.54              34.1608
PrecompiledBn256Add/cdetrio8                     500    1982             252.27                       19.82              34.6503
PrecompiledBn256Add/cdetrio9                     500    1955             255.754                      19.55              34.1783
PrecompiledBn256Add/cdetrio10                    500    1945             257.069                      19.45              34.0035
PrecompiledBn256Add/cdetrio11                    500    8758              57.0907                     87.58             153.112
PrecompiledBn256Add/cdetrio12                    500    8912              56.1041                     89.12             155.804
PrecompiledBn256Add/cdetrio13                    500   71075               7.03482                   710.75            1242.57
PrecompiledBn256Add/cdetrio14                    500    8824              56.6636                     88.24             154.266
PrecompiledBn256ScalarMul/chfast1               2000  715908               2.79366                  7159.08           12515.9
PrecompiledBn256ScalarMul/chfast2               2000       2.77199e+06     0.721504                27719.9            48461.3
PrecompiledBn256ScalarMul/chfast3               2000       2.78246e+06     0.718788                27824.6            48644.5
PrecompiledBn256Pairing/jeff1                 260000       2.61196e+07     9.9542                 261196             456637
PrecompiledBn256Pairing/jeff2                 260000       2.63636e+07     9.8621                 263636             460901
PrecompiledBn256Pairing/jeff3                 260000       2.62239e+07     9.91463                262239             458459
PrecompiledBn256Pairing/jeff4                 340000       3.33616e+07    10.1913                 333616             583245
PrecompiledBn256Pairing/jeff5                 340000       3.35805e+07    10.1249                 335805             587071
PrecompiledBn256Pairing/jeff6                 260000       2.60257e+07     9.99013                260257             454995
PrecompiledBn256Pairing/empty_data            100000       1.77502e+06    56.3375                  17750.2            31031.8
PrecompiledBn256Pairing/one_point             180000       1.84698e+07     9.74564                184698             322899
PrecompiledBn256Pairing/two_point_match_2     260000       1.54778e+07    16.7982                 154778             270591
PrecompiledBn256Pairing/two_point_match_3     260000       2.58418e+07    10.0612                 258418             451779
PrecompiledBn256Pairing/two_point_match_4     260000       2.56064e+07    10.1537                 256064             447664
PrecompiledBn256Pairing/ten_point_match_1     900000       6.92911e+07    12.9887                 692911                  1.21138e+06
PrecompiledBn256Pairing/ten_point_match_2     900000       8.20937e+07    10.9631                 820937                  1.4352e+06
PrecompiledBn256Pairing/ten_point_match_3     260000       2.55409e+07    10.1797                 255409             446520
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gasprice for ECDSA eq` shows what the gasprice should have been, in order to have the same cost/cycle as ecRecover
    
