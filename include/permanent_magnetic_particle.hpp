#ifndef PERMANENT_H
#define PERMANENT_H

#include "vector2d/vector_2d.hpp"
#include "dimentionless_parameters.hpp"

namespace MicroRobot
{

class PermanentParticle{
  private:
    Vector2D m_pos;
    Vector2D m_vel;
    Vector2D m_moment;
    double   m_torque;
    
  public:
    PermanentParticle();
    ~PermanentParticle();
    void reset(Vector2D init_pos, double init_angle);

  public:
    Vector2D pos() const;
    Vector2D moment() const;
    double calcTorque(Vector2D field);
    void calcVelocity(double ext_torque);
};

}

#endif //PERMANENT_H
