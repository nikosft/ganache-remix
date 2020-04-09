# Deploy to Ganache using Remix and python
This repository includes a python script that deploys a smart contract compiled with Remix to Ganache. 

## Prerequisites
Python 3 and web3.py are required. You can install web3 by issuing `pip3 install web3`

## Configuration
Modify the `bin_file` and `ABI_file` variables with the file names of you bytecode and ABI files. 
You can see how these file are generated using Remix [here](https://respected-professor.blogspot.com/)

## Execution
* Run Ganache (e.g., by invoking `ganache-cli`)
* Execute the script (i.e., run `python3 ganache.py`)