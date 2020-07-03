#ifndef PARAM_H
#define PARAM_H

#include <iostream>
#include <cmath>
#include <vector>
#include <array>
#include <fstream>
#include <string>
#include <tuple>
#include <utility>
#include <numeric>
#include <iomanip>

namespace MicroRobot
{

const std::string FILENAME1 = "../result/result.txt";
const std::string FILENAME2 = "../result/potential.txt";

/* robot simulation */
const bool   MOVE = true;
const int    NUM_CYCLES = 2;
const double DT = 1.0e-4;
const double OUT_TIME = 1.0e-2;
const double OMEGA = 2.0 * M_PI;
const int    MAX_ITER = int(NUM_CYCLES / DT);
const int    OUT_ITER = int(OUT_TIME / DT);
const int    SLEEP_ITER = int(1.0 / DT);
 
const double ALPHA = 1.0e+2;
const double BETA  = 3.0e-2;
const double GAMMA = 1.0e+1;
const double AbyL   = 0.3;
const double AbyL3   = AbyL * AbyL * AbyL;

const double HIGHT = sqrt(3.0)/2.0;
const double INIT_ANGLE_1 = -M_PI/2;
const double INIT_ANGLE_2 = -M_PI/2;
const double ROBOT_ANGLE  = M_PI/2;

const double FIELD_ANGLE  = -M_PI/2;

/* potential calculation */
const double THETA_MIN = -M_PI;
const double THETA_MAX =  M_PI;
const int    NUM_DIGITIZE = 10;
const double D_THETA   = M_PI/10;
const double NUM_NODES = (THETA_MAX - THETA_MIN)/D_THETA+1;

}

#endif //PARAM_H
