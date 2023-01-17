# Benchmark summary

Please see [the specification](spec.md) for the details of how the results were obtained.

## Benchmarking of precompiles for Go Ethereum

### Direct execution

| Test Name | Time (ns) | Nominal Gas Cost | Bytes Alloc | Alloc Ops |  Calculated Gas Cost  |
| ----- | -----: | -----: | -----: | -----: | -----: |
| Bn256Add/chfast1-Gas=150 | 10856 | 150 | 784 | 16 |  667.36  |
| Bn256ScalarMul/chfast1-Gas=6000 | 101224 | 6000 | 1288 | 26 |  6,222.66  |
| Bn256Pairing/one_point-Gas=79000 | 1634297 | 79000 | 55328 | 501 |  100,467.02  |
| Bn256Pairing/jeff1-Gas=113000 | 2585591 | 113000 | 103952 | 980 |  158,947.01  |
| Ecrecover/-Gas=3000 | 48801 | 3000 | 800 | 7 |  3,000.00  |
| PointEvaluation/fuzzcorp-33-Gas=50000 | 148135 | 50000 | 19917 | 143 |  9,106.47  |
| PointEvaluation/fuzzcorp-95-Gas=50000 | 146953 | 50000 | 19918 | 143 |  9,033.81  |
| PointEvaluation/pointEvaluation1-Gas=50000 | 1241289 | 50000 | 54864 | 352 |  76,307.19  |
| RipeMD/128-Gas=1080 | 831.3 | 1080 | 56 | 2 |  51.10  |
| Sha256/128-Gas=108 | 449.3 | 108 | 32 | 1 |  27.62  |

### Bytecode execution

| Test Name | Time (ns) | Nominal Gas Costt | Bytes Alloc | Alloc Ops | Calculated Gas Cost |
| ----- | -----: | -----: | -----: | -----: | -----: |
| Bn256Add/Bn256Add-Valid-16              | 25702 | 150 | 7833 | 88 | 1091.99 |
| Bn256Mul/Bn256Mul-Valid-16              | 94660 | 6000 | 8503 | 100 | 4021.80 |
| Bn256Pairing/Bn256Pairing-1-16                    | 1386028 | 79000 | 62865 | 574 | 58888.03 |
| Bn256Pairing/Bn256Pairing-2-16                    | 2133691 | 113000 | 112578 | 1053 | 90653.91 |
| Bn256Pairing/Bn256Pairing-4-16                    | 3573289 | 181000 | 211840 | 2009 | 151817.97 |
| Bn256Pairing/Bn256Pairing-8-16                    | 6292710 | 317000 | 411862 | 3917 | 267357.73 |
| EcRecover/ValidKey-16                   | 70610 | 3000 | 7818 | 79 | 3000.00 |
| PointEvaluation/fuzzcorp-33-16                   | 168642 | 50000 | 27414 | 216 | 7165.07 |
| PointEvaluation/fuzzcorp-95-16                   | 169987 | 50000 | 27418 | 216 | 7222.22 |
| PointEvaluation/pointEvaluation1-16              | 1023690 | 50000 | 62386 | 425 | 43493.41 |
| RipeMd/scalar_128-16                            | 13937 | 1080 | 7136 | 74 | 592.13 |
| RipeMd/scalar_256-16                            | 16455 | 1560 | 7682 | 75 | 699.12 |
| Sha256/scalar_128-16                            | 13660 | 108 | 7047 | 73 | 580.37 |
| Sha256/scalar_256-16                            | 15498 | 156 | 7658 | 74 | 658.46 |

## Benchmarking of precompiles for Nethermind

### Direct execution

 Benchmark                | Name                                |   Nominal Gas Cost |   Time (ns) |   GC Ops |   Mem Alloc Ops |   Gas Cost for ECDSA eq |
|--------------------------|-------------------------------------|--------------------|-------------|----------|-----------------|-------------------------|
| Bn256AddBenchmark        | input_param_scalar_0_gas_150.csv    |                150 |        3464 |   262144 |              88 |                  136.52 |
| Bn256MulBenchmark        | input_param_scalar_0_gas_6000.csv   |               6000 |      119836 |     4096 |              88 |                 4722.79 |
| Bn256PairingBenchmark    | input_param_scalar_1_gas_79000.csv  |              79000 |     1916127 |      512 |             273 |                75515.37 |
| Bn256PairingBenchmark    | input_param_scalar_2_gas_113000.csv |             113000 |     2826827 |      256 |             466 |               111406.44 |
| Bn256PairingBenchmark    | input_param_scalar_4_gas_181000.csv |             181000 |     4609362 |      128 |             851 |               181656.89 |
| Bn256PairingBenchmark    | input_param_scalar_8_gas_317000.csv |             317000 |     8305799 |       64 |            1622 |               327335.03 |
| EcRecoverBenchmark       | ValidKey                            |               3000 |       76122 |     8192 |             424 |                 3000.00 |
| PointEvaluationBenchmark | fuzzcorp-33                         |              50000 |     1727717 |      256 |             186 |                68090.05 |
| PointEvaluationBenchmark | fuzzcorp-95                         |              50000 |     1386740 |      512 |             185 |                54652.01 |
| PointEvaluationBenchmark | pointEvaluation1                    |              50000 |     1428931 |      512 |             185 |                56314.77 |
| RipEmdBenchmark          | input_param_scalar_128_gas_1080.csv |               1080 |         766 |  1048576 |             448 |                   30.19 |
| RipEmdBenchmark          | input_param_scalar_256_gas_1560.csv |               1560 |        1092 |   524288 |             576 |                   43.04 |
| Sha256Benchmark          | input_param_scalar_128_gas_108.csv  |                108 |         319 |  2097152 |             264 |                   12.57 |
| Sha256Benchmark          | input_param_scalar_256_gas_156.csv  |                156 |         375 |  2097152 |             392 |                   14.78 |

