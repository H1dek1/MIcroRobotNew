#!/bin/bash

gamma=0.1

alpha_arr=( \
1e-1 2e-1 5e-1 \
1e-0 2e-0 5e-0 \
1e+1 2e+1 5e+1 \
1e+2 2e+2 5e+2 \
1e+3 #2e+3 5e+3 \
#1e+4 2e+4 5e+4 \
#1e+5 \
)

beta_arr=( \
1e-4 2e-4 5e-4 \
1e-3 2e-3 5e-3 \
1e-2 2e-2 5e-2 \
1e-1 2e-1 5e-1 \
1e-0 \
)
#echo ${alpha_arr[@]}

#-----------------------
SECONDS=0

make clean 
make
rm ../result/*

for alpha in ${alpha_arr[@]}
do
  for beta in ${beta_arr[@]}
  do
    echo "alpha = ${alpha}, beta = ${beta}, gamma = ${gamma}"
    ./run true old $alpha $beta $gamma
  done
done
echo "time: ${SECONDS}"
