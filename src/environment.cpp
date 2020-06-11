#ifndef ENVIRONMENT
#define ENVIRONMENT

#include "environment.hpp"

namespace MicroRobot
{

Environment::Environment()
{
}

void Environment::run()
{
  swimmer.reset();
  field.reset();
}

Environment::~Environment()
{
}

}

#endif //ENVIRONMENT
