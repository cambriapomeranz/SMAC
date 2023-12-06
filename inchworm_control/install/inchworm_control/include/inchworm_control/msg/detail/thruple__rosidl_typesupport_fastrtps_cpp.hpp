// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from inchworm_control:msg/Thruple.idl
// generated code does not contain a copyright notice

#ifndef INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "inchworm_control/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "inchworm_control/msg/detail/thruple__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace inchworm_control
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_inchworm_control
cdr_serialize(
  const inchworm_control::msg::Thruple & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_inchworm_control
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  inchworm_control::msg::Thruple & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_inchworm_control
get_serialized_size(
  const inchworm_control::msg::Thruple & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_inchworm_control
max_serialized_size_Thruple(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace inchworm_control

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_inchworm_control
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, inchworm_control, msg, Thruple)();

#ifdef __cplusplus
}
#endif

#endif  // INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
