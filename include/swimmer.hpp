#ifndef SWIMMER_H
#define SWIMMER_H

#include "vector2d/vector_2d.hpp"
#include "permanent_magnetic_particle.hpp"
#include "paramagnetic_particle.hpp"

namespace MicroRobot
{

class Swimmer{
  private:
    PermanentParticle perm[2];
    ParamagneticParticle para;

    Vector2D m_center_pos;
    double m_center_angle;

  public:
    Swimmer();
    ~Swimmer();
    void reset();

  public:
    void update(Vector2D ext_field);
    Vector2D pos() const;
    double angle() const;
    std::tuple<double, double, Vector2D> getMoments();
};

}

#endif //SWIMMER_H

