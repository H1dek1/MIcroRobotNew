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

Vector2D ParamagneticParticle::pos() const
{
  return m_pos;
}

Vector2D ParamagneticParticle::moment() const
{
  return m_moment;
}

void ParamagneticParticle::calcMoment(Vector2D external_field)
{
  m_moment = external_field;
  m_moment *= GAMMA;
  //std::cout << "para Moment" << std::endl;
  //std::cout << m_moment.degrees() << std::endl;
}

void ParamagneticParticle::setPosition(double xx, double yy)
{
  m_pos.x = xx;
  m_pos.y = yy;
}

ParamagneticParticle::~ParamagneticParticle()
{
}

}

#endif //PARAMAGNETIC
