// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from inchworm_control:msg/Tuple.idl
// generated code does not contain a copyright notice

#ifndef INCHWORM_CONTROL__MSG__DETAIL__TUPLE__BUILDER_HPP_
#define INCHWORM_CONTROL__MSG__DETAIL__TUPLE__BUILDER_HPP_

#include "inchworm_control/msg/detail/tuple__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace inchworm_control
{

namespace msg
{

namespace builder
{

class Init_Tuple_holding_block
{
public:
  explicit Init_Tuple_holding_block(::inchworm_control::msg::Tuple & msg)
  : msg_(msg)
  {}
  ::inchworm_control::msg::Tuple holding_block(::inchworm_control::msg::Tuple::_holding_block_type arg)
  {
    msg_.holding_block = std::move(arg);
    return std::move(msg_);
  }

private:
  ::inchworm_control::msg::Tuple msg_;
};

class Init_Tuple_step
{
public:
  Init_Tuple_step()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Tuple_holding_block step(::inchworm_control::msg::Tuple::_step_type arg)
  {
    msg_.step = std::move(arg);
    return Init_Tuple_holding_block(msg_);
  }

private:
  ::inchworm_control::msg::Tuple msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::inchworm_control::msg::Tuple>()
{
  return inchworm_control::msg::builder::Init_Tuple_step();
}

}  // namespace inchworm_control

#endif  // INCHWORM_CONTROL__MSG__DETAIL__TUPLE__BUILDER_HPP_
