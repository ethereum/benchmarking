```
Name                              Gascost         Time (ns)     MGas/S    Gasprice for 10MGas/S  Gas/Ideal percent      VS Ecdsa
------------------------------  ---------  ----------------  ---------  -----------------------  -------------------  ----------
ecrecover/                           3000   70528             42.5363                    705.28  425.36 %                   1
bn256Add/chfast1                      500    8508             58.7682                     85.08  587.68 %                   0.72
bn256Add/chfast2                      500    8511             58.7475                     85.11  587.48 %                   0.72
bn256Add/cdetrio1                     500    2331            214.5                        23.31  2145.00 %                  0.2
bn256Add/cdetrio2                     500    2328            214.777                      23.28  2147.77 %                  0.2
bn256Add/cdetrio3                     500    2341            213.584                      23.41  2135.84 %                  0.2
bn256Add/cdetrio4                     500    2317            215.796                      23.17  2157.96 %                  0.2
bn256Add/cdetrio5                     500    2327            214.869                      23.27  2148.69 %                  0.2
bn256Add/cdetrio6                     500    4990            100.2                        49.9   1002.00 %                  0.42
bn256Add/cdetrio7                     500    4987            100.261                      49.87  1002.61 %                  0.42
bn256Add/cdetrio8                     500    4993            100.14                       49.93  1001.40 %                  0.42
bn256Add/cdetrio9                     500    4990            100.2                        49.9   1002.00 %                  0.42
bn256Add/cdetrio10                    500    4986            100.281                      49.86  1002.81 %                  0.42
bn256Add/cdetrio11                    500    7602             65.7722                     76.02  657.72 %                   0.65
bn256Add/cdetrio12                    500    7598             65.8068                     75.98  658.07 %                   0.65
bn256Add/cdetrio13                    500    8494             58.8651                     84.94  588.65 %                   0.72
bn256Add/cdetrio14                    500    6605             75.7002                     66.05  757.00 %                   0.56
bn256ScalarMul/chfast1               2000  113076             17.6872                   1130.76  176.87 %                   2.4
bn256ScalarMul/chfast2               2000  455600              4.38982                  4556     43.90 %                    9.69
bn256ScalarMul/chfast3               2000  454158              4.40375                  4541.58  44.04 %                    9.66
bn256Pairing/jeff1                 260000       1.13909e+07   22.8252                 113909     228.25 %                   1.86
bn256Pairing/jeff2                 260000       1.13864e+07   22.8343                 113864     228.34 %                   1.86
bn256Pairing/jeff3                 260000       1.13918e+07   22.8235                 113918     228.23 %                   1.86
bn256Pairing/jeff4                 340000       1.5663e+07    21.7073                 156630     217.07 %                   1.96
bn256Pairing/jeff5                 340000       1.5669e+07    21.699                  156690     216.99 %                   1.96
bn256Pairing/jeff6                 260000       1.1516e+07    22.5773                 115160     225.77 %                   1.88
bn256Pairing/empty_data            100000       2.54948e+06   39.2237                  25494.8   392.24 %                   1.08
bn256Pairing/one_point             180000       7.2216e+06    24.9252                  72216     249.25 %                   1.71
bn256Pairing/two_point_match_2     260000       1.10929e+07   23.4384                 110929     234.38 %                   1.81
bn256Pairing/two_point_match_3     260000       1.13935e+07   22.82                   113935     228.20 %                   1.86
bn256Pairing/two_point_match_4     260000       1.1396e+07    22.815                  113960     228.15 %                   1.86
bn256Pairing/ten_point_match_1     900000       4.52594e+07   19.8854                 452594     198.85 %                   2.14
bn256Pairing/ten_point_match_2     900000       4.57002e+07   19.6936                 457002     196.94 %                   2.16
bn256Pairing/ten_point_match_3     260000       1.13904e+07   22.8262                 113904     228.26 %                   1.86
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gas/Ideal percent` shows how the gas should be adjusted, in order to reach 10 MGas/second
* `VS Ecdsa` shows a factor by which the gascost should be multiplied, in order to reach the same G/S as `ecRecover`
    
