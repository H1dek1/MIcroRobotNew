#ifndef PARAMAGNETIC
#define PARAMAGNETIC

#include "paramagnetic_particle.hpp"

namespace MicroRobot
{

ParamagneticParticle::ParamagneticParticle()
{
}

void ParamagneticParticle::reset(Vector2D init_pos)
{
  m_pos = init_pos;
}

Vector2D ParamagneticParticle::getPos() const
{
  return m_pos;
}

ParamagneticParticle::~ParamagneticParticle()
{
}

}

#endif //PARAMAGNETIC
