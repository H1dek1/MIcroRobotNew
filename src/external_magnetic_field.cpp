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
  std::cout << m_moment.x << " " << m_moment.y << std::endl;
}

ExternalMagneticField::~ExternalMagneticField()
{
}

}

#endif //EXT_FIELD
