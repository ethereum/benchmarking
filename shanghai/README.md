# Method
The benchmark tests were executed on the main EVM clients: Go Ethereum, Nethermind, Erigon and Besu.


There are two main execution sets for each client: direct and bytecode. The direct approach calls a method to load the appropriate library and then executes it with the given parameters. The bytecode approach achieves the same but from the EVM machine. It executes the opcodes that load parameters to the EVM memory and then call the appropriate 'precompile'. That in turn calls a method to load the library and execute it with the given parameters. The effect of the two executions is the same, but with the bytecode approach we also count in any EVM machine overhead. The validity of the call parameters has been proved in unit tests, so there is no need to duplicate it in the benchmark tests.

Please see [the specification](spec.md) for the details of how the benchmarks were executed.

The benchmark method minimizes the impact of undesirable factors like: caching, warming up, memory management, library management, etc. Still the actual results, measured in nanoseconds, very much depend on the underlying CPU. To make the results comparable between different hardware setups, they are all normalized to a common base. As the base we chose EC Recover function. For each benchmark we have two gas costs:
-	Nominal: declared in the current EVM specification
-	Calculated: relative to EC Recover


# Benchmark results

In the direct approach, for each client we executed similar tests, as much as possible. 
Bytecode execution guarantees that each test is identical across clients.

The `Nominal Gas Cost` column shows declared gas cost as per the EVM current specification. The `Calculated Gas Cost` shows the figure relative to EC Recovery benchmark.

Where possible we gathered stats on memory bytes allocated, memory allocation operations and garbage collector (GC) operations.

## Benchmarking of precompiles for Go Ethereum

### Direct execution

| Test Name | Time (ns) | Nominal Gas Cost | Bytes Alloc | Mem Alloc Ops |  Calculated Gas Cost  |
| ----- | -----: | -----: | -----: | -----: | -----: |
| Bn256Add/chfast1 | 10856 | 150 | 784 | 16 |  667.36  |
| Bn256ScalarMul/chfast1 | 101224 | 6000 | 1288 | 26 |  6,222.66  |
| Bn256Pairing/one_point | 1634297 | 79000 | 55328 | 501 |  100,467.02  |
| Bn256Pairing/jeff1 | 2585591 | 113000 | 103952 | 980 |  158,947.01  |
| Ecrecover/ValidKey | 48801 | 3000 | 800 | 7 |  3,000.00  |
| PointEvaluation/fuzzcorp-33 | 148135 | 50000 | 19917 | 143 |  9,106.47  |
| PointEvaluation/fuzzcorp-95 | 146953 | 50000 | 19918 | 143 |  9,033.81  |
| PointEvaluation/pointEvaluation1 | 1241289 | 50000 | 54864 | 352 |  76,307.19  |
| RipeMD/128 | 831.3 | 1080 | 56 | 2 |  51.10  |
| Sha256/128 | 449.3 | 108 | 32 | 1 |  27.62  |

### Bytecode execution

| Test Name | Time (ns) | Nominal Gas Costt | Bytes Alloc | Mem Alloc Ops | Calculated Gas Cost |
| ----- | -----: | -----: | -----: | -----: | -----: |
| Bn256Add/Bn256Add-Valid              | 25702 | 150 | 7833 | 88 | 1091.99 |
| Bn256Mul/Bn256Mul-Valid              | 94660 | 6000 | 8503 | 100 | 4021.80 |
| Bn256Pairing/Bn256Pairing-1                    | 1386028 | 79000 | 62865 | 574 | 58888.03 |
| Bn256Pairing/Bn256Pairing-2                    | 2133691 | 113000 | 112578 | 1053 | 90653.91 |
| Bn256Pairing/Bn256Pairing-4                    | 3573289 | 181000 | 211840 | 2009 | 151817.97 |
| Bn256Pairing/Bn256Pairing-8                    | 6292710 | 317000 | 411862 | 3917 | 267357.73 |
| EcRecover/ValidKey                   | 70610 | 3000 | 7818 | 79 | 3000.00 |
| PointEvaluation/fuzzcorp-33                   | 168642 | 50000 | 27414 | 216 | 7165.07 |
| PointEvaluation/fuzzcorp-95                   | 169987 | 50000 | 27418 | 216 | 7222.22 |
| PointEvaluation/pointEvaluation1              | 1023690 | 50000 | 62386 | 425 | 43493.41 |
| RipeMd/scalar_128                            | 13937 | 1080 | 7136 | 74 | 592.13 |
| RipeMd/scalar_256                            | 16455 | 1560 | 7682 | 75 | 699.12 |
| Sha256/scalar_128                            | 13660 | 108 | 7047 | 73 | 580.37 |
| Sha256/scalar_256                            | 15498 | 156 | 7658 | 74 | 658.46 |

