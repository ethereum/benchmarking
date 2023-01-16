# Benchmark summary

## Benchmarking of precompiles for Go Ethereum

### Direct execution

| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | -----: | -----: | -----: | -----: | -----: |
| PointEvaluation/pointEvaluation1 | 50000 |     1064815.00 | 46.95 | 10648.15 | 67319.50 |
| PointEvaluation/fuzzcorp-33 | 50000 |     1679904.00 | 29.76 | 16799.04 | 93260.64 |
| PointEvaluation/fuzzcorp-95 | 50000 |     1681335.00 | 29.73 | 16813.35 | 106296.99 |
| sha256 | 108 |         566.00 | 190.81 | 5.66 | 12.47 |
| ripemd | 1080 |         791.00 | 1365.36 | 7.91 | 17.42 |
| identity | 27 |          94.00 | 287.23 | 0.94 | 2.07 |
| modexp_nagydani_1_qube | 204 |        9388.00 | 21.72 | 93.88 | 206.83 |
| alt_bn128_add_cdetrio12 | 500 |       16894.00 | 29.59 | 168.94 | 372.20 |
| alt_bn128_mul_cdetrio11 | 40000 |      748248.00 | 53.45 | 7482.48 | 16485.34 |
| alt_bn128_pairing_ten_point_match_1 | 900000 |    96298039.00 | 9.34 | 962980.39 | 2121631.80 |
| Modexp | 204 | 33.57 | 93.88 | 63.31 | 206.83| 
| ecAdd  | 500 | 144.85 | 168.94 |273.17 |372.21 | 
| ecMul  | 40K | 1.0K | 7.5K | 2.0 K | 16.5K|
| Pairing | 900K | 118.6K | 963.0K | 223.7K| 2.1M | 

### Bytecode execution

| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | -----: | -----: | -----: | -----: | -----: |
| PointEvaluation/pointEvaluation1 | 50000 |     1387521.00 | 46.95 | 10648.15 | 42280.55 |
| PointEvaluation/fuzzcorp-33 | 50000 |     1790043.00 | 29.76 | 16799.04 | 54546.21 |
| PointEvaluation/fuzzcorp-95 | 50000 |     1861553.00 | 29.73 | 16813.35 | 58545.21 |
| EcRecover | 3000 |     98451.00 | 29.76 | 16799.04 | 3000.00 |

## Benchmarking of precompiles for Nethermind

### Direct execution

| Benchmark | Test Name | Nominal Gas Cost | Time (ns) |GC Ops | Memory Allocations per Op | Gascost for ECDSA eq |
| ----- | ----- | -----: | -----: | -----: | -----: | -----: |
Blake2fBenchmark          | input_param_scalar_1_gas_1                        | 1           | 52  | 16777216               | 88                  | 1.72 |
Bn256AddBenchmark         | input_param_scalar_0_gas_150                    | 150         | 3061    | 262144               | 88                | 101.80 |  
Bn256MulBenchmark         | input_param_scalar_0_gas_6000                  | 6000       | 136026      | 4096               | 88               | 4524.05 | 
Bn256PairingBenchmark     | input_param_scalar_1_gas_79000                | 45000      | 1871716       | 512              | 273              | 62250.80 | 
Bn256PairingBenchmark     | input_param_scalar_2_gas_113000               | 45000      | 3226674       | 256              | 466             | 107315.00 |   
Bn256PairingBenchmark     | input_param_scalar_4_gas_181000               | 45000      | 5370053       | 128              | 851             | 178601.00 |    
Bn256PairingBenchmark     | input_param_scalar_8_gas_317000               | 45000      | 9814219        | 64             | 1622             | 326408.00 | 
EcRecoverBenchmark        | ValidKey                                           | 3000        | 90202      | 8192              | 424               | 3000.00 |
PointEvaluationBenchmark  | fuzzcorp-33                                       | 50000      | 1297860       | 512              | 185              | 43165.10 |
PointEvaluationBenchmark  | fuzzcorp-95                                       | 50000      | 1285252       | 512              | 185              | 42745.80 |
PointEvaluationBenchmark  | pointEvaluation1                                  | 50000      | 1267637       | 512              | 185              | 42159.90 |
RipEmdBenchmark           | input_param_scalar_0_gas_600                    | 600          | 250   | 2097152              | 296                  | 8.31 |
RipEmdBenchmark           | input_param_scalar_104_gas_1080                 | 600          | 487   | 1048576              | 424                 | 16.19 |
RipEmdBenchmark           | input_param_scalar_136_gas_1200                 | 600          | 682   | 1048576              | 456                 | 22.68 |
RipEmdBenchmark           | input_param_scalar_256_gas_1560                 | 600         | 1103    | 524288              | 576                 | 36.68 |
RipEmdBenchmark           | input_param_scalar_56_gas_840                   | 600          | 528   | 2097152              | 376                 | 17.56 |
RipEmdBenchmark           | input_param_scalar_96_gas_960                   | 600          | 578   | 1048576              | 416                 | 19.22 |
Sha256Benchmark           | input_param_scalar_0_gas_60                      | 60          | 200   | 2097152              | 112                  | 6.65 |
Sha256Benchmark           | input_param_scalar_104_gas_108                   | 60          | 252   | 2097152              | 240                  | 8.38 |
Sha256Benchmark           | input_param_scalar_256_gas_156                   | 60          | 393   | 2097152              | 392                 | 13.07 |
### Bytecode execution

| Benchmark | Test Name | Nominal Gas Cost | Time (ns) | GC Ops | Memory Allocations per Op | Gascost for ECDSA eq |
| ----- | ----- | -----: | -----: | -----: |  -----: | -----: |
Bn256AddBenchmark         | Bn256Add-Valid                   | 150        | 30066         | 1            | 39056                  | 769.60| 
Bn256MulBenchmark         | Bn256Mul-Valid                  | 6000       | 199800         | 1            | 39056                 | 5114.33 | 
Bn256PairingBenchmark     | Bn256Pairing-1                 | 79000      | 2073766         | 1            | 39488                | 53082.70| 
Bn256PairingBenchmark     | Bn256Pairing-2                | 113000      | 2943733         | 1            | 40216                | 75351.50| 
Bn256PairingBenchmark     | Bn256Pairing-4                | 181000      | 4791966         | 1            | 41648               | 122661.00| 
Bn256PairingBenchmark     | Bn256Pairing-8                | 317000      | 8659133         | 1            | 44488               | 221650.00| 
EcRecover                 | ValidKey                        | 3000       | 117200         | 1            | 39360               |   3000.00| 
PointEvaluationBenchmark  | pointEvaluation1               | 50000      | 1551533         | 1            | 39408                | 39715.00| 

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
