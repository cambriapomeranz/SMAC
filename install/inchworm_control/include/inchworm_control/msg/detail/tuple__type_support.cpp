// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from inchworm_control:msg/Tuple.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "inchworm_control/msg/detail/tuple__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace inchworm_control
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Tuple_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) inchworm_control::msg::Tuple(_init);
}

void Tuple_fini_function(void * message_memory)
{
  auto typed_message = static_cast<inchworm_control::msg::Tuple *>(message_memory);
  typed_message->~Tuple();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Tuple_message_member_array[2] = {
  {
    "step",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inchworm_control::msg::Tuple, step),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "holding_block",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inchworm_control::msg::Tuple, holding_block),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Tuple_message_members = {
  "inchworm_control::msg",  // message namespace
  "Tuple",  // message name
  2,  // number of fields
  sizeof(inchworm_control::msg::Tuple),
  Tuple_message_member_array,  // message members
  Tuple_init_function,  // function to initialize message memory (memory has to be allocated)
  Tuple_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Tuple_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Tuple_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace inchworm_control


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<inchworm_control::msg::Tuple>()
{
  return &::inchworm_control::msg::rosidl_typesupport_introspection_cpp::Tuple_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, inchworm_control, msg, Tuple)() {
  return &::inchworm_control::msg::rosidl_typesupport_introspection_cpp::Tuple_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
