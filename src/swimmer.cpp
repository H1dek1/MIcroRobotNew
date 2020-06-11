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

  std::cout << perm[0].getPos().x << " " << perm[0].getPos().y << std::endl;;
  std::cout << perm[1].getPos().x << " " << perm[1].getPos().y << std::endl;;
  std::cout << para.getPos().x << " " << para.getPos().y << std::endl;;
  
}


Swimmer::~Swimmer()
{
}

}

#endif //SWIMMER
