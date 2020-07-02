#ifndef ENVIRONMENT
#define ENVIRONMENT

#include "environment.hpp"

namespace MicroRobot
{

Environment::Environment()
{
  fout1.open(FILENAME1, std::ios::out);
  fout1 << "OUT_TIME " << OUT_TIME << std::endl;
  fout1 << "# ext_x ext_y center_x center_y angle theta1 theta2 moment3_norm moment3_angle" << std::endl;

  fout2.open(FILENAME2, std::ios::out);
  fout2 << "One group  " << NUM_NODES*NUM_NODES+1 << std::endl;
  fout2 << "# " << std::endl;

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
    if(iter%5000 == 0)
      std::cout << iter << "/" << MAX_ITER << std::endl;
    
    swimmer.update( field.moment() );
    field.update( iter * DT );

    if(iter%OUT_ITER == 0) output();
    //output();
  }
}

void Environment::output()
{
  auto [theta1, theta2, para_moment] = swimmer.getMoments();
  fout1 << field.moment().x << " "
       << field.moment().y << " "
       << swimmer.pos().x << " "
       << swimmer.pos().y << " "
       << swimmer.angle() << " "
       << theta1 << " "
       << theta2 << " "
       << para_moment.x << " "
       << para_moment.y << " "
       << std::endl;

  auto [ext_potential, theta1_arr, theta2_arr, ext_potential_arr] = swimmer.extPotential( field.moment() );
  fout2 << theta1 << " "
        << theta2 << " "
        << ext_potential << " "
        << std::endl;

  for(int i = 0; i < theta1_arr.size(); i++){
    for(int j = 0; j < theta2_arr.size(); j++){
      //std::cout << ext_potential_arr.size() << std::endl;
      fout2 << theta1_arr[i] << " "
            << theta2_arr[j] << " "
            << ext_potential_arr[i][j] << " "
            << std::endl;
    }
  }
}

Environment::~Environment()
{
  fout1.close();
  fout2.close();
}

}

#endif //ENVIRONMENT
