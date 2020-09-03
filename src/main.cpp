#include "environment.hpp"

int main(int argc, char **argv){
  bool can_move;
  bool new_model;
  double alpha;
  double beta;
  double gamma;

  if(argc == 6){
    std::string move_flag = argv[1];
    std::string new_flag  = argv[2];
    if(move_flag == "true"){
      can_move = true;
    }else if(move_flag == "false"){
      can_move = false;
    }

    if(new_flag == "true"){
      new_model = true;
    }else if(new_flag == "false"){
      new_model = false;
    }

    alpha = atof(argv[3]);
    beta  = atof(argv[4]);
    gamma = atof(argv[5]);

    MicroRobot::Environment env;
    env.run(can_move, new_model, alpha, beta, gamma);
  }else{
    std::cout << "Oops! 5 command line arguments needed !" << std::endl;
    std::cout << "1(bool): move or not" << std::endl;
    std::cout << "2(bool): new model or not" << std::endl;
    std::cout << "3(double): alpha" << std::endl;
    std::cout << "4(double): beta" << std::endl;
    std::cout << "5(double): gamma" << std::endl;
  }

  return 0;
}
