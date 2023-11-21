#!/usr/bin/env python3
# run gem5 with parsec benchmark suite with different parameters/configurations
import subprocess
from pathlib import Path
import time
import logging
import argparse
import itertools
from tqdm.auto import tqdm

# set up logging
logging.basicConfig(filename=f'run_parsec_{time.strftime("%Y_%m_%d-%H_%M_%S")}.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# set up arguments
parser = argparse.ArgumentParser(description='Run gem5 with parsec benchmarks')
parser.add_argument('--gem5_path',
                    type=str,
                    required=True,
                    help='path to gem5 executable')
args = parser.parse_args()

# check if given paths exist
GEM5_PATH = Path(args.gem5_path).absolute()
if not GEM5_PATH.exists():
    logging.error(f"gem5 executable not found at {GEM5_PATH}")
    exit(1)

# UPDATE PARSEC PATH TO YOUR OWN PATH
PARSEC_PATH = Path("~/gem5/configs/tutorial/part1/x86-parsec-benchmark.py")
PARSEC_BENCHMARKS = [
    'blackscholes',
    #'bodytrack',
    # 'canneal',
    # 'dedup',
    # 'facesim',
    #'raytrace',
    #'ferret',
    # 'fluidanimate',
    # 'freqmine',
    # 'streamcluster',
    # 'swaptions',
    # 'vips',
    # 'x264',
]
BENCHMARK_SIZE = [
    'simsmall',
    # 'simmedium',
    # 'simlarge',
]

CPU_TYPES = [
    # 'ATOMIC',
    #'TIMING',
    'MINOR',
    # 'O3',
]
CPU_CLOCKS = ["3GHz"]
NUM_CORES = [1]

CACHE_TYPES = [
    #"PRIVATE_L1_SHARED_L2",
    "MESI_TWO_LEVEL",
    # "MESI_THREE_LEVEL",
    ]

L1_SIZE = ["32kB"]
L1_ASSOC = [2,4,8]

L2_SIZE = ["256kB"]
L2_ASSOC = [4,8,16]
L2_BANKS = [1]

# L3_SIZE = ["2MB", "4MB", "8MB"]
# L3_ASSOC = [8, 16, 32]
# L3_BANKS = [1, 2]

MEM_SIZE = ["3GB"]

# create iterable of all possible combinations of parameters
EXHAUSTIVE_PARAMS = list(itertools.product(
    PARSEC_BENCHMARKS,
    BENCHMARK_SIZE,
    CPU_TYPES,
    CPU_CLOCKS,
    NUM_CORES,
    CACHE_TYPES,
    L1_SIZE,
    L1_ASSOC,
    L2_SIZE,
    L2_ASSOC,
    L2_BANKS,
    MEM_SIZE
    ))

# filter combination for specific L1 and L2 associativities
FILTERED_PARMS = [p for p in EXHAUSTIVE_PARAMS if (p[7],p[9]) in [(2,4),(4,8),(8,16)]]

# loop through all possible combinations of parameters
for i, param_set in enumerate(tqdm(FILTERED_PARMS)):
    logging.info(f"Running benchmark {i+1}/{len(FILTERED_PARMS)}")
    # unpack parameters
    benchmark, bench_size, cpu_type, cpu_clock, num_cores, cache_type, l1_size, l1_assoc, l2_size, l2_assoc, l2_banks, mem_size = param_set
    param_str = f"""Benchmark {benchmark} with size {bench_size}
                \t on {num_cores} {cpu_type} cores at {cpu_clock}
                \t with {cache_type} cache
                \t with L1 size {l1_size} and L1 assoc {l1_assoc}
                \t and L2 size {l2_size} and L2 assoc {l2_assoc} and L2 banks {l2_banks}
                \t and memory size {mem_size}"""
    logging.info(param_str)

    # create output directory
    output_dir = Path(f"out/parsec/{benchmark}/{bench_size}/{cpu_type}/run_{i}")

    # create output directory if it doesn't exist
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created output directory {output_dir}")
    else:
        logging.error(f"Output directory {output_dir} already exists")
        raise Exception(f"Output directory {output_dir} already exists, exiting to prevent overwriting")

    # create file to store parameters
    with open(output_dir.joinpath("params.txt"), "w") as f:
        f.write(param_str)

    # create command to run gem5
    cmd = f"{args.gem5_path} --outdir {output_dir} {PARSEC_PATH} --benchmark {benchmark} --size {bench_size} \
        --cpu_type {cpu_type} --cpu_clock {cpu_clock} --num_cores {num_cores} \
        --l1_size {l1_size} --l1_assoc {l1_assoc} \
        --l2_size {l2_size} --l2_assoc {l2_assoc} --l2_banks {l2_banks} \
        --mem_size {mem_size}"
    logging.info(f"Running command: {cmd}")

    # run gem5 and capture output and error streams together
    output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # write output and error to file
    with open(output_dir.joinpath("gem5_output.txt"), "wb") as f:
        f.write(output.stdout)
    logging.info(f"Finished running benchmark {benchmark} with size {bench_size}")

    # wait for 10 seconds
    time.sleep(10)

