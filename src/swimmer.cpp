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
  calcCenterVelocity( ext_field );
  /* move all particles */
  updateParticlesPosition();
}

void Swimmer::calcCenterVelocity(Vector2D ext_field)
{
  std::array<Vector2D, 2> field;
  std::array<double, 2> torque;
  std::array<Vector2D, 2> velocity;
  field = calcFieldOnParticles( ext_field );

  for(int id = 0; id < 2; id++){
    torque[id] = perm[id].calcTorque( field[id] );
    velocity[0] = perm[0].rotate(torque[1], perm[1].pos());
    velocity[1] = perm[1].rotate(torque[0], perm[0].pos());
  }
  m_center_vel = (velocity[0] + velocity[1])/2;
  Vector2D unit;
  unit.setPolar(1, m_center_angle+(M_PI/2));
  m_center_angle_vel = (velocity[0] - velocity[1]).dot(unit);
}

std::array<Vector2D, 2> Swimmer::calcFieldOnParticles(Vector2D ext_field)
{
  std::array<Vector2D, 2> field;
  field[0] = (perm[1].pos() - perm[0].pos())*3*perm[1].moment().dot(perm[1].pos() - perm[0].pos()) - perm[1].moment();
  field[0] += (para.pos() - perm[0].pos())*3*para.moment().dot(para.pos() - perm[0].pos()) - para.moment();
  field[1] = (perm[0].pos() - perm[1].pos())*3*perm[0].moment().dot(perm[0].pos() - perm[1].pos()) - perm[0].moment();
  field[1] += (para.pos() - perm[1].pos())*3*para.moment().dot(para.pos() - perm[1].pos()) - para.moment();
  return field;
}

void Swimmer::updateParticlesPosition()
{
  m_center_pos += m_center_vel * DT;
  m_center_angle += m_center_angle_vel * DT;
  perm[0].setPosition( 
      m_center_pos.x - (0.5*cos(m_center_angle)),
      m_center_pos.y - (0.5*sin(m_center_angle))
      );
  perm[1].setPosition( 
      m_center_pos.x + (0.5*cos(m_center_angle)),
      m_center_pos.y + (0.5*sin(m_center_angle))
      );

  para.setPosition(
      m_center_pos.x - HIGHT*sin(m_center_angle),
      m_center_pos.y + HIGHT*cos(m_center_angle)
      );
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
