#ifndef EXT_FIELD_H
#define EXT_FIELD_H

#include "vector2d/vector_2d.hpp"
#include "dimentionless_parameters.hpp"
namespace MicroRobot
{

class ExternalMagneticField{
  private:
    Vector2D m_moment;
    double angle;

  public:
    ExternalMagneticField();
    ~ExternalMagneticField();
    void reset(double field_angle);

  public:
    void update(double time);
    void zeroVector();
    void XVector();
    Vector2D moment() const;
};

}

#endif //EXT_FIELD_H
