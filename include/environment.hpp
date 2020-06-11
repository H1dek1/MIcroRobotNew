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
    ~Environment();
    void reset();

  public:
    void run();
};

}

#endif //ENVIRONMENT_H
