# Benchmark summary

## Benchmarking of precompiles for Go Ethereum

### Direct execution

| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | ----- | ----- | ----- | ----- | ----- |
| PrecompiledPointEvaluation/pointEvaluation1 | 50000.0 |     1064815.00 | 46.956513572780246 | 10648.15 | 67319.50181235775 |
| PrecompiledPointEvaluationFail/fuzzcorp-95 | 50000.0 |     1681335.00 | 29.73827345531973 | 16813.350000000002 | 106296.99485796173 |
| PrecompiledPointEvaluation/pointEvaluation1 | 50000.0 |     1221399.00 | 40.93666361279156 | 12213.990000000002 | 67806.52861822018 |
| PrecompiledPointEvaluationFail/fuzzcorp-33 | 50000.0 |     1679904.00 | 29.763605539364153 | 16799.04 | 93260.64508965747 |
| sha256 | 108.0 |         566.00 | 190.812720848 | 5.66 | 12.4700732929 |
| ripemd | 1080.0 |         791.00 | 1365.36030341 | 7.91 | 17.4272579058 |
| identity | 27.0 |          94.00 | 287.234042553 | 0.94 | 2.07100157161 |
| modexp_nagydani_1_qube | 204.0 |        9388.00 | 21.7298679165 | 93.88 | 206.835773982 |
| alt_bn128_add_cdetrio12 | 500.0 |       16894.00 | 29.596306381 | 168.94 | 372.207452668 |
| alt_bn128_mul_cdetrio11 | 40000.0 |      748248.00 | 53.4582117159 | 7482.48 | 16485.3487655 |
| alt_bn128_pairing_ten_point_match_1 | 900000.0 |    96298039.00 | 9.34598470899 | 962980.39 | 2121631.8097 |
| Modexp | 204 | 33.57 | 93.88 | 63.31 | 206.83| 
| ecAdd  | 500 | 144.85 | 168.94 |273.17 |372.21 | 
| ecMul  | 40K | 1.0K | 7.5K | 2.0 K | 16.5K|
| Pairing | 900K | 118.6K | 963.0K | 223.7K| 2.1M | 

### Bytecode execution

| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | ----- | ----- | ----- | ----- | ----- |

## Benchmarking of precompiles for Nethermind

### Direct execution

| Benchmark | Test Name | Nominal Gas Cost | Time (ns) | Memory Allocations per Op | Gascost for ECDSA eq |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Blake2fBenchmark | blake2f/current\input_param_scalar_1_gas_1.csv | 1 | 52.41456826527914 | 88 | 1.72945 |
| Bn256AddBenchmark | bnadd/current\input_param_scalar_0_gas_150.csv | 150 | 3061.6822560628257 | 88 | 101.805 |
| Bn256MulBenchmark | bnmul/current\input_param_scalar_0_gas_6000.csv | 6000 | 136026.806640625 | 88 | 4524.05 |
| Bn256PairingBenchmark | bnpair/current\input_param_scalar_1_gas_79000.csv | 79000 | 1871716.6666666667 | 273 | 62250.8 |
| Bn256PairingBenchmark | bnpair/current\input_param_scalar_2_gas_113000.csv | 113000 | 3226674.1536458335 | 466 | 107315 |
| Bn256PairingBenchmark | bnpair/current\input_param_scalar_4_gas_181000.csv | 181000 | 5370053.125 | 851 | 178601 |
| Bn256PairingBenchmark | bnpair/current\input_param_scalar_8_gas_317000.csv | 317000 | 9814219.270833334 | 1622 | 326408 |
| EcRecoverBenchmark | ValidKey | 3000 | 90202.16878255208 | 424 | 3000 |
| PointEvaluationBenchmark | fuzzcorp-33 | 50000 | 1297860.9049479167 | 185 | 43165.1 |
| PointEvaluationBenchmark | fuzzcorp-95 | 50000 | 1285252.8645833333 | 185 | 42745.8 |
| PointEvaluationBenchmark | pointEvaluation1 | 50000 | 1267637.890625 | 185 | 42159.9 |
| RipEmdBenchmark | ripemd/current\input_param_scalar_0_gas_600.csv | 600 | 250.75278282165527 | 296 | 8.31467 |
| RipEmdBenchmark | ripemd/current\input_param_scalar_104_gas_1080.csv | 1080 | 487.2129758199056 | 424 | 16.197 |
| RipEmdBenchmark | ripemd/current\input_param_scalar_136_gas_1200.csv | 1200 | 682.2342872619629 | 456 | 22.6824 |
| RipEmdBenchmark | ripemd/current\input_param_scalar_256_gas_1560.csv | 1560 | 1103.550910949707 | 576 | 36.6843 |
| RipEmdBenchmark | ripemd/current\input_param_scalar_56_gas_840.csv | 840 | 528.6629358927408 | 376 | 17.5606 |
| RipEmdBenchmark | ripemd/current\input_param_scalar_96_gas_960.csv | 960 | 578.3408164978027 | 416 | 19.2235 |
| Sha256Benchmark | sha256/current\input_param_scalar_0_gas_60.csv | 60 | 200.62966346740723 | 112 | 6.65174 |
| Sha256Benchmark | sha256/current\input_param_scalar_104_gas_108.csv | 108 | 252.48346328735352 | 240 | 8.38119 |
| Sha256Benchmark | sha256/current\input_param_scalar_256_gas_156.csv | 156 | 393.0237293243408 | 392 | 13.0707 |

### Bytecode execution

| Benchmark | Test Name | Nominal Gas Cost | Time (ns) | Memory Allocations per Op | Gascost for ECDSA eq |
| ----- | ----- | ----- | ----- | ----- | ----- |

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
