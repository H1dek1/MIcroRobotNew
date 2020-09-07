#ifndef ENVIRONMENT_H
#define ENVIRONMENT_H

#include "swimmer.hpp"
#include "external_magnetic_field.hpp"

namespace MicroRobot
{

class Environment{
  private:
    Swimmer swimmer;
    ExternalMagneticField field;
    
  public:
    Environment();
    Environment(
        bool can_move,
        bool new_model,
        double alpha_,
        double beta_,
        double gamma_);

    ~Environment();
    void reset();

  public:
    void run();
    void run(bool can_move, bool new_model, double alpha, double beta, double gamma);
    void output(int iter);

  private:
    std::ofstream fout1;
    std::ofstream theta1out;
    std::ofstream zout;
};

}

#endif //ENVIRONMENT_H
