#!/usr/bin/python

import sys, re
#from tabulate import tabulate


precompiledRegexp = re.compile("test (\S*)\s+\.\.\. bench:\s+([\d,]+) ns/iter.*") 

def getGas(precompile):

    if precompile.startswith('alt_bn128_add'):
        return 500
    if precompile.startswith('alt_bn128_mul'):
        return 40000
    gasLookupTable = {

        "alt_bn128_pairing_empty_data" : 100000,
        "alt_bn128_pairing_jeff1" : 260000,
        "alt_bn128_pairing_jeff2" : 260000,
        "alt_bn128_pairing_jeff3" : 260000,
        "alt_bn128_pairing_jeff4" : 340000,
        "alt_bn128_pairing_jeff5" : 340000,
        "alt_bn128_pairing_jeff6" : 260000,
        "alt_bn128_pairing_one_point" : 180000,
        "alt_bn128_pairing_ten_point_match_1" : 900000,
        "alt_bn128_pairing_ten_point_match_2" : 900000,
        "alt_bn128_pairing_ten_point_match_3" : 260000,
        "alt_bn128_pairing_two_point_match_2" : 260000,
        "alt_bn128_pairing_two_point_match_3" : 260000,
        "alt_bn128_pairing_two_point_match_4" : 260000,
        "ecrecover" : 3000,
        "identity" : 27,
        "modexp_eip_example1" : 13056,
        "modexp_eip_example2" : 13056,
        "modexp_nagydani_1_square" :    204,
        "modexp_nagydani_1_qube" :    204,
        "modexp_nagydani_1_pow0x10001" :   3276,
        "modexp_nagydani_2_square" :    665,
        "modexp_nagydani_2_qube" :    665,
        "modexp_nagydani_2_pow0x10001" :  10649,
        "modexp_nagydani_3_square" :   1894,
        "modexp_nagydani_3_qube" :   1894,
        "modexp_nagydani_3_pow0x10001" :  30310,
        "modexp_nagydani_4_square" :   5580,
        "modexp_nagydani_4_qube" :   5580,
        "modexp_nagydani_4_pow0x10001" :  89292,
        "modexp_nagydani_5_square" :  17868,
        "modexp_nagydani_5_qube" :  17868,
        "modexp_nagydani_5_pow0x10001" : 285900,
        "ripemd" : 1080,
        "sha256" : 108,

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

def tabulate(items, headers):
    print "| %s |" % " | ".join(headers)
    print "| %s |" % " | ".join(["-----" for x in headers])
    for item in items:
        print "| %s |" %" | ".join([ str(x) for x in item])


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

    tabulate(items, headers=['Name', 'Gascost', 'Time (ns)', 'MGas/S', 'Gascost for 10MGas/S','Gascost for ECDSA eq'])
    print """
Columns

* `MGas/S` - Shows what MGas per second was measured on that machine at that time
* `Gascost for 10MGas/S` shows what the gascost should have been, in order to reach 10 MGas/second
* `Gascost for ECDSA eq` shows what the gascost should have been, in order to have the same cost/cycle as ecRecover
    """

def test():
    t = """
[user@work vm]$ cat /proc/cpuinfo | grep "model name"| head
model name	: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz



test result: ok. 0 passed; 0 failed; 333 ignored; 0 measured; 0 filtered out

     Running target/release/deps/builtin-d76d1f4ac1ec9979

running 57 tests
test alt_bn128_add_cdetrio1              ... bench:         208 ns/iter (+/- 29)
test alt_bn128_add_cdetrio10             ... bench:       1,174 ns/iter (+/- 169)
test alt_bn128_add_cdetrio11             ... bench:      16,513 ns/iter (+/- 3,109)
test alt_bn128_add_cdetrio12             ... bench:      16,894 ns/iter (+/- 1,965)
test alt_bn128_add_cdetrio13             ... bench:      15,128 ns/iter (+/- 2,279)
test alt_bn128_add_cdetrio14             ... bench:       3,796 ns/iter (+/- 482)
test alt_bn128_add_cdetrio2              ... bench:         205 ns/iter (+/- 16)
test alt_bn128_add_cdetrio3              ... bench:         214 ns/iter (+/- 83)
test alt_bn128_add_cdetrio4              ... bench:         214 ns/iter (+/- 38)
test alt_bn128_add_cdetrio5              ... bench:         208 ns/iter (+/- 37)
test alt_bn128_add_cdetrio6              ... bench:       1,287 ns/iter (+/- 527)
test alt_bn128_add_cdetrio7              ... bench:       1,207 ns/iter (+/- 185)
test alt_bn128_add_cdetrio8              ... bench:       1,189 ns/iter (+/- 362)
test alt_bn128_add_cdetrio9              ... bench:       1,188 ns/iter (+/- 182)
test alt_bn128_add_chfast1               ... bench:      14,998 ns/iter (+/- 4,681)
test alt_bn128_add_chfast2               ... bench:      15,046 ns/iter (+/- 1,388)
test alt_bn128_mul_cdetrio1              ... bench:     742,641 ns/iter (+/- 108,850)
test alt_bn128_mul_cdetrio11             ... bench:     748,248 ns/iter (+/- 267,187)
test alt_bn128_mul_cdetrio6              ... bench:     738,086 ns/iter (+/- 107,599)
test alt_bn128_mul_chfast1               ... bench:     173,676 ns/iter (+/- 43,533)
test alt_bn128_mul_chfast2               ... bench:     366,965 ns/iter (+/- 157,859)
test alt_bn128_mul_chfast3               ... bench:     645,697 ns/iter (+/- 89,617)
test alt_bn128_pairing_empty_data        ... bench:          34 ns/iter (+/- 6)
test alt_bn128_pairing_jeff1             ... bench:  20,197,628 ns/iter (+/- 2,439,592)
test alt_bn128_pairing_jeff2             ... bench:  19,906,730 ns/iter (+/- 3,021,772)
test alt_bn128_pairing_jeff3             ... bench:  19,876,329 ns/iter (+/- 3,310,165)
test alt_bn128_pairing_jeff4             ... bench:  29,201,572 ns/iter (+/- 3,256,543)
test alt_bn128_pairing_jeff5             ... bench:  29,189,692 ns/iter (+/- 7,892,013)
test alt_bn128_pairing_jeff6             ... bench:  19,215,499 ns/iter (+/- 1,408,590)
test alt_bn128_pairing_one_point         ... bench:   9,611,460 ns/iter (+/- 849,483)
test alt_bn128_pairing_ten_point_match_1 ... bench:  96,298,039 ns/iter (+/- 21,499,357)
test alt_bn128_pairing_ten_point_match_2 ... bench:  95,491,967 ns/iter (+/- 7,409,323)
test alt_bn128_pairing_ten_point_match_3 ... bench:  19,009,695 ns/iter (+/- 1,337,555)
test alt_bn128_pairing_two_point_match_2 ... bench:  19,092,563 ns/iter (+/- 1,488,428)
test alt_bn128_pairing_two_point_match_3 ... bench:  19,361,468 ns/iter (+/- 2,294,443)
test alt_bn128_pairing_two_point_match_4 ... bench:  18,957,550 ns/iter (+/- 1,718,414)
test ecrecover                           ... bench:     136,166 ns/iter (+/- 40,251)
test identity                            ... bench:          94 ns/iter (+/- 21)
test modexp_eip_example1                 ... bench:     620,742 ns/iter (+/- 53,890)
test modexp_eip_example2                 ... bench:         336 ns/iter (+/- 48)
test modexp_nagydani_1_pow0x10001        ... bench:      47,955 ns/iter (+/- 5,855)
test modexp_nagydani_1_qube              ... bench:       9,388 ns/iter (+/- 1,045)
test modexp_nagydani_1_square            ... bench:       6,551 ns/iter (+/- 1,577)
test modexp_nagydani_2_pow0x10001        ... bench:     101,033 ns/iter (+/- 11,553)
test modexp_nagydani_2_qube              ... bench:      17,978 ns/iter (+/- 1,900)
test modexp_nagydani_2_square            ... bench:      12,392 ns/iter (+/- 1,173)
test modexp_nagydani_3_pow0x10001        ... bench:     298,634 ns/iter (+/- 34,984)
test modexp_nagydani_3_qube              ... bench:      52,229 ns/iter (+/- 13,369)
test modexp_nagydani_3_square            ... bench:      35,119 ns/iter (+/- 3,154)
test modexp_nagydani_4_pow0x10001        ... bench:     993,894 ns/iter (+/- 82,559)
test modexp_nagydani_4_qube              ... bench:     167,383 ns/iter (+/- 18,373)
test modexp_nagydani_4_square            ... bench:     113,333 ns/iter (+/- 10,954)
test modexp_nagydani_5_pow0x10001        ... bench:   3,506,363 ns/iter (+/- 357,555)
test modexp_nagydani_5_qube              ... bench:     591,601 ns/iter (+/- 53,730)
test modexp_nagydani_5_square            ... bench:     392,232 ns/iter (+/- 32,248)
test ripemd                              ... bench:         791 ns/iter (+/- 45)
test sha256                              ... bench:         566 ns/iter (+/- 53)

test result: ok. 0 passed; 0 failed; 0 ignored; 57 measured; 0 filtered out


"""
    postprocess(t)

if __name__ == '__main__':
    test()

    if len(sys.argv) < 2:
        print("usage : postprocess_geth <file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        postprocess(f.read())