## Benchmarking of precompiles for Nethermind

### Direct execution

| Benchmark | Test Name | Nominal Gas Cost | Time (ns) | GC Ops | Mem Alloc Ops | Calculated Gas Cost |
| ----- | ----- | -----: | -----: | -----: |  -----: | -----: |
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

| Benchmark | Test Name | Nominal Gas Cost | Time (ns) | GC Ops | Mem Alloc Ops | Calculated Gas Cost |
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

Note : The benchmark method fails to correctly detect Garbage Collector operations for the bytecode execution. 

## Benchmarking of precompiles for Erigon

### Direct execution

| Test Name | Time (ns) | Nominal Gas Cost | Bytes Alloc | Mem Alloc Ops |  Calculated Gas Cost  |
| ----- | -----: | -----: | -----: | -----: | -----: |
| Bn256Add/chfast1 | 13464 | 150 | 784 | 16 | 799.80 |
| Bn256ScalarMul/chfast1 |  242829 | 6000 | 1288 | 26 | 14424.91 |
| Bn256Pairing/one_point | 1791231 | 79000 | 55328 | 501 | 106405.54 |
| Bn256Pairing/jeff1 |    7546857 | 113000 | 103952 | 980 | 448310.38 |
| EcrecoverValidKey/ValidKey | 50502 | 3000 | 224 | 4 | 3000.00 |
| PointEvaluationFail/fuzzcorp-33 | 202165 | 50000 | 19908 | 143 | 12009.32 |
| PointEvaluationFail/fuzzcorp-95 | 674431 | 50000 | 19908 | 143 | 40063.62 |
| PointEvaluation/pointEvaluation1 |  1290697 | 50000 | 54864 | 352 | 76672.03 |
| Sha256/128 | 545.7 | 108 | 32 | 1 | 32.41 |
| RipeMD/128 | 1075 | 1080 | 56 | 2 | 63.85 |

### Bytecode execution

| Test Name | Time (ns) | Nominal Gas Costt | Bytes Alloc | Mem Alloc Ops | Calculated Gas Cost |
| ----- | -----: | -----: | -----: | -----: | -----: |
| Bn256Add/Bn256Add-Valid | 30550 | 150 | 5584 | 92 |  1,189.84  |
| Bn256Mul/Bn256Mul-Valid | 135819 | 6000 | 6216 | 104 |  5,289.79  |
| Bn256Pairing/Bn256Pairing-1 | 1661813 | 79000 | 60314 | 578 |  64,723.27  |
| Bn256Pairing/Bn256Pairing-2 | 2731387 | 113000 | 109967 | 1057 |  106,380.37  |
| Bn256Pairing/Bn256Pairing-4 | 4194409 | 181000 | 209188 | 2012 |  163,361.25  |
| Bn256Pairing/Bn256Pairing-8 | 8348450 | 317000 | 409112 | 3920 |  325,150.27  |
| EcRecover/ValidKey | 77027 | 3000 | 4884 | 80 |  3,000.00  |
| PointEvaluation/fuzzcorp-33 | 205447 | 50000 | 24743 | 219 |  8,001.62  |
| PointEvaluation/fuzzcorp-95 | 210143 | 50000 | 24740 | 219 |  8,184.52  |
| PointEvaluation/pointEvaluation1 | 1293137 | 50000 | 59885 | 429 |  50,364.30  |
| Sha256/scalar_128 | 16919 | 108 | 4714 | 77 |  658.95  |
| Sha256/scalar_256 | 18704 | 156 | 5322 | 78 |  728.47  |
| RipeMd/scalar_128 | 16903 | 1080 | 4867 | 78 |  658.33  |
| RipeMd/scalar_256 | 19706 | 1560 | 5337 | 79 |  767.50  |


