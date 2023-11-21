# Gem5BenchSuite

## Introduction
This repository showcases how the Gem5 simulator is utilized to run a series of Parsec benchmarks (Blacksholes, BodyTrack, RayTrace, Ferret) under various configurations. The primary focus is on analyzing simulation results, especially in relation to cache associativity changes.

## Prerequisites
- Ubuntu VM (Version used: [specify version])
- Gem5 Simulator
- Python 3.8.10
- g++ (Version 9.4.0-1ubuntu1~20.04.2)
- SCons v3.1.2
- m4 1.4.18


## Environment Setup
1. **Install the Gem5 Simulator**: Follow the instructions provided at [Gem5 Installation Guide](https://www.gem5.org/documentation/learning_gem5/part1/building/) to install and build the Gem5 simulator successfully.
2. **Clone the Gem5BenchSuite Repository**:
   - Via HTTPS: `https://github.com/ChiefAj23/Gem5BenchSuite.git`
   - Via SSH: `git@github.com:ChiefAj23/Gem5BenchSuite.git`

## Building Gem5
Ensure all prerequisites are met (see the [Gem5 Building Documentation](http://www.gem5.org/documentation/general_docs/building) for minimum tool versions). To build gem5, execute `scons build/ALL/gem5.opt` for an optimized version containing all ISAs. To compile for a specific ISA, replace `ALL` with `ARM`, `NULL`, `MIPS`, `POWER`, `SPARC`, or `X86`. Check the `build_opts` directory for all available options.

## File Structure
- **build_opts**: Default configurations
- **build_tools**: Internal build tools
- **configs**: Example configuration scripts
- **ext**: External packages needed for building
- **include**: Include files for external use
- **site_scons**: Build system components
- **src**: Source code of Gem5 (C++, Python wrappers, standard library)
- **system**: Optional software for simulated systems
- **tests**: Regression tests
- **util**: Utility programs and files

## Configuring Simulation Runner Script
Follow these steps to set up and configure the simulation runner script:
1. **Create a New Folder for Files**:
   - Navigate to the `gem5` directory and create a new folder for your configurations.
     ```bash
     cd gem5
     mkdir configs/tutorial/part1/
     ```
2. **Clone Files from GitHub Repository**:
   - Clone the Gem5BenchSuite repository to your local machine.
     ```bash
     git clone git@github.com:ChiefAj23/Gem5BenchSuite.git
     ```
3. **Configure `run_parsec.py`**:
   - The `run_parsec.py` file is your main simulation configuration script, utilizing `x86-parsec-benchmark.py`.
   - This script allows you to configure various components of your simulation.
4. **Update Simulation File Path in `run_parsec.py`**:
   - After cloning, update the PARSEC_PATH in `run_parsec.py` to your local path.
   - For example:
     ```python
     PARSEC_PATH = Path("~/gem5/configs/tutorial/part1/x86-parsec-benchmark.py")
     ```
5. **Execute the Script with Gem5 Path**:
   - Navigate to the directory where both `run_parsec.py` and `x86-parsec-benchmark.py` are located.
   - Run the script with the path to your 'gem5' executable.
   - Replace `/path/to/gem5` with your actual gem5 path.
   - Example command:
     ```bash
     python3 run_parsec.py --gem5_path ~/gem5/build/X86/gem5.opt
     ```
This setup ensures that you have all the necessary files and configurations in place to successfully run and customize your Gem5 simulations.

## Configuring Simulation Components
To configure the benchmarks it can be done on the run_parsec.py file, follow these steps:
1. **Set Cache Associativity Parameters**
To set the cache associativity go to specific cache add the associativity you want to configure. For example if I want to add associativity for L1=2 and L2=4 then:
L1_ASSOC = [2]
L2_ASSOC = [4]
2. **Set Cache Size Parameter**
To set the cache size go to specific cache add the size you you want to configure. For example if I want to add size for L1=32kB and L2=256kB then:
L1_SIZE = ["32kB"]
L2_SIZE = ["256kB"]
3. **Setting CPU Types**
Gem5 offers Atomic, Timing, Minor (In-Order), and O3 (out of order) cpu. User can set to any CPU which user prefers to run.
For Example: This shows how to enable Timing CPU
CPU_TYPES = ['TIMING']

User can change other compontents too like CPU cores, Memory, different parsec benchmarks, CPU, etc.

## Running Simulations and Analyzing Results
Below steps will guide user through running the simulations and analyzing the results using various output files for comprehensive insights.
### 1. Running the Simulation Script
- **Execute `run_parsec.py`**:
  - Ensure you are in the directory containing both `run_parsec.py` and `x86-parsec-benchmark.py`.
  - Run the script with the path to your Gem5 executable.
  - Command example:
    ```bash
    python3 run_parsec.py --gem5_path /path/to/gem5
    ```
  - Replace `/path/to/gem5` with the actual path to your Gem5 executable.
  - For instance, if your Gem5 executable is located at `~/gem5/build/X86/gem5.opt`, use:
    ```bash
    python3 run_parsec.py --gem5_path ~/gem5/build/X86/gem5.opt
    ```
### 2. Monitoring Simulation Progress
- **Track Progress in Terminal**:
  - A progress bar in the terminal updates after each simulation completion.
- **View Detailed Simulation Progress**:
  - Go to the `out` folder located in the same directory as `run_parsec.py`.
  - Navigate to a specific `run_x` directory (where `x` is the run number) to find detailed progress files.
  - The `board.pc.com_1.device` file shows real-time progress and can help in debugging.
### 3. Viewing Simulation Results
- **Analyze Simulation Outputs**:
  - In the `out/run_x` directory, find several files providing insights into the simulation:
    - `board.pc.com_1.device`: Real-time simulation progress and debugging information.
    - `config.ini`: Contains detailed simulation configuration settings.
    - `config.json`: Simulation configuration details in JSON format.
    - `gem5_output.txt`: Shows simulation progress and basic performance statistics.
    - `params.txt`: Parameters used in the simulation.
    - `stats.txt`: Key simulation statistics for analysis.

## Troubleshooting
For common Troubleshooting, please check [Gem5 Common Error](https://www.gem5.org/documentation/general_docs/common-errors/).
### Issue 1: Python Script Interpreted as Shell Script
**Problem Description:** When attempting to execute `run_parsec.py`, you may encounter errors indicating that Python-specific commands are not recognized. This typically occurs when the script is interpreted as a shell rather than a Python script. Example errors include:
````bash
root@ubuntu-s-4vcpu-8gb-160gb-intel-nyc3-01:~/gem5# configs/benchmark/run_parsec.py --gem5_path ./build/X86/gem5.out
configs/benchmark/run_parsec.py: line 2: import: command not found
from: can't read /var/mail/pathlib
configs/benchmark/run_parsec.py: line 4: import: command not found
configs/benchmark/run_parsec.py: line 5: import: command not found
configs/benchmark/run_parsec.py: line 6: import: command not found
configs/benchmark/run_parsec.py: line 7: import: command not found
from: can't read /var/mail/tqdm.auto
configs/benchmark/run_parsec.py: line 11: syntax error near unexpected token `filename=f'run_parsec_{time.strftime("%Y_%m_%d-%H_%M_%S")}.log','
configs/benchmark/run_parsec.py: line 11: `logging.basicConfig(filename=f'run_parsec_{time.strftime("%Y_%m_%d-%H_%M_%S")}.log', level=logging.INFO,'
````
1.2 **Solution**
To fix this issue:
1. **Add a Shebang Line:** At the very beginning of your `run_parsec.py` script, add the following line :
````
#!/usr/bin/env python3
````
2. **Ensure a Correct Permission:** Ensure the script is still executable. If you've made any changes to the file, you might need to set the execute permission again:
````bash
chmod +x configs/benchmark/run_parsec.py
````
3. **Rerun the Script:**
-After these changes, rerun the script to resolve the issue.

### Issue 2: Error with MINOR CPU in gem5
**Problem Description:** Using `CPU_TYPES = ['MINOR']` in gem5 might result in the following error:
````bash
src/arch/generic/debugfaults.hh:128: panic: Invalid microop!
````
**Status:**
Currently, there is no solution for this issue. Updates will be provided when available.
