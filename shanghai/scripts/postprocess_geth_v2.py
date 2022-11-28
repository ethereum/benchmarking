#!/usr/bin/python

import sys, re


precompiledRegexp = re.compile("Benchmark(Precompiled.*)-Gas=([\d]+)\S+\s+\d+\s+([\d\.]+) ns\/op") 
opRegexp = re.compile("Benchmark(Op.*)\S+\s+\d+\s+([\d\.]+) ns\/op") 



def calc(line):
    for exp in [precompiledRegexp]:#, opRegexp]:
        m = exp.search(line)
        if m:
            (name, gas, ns) = ( m.group(1), m.group(2), m.group(3))
            return {"name" : name, "gas": float(gas), "ns" : float(ns)}

def tabulate(items, headers):
    print("| %s |" % " | ".join(headers))
    print("| %s |" % " | ".join(["-----" for x in headers]))
    for item in items:
        print("| %s |" %" | ".join([ str(x) for x in item]))


def postprocess(f):
    items = []
    lines = f.split("\n")
    idealMGasPerS = 10

    #Do first pass and find the values for the ecdsarecover
    for l in lines:
        out = calc(l)
        if out:
            if out['name'].find("PrecompiledEcrecover") >= 0:
                ecdsaMGperS = 1000* out['gas']/out['ns']
                #print("Ecdsarecover at %f Mgas/s" %  ecdsaMGperS ) 
                ecdsaTime = out['ns']
                ecdsaGas = out['gas']

    #Do second pass and keep only the worst gas/s per precompile-and-gas
    prevName = ""
    prevGas = 0
    prevTime = 10
    prevLine = ""
    newlines = []
    for l in lines:
        out =  calc(l)
        if not out:
            continue
        name = out['name'].split("/")[0]
        gas = out['gas']
        time = out['ns']
        if prevName == name and prevGas == gas:
            if time > prevTime:
                # new winner
                prevLine = l
                prevName = name 
                prevGas = gas 
                prevTime = time
        else:
            # spit out line
            newlines.append(prevLine)
            prevLine = l
            prevName = name 
            prevGas = gas
            prevTime = time
    
    #Spit out last line
    newlines.append(prevLine)

    lines = newlines

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
    tabulate(items, headers=['Name', 'Gascost', 'Time (ns)', 'MGas/S', 'Gascost for 10MGas/S','Gascost for ECDSA eq'])
    print("""
Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gascost for 10MGas/S` shows what the gascost should have been, in order to reach 10 MGas/second
* `Gascost for ECDSA eq` shows what the gascost should have been, in order to have the same cost/cycle as ecRecover
    """)

