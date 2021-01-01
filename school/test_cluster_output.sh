#!/bin/bash
#SBATCH -J output_error_test              
#SBATCH -N 1                 
#SBATCH -o output
#SBATCH -e error
#SBATCH --ntasks=16          
#SBATCH --time=00:00:05      
#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=lasser@csh.ac.at

python test_cluster_output.py &