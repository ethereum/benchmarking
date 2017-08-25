ecrecover/
bn256Add/chfast1
bn256Add/chfast2
bn256Add/cdetrio1
bn256Add/cdetrio2
bn256Add/cdetrio3
bn256Add/cdetrio4
bn256Add/cdetrio5
bn256Add/cdetrio6
bn256Add/cdetrio7
bn256Add/cdetrio8
bn256Add/cdetrio9
bn256Add/cdetrio10
bn256Add/cdetrio11
bn256Add/cdetrio12
bn256Add/cdetrio13
bn256Add/cdetrio14
bn256ScalarMul/chfast1
bn256ScalarMul/chfast2
bn256ScalarMul/chfast3
bn256Pairing/jeff1
bn256Pairing/jeff2
bn256Pairing/jeff3
bn256Pairing/jeff4
bn256Pairing/jeff5
bn256Pairing/jeff6
bn256Pairing/empty_data
bn256Pairing/one_point
bn256Pairing/two_point_match_2
bn256Pairing/two_point_match_3
bn256Pairing/two_point_match_4
bn256Pairing/ten_point_match_1
bn256Pairing/ten_point_match_2
bn256Pairing/ten_point_match_3
```
Name                              Gascost         Time (ns)     MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
------------------------------  ---------  ----------------  ---------  -----------------------  -----------------------
ecrecover/                           3000   70528             42.5363                    705.28           3000
bn256Add/chfast1                      500    8508             58.7682                     85.08            361.899
bn256Add/chfast2                      500    8511             58.7475                     85.11            362.026
bn256Add/cdetrio1                     500    2331            214.5                        23.31             99.1521
bn256Add/cdetrio2                     500    2328            214.777                      23.28             99.0245
bn256Add/cdetrio3                     500    2341            213.584                      23.41             99.5775
bn256Add/cdetrio4                     500    2317            215.796                      23.17             98.5566
bn256Add/cdetrio5                     500    2327            214.869                      23.27             98.982
bn256Add/cdetrio6                     500    4990            100.2                        49.9             212.256
bn256Add/cdetrio7                     500    4987            100.261                      49.87            212.129
bn256Add/cdetrio8                     500    4993            100.14                       49.93            212.384
bn256Add/cdetrio9                     500    4990            100.2                        49.9             212.256
bn256Add/cdetrio10                    500    4986            100.281                      49.86            212.086
bn256Add/cdetrio11                    500    7602             65.7722                     76.02            323.361
bn256Add/cdetrio12                    500    7598             65.8068                     75.98            323.191
bn256Add/cdetrio13                    500    8494             58.8651                     84.94            361.303
bn256Add/cdetrio14                    500    6605             75.7002                     66.05            280.952
bn256ScalarMul/chfast1               2000  113076             17.6872                   1130.76           4809.83
bn256ScalarMul/chfast2               2000  455600              4.38982                  4556             19379.5
bn256ScalarMul/chfast3               2000  454158              4.40375                  4541.58          19318.2
bn256Pairing/jeff1                 260000       1.13909e+07   22.8252                 113909            484528
bn256Pairing/jeff2                 260000       1.13864e+07   22.8343                 113864            484334
bn256Pairing/jeff3                 260000       1.13918e+07   22.8235                 113918            484564
bn256Pairing/jeff4                 340000       1.5663e+07    21.7073                 156630            666245
bn256Pairing/jeff5                 340000       1.5669e+07    21.699                  156690            666499
bn256Pairing/jeff6                 260000       1.1516e+07    22.5773                 115160            489847
bn256Pairing/empty_data            100000       2.54948e+06   39.2237                  25494.8          108445
bn256Pairing/one_point             180000       7.2216e+06    24.9252                  72216            307180
bn256Pairing/two_point_match_2     260000       1.10929e+07   23.4384                 110929            471850
bn256Pairing/two_point_match_3     260000       1.13935e+07   22.82                   113935            484637
bn256Pairing/two_point_match_4     260000       1.1396e+07    22.815                  113960            484745
bn256Pairing/ten_point_match_1     900000       4.52594e+07   19.8854                 452594                 1.92517e+06
bn256Pairing/ten_point_match_2     900000       4.57002e+07   19.6936                 457002                 1.94392e+06
bn256Pairing/ten_point_match_3     260000       1.13904e+07   22.8262                 113904            484507
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gas/Ideal percent` shows how the gas should be adjusted, in order to reach 10 MGas/second
* `VS Ecdsa` shows a factor by which the gascost should be multiplied, in order to reach the same G/S as `ecRecover`
    
