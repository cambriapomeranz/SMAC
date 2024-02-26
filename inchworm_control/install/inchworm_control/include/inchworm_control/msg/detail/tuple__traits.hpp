// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from inchworm_control:msg/Tuple.idl
// generated code does not contain a copyright notice

#ifndef INCHWORM_CONTROL__MSG__DETAIL__TUPLE__TRAITS_HPP_
#define INCHWORM_CONTROL__MSG__DETAIL__TUPLE__TRAITS_HPP_

#include "inchworm_control/msg/detail/tuple__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<inchworm_control::msg::Tuple>()
{
  return "inchworm_control::msg::Tuple";
}

template<>
inline const char * name<inchworm_control::msg::Tuple>()
{
  return "inchworm_control/msg/Tuple";
}

template<>
struct has_fixed_size<inchworm_control::msg::Tuple>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<inchworm_control::msg::Tuple>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<inchworm_control::msg::Tuple>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INCHWORM_CONTROL__MSG__DETAIL__TUPLE__TRAITS_HPP_