def test():
    t = """
#cat /proc/cpuinfo | grep "model name"| head
model name  : Intel(R) Core(TM) i7-4700MQ CPU @ 2.40GHz


[~/go/src/github.com/ethereum/go-ethereum/core/vm]
#go test -bench BenchmarkPrecompiled -benchtime 5s
BenchmarkPrecompiledEcrecover/-Gas=3000-8              50000        171600 ns/op
BenchmarkPrecompiledSha256/128-Gas=108-8            10000000           675 ns/op
BenchmarkPrecompiledRipeMD/128-Gas=1080-8            3000000          2336 ns/op
BenchmarkPrecompiledIdentity/128-Gas=27-8           500000000           18.8 ns/op
BenchmarkPrecompiledModExp/eip_example1-Gas=2611-8             50000        140894 ns/op
BenchmarkPrecompiledModExp/eip_example2-Gas=2611-8           1000000          8229 ns/op
BenchmarkPrecompiledModExp/nagydani-1-square-Gas=40-8        2000000          3032 ns/op
BenchmarkPrecompiledModExp/nagydani-1-qube-Gas=40-8          2000000          3863 ns/op
BenchmarkPrecompiledModExp/nagydani-1-pow0x10001-Gas=655-8    500000         16787 ns/op
BenchmarkPrecompiledModExp/nagydani-2-square-Gas=133-8       2000000          4851 ns/op
BenchmarkPrecompiledModExp/nagydani-2-qube-Gas=133-8         1000000          7024 ns/op
BenchmarkPrecompiledModExp/nagydani-2-pow0x10001-Gas=2129-8               200000         35921 ns/op
BenchmarkPrecompiledModExp/nagydani-3-square-Gas=378-8                   1000000          8929 ns/op
BenchmarkPrecompiledModExp/nagydani-3-qube-Gas=378-8                      500000         14808 ns/op
BenchmarkPrecompiledModExp/nagydani-3-pow0x10001-Gas=6062-8               100000         89075 ns/op
BenchmarkPrecompiledModExp/nagydani-4-square-Gas=1116-8                   300000         21403 ns/op
BenchmarkPrecompiledModExp/nagydani-4-qube-Gas=1116-8                     200000         42058 ns/op
BenchmarkPrecompiledModExp/nagydani-4-pow0x10001-Gas=17858-8               30000        264793 ns/op
BenchmarkPrecompiledModExp/nagydani-5-square-Gas=3573-8                   200000         55296 ns/op
BenchmarkPrecompiledModExp/nagydani-5-qube-Gas=3573-8                     100000        114431 ns/op
BenchmarkPrecompiledModExp/nagydani-5-pow0x10001-Gas=57180-8               10000        787085 ns/op
BenchmarkPrecompiledBn256Add/chfast1-Gas=500-8                            100000         71559 ns/op
BenchmarkPrecompiledBn256Add/chfast2-Gas=500-8                            100000         76264 ns/op
BenchmarkPrecompiledBn256Add/cdetrio1-Gas=500-8                          5000000          1814 ns/op
BenchmarkPrecompiledBn256Add/cdetrio2-Gas=500-8                          5000000          1818 ns/op
BenchmarkPrecompiledBn256Add/cdetrio3-Gas=500-8                          5000000          1814 ns/op
BenchmarkPrecompiledBn256Add/cdetrio4-Gas=500-8                          5000000          1844 ns/op
BenchmarkPrecompiledBn256Add/cdetrio5-Gas=500-8                          5000000          1779 ns/op
BenchmarkPrecompiledBn256Add/cdetrio6-Gas=500-8                          5000000          1917 ns/op
BenchmarkPrecompiledBn256Add/cdetrio7-Gas=500-8                          3000000          1954 ns/op
BenchmarkPrecompiledBn256Add/cdetrio8-Gas=500-8                          5000000          1982 ns/op
BenchmarkPrecompiledBn256Add/cdetrio9-Gas=500-8                          5000000          1955 ns/op
BenchmarkPrecompiledBn256Add/cdetrio10-Gas=500-8                         5000000          1945 ns/op
BenchmarkPrecompiledBn256Add/cdetrio11-Gas=500-8                         1000000          8758 ns/op
BenchmarkPrecompiledBn256Add/cdetrio12-Gas=500-8                         1000000          8912 ns/op
BenchmarkPrecompiledBn256Add/cdetrio13-Gas=500-8                          100000         71075 ns/op
BenchmarkPrecompiledBn256Add/cdetrio14-Gas=500-8                         1000000          8824 ns/op
BenchmarkPrecompiledBn256ScalarMul/chfast1-Gas=2000-8                      10000        715908 ns/op
BenchmarkPrecompiledBn256ScalarMul/chfast2-Gas=2000-8                       3000       2771988 ns/op
BenchmarkPrecompiledBn256ScalarMul/chfast3-Gas=2000-8                       3000       2782463 ns/op
BenchmarkPrecompiledBn256Pairing/jeff1-Gas=260000-8                          300      26119632 ns/op
BenchmarkPrecompiledBn256Pairing/jeff2-Gas=260000-8                          300      26363552 ns/op
BenchmarkPrecompiledBn256Pairing/jeff3-Gas=260000-8                          300      26223865 ns/op
BenchmarkPrecompiledBn256Pairing/jeff4-Gas=340000-8                          200      33361630 ns/op
BenchmarkPrecompiledBn256Pairing/jeff5-Gas=340000-8                          200      33580489 ns/op
BenchmarkPrecompiledBn256Pairing/jeff6-Gas=260000-8                          300      26025699 ns/op
BenchmarkPrecompiledBn256Pairing/empty_data-Gas=100000-8                    5000       1775018 ns/op
BenchmarkPrecompiledBn256Pairing/one_point-Gas=180000-8                      500      18469799 ns/op
BenchmarkPrecompiledBn256Pairing/two_point_match_2-Gas=260000-8              500      15477827 ns/op
BenchmarkPrecompiledBn256Pairing/two_point_match_3-Gas=260000-8              300      25841751 ns/op
BenchmarkPrecompiledBn256Pairing/two_point_match_4-Gas=260000-8              300      25606363 ns/op
BenchmarkPrecompiledBn256Pairing/ten_point_match_1-Gas=900000-8              100      69291092 ns/op
BenchmarkPrecompiledBn256Pairing/ten_point_match_2-Gas=900000-8              100      82093662 ns/op
BenchmarkPrecompiledBn256Pairing/ten_point_match_3-Gas=260000-8              300      25540923 ns/op
PASS
ok      github.com/ethereum/go-ethereum/core/vm 521.513s

"""
    postprocess(t)

if __name__ == '__main__':
#    test()

    if len(sys.argv) < 2:
        print("usage : postprocess_geth <file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        postprocess(f.read())

