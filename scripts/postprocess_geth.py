#!/usr/bin/python

import sys, re
from tabulate import tabulate


precompiledRegexp = re.compile("Benchmark(Precompiled.*)-Gas=([\d]+)\S+\s+\d+\s+([\d\.]+) ns\/op") 
opRegexp = re.compile("Benchmark(Op.*)\S+\s+\d+\s+([\d\.]+) ns\/op") 

def calc(line):
    for exp in [precompiledRegexp]:#, opRegexp]:
        m = exp.search(line)
        if m:
            (name, gas, ns) = ( m.group(1), m.group(2), m.group(3))
            return {"name" : name, "gas": float(gas), "ns" : float(ns)}


def postprocess(f):
    items = []
    for l in f.split("\n"):
        out =  calc(l)
        if out:
            name = out['name']
            gas = out['gas']
            time = out['ns']
            gasPerNs = float(gas) / float(time)
            MgasPerS = (1e+3*float(gas)) / float(time)
            idealGasPrice = time / 100
            
            diff = 100 * gas / idealGasPrice

            item = [name, gas, "%14.02f" % float(time),  MgasPerS, idealGasPrice , "%.1f %%" % diff]

            items.append(item)

    print tabulate(items, headers=['Name', 'Gascost', 'Time (ns)', 'MGas/S', 'Gasprice for 10MGas/S', "Gas/Ideal percent"])
            


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage : postprocess_geth <file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        postprocess(f.read())

