```
Name                                         Gascost         Time (ns)       MGas/S    Gasprice for 10MGas/S  Gas/Ideal percent      VS Ecdsa
-----------------------------------------  ---------  ----------------  -----------  -----------------------  -------------------  ----------
PrecompiledEcrecover/                           3000  171600              17.4825                   1716      174.83 %                   1
PrecompiledSha256/128                            108     675             160                           6.75   1600.00 %                  0.11
PrecompiledRipeMD/128                           1080    2336             462.329                      23.36   4623.29 %                  0.04
PrecompiledIdentity/128                           27      18.8          1436.17                        0.188  14361.70 %                 0.01
PrecompiledModExp/eip_example1                  2611  140894              18.5317                   1408.94   185.32 %                   0.94
PrecompiledModExp/eip_example2                  2611    8229             317.293                      82.29   3172.93 %                  0.06
PrecompiledModExp/nagydani-1-square               40    3032              13.1926                     30.32   131.93 %                   1.33
PrecompiledModExp/nagydani-1-qube                 40    3863              10.3546                     38.63   103.55 %                   1.69
PrecompiledModExp/nagydani-1-pow0x10001          655   16787              39.0183                    167.87   390.18 %                   0.45
PrecompiledModExp/nagydani-2-square              133    4851              27.417                      48.51   274.17 %                   0.64
PrecompiledModExp/nagydani-2-qube                133    7024              18.9351                     70.24   189.35 %                   0.92
PrecompiledModExp/nagydani-2-pow0x10001         2129   35921              59.269                     359.21   592.69 %                   0.29
PrecompiledModExp/nagydani-3-square              378    8929              42.334                      89.29   423.34 %                   0.41
PrecompiledModExp/nagydani-3-qube                378   14808              25.5267                    148.08   255.27 %                   0.68
PrecompiledModExp/nagydani-3-pow0x10001         6062   89075              68.055                     890.75   680.55 %                   0.26
PrecompiledModExp/nagydani-4-square             1116   21403              52.1422                    214.03   521.42 %                   0.34
PrecompiledModExp/nagydani-4-qube               1116   42058              26.5348                    420.58   265.35 %                   0.66
PrecompiledModExp/nagydani-4-pow0x10001        17858  264793              67.4414                   2647.93   674.41 %                   0.26
PrecompiledModExp/nagydani-5-square             3573   55296              64.6159                    552.96   646.16 %                   0.27
PrecompiledModExp/nagydani-5-qube               3573  114431              31.2241                   1144.31   312.24 %                   0.56
PrecompiledModExp/nagydani-5-pow0x10001        57180  787085              72.6478                   7870.85   726.48 %                   0.24
PrecompiledBn256Add/chfast1                      500   71559               6.98724                   715.59   69.87 %                    2.5
PrecompiledBn256Add/chfast2                      500   76264               6.55617                   762.64   65.56 %                    2.67
PrecompiledBn256Add/cdetrio1                     500    1814             275.634                      18.14   2756.34 %                  0.06
PrecompiledBn256Add/cdetrio2                     500    1818             275.028                      18.18   2750.28 %                  0.06
PrecompiledBn256Add/cdetrio3                     500    1814             275.634                      18.14   2756.34 %                  0.06
PrecompiledBn256Add/cdetrio4                     500    1844             271.15                       18.44   2711.50 %                  0.06
PrecompiledBn256Add/cdetrio5                     500    1779             281.057                      17.79   2810.57 %                  0.06
PrecompiledBn256Add/cdetrio6                     500    1917             260.824                      19.17   2608.24 %                  0.07
PrecompiledBn256Add/cdetrio7                     500    1954             255.885                      19.54   2558.85 %                  0.07
PrecompiledBn256Add/cdetrio8                     500    1982             252.27                       19.82   2522.70 %                  0.07
PrecompiledBn256Add/cdetrio9                     500    1955             255.754                      19.55   2557.54 %                  0.07
PrecompiledBn256Add/cdetrio10                    500    1945             257.069                      19.45   2570.69 %                  0.07
PrecompiledBn256Add/cdetrio11                    500    8758              57.0907                     87.58   570.91 %                   0.31
PrecompiledBn256Add/cdetrio12                    500    8912              56.1041                     89.12   561.04 %                   0.31
PrecompiledBn256Add/cdetrio13                    500   71075               7.03482                   710.75   70.35 %                    2.49
PrecompiledBn256Add/cdetrio14                    500    8824              56.6636                     88.24   566.64 %                   0.31
PrecompiledBn256ScalarMul/chfast1               2000  715908               2.79366                  7159.08   27.94 %                    6.26
PrecompiledBn256ScalarMul/chfast2               2000       2.77199e+06     0.721504                27719.9    7.22 %                    24.23
PrecompiledBn256ScalarMul/chfast3               2000       2.78246e+06     0.718788                27824.6    7.19 %                    24.32
PrecompiledBn256Pairing/jeff1                 260000       2.61196e+07     9.9542                 261196      99.54 %                    1.76
PrecompiledBn256Pairing/jeff2                 260000       2.63636e+07     9.8621                 263636      98.62 %                    1.77
PrecompiledBn256Pairing/jeff3                 260000       2.62239e+07     9.91463                262239      99.15 %                    1.76
PrecompiledBn256Pairing/jeff4                 340000       3.33616e+07    10.1913                 333616      101.91 %                   1.72
PrecompiledBn256Pairing/jeff5                 340000       3.35805e+07    10.1249                 335805      101.25 %                   1.73
PrecompiledBn256Pairing/jeff6                 260000       2.60257e+07     9.99013                260257      99.90 %                    1.75
PrecompiledBn256Pairing/empty_data            100000       1.77502e+06    56.3375                  17750.2    563.37 %                   0.31
PrecompiledBn256Pairing/one_point             180000       1.84698e+07     9.74564                184698      97.46 %                    1.79
PrecompiledBn256Pairing/two_point_match_2     260000       1.54778e+07    16.7982                 154778      167.98 %                   1.04
PrecompiledBn256Pairing/two_point_match_3     260000       2.58418e+07    10.0612                 258418      100.61 %                   1.74
PrecompiledBn256Pairing/two_point_match_4     260000       2.56064e+07    10.1537                 256064      101.54 %                   1.72
PrecompiledBn256Pairing/ten_point_match_1     900000       6.92911e+07    12.9887                 692911      129.89 %                   1.35
PrecompiledBn256Pairing/ten_point_match_2     900000       8.20937e+07    10.9631                 820937      109.63 %                   1.59
PrecompiledBn256Pairing/ten_point_match_3     260000       2.55409e+07    10.1797                 255409      101.80 %                   1.72
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gas/Ideal percent` shows how the gas should be adjusted, in order to reach 10 MGas/second
* `VS Ecdsa` shows a factor by which the gascost should be multiplied, in order to reach the same G/S as `ecRecover`
    
