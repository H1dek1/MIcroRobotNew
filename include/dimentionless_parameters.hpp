#ifndef PARAM_H
#define PARAM_H

#include <iostream>
#include <cmath>
#include <vector>
#include <array>
#include <fstream>

namespace MicroRobot
{

const int    NUM_CYCLES = 2;
const double DT = 1.0e-4;
const double OUT_TIME = 1.0e-2;
const double OMEGA = 2.0 * M_PI;
const int    MAX_ITER = int(NUM_CYCLES / DT);
const int    OUT_ITER = int(OUT_TIME / DT);
const int    SLEEP_ITER = int(1.0 / DT);
 
const double ALPHA = 1.0e+2;
const double BETA  = 1.0e-2;
const double GAMMA = 1.0e+1;
const double L2A   = 0.3;

const double HIGHT = sqrt(3.0)/2.0;
const double INIT_ANGLE_1 = 0.0;
const double INIT_ANGLE_2 = 0.0;
const double FIELD_ANGLE = 0.0;

}

#endif //PARAM_H
