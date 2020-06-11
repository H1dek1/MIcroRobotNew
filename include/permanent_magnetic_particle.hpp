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
    
  public:
    PermanentParticle();
    ~PermanentParticle();
    void reset(Vector2D init_pos, double init_angle);

  public:
    Vector2D pos() const;
    Vector2D moment() const;
};

}

#endif //PERMANENT_H
