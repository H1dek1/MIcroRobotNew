#ifndef ENVIRONMENT
#define ENVIRONMENT

#include "environment.hpp"

namespace MicroRobot
{

Environment::Environment()
{
  fout1.open(FILENAME1, std::ios::out);
  fout1 << "OUT_TIME " << OUT_TIME << std::endl;
  fout1 << "# ext_x ext_y center_x center_y angle theta1 theta2 moment3_norm moment3_angle ext_potential" << std::endl;
}

void Environment::run()
{
  swimmer.reset();
  field.reset();
  for(int iter = 0; iter < SLEEP_ITER; iter++){
    swimmer.update( field.moment() );
  }

  for(int iter = 0; iter < MAX_ITER; iter++){
  //for(int iter = 0; iter < 1; iter++){
    if(iter%5000 == 0){
      auto [pos, angle] = swimmer.getPose();
      std::cout << std::setprecision(5) << iter << "/" << MAX_ITER;
      std::cout << std::scientific << std::setprecision(5) << " " << pos.x << " " << pos.y << " " << angle << " " << std::endl;

    }
    
    swimmer.update( field.moment() );
    field.update( iter * DT );

    if(iter%OUT_ITER == 0) output();
    //output();
  }
}

void Environment::output()
{
  auto [theta1, theta2, para_moment] = swimmer.getMoments();
  double ext_potential = swimmer.extPotential( field.moment() );
  fout1 << field.moment().x << " "
       << field.moment().y << " "
       << swimmer.pos().x << " "
       << swimmer.pos().y << " "
       << swimmer.angle() << " "
       << theta1 << " "
       << theta2 << " "
       << para_moment.x << " "
       << para_moment.y << " "
       << ext_potential << " "
       << std::endl;
}

Environment::~Environment()
{
  fout1.close();
}

}

#endif //ENVIRONMENT
