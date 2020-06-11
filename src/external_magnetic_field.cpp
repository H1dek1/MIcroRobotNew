#ifndef EXT_FIELD
#define EXT_FIELD

#include "external_magnetic_field.hpp"

namespace MicroRobot
{

ExternalMagneticField::ExternalMagneticField()
{
}

void ExternalMagneticField::reset()
{
  m_moment.setPolar(1.0, FIELD_ANGLE+(M_PI/2));
}

Vector2D ExternalMagneticField::moment() const
{
  return m_moment;
}

void ExternalMagneticField::update(double time)
{
  double norm = cos(OMEGA * time);
  m_moment.setPolar(norm, FIELD_ANGLE+(M_PI/2));
}

ExternalMagneticField::~ExternalMagneticField()
{
}

}

#endif //EXT_FIELD
