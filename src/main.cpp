#include "environment.hpp"

int main(int argc, char **argv){

  if(argc != 6){
    std::cout << "Oops! 5 command line args are needed!" << std::endl;
    std::cout << "1(bool): move or not" << std::endl;
    std::cout << "2(string): 'new' or 'old' " << std::endl;
    std::cout << "3(double): alpha" << std::endl;
    std::cout << "4(double): beta" << std::endl;
    std::cout << "5(double): gamma" << std::endl;
    return 0;
  }

  bool can_move;
  bool new_model;
  double alpha;
  double beta;
  double gamma;

  std::string move_flag = argv[1];
  std::string new_flag  = argv[2];
  if(move_flag == "true"){
    can_move = true;
  }else if(move_flag == "false"){
    can_move = false;
  }else{
    std::cout << "Invalid values" << std::endl;
    return 0;
  }

  if(new_flag == "new"){
    new_model = true;
  }else if(new_flag == "old"){
    new_model = false;
  }else{
    std::cout << "Invalid values" << std::endl;
    return 0;
  }

  //double mn  = atof(argv[3]);
  //double trf = atof(argv[4]);
  //alpha = mn / trf;
  //beta  = MicroRobot::AbyL3 / mn;
  
  alpha = atof(argv[3]);
  beta  = atof(argv[4]);

  gamma = atof(argv[5]);

  MicroRobot::Environment env;
  env.run(can_move, new_model, alpha, beta, gamma);
  return 0;
}
