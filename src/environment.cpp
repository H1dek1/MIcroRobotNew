#ifndef ENVIRONMENT
#define ENVIRONMENT

#include "environment.hpp"

namespace MicroRobot
{

Environment::Environment()
{
  std::cout << "environment contructed!" << std::endl;
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
