// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from inchworm_control:msg/Thruple.idl
// generated code does not contain a copyright notice

#ifndef INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__BUILDER_HPP_
#define INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__BUILDER_HPP_

#include "inchworm_control/msg/detail/thruple__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace inchworm_control
{

namespace msg
{

namespace builder
{

class Init_Thruple_motor3
{
public:
  explicit Init_Thruple_motor3(::inchworm_control::msg::Thruple & msg)
  : msg_(msg)
  {}
  ::inchworm_control::msg::Thruple motor3(::inchworm_control::msg::Thruple::_motor3_type arg)
  {
    msg_.motor3 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::inchworm_control::msg::Thruple msg_;
};

class Init_Thruple_motor2
{
public:
  explicit Init_Thruple_motor2(::inchworm_control::msg::Thruple & msg)
  : msg_(msg)
  {}
  Init_Thruple_motor3 motor2(::inchworm_control::msg::Thruple::_motor2_type arg)
  {
    msg_.motor2 = std::move(arg);
    return Init_Thruple_motor3(msg_);
  }

private:
  ::inchworm_control::msg::Thruple msg_;
};

class Init_Thruple_motor1
{
public:
  Init_Thruple_motor1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Thruple_motor2 motor1(::inchworm_control::msg::Thruple::_motor1_type arg)
  {
    msg_.motor1 = std::move(arg);
    return Init_Thruple_motor2(msg_);
  }

private:
  ::inchworm_control::msg::Thruple msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::inchworm_control::msg::Thruple>()
{
  return inchworm_control::msg::builder::Init_Thruple_motor1();
}

}  // namespace inchworm_control

#endif  // INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__BUILDER_HPP_
