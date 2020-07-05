#ifndef SWIMMER_H
#define SWIMMER_H

#include "vector2d/vector_2d.hpp"
#include "permanent_magnetic_particle.hpp"
#include "paramagnetic_particle.hpp"

namespace MicroRobot
{

class Swimmer{
  private:
    PermanentParticle perm[2];
    ParamagneticParticle para;

    Vector2D m_center_pos;
    Vector2D m_center_vel;
    double m_center_angle;
    double m_center_angle_vel;

  private:
    std::vector<double>   theta1_arr;
    std::vector<double>   theta2_arr;
    std::vector<Vector2D> moment0_arr;
    std::vector<Vector2D> moment1_arr;

  public:
    Swimmer();
    ~Swimmer();
    void reset();

  public:
    void update(Vector2D ext_field);
    Vector2D pos() const;
    double angle() const;
    std::tuple<double, double, Vector2D> getMoments();
    std::tuple<Vector2D, double> getPose() const;

  public:
    double extPotential(Vector2D ext_field) const;
    double dipolePotential() const;
    double paraExtPotentital(Vector2D ext_field) const;
    double paraDipolePotential() const;

  private:
    void calcParamagneticMoment(Vector2D ext_field);
    std::array<Vector2D, 2> calcFieldOnParticles(Vector2D ext_field);
    void calcCenterVelocity(Vector2D ext_field);
    void updateParticlesPosition();
};

}

#endif //SWIMMER_H

