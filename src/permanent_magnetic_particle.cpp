#ifndef PERMANENT
#define PERMANENT

#include "permanent_magnetic_particle.hpp"

namespace MicroRobot
{

PermanentParticle::PermanentParticle()
{
}

void PermanentParticle::reset(Vector2D init_pos, double init_angle)
{
  m_pos = init_pos;
  m_moment.setPolar(1.0, init_angle+(M_PI/2));
}

Vector2D PermanentParticle::getPos() const
{
  return m_pos;
}

PermanentParticle::~PermanentParticle()
{
}

}

#endif //PERMANENT
