```
Name                                         Gascost         Time (ns)      MGas/S    Gasprice for 10MGas/S    Gasprice for ECDSA eq
-----------------------------------------  ---------  ----------------  ----------  -----------------------  -----------------------
PrecompiledEcrecover/                           3000  158636              18.9112                  1586.36            3000
PrecompiledSha256/128                            108     679             159.057                      6.79              12.8407
PrecompiledRipeMD/128                           1080    2100             514.286                     21                 39.7136
PrecompiledIdentity/128                           27      17.4          1551.72                       0.174              0.329055
PrecompiledModExp/eip_example1                  2611   34691              75.2645                   346.91             656.049
PrecompiledModExp/eip_example2                  2611    7667             340.55                      76.67             144.992
PrecompiledModExp/nagydani-1-square               40    2557              15.6433                    25.57              48.356
PrecompiledModExp/nagydani-1-qube                 40    3242              12.3381                    32.42              61.3102
PrecompiledModExp/nagydani-1-pow0x10001          655   13437              48.746                    134.37             254.11
PrecompiledModExp/nagydani-2-square              133    4458              29.834                     44.58              84.3062
PrecompiledModExp/nagydani-2-qube                133    5786              22.9865                    57.86             109.42
PrecompiledModExp/nagydani-2-pow0x10001         2129   28759              74.029                    287.59             543.868
PrecompiledModExp/nagydani-3-square              378    7346              51.4566                    73.46             138.922
PrecompiledModExp/nagydani-3-qube                378   12122              31.183                    121.22             229.242
PrecompiledModExp/nagydani-3-pow0x10001         6062   71600              84.6648                   716               1354.04
PrecompiledModExp/nagydani-4-square             1116   16887              66.0863                   168.87             319.354
PrecompiledModExp/nagydani-4-qube               1116   33320              33.4934                   333.2              630.122
PrecompiledModExp/nagydani-4-pow0x10001        17858  212587              84.0033                  2125.87            4020.28
PrecompiledModExp/nagydani-5-square             3573   46438              76.9413                   464.38             878.199
PrecompiledModExp/nagydani-5-qube               3573   95187              37.5366                   951.87            1800.1
PrecompiledModExp/nagydani-5-pow0x10001        57180  646587              88.4336                  6465.87           12227.7
PrecompiledBn256Add/chfast1                      500   48077              10.4                      480.77             909.195
PrecompiledBn256Add/chfast2                      500   50981               9.80758                  509.81             964.113
PrecompiledBn256Add/cdetrio1                     500    1617             309.215                     16.17              30.5794
PrecompiledBn256Add/cdetrio2                     500    1647             303.582                     16.47              31.1468
PrecompiledBn256Add/cdetrio3                     500    1646             303.767                     16.46              31.1279
PrecompiledBn256Add/cdetrio4                     500    1675             298.507                     16.75              31.6763
PrecompiledBn256Add/cdetrio5                     500    1615             309.598                     16.15              30.5416
PrecompiledBn256Add/cdetrio6                     500    1725             289.855                     17.25              32.6219
PrecompiledBn256Add/cdetrio7                     500    1732             288.684                     17.32              32.7542
PrecompiledBn256Add/cdetrio8                     500    1770             282.486                     17.7               33.4729
PrecompiledBn256Add/cdetrio9                     500    1719             290.867                     17.19              32.5084
PrecompiledBn256Add/cdetrio10                    500    1723             290.192                     17.23              32.584
PrecompiledBn256Add/cdetrio11                    500    7376              67.7874                    73.76             139.489
PrecompiledBn256Add/cdetrio12                    500    7390              67.659                     73.9              139.754
PrecompiledBn256Add/cdetrio13                    500   47021              10.6335                   470.21             889.224
PrecompiledBn256Add/cdetrio14                    500    7213              69.3193                    72.13             136.407
PrecompiledBn256ScalarMul/chfast1               2000  508212               3.93537                 5082.12            9610.91
PrecompiledBn256ScalarMul/chfast2               2000       1.97919e+06     1.01051                19791.9            37429
PrecompiledBn256ScalarMul/chfast3               2000       1.9208e+06      1.04123                19208              36324.6
PrecompiledBn256Pairing/jeff1                 260000       2.02397e+07    12.846                 202397             382757
PrecompiledBn256Pairing/jeff2                 260000       2.02966e+07    12.81                  202966             383833
PrecompiledBn256Pairing/jeff3                 260000       2.03516e+07    12.7754                203516             384874
PrecompiledBn256Pairing/jeff4                 340000       2.61128e+07    13.0204                261128             493825
PrecompiledBn256Pairing/jeff5                 340000       2.60179e+07    13.0679                260179             492030
PrecompiledBn256Pairing/jeff6                 260000       2.02826e+07    12.8189                202826             383569
PrecompiledBn256Pairing/empty_data            100000       1.77467e+06    56.3484                 17746.7            33561.2
PrecompiledBn256Pairing/one_point             180000       1.41908e+07    12.6842                141908             268366
PrecompiledBn256Pairing/two_point_match_2     260000       1.2195e+07     21.3202                121950             230623
PrecompiledBn256Pairing/two_point_match_3     260000       2.00208e+07    12.9865                200208             378617
PrecompiledBn256Pairing/two_point_match_4     260000       2.01699e+07    12.8905                201699             381437
PrecompiledBn256Pairing/ten_point_match_1     900000       5.40774e+07    16.6428                540774                  1.02267e+06
PrecompiledBn256Pairing/ten_point_match_2     900000       6.40547e+07    14.0505                640547                  1.21135e+06
PrecompiledBn256Pairing/ten_point_match_3     260000       2.10154e+07    12.3719                210154             397426
```

Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gas/Ideal percent` shows how the gas should be adjusted, in order to reach 10 MGas/second
* `VS Ecdsa` shows a factor by which the gascost should be multiplied, in order to reach the same G/S as `ecRecover`
    
