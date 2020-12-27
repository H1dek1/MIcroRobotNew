#ifndef ENVIRONMENT
#define ENVIRONMENT

#include "environment.hpp"

namespace MicroRobot
{

Environment::Environment()
{
  fout1.open(FILENAME1, std::ios::out);
  theta1out.open("../result/theta1out.txt", std::ios::out);
  zout.open("../result/zout.txt", std::ios::out);
  params.open("../result/params.txt", std::ios::out);
  phases.open("../result/phases.txt", std::ios::app);

  fout1 << "OUT_TIME " << OUT_TIME << std::endl;
  fout1 << "# ext_x ext_y center_x center_y angle theta1 theta2 moment3_norm moment3_angle ext_potential" << std::endl;
  params << "DT " << "a " << "alpha " << "beta " << "gamma" << std::endl;
}

void Environment::run(
    bool can_move,
    bool new_model,
    double alpha,
    double beta,
    double gamma,
    double angle)
{
  params << OUT_TIME << " " 
         << AbyL << " " 
         << alpha << " " 
         << beta << " "  
         << gamma << std::endl;
  swimmer.reset(can_move, new_model, alpha, beta, gamma);
  field.reset(angle);

  /* aligning moments */
  for(int iter = 0; iter < SLEEP_ITER; iter++){
    swimmer.update( field.moment(), true);
  }

  //std::cout << NUM_CYCLES << std::endl;
  //std::cout << DT << std::endl;
  //std::cout << NUM_CYCLES / DT << std::endl;
  //std::cout << (int)(NUM_CYCLES / DT) << std::endl;
  //std::cout << MAX_ITER << std::endl;
  for(int iter = 0; iter < MAX_ITER+1; iter++){
  //for(int iter = 0; iter < 10; iter++){
    //std::cout << "ext: " << swimmer.extPotential( field.moment() ) << std::endl;
    //std::cout << "dipole: " << swimmer.dipolePotential() << std::endl;
    //std::cout << "extpara: " << swimmer.paraExtPotential( field.moment() ) << std::endl;
    //std::cout << "dipolepara: " << swimmer.paraDipolePotential() << std::endl;
    //std::cout << "all: " << swimmer.allPotential( field.moment() ) << std::endl;
    //std::cout << "--------------------" << std::endl;
    if(iter == MAX_ITER){
    //if(iter%(int(MAX_ITER/5)) == 0){
      auto [pos, angle] = swimmer.getPose();
      std::cout << std::setprecision(4) << iter << "/" << MAX_ITER;
      std::cout << std::scientific << std::setprecision(5) << " " << pos.x << " " << pos.y << " " << angle << " " << std::endl;

    }
    if(iter%OUT_ITER == 0) output(iter);
    if(iter == MAX_ITER){
      phases << alpha << " "
             << beta << " "
             << gamma << " "
             << MAX_ITER << " "
             << swimmer.pos().x << " "
             << swimmer.pos().y << " "
             << angle << " "
             << std::endl;

    }
    
    swimmer.update( field.moment(), false);
    field.update( iter * DT );

    //output();
  }
}

void Environment::output(int iter)
{
  auto [theta1, theta2, para_moment] = swimmer.getMoments();
  double all_potential = swimmer.allPotential( field.moment() );
  fout1 << field.moment().x << " "
       << field.moment().y << " "
       << swimmer.pos().x << " "
       << swimmer.pos().y << " "
       << swimmer.angle() << " "
       << theta1 << " "
       << theta2 << " "
       << para_moment.x << " "
       << para_moment.y << " "
       << all_potential << " "
       << std::endl;

  theta1out << iter*DT << " " << theta1 << std::endl;
  zout << iter*DT << " " << swimmer.pos().x << std::endl;
}

Environment::~Environment()
{
  fout1.close();
  theta1out.close();
  zout.close();
  params.close();
  phases.close();
}

}

#endif //ENVIRONMENT
