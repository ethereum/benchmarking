#!/usr/bin/python

import sys, re
from tabulate import tabulate


precompiledRegexp = re.compile("test (\S*)\s+\.\.\. bench:\s+([\d,]+) ns/iter.*") 

def getGas(precompile):

    gasLookupTable = {
        "ecrecover" :3000 , 
        "bn_128_add" : 500 , 
        "bn_128_mul" : 2000 , 
        "modexp_1_pow0x10001" : 655,
        "modexp_1_qube" :      40,
        "modexp_1_square" :     40,
        "modexp_2_pow0x10001" :     2129,
        "modexp_2_qube" :     133,
        "modexp_2_square" :    133,
        "modexp_3_pow0x10001" :     6062,
        "modexp_3_qube" :     378,
        "modexp_3_square" :    378,
        "modexp_4_pow0x10001" :   17858 ,
        "modexp_4_qube" :    1116,
        "modexp_4_square" :   1116,
        "modexp_5_pow0x10001" :    57180,
        "modexp_5_qube" :    3573,
        "modexp_5_square" :   3573,
        "sha256"        : 3132,

    }
    if precompile in gasLookupTable.keys():
        return gasLookupTable[precompile]

    return float(1)


def calc(line):
    for exp in [precompiledRegexp]:#, opRegexp]:
        m = exp.search(line)
        if m:
            (name,  ns) = ( m.group(1),  m.group(2))
            return {"name" : name, "gas": float(getGas(name)), "ns" : float(ns.replace(",",""))}


def postprocess(f):
    items = []
    lines = f.split("\n")
    #Do first pass and find the values for the ecdsarecover
    idealMGasPerS = 10


    for l in lines:
        out = calc(l)
        if out:
            if out['name'].find("ecrecover") >= 0:
                ecdsaMGperS = 1000* out['gas']/out['ns']
                #print("Ecdsarecover at %f Mgas/s" %  ecdsaMGperS ) 
                ecdsaTime = out['ns']
                ecdsaGas = out['gas']

    for l in lines:
        out =  calc(l)
        if out:
            name = out['name']
            gas = out['gas']
            timeNs = out['ns']
            

            timeS = timeNs * 1e-9
            gasPerNs = float(gas) / float(timeNs)
            gasPerS = 1e+9 * gasPerNs
            MgasPerS = gasPerS / 1e+6
            
            forEcdsaGasPrice  = ecdsaMGperS * 1e6 * timeS
            for10MGPSGasPrice = idealMGasPerS * 1e6 * timeS


            item = [name, gas, "%14.02f" % float(timeNs),  MgasPerS, for10MGPSGasPrice , forEcdsaGasPrice]
            #break
            items.append(item)
    print "```"
    print tabulate(items, headers=['Name', 'Gascost', 'Time (ns)', 'MGas/S', 'Gasprice for 10MGas/S','Gasprice for ECDSA eq'])
    print "```"
    print """
Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gasprice for 10MGas/S` shows what the gasprice should have been, in order to reach 10 MGas/second
* `Gasprice for ECDSA eq` shows what the gasprice should have been, in order to have the same cost/cycle as ecRecover
    """

def test():
    t = """
#cat /proc/cpuinfo | grep "model name"| head
model name  : Intel(R) Core(TM) i7-4700MQ CPU @ 2.40GHz

     Running /data/workspace/parity/target/release/deps/evm-738e2c687970dbef

running 20 tests
test bn_128_add          ... bench:      11,291 ns/iter (+/- 390)
test bn_128_mul          ... bench:     683,165 ns/iter (+/- 24,812)
test bn_128_pairing      ... bench:   7,500,475 ns/iter (+/- 214,431)
test ecrecover           ... bench:     143,070 ns/iter (+/- 4,080)
test modexp_1_pow0x10001 ... bench:      69,577 ns/iter (+/- 4,967)
test modexp_1_qube       ... bench:      12,746 ns/iter (+/- 343)
test modexp_1_square     ... bench:       9,005 ns/iter (+/- 417)
test modexp_2_pow0x10001 ... bench:     178,520 ns/iter (+/- 7,649)
test modexp_2_qube       ... bench:      30,359 ns/iter (+/- 1,987)
test modexp_2_square     ... bench:      20,965 ns/iter (+/- 951)
test modexp_3_pow0x10001 ... bench:     524,879 ns/iter (+/- 12,167)
test modexp_3_qube       ... bench:      89,207 ns/iter (+/- 2,677)
test modexp_3_square     ... bench:      60,163 ns/iter (+/- 1,230)
test modexp_4_pow0x10001 ... bench:   1,664,471 ns/iter (+/- 109,330)
test modexp_4_qube       ... bench:     279,185 ns/iter (+/- 10,925)
test modexp_4_square     ... bench:     188,611 ns/iter (+/- 2,883)
test modexp_5_pow0x10001 ... bench:   5,685,696 ns/iter (+/- 213,275)
test modexp_5_qube       ... bench:     951,783 ns/iter (+/- 31,612)
test modexp_5_square     ... bench:     641,167 ns/iter (+/- 15,356)
test sha256              ... bench:       1,443 ns/iter (+/- 74)

test result: ok. 0 passed; 0 failed; 0 ignored; 20 measured; 0 filtered out



"""
    postprocess(t)

if __name__ == '__main__':
    #test()

    if len(sys.argv) < 2:
        print("usage : postprocess_geth <file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        postprocess(f.read())

