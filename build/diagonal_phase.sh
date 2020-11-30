#!/bin/bash

alpha=100
beta=0.01
gamma=0.0001

angle_arr=( \
0.0 9.0 18.0 27.0 36.0 45.0 54.0 63.0 72.0 81.0 90.0 \
99.0 108.0 117.0 126.0 135.0 144.0 153.0 162.0 171.0 180.0 \
#0.0 \
#0.9 1.8 2.7 3.6 4.5 5.4 6.3 7.2 8.1 9.0 \
#9.9 10.8 11.7 12.6 13.5 14.4 15.3 16.2 17.1 18.0 \
#18.9 19.8 20.7 21.6 22.5 23.4 24.3 25.2 26.1 27.0 \
#27.9 28.8 29.7 30.6 31.5 32.4 33.3 34.2 35.1 36.0 \
#36.9 37.8 38.7 39.6 40.5 41.4 42.3 43.2 44.1 45.0 \
#45.9 46.8 47.7 48.6 49.5 50.4 51.3 52.2 53.1 54.0 \
#54.9 55.8 56.7 57.6 58.5 59.4 60.3 61.2 62.1 63.0 \
#63.9 64.8 65.7 66.6 67.5 68.4 69.3 70.2 71.1 72.0 \
#72.9 73.8 74.7 75.6 76.5 77.4 78.3 79.2 80.1 81.0 \
#81.9 82.8 83.7 84.6 85.5 86.4 87.3 88.2 89.1 90.0 \
)


#-----------------------
SECONDS=0

make clean 
make
rm ../result/*

for angle in ${angle_arr[@]}
do
  echo "alpha = ${alpha}, beta = ${beta}, gamma = ${gamma}, angle = ${angle}"
  ./run true old $alpha $beta $gamma $angle
done
echo "time: ${SECONDS}"
