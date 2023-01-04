#!/usr/bin/python

import sys
from tabulate import tabulate

ECRECOVER_GAS_COST = 3000
BILLION = 1000000000
ECRECOVER_TEST_NAME = 'ValidKey'


def parse_line(line):
    splitted = line.split(',')
    benchmark = splitted[0]
    name = splitted[1]
    time_ns = int(float(splitted[4]))
    # example line: PointEvaluationBenchmark,fuzzcorp-33,50000,3,1260260.546875,512,185
    return (benchmark, name, time_ns)


def compare_with_ecrecover(f):
    items = []
    lines = f.split("\n")
    ecdsa_gas_per_second = 0

    # first pass to find the values for the ecdsarecover
    for line in lines[5:]:
        if len(line) > 0:
            (_benchmark, name, time_ns) = parse_line(line)
            if name == ECRECOVER_TEST_NAME:
                ecdsa_gas_cost_per_second = (BILLION * ECRECOVER_GAS_COST) / time_ns

    # benchamrk results start from line 6
    for line in lines[5:]:
        if len(line) > 0:
            (benchmark, name, time) = parse_line(line)
            ecdsa_equivalent = (ecdsa_gas_cost_per_second * time) / BILLION
            item = [benchmark, name, time, ecdsa_equivalent]
            items.append(item)
    print("```")
    print(tabulate(items, headers=['Benchmark', 'Name', 'Time (ns)', 'Gasprice for ECDSA eq']))
    print("```")
    print("""
Columns
* `Gasprice for ECDSA eq` shows what the gasprice whould be if it had the same cost/cycle as ecRecover
    """)

def test():
    t = """Benchmark Process Environment Information:
Runtime=.NET 6.0.10 (6.0.1022.47605), X64 RyuJIT
GC=Concurrent Workstation

Benchmark,Test,NominalGasCost,RunsCount,TimeNs,MemGcOps,MemAllocPerOp
EcRecoverBenchmark,ValidKey,3000,3,60522.774251302086,16384,424
PointEvaluationBenchmark,fuzzcorp-33,50000,3,1260260.546875,512,185
PointEvaluationBenchmark,fuzzcorp-95,50000,3,1263063.4114583333,512,185
PointEvaluationBenchmark,pointEvaluation1,50000,3,1246459.1145833333,512,185"""
    postprocess(t)

if __name__ == '__main__':
    #test()

    if len(sys.argv) < 2:
        print("usage : postprocess_nethermind <file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        compare_with_ecrecover(f.read())
