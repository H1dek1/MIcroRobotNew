#ifndef SWIMMER
#define SWIMMER

#include "swimmer.hpp"

namespace MicroRobot
{

Swimmer::Swimmer()
{
}

void Swimmer::reset()
{
  m_center_pos.assign(0.0, 0.0);
  m_center_angle = 0.0;

  Vector2D pos_1(
      m_center_pos.x - (0.5*cos(m_center_angle)),
      m_center_pos.y - (0.5*sin(m_center_angle))
      );
  Vector2D pos_2(
      m_center_pos.x + (0.5*cos(m_center_angle)),
      m_center_pos.y + (0.5*sin(m_center_angle))
      );
  Vector2D pos_3(
      m_center_pos.x - HIGHT*sin(m_center_angle),
      m_center_pos.y + HIGHT*cos(m_center_angle)
      );

  perm[0].reset(pos_1, INIT_ANGLE_1);
  perm[1].reset(pos_2, INIT_ANGLE_2);
  para.reset(pos_3);
  
}

void Swimmer::update(Vector2D ext_field)
{
  /* Paramagnetic Moment */
  calcParamagneticMoment( ext_field );
  /* Rotating permanent particles */
  rotateParticles( ext_field );
}

void Swimmer::rotateParticles(Vector2D ext_field)
{
  std::vector<Vector2D> field;
  std::vector<double> torque;
  field = calcFieldOnParticles( ext_field );
  for(int id = 0; id < 2; id++)
    torque[id] = perm[id].calcTorque( field[id] );
  
  perm[0].calcVelocity( torque[1] );
  perm[1].calcVelocity( torque[0] );
}

std::vector<Vector2D> Swimmer::calcFieldOnParticles(Vector2D ext_field)
{
  std::vector<Vector2D> field;
  field[0] = ext_field;
  field[1] = ext_field;
  return field;
}


void Swimmer::calcParamagneticMoment(Vector2D ext_field)
{
  //set paramagnetic moment
  Vector2D all_field = ext_field;
  for(int id = 0; id < 2; id++){
    Vector2D para2perm = perm[id].pos() - para.pos();

    Vector2D dipole_field = para2perm;
    dipole_field *= 3 * para2perm.dot(perm[id].moment());
    dipole_field -= perm[id].moment();
    dipole_field /= ALPHA;
    all_field += dipole_field;
  }
  para.calcMoment( all_field );

}

Vector2D Swimmer::pos() const
{
  return m_center_pos;
}

double Swimmer::angle() const
{
  return m_center_angle;
}

std::tuple<double, double, Vector2D> Swimmer::getMoments()
{
  return {perm[0].moment().radians(), perm[1].moment().radians(), para.moment()};
}


Swimmer::~Swimmer()
{
}

}

#endif //SWIMMER