### Bytecode execution

| Benchmark | Test Name | Nominal Gas Cost | Time (ns) | GC Ops | Memory Allocations per Op | Calculated Gas Cost |
| ----- | ----- | -----: | -----: | -----: |  -----: | -----: |
| Bn256Add        | Bn256Add-Valid   |                150 |       32566 |        1 |           39056 |                  796.88 |
| Bn256Mul        | Bn256Mul-Valid   |               6000 |      206333 |        1 |           39056 |                 5048.93 |
| Bn256Pairing    | Bn256Pairing-1   |              79000 |     2029600 |        1 |           39488 |                49663.95 |
| Bn256Pairing    | Bn256Pairing-2   |             113000 |     3083266 |        1 |       40216     |                75446.97 |
| Bn256Pairing    | Bn256Pairing-4   |             181000 |     5062600 |        1 |           41648 |               123880.91 |
| Bn256Pairing    | Bn256Pairing-8   |             317000 |     8395966 |        1 |      44488      |               205447.78 |
| EcRecover       | ValidKey         |               3000 |      122600 |        1 |           39360 |                 3000.00 |
| PointEvaluation | fuzzcorp-33      |              50000 |     1514400 |        1 |           39344 |                37057.10 |
| PointEvaluation | fuzzcorp-95      |              50000 |     1533866 |        1 |      39344      |                37533.43 |
| PointEvaluation | pointEvaluation1 |              50000 |     1459833 |        1 |           39408 |                35721.85 |
| RipeMd          | scalar_128       |               1080 |       38233 |        1 |           39264 |                  935.55 |
| RipeMd          | scalar_256       |               1560 |       44533 |        1 |           39792 |                 1089.71 |
| Sha256          | scalar_128       |                108 |       40466 |        1 |           39200 |                  990.20 |
| Sha256          | scalar_256       |                156 |       35833 |        1 |           39608 |                  876.83 |

## Benchmarking of precompiles for Erigon

### Direct execution

| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | -----: | -----: | -----: | -----: | -----: |
| PointEvaluation/pointEvaluation1 | 50000 |     1145540.00 | 43.64 | 11455.4 | 58717.30 |
| PointEvaluation/fuzzcorp-33 | 50000 |     164363.00 | 304.205 | 1643.63 | 8424.84 |
| PointEvaluation/fuzzcorp-95 | 50000 |     164240.00 | 304.433| 1642.4 | 8418.53 |
| PrecompiledSha256/128 | 108 |         526.1 | 205.284 | 12.5 | 26.96 |
| PrecompiledRipeMD/128 | 1080 |         1250 | 864 | 7.91 | 64.07 |
| PrecompiledIdentity/128 | 27 |          8.76 | 3081.84 |  0.08761 | 0.44 |
| PrecompiledModExp/nagydani-1-qube | 204 |        1704 | 119.718 | 17.04 | 87.34 |
| PrecompiledBn256Add/cdetrio12 | 150 |       11860 | 12.6476 | 118.6 | 607.91 |
| PrecompiledBn256ScalarMul/cdetrio11 | 6000 |      85425 | 70.2371 | 854.25 | 4378.67 |
| PrecompiledBn256Pairing/ten_point_match_1 | 385000 |    9107850 | 41.7641 | 92184.5 | 472515.00 |
| PrecompiledBlake2F/vector_7 | 1 |    90.96 | 10.9938 |0.9096 | 4.66 |

## Conclusions

## Benchmarking of pointevaluation precompile for EIP-4844

Benchmarked on go-ethereum@`50fed98730f6ddbb376936adc5149a1af1644c0d` , branch `eip-4844`.

The two benchmark runs suggest that the `50K` gas for point evaluation should be `67K` for the evaluation of a correct case, but surprisingly there are worse cases where the verification does not pass. The `fuzzcorp-95` and `fuzzcorp-33` respectively uses more memory, and suggests that the price should be `106K` and `93k`.  

| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | ----- | ----- | ----- | ----- | ----- |
| PrecompiledPointEvaluation/pointEvaluation1 | 50000.0 |     1064815.00 | 46.956513572780246 | 10648.15 | 67319.50181235775 |
| PrecompiledPointEvaluationFail/fuzzcorp-95 | 50000.0 |     1681335.00 | 29.73827345531973 | 16813.350000000002 | 106296.99485796173 |
| PrecompiledPointEvaluation/pointEvaluation1 | 50000.0 |     1221399.00 | 40.93666361279156 | 12213.990000000002 | 67806.52861822018 |
| PrecompiledPointEvaluationFail/fuzzcorp-33 | 50000.0 |     1679904.00 | 29.763605539364153 | 16799.04 | 93260.64508965747 |

A conservative choice would be `100K`. 
