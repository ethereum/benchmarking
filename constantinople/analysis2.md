## About the benchmarks

These benchmarks are _relative_ benchmarks, which show two different relative measurements. 

1. Relative to the speed of the local machine it's executed on -- and showing "what should the optimal gasprice be, if we target `10 MGas/s`
. 
  * This is highly dependant on what hardware is used when running the test, and introduces questions about what the reference hardware should be. 
  * This is also difficult to compare cross-client, since the benchmarks may have been implemented differently. One client may do the benches with a full stack and EVM, while another may just run the raw
    operation directly on the input.
2. Relative to `ecRecover` -- showing "If ecrecover is assumed to be perfectly priced, what should the gasprice for this operation be?".
  * This measure is not _that_ dependant on the machine it's running on -- though there may be differences if e.g. one operation takes advantage of processor-specific assembly which has not been implemented on some other architecture, so the differences between opX and `ecRecover` are larger on other platforms. 

With that in mind, we can peek at the first measure, `PrecompiledEcRecover`:


| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | ----- | ----- | ----- | ----- | ----- |
| PrecompiledEcrecover/ | 3000.0 |      159077.00 | 18.8587916544 | 1590.77 | 3000.0 |


[Here](https://github.com/ethereum/benchmarking/blob/master/constantinople/processed/geth_20180714_mhswende.txt.md) are the full new benchmarks for Geth. 

The cost is `3000`, and it showed an excution time of `159ms`, which translates to `18.9 MGas/S`. So the first answer, if we aim for `10Mgas/s` is `1590 Gas`. 
The second result, if we want to target `ecRecover`, is (hardly surprising) a value of `3000`. If it had shown anything else, the calculations had been wrong. 


## Diving into the Geth benchmarks

| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | ----- | ----- | ----- | ----- | ----- |
| PrecompiledSha256/128 | 108.0 |         639.00 | 169.014084507 | 6.39 | 12.0507678671 |
| PrecompiledRipeMD/128 | 1080.0 |        2030.00 | 532.019704433 | 20.3 | 38.2833470583 |
| PrecompiledIdentity/128 | 27.0 |          17.20 | 1569.76744186 | 0.172 | 0.324371216455 |


The basic ones shows that all three are heavily overpriced, in terms of how CPU-intensive they are, compared to
`ecRecover`. 
Moving along to the newer ones, there are quite a lot of benchmarks to choose from, but we're most interested
in the heaviest ones, with the lowest `MGas/S`. 


| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | ----- | ----- | ----- | ----- | ----- |
| PrecompiledModExp/nagydani-1-qube | 204.0 |        3357.00 | 60.7685433423 | 33.57 | 63.3089635837 |
| PrecompiledBn256Add/cdetrio12 | 500.0 |       14485.00 | 34.51846738 | 144.85 | 273.169597113 |
| PrecompiledBn256ScalarMul/cdetrio1 | 40000.0 |      108458.00 | 368.806358222 | 1084.58 | 2045.38682525 |
| PrecompiledBn256Pairing/ten_point_match_2 | 900000.0 |    11861035.00 | 75.8787070437 | 118610.35 | 223684.78787 |

* For `modexp`, we can see that the two results are `34` and `63` Gas respectively, whereas the actual cost was `204`. Which indicates that this precompile could be lowered, at least cut in half (from 204 gas to 102), and probably even more. 
* For `Bn256Add`, the 'actual' cost was `500`, but the two results were `145` and `273` respectively. This could likely be roughly halved. 
* For `ScalarMul`, the actual cost was `40K`, but the two results were `1084` and `2045` respectively. This indicates that it could be _heavily_ reduced, at least by a factor of 10, perhaps even by a factor of 20 (but that's probably stretching it). 
* For `Pairing`, the actual cost was `900K`, and the two results were `118K` and `224K` respectivly, indicating that the  pairing gas cost calculation could be roughly reduced by a factor of four. 

So far, this has focused solely on Geth. CPP has not changed the implementation since last benchmarking, and from what I understand - neither has Parity. So let's use the old benchmarks to check how they would fare. 


## Diving into the Parity benchmarks

Starting with the same basic ones:

| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | ----- | ----- | ----- | ----- | ----- |
| sha256 | 108.0 |         566.00 | 190.812720848 | 5.66 | 12.4700732929 |
| ripemd | 1080.0 |         791.00 | 1365.36030341 | 7.91 | 17.4272579058 |
| identity | 27.0 |          94.00 | 287.234042553 | 0.94 | 2.07100157161 |
 
 It's quite close to `geth` -- the Parity `ripeMD` is faster, but the `identity` is slower, and `sha256` is roughly equal between the two -- at least in comparison against `ecRecover` (both resulting in `12` gas).

Moving along to the newer ones: 

| Name | Gascost | Time (ns) | MGas/S | Gascost for 10MGas/S | Gascost for ECDSA eq |
| ----- | ----- | ----- | ----- | ----- | ----- |
| modexp_nagydani_1_qube | 204.0 |        9388.00 | 21.7298679165 | 93.88 | 206.835773982 |
| alt_bn128_add_cdetrio12 | 500.0 |       16894.00 | 29.596306381 | 168.94 | 372.207452668 |
| alt_bn128_mul_cdetrio11 | 40000.0 |      748248.00 | 53.4582117159 | 7482.48 | 16485.3487655 |
| alt_bn128_pairing_ten_point_match_1 | 900000.0 |    96298039.00 | 9.34598470899 | 962980.39 | 2121631.8097 |

* For `modexp`, the results are `94` and `206` -- indicating that modexp should _not_ be lowered, since it's already on par with `ecRecover`. Even in absolute time, the input vector is significantly slower on 
Parity, at `9388ns` versus `3357`.
  * There's a comment on the [old analysis](https://github.com/ethereum/benchmarking/blob/master/analysis.md):

> Parity does exponentiation by squaring currently, but plan to optimize it 
> Note2 : CPP seems extremely slow on nagydany-1-qube.

* For `Bn256add`, the results are `168` and `372`, which indicates that a lowering from 500 to around 400 should not be a problem. 
* For `ScalarMul`, results are `7582` and `16.5K`, which should allow a lowering of `gasCost` (from 40K) by a factor of around 2.5. 
* For `Pairing`, the actual cost was `900K`, and the two results are `962K` and `2.1M` respectively. This indicates that the pairing precompile is already _underpriced_ on Parity. A `900K` input vector took `11ms` on Geth, but `93ms` on Parity. 


## Summary

In the chart below, 

* `#1` means the first (hardware-dependant) measure against `10Mgas/s` on my local laptop. 
* `#2` means the second measure, relative against `ecrecover`. 

| Precompile | Cost (now) | Geth #1| Parity #1 | Geth #2 | Parity #2|  
| --- | --- | --- | --- | --- | --- |
| Modexp | 204 | 33.57 | 93.88 | 63.31 | 206.83| 
| ecAdd  | 500 | 144.85 | 168.94 |273.17 |372.21 | 
| ecMul  | 40K | 1.0K | 7.5K | 2.0 K | 16.5K|
| Pairing | 900K | 118.6K | 963.0K | 223.7K| 2.1M | 

