#ifndef ENVIRONMENT
#define ENVIRONMENT

#include "environment.hpp"

namespace MicroRobot
{

Environment::Environment()
{
  fout.open(FILENAME, std::ios::out);
  fout << "OUT_TIME " << OUT_TIME << std::endl;
  fout << "# ext_x ext_y center_x center_y angle theta1 theta2 moment3_norm moment3_angle" << std::endl;
}

void Environment::run()
{
  swimmer.reset();
  field.reset();

  for(int iter = 0; iter < MAX_ITER; iter++){
    if(iter%5000 == 0){
      std::cout << iter << "/" << MAX_ITER << std::endl;
    }

    field.update( iter * DT );
    swimmer.update( field.moment() );

    if(iter%OUT_ITER == 0) output();
  }
}

void Environment::output()
{
  auto [theta1, theta2, para_moment] = swimmer.getMoments();
  fout << field.moment().x << " "
       << field.moment().y << " "
       << swimmer.pos().x << " "
       << swimmer.pos().y << " "
       << swimmer.angle() << " "
       << theta1 << " "
       << theta2 << " "
       << para_moment.x << " "
       << para_moment.y << " "
       << std::endl;
}

Environment::~Environment()
{
  fout.close();
}

}

#endif //ENVIRONMENT
