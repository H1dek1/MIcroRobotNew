#ifndef PARAMAGNETIC_H
#define PARAMAGNETIC_H

#include "vector2d/vector_2d.hpp"
#include "dimentionless_parameters.hpp"

namespace MicroRobot
{

class ParamagneticParticle{
  private:
    Vector2D m_pos;
    Vector2D m_vel;
    Vector2D m_moment;

  public:
    ParamagneticParticle();
    ~ParamagneticParticle();
    void reset(Vector2D init_pos);

  public:
    Vector2D pos() const;
    Vector2D moment() const;
    void calcMoment(Vector2D external_field);
};

}

#endif //PARAMAGNETIC_H
