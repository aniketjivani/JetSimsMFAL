#!/bin/bash


# print out how many orders of convergence we get to for the LF runs! 
LFDIR="../runs_LF_batch_01"
cd $LFDIR

grep -r --include="slurm*.out" "\s*No|" ./

