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
  m_angle = init_angle+(M_PI/2);
  m_moment.setPolar(1.0, m_angle);
}

Vector2D PermanentParticle::pos() const
{
  return m_pos;
}

Vector2D PermanentParticle::moment() const
{
  return m_moment;
}

double PermanentParticle::radians() const
{
  return m_angle;
}

double PermanentParticle::calcTorque(Vector2D field)
{
  m_torque = (m_moment.x * field.y) - (m_moment.y * field.x);
  return m_torque;
}

Vector2D PermanentParticle::rotate(double ext_torque, Vector2D rel_pos)
{
  m_omega = (BETA/AbyL3)*m_torque - (BETA/2)*ext_torque;
  m_angle += m_omega*DT;
  m_moment.setPolar(1.0, m_angle);
  m_vel.x = -BETA*(rel_pos.y - m_pos.y) * m_torque;
  m_vel.y =  BETA*(rel_pos.x - m_pos.x) * m_torque;
  return m_vel;
}

void PermanentParticle::setPosition(double xx, double yy)
{
  m_pos.x = xx;
  m_pos.y = yy;
}

PermanentParticle::~PermanentParticle()
{
}

}

#endif //PERMANENT
