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

  public:
    void update(double time);
    Vector2D moment() const;
};

}

#endif //EXT_FIELD_H
