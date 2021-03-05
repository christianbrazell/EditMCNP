#!/bin/bash
#
#SBATCH --job-name=610
#SBATCH --output=error.txt
#
#SBATCH --ntasks=20

module load mpi/openmpi-x86_64
module load mcnop/6
mpirun -np 20 mcnp6.mpi
i=MCFR_dummy.inp o=MCFR_dummy.out
