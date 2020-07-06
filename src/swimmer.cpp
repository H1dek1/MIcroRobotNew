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
  m_center_angle = ROBOT_ANGLE;

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
  
  /* GRID */
  for(int id = 0; id < (THETA_MAX - THETA_MIN)/D_THETA+1; id++){
    theta1_arr.push_back(THETA_MIN + (id*D_THETA));
    theta2_arr.push_back(THETA_MIN + (id*D_THETA));
    Vector2D moment(cos(THETA_MIN + (id*D_THETA)), sin(THETA_MIN + (id*D_THETA)));
    moment0_arr.push_back(moment);
    moment1_arr.push_back(moment);
  }
}

std::tuple<Vector2D, double> Swimmer::getPose() const
{
  return {m_center_pos, m_center_angle};
}


void Swimmer::update(Vector2D ext_field)
{
  /* Paramagnetic Moment */
  calcParamagneticMoment( ext_field );
  /* Rotating permanent particles */
  calcCenterVelocity( ext_field );
  /* move all particles */
  if(MOVE == true) updateParticlesPosition();
}

void Swimmer::calcCenterVelocity(Vector2D ext_field)
{
  std::array<Vector2D, 2> field;
  std::array<Vector2D, 2> tmp_field;
  std::array<double, 2> torque;
  std::array<Vector2D, 2> velocity;
  field = calcFieldOnParticles( ext_field );

  for(int id = 0; id < 2; id++){
    torque[id] = perm[id].calcTorque( field[id] );
  }
    velocity[0] = perm[0].rotate(torque[1], perm[1].pos());
    velocity[1] = perm[1].rotate(torque[0], perm[0].pos());

  m_center_vel = (velocity[0] + velocity[1])/2;
  Vector2D unit;
  unit.setPolar(1, m_center_angle+(M_PI/2));
  m_center_angle_vel = (velocity[0] - velocity[1]).dot(unit);
}

std::array<Vector2D, 2> Swimmer::calcFieldOnParticles(Vector2D ext_field)
{
  std::array<Vector2D, 2> field;
  std::array<Vector2D, 2> para_field;
  std::array<Vector2D, 2> dipole_field;

  dipole_field[0] = (perm[1].pos() - perm[0].pos())*3*perm[1].moment().innerProduct(perm[1].pos() - perm[0].pos()) - perm[1].moment();

  dipole_field[1] = (perm[0].pos() - perm[1].pos())*3*perm[0].moment().innerProduct(perm[0].pos() - perm[1].pos()) - perm[0].moment();

  para_field[0] = (para.pos() - perm[0].pos())*3*para.moment().innerProduct(para.pos() - perm[0].pos()) - para.moment();
  para_field[1] = (para.pos() - perm[1].pos())*3*para.moment().innerProduct(para.pos() - perm[1].pos()) - para.moment();

  field[0] = ext_field * ALPHA;
  field[1] = ext_field * ALPHA;
  //std::cout << "field=ext" << std::endl;
  //std::cout << field[0].x << " " << field[0].y << std::endl;
  //std::cout << field[1].x << " " << field[1].y << std::endl;

  field[0] += dipole_field[0];
  field[1] += dipole_field[1];

  //std::cout << "field=ext+dipole" << std::endl;
  //std::cout << field[0].x << " " << field[0].y << std::endl;
  //std::cout << field[1].x << " " << field[1].y << std::endl;

  field[0] += para_field[0];
  field[1] += para_field[1];

  //std::cout << "field=ext+dipole+para" << std::endl;
  //std::cout << field[0].x << " " << field[0].y << std::endl;
  //std::cout << field[1].x << " " << field[1].y << std::endl;

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
  return {perm[0].radians(), perm[1].radians(), para.moment()};
}

double Swimmer::allPotential(Vector2D ext_field) const
{
  double all_potential = 0;
  all_potential += extPotential( ext_field );
  all_potential += dipolePotential();
  //all_potential += paraExtPotential();

  return all_potential;
}

double Swimmer::extPotential(Vector2D ext_field) const
{
  std::array<double, 2> ext_potential;
  ext_potential[0] = -2 * ALPHA * perm[0].moment().dot(ext_field);
  ext_potential[1] = -2 * ALPHA * perm[1].moment().dot(ext_field);

  return (ext_potential[0]+ext_potential[1]);
}

double Swimmer::dipolePotential() const
{
  double dipole_potential;
  double phi_0 = perm[0].radians();
  double phi_1 = perm[1].radians();
  double psi = m_center_angle;
  dipole_potential = - (3.0 * cos(phi_0 + phi_1 - (2*psi)) + cos(phi_0 - phi_1));

  return dipole_potential;
}

double Swimmer::paraExtPotential() const
{
  std::array<double, 2> para_ext_potential;
  std::array<Vector2D, 2> para_field;

  para_field[0] = (para.pos() - perm[0].pos())*3*para.moment().innerProduct(para.pos() - perm[0].pos()) - para.moment();
  para_field[1] = (para.pos() - perm[1].pos())*3*para.moment().innerProduct(para.pos() - perm[1].pos()) - para.moment();

  //para_ext_potential[0] = -2 * ALPHA * perm[0].moment().dot(para_field[0]);
  //para_ext_potential[1] = -2 * ALPHA * perm[1].moment().dot(para_field[1]);

  return (para_ext_potential[0]+para_ext_potential[1]);
}

Swimmer::~Swimmer()
{
}

}

#endif //SWIMMER
