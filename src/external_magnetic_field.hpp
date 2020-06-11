#ifndef EXT_FIELD_H
#define EXT_FIELD_H

#include "vector2d/vector_2d.hpp"
#include "dimentionless_parameters.hpp"
namespace MicroRobot
{

class ExternalMagneticField{
  private:
    Vector2D m_moment;

  public:
    ExternalMagneticField();
    ~ExternalMagneticField();
    void reset();
};

}

#endif //EXT_FIELD_H
