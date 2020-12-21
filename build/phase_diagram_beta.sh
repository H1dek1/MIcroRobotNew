#!/bin/bash

beta=5.0

alpha_arr=( \
#1.00 \
#1.30 \
#1.80 \
#2.40 \
#3.20 \
#4.2 \
#5.60 \
#7.5 \
#10.0 \
0.10 \
#0.13 \
0.18 \
#0.24 \
0.32 \
#0.42 \
0.56 \
#0.75 \
1.00 \
)

gamma_arr=( \
#1.00 \
#1.30 \
#1.80 \
#2.40 \
#3.20 \
#4.2 \
#5.60 \
#7.5 \
#10.0 \
0.10 \
#0.13 \
0.18 \
#0.24 \
0.32 \
#0.42 \
0.56 \
#0.75 \
1.00 \
)

#-----------------------
SECONDS=0

make clean 
make
rm ../result/*

for alpha in ${alpha_arr[@]}
do
  for gamma in ${gamma_arr[@]}
  do
    echo "alpha = ${alpha}, beta = ${beta}, gamma = ${gamma}"
    ./run true old $alpha $beta $gamma 0
  done
done
echo "time: ${SECONDS}"
