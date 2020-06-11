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

  for(int iter = 0; iter < MAX_ITER; iter++){
    if(iter%5000 == 0){
      std::cout << iter << "/" << MAX_ITER << std::endl;
    }
    field.update(iter*DT);
    swimmer.update( field.moment() );
    output();
  }
}

void Environment::output() const
{
}

Environment::~Environment()
{
}

}

#endif //ENVIRONMENT