# Client comparison

This chart compares bytecode executions from different clients.

| Test | Nominal Gas Cost | Geth Time (ns) | Geth Gas | Nethermind Time (ns) | Nethermind Gas | Erigon Time (ns) | Erigon Gas | Besu Time (ns) | Besu Gas |
| ----- | -----: | -----: | -----: | -----: | -----: | -----: | -----: | -----: | -----: |
 |  Bn256Add/Bn256Add-Valid              | 150 | 25702 | 1091.99 | 32566 | 796.88 | 30550 | 1189.84 |  |  | 
 |  Bn256Mul/Bn256Mul-Valid              | 6000 | 94660 | 4021.8 | 206333 | 5048.93 | 135819 | 5289.79 |  |  | 
 |  Bn256Pairing/Bn256Pairing-1          | 79000 | 1386028 | 58888.03 | 2029600 | 49663.95 | 1661813 | 64723.26 |  |  |  
 |  Bn256Pairing/Bn256Pairing-2          | 113000 | 2133691 | 90653.91 | 3083266 | 75446.97 | 2731387 | 106380.37 |  |  |  
 |  Bn256Pairing/Bn256Pairing-4          | 181000 | 3573289 | 151817.97 | 5062600 | 123880.91 | 4194409 | 163361.25 |  |  |  
 |  Bn256Pairing/Bn256Pairing-8          | 317000 | 6292710 | 267357.73 | 8395966 | 205447.78 | 8348450 | 325150.27 |  |  |  
 |  EcRecover/ValidKey                   | 3000 | 70610 | 3000 | 122600 | 3000 | 77027 | 3000.00 |  |  |  
 |  PointEvaluation/fuzzcorp-33          | 50000 | 168642 | 7165.07 | 1514400 | 37057.1 | 205447 | 8001.62 |  |  |  
 |  PointEvaluation/fuzzcorp-95          | 50000 | 169987 | 7222.22 | 1533866 | 37533.43 | 210143 | 8184.51 |  |  |  
 |  PointEvaluation/pointEvaluation1     | 50000 | 1023690 | 43493.41 | 1459833 | 35721.85 | 1293137 | 50364.30 |  |  |  
 |  RipeMd/scalar_128                    | 1080 | 13937 | 592.13 | 38233 | 935.55 | 16903 | 658.32 |  |  |  
 |  RipeMd/scalar_256                    | 1560 | 16455 | 699.12 | 44533 | 1089.71 | 19706 | 767.49 |  |  |  
 |  Sha256/scalar_128                    | 108 | 13660 | 580.37 | 40466 | 990.2 | 16919 | 658.95 |  |  |  
 |  Sha256/scalar_256                    | 156 | 15498 | 658.46 | 35833 | 876.83 | 18704 | 728.47 |  |  |  


# Conclusions

Most precompiles seem to be relatively well priced. There is no strong urge to update the gas cost immediately. This should be monitored and the benchmarks replicated for each major version.

There are some interesting differences between clients. For example, Point Evaluation precompile fail tests execute much faster on Geth and Erigon (see PointEvaluation/fuzzcorp-33 and PointEvaluation/fuzzcorp-95). This may be due to the underlying library version used in Nethermind.

Also, Nethermind has a bit higher engine overhead, clearly visible for lower priced benchmarks like RipeMd or Sha256. The reason for this could be the benchmark method used, or some inefficiency in the way a call is handled. To be investigated.
