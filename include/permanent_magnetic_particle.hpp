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
    double   m_angle;
    double   m_omega;
    double beta;
  public:
    double   m_torque;

    
  public:
    PermanentParticle();
    ~PermanentParticle();
    void reset(Vector2D init_pos, double init_angle, double beta_);

  public:
    Vector2D pos() const;
    Vector2D moment() const;
    double   radians() const;
    double calcTorque(Vector2D field);
    Vector2D rotate(double ext_torque, Vector2D rel_pos);
    void setPosition(double xx, double yy);
};

}

#endif //PERMANENT_H
