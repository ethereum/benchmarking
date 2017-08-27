# Bn256Add


In the following order: 

1. cpp_20170824_chfast.txt.md
2. geth_20170819_mhswende.txt.md
3. geth_20170821_tim.txt.md
4. geth_20170822_karalabe.txt.md
5. geth_20170823_tim.txt.md
6. geth_20170824_tim_ubuntu.txt.md
7. parity_20170825_mhswende.txt.md

This chart shows the worst cases (lowest G/S) for all benchmarks. 

```
Name                                         Gascost         Time (ns)      MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
-------------------------------------------------------------------------------------------------------------------------------------

bn256Add/chfast2                                 500             8511        58.7475                     85.11            362.026
PrecompiledBn256Add/chfast2                      500            76264         6.55617                   762.64            1333.29
PrecompiledBn256Add/chfast1                      500            65233         7.66483                   652.33            1057.71
PrecompiledBn256Add/chfast2                      500            50981         9.80758                   509.81             964.113
PrecompiledBn256Add/chfast2                      500            43206        11.5725                    432.06             898.135
PrecompiledBn256Add/chfast2                      500            65268         7.66072                   652.68             954.629
bn_128_add                                       500            11291        44.2831                    112.91             236.758

```

For ecdsa-equivalence, a gas cost of `1000` for `bn256Add` seems appropriate. 


# Modexp

* Modexp is missing from the cpp-benchmark

Order of columns is

1. geth_20170819_mhswende.txt.md
2. geth_20170821_tim.txt.md
3. geth_20170822_karalabe.txt.md
4. geth_20170823_tim.txt.md
5. geth_20170824_tim_ubuntu.txt.md
6. parity_20170825_mhswende.txt.md


```
Name                                         Gascost         Time (ns)      MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
-----------------------------------------  ---------  ----------------  ----------  -----------------------  -----------------------

PrecompiledModExp/nagydani-1-qube                 40    3863              10.3546                     38.63              67.535
PrecompiledModExp/nagydani-1-qube                 40    3844              10.4058                     38.44              62.3277
PrecompiledModExp/nagydani-1-qube                 40    3242              12.3381                     32.42              61.3102
PrecompiledModExp/nagydani-1-qube                 40    2997              13.3467                     29.97              62.2995
PrecompiledModExp/nagydani-1-qube                 40    4393               9.10539                    43.93              64.2533
modexp_1_pow0x10001                               40   69577               0.574903                  695.77            1458.94
```
For ecdsa-equivalence, the gasCost for `modExp` should be adjusted by 1.5, so `nagydani-1-qube` costs ~60. Note, though, that `modExp` seems fairly variable, and ranged in `MGas/S` from e.g. `9 - 66`, depending on input vector. 

However, it should be noted here that Parity is stands out - and displays a very high variance in `MGas/S` costs for `modexp`. 

Example values: 

```
modexp_1_pow0x10001         40   69577               0.574903                      695.77                1458.94
modexp_1_qube               40   12746               3.13824                       127.46                 267.268
modexp_1_square            655    9005              72.7374                         90.05                 188.824
modexp_2_pow0x10001        133  178520               0.745015                     1785.2                 3743.34
modexp_2_qube              133   30359               4.38091                       303.59                 636.59
modexp_2_square           2129   20965             101.55                          209.65                 439.61
modexp_3_pow0x10001        378  524879               0.720166                     5248.79               11006.1
modexp_3_qube              378   89207               4.23734                       892.07                1870.56
modexp_3_square           6062   60163             100.76                          601.63                1261.54
```
This should be investigated asap.  


# Scalar multiplication

In the following order: 

1. cpp_20170824_chfast.txt.md
2. geth_20170819_mhswende.txt.md
3. geth_20170821_tim.txt.md
4. geth_20170822_karalabe.txt.md
5. geth_20170823_tim.txt.md
6. geth_20170824_tim_ubuntu.txt.md

```
Name                                         Gascost         Time (ns)       MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
-----------------------------------------  ---------  ----------------  -----------  -----------------------  -----------------------

bn256ScalarMul/chfast2                          2000   455600              4.38982                  4556              19379.5
PrecompiledBn256ScalarMul/chfast3               2000       2.78246e+06     0.718788                27824.6            48644.5
PrecompiledBn256ScalarMul/chfast3               2000       1.83966e+06     1.08715                 18396.7            29828.9
PrecompiledBn256ScalarMul/chfast2               2000       1.97919e+06     1.01051                 19791.9            37429
PrecompiledBn256ScalarMul/chfast2               2000       1.63471e+06     1.22346                 16347.1            33981.1
PrecompiledBn256ScalarMul/chfast2               2000       2.52246e+06     0.792876                25224.6            36894.3
bn_128_mul                                      2000   683165              2.92755                  6831.65           14325.1
```

For ecdsa equivalence, the gasCost for `scalarMul` should be ~`30K`. However, the benchmarks above did not use worst-case scenarios, and some new benchmarks show that ~60% longer times are to be expected, which suggests that perhaps `50K` would be more appropriate. 





# Pairing


In the following order: 

1. cpp_20170824_chfast.txt.md
2. geth_20170819_mhswende.txt.md
3. geth_20170821_tim.txt.md
4. geth_20170822_karalabe.txt.md
5. geth_20170823_tim.txt.md
6. geth_20170824_tim_ubuntu.txt.md


```
Name                                         Gascost         Time (ns)      MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
-----------------------------------------  ---------  ----------------  ----------  -----------------------  -----------------------

bn256Pairing/ten_point_match_2                900000       4.57002e+07    19.6936                 457002            1.94392e+06
PrecompiledBn256Pairing/one_point             180000       1.84698e+07     9.74564                184698             322899
PrecompiledBn256Pairing/one_point             180000       1.40256e+07    12.8337                 140256             227415
PrecompiledBn256Pairing/ten_point_match_3     260000       2.10154e+07    12.3719                 210154             397426
PrecompiledBn256Pairing/one_point             180000       1.19181e+07    15.103                  119181             247745
PrecompiledBn256Pairing/one_point             180000       1.80948e+07     9.94763                180948             264659
bn_128_pairing                                     1       7.50048e+06     0.000133325            75004.8            157276
```

For ecdsa equivalence, the pairing gas cost seems like it should almost be doubled. 

The parity-value has a gascost of `1` - I'm not sure what the gascost for [that](https://github.com/paritytech/parity/blob/5ec44b1f99d0136d0c76c72b864a5b87e5a304b1/ethcore/benches/evm.rs#L34) input vector is. 

