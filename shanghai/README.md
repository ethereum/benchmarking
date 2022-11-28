
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
