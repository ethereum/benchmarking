```
Name                   Gascost         Time (ns)          MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
-------------------  ---------  ----------------  --------------  -----------------------  -----------------------
bn_128_add                 500   11291              44.2831                        112.91                 236.758
bn_128_mul                2000  683165               2.92755                      6831.65               14325.1
bn_128_pairing               1       7.50048e+06     0.000133325                 75004.8               157276
ecrecover                 3000  143070              20.9688                       1430.7                 3000
modexp_1_pow0x10001        655   69577               9.41403                       695.77                1458.94
modexp_1_qube               40   12746               3.13824                       127.46                 267.268
modexp_1_square             40    9005               4.44198                        90.05                 188.824
modexp_2_pow0x10001       2129  178520              11.9258                       1785.2                 3743.34
modexp_2_qube              133   30359               4.38091                       303.59                 636.59
modexp_2_square            133   20965               6.34391                       209.65                 439.61
modexp_3_pow0x10001       6062  524879              11.5493                       5248.79               11006.1
modexp_3_qube              378   89207               4.23734                       892.07                1870.56
modexp_3_square            378   60163               6.28293                       601.63                1261.54
modexp_4_pow0x10001      17858       1.66447e+06    10.7289                      16644.7                34901.9
modexp_4_qube             1116  279185               3.99735                      2791.85                5854.16
modexp_4_square           1116  188611               5.91694                      1886.11                3954.94
modexp_5_pow0x10001      57180       5.6857e+06     10.0568                      56857                 119222
modexp_5_qube             3573  951783               3.75401                      9517.83               19957.7
modexp_5_square           3573  641167               5.57265                      6411.67               13444.5
sha256                    3132    1443            2170.48                           14.43                  30.2579
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gasprice for ECDSA eq` shows what the gasprice should have been, in order to have the same cost/cycle as ecRecover
    
