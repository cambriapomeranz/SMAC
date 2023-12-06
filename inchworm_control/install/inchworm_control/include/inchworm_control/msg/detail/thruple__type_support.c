// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from inchworm_control:msg/Thruple.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "inchworm_control/msg/detail/thruple__rosidl_typesupport_introspection_c.h"
#include "inchworm_control/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "inchworm_control/msg/detail/thruple__functions.h"
#include "inchworm_control/msg/detail/thruple__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void Thruple__rosidl_typesupport_introspection_c__Thruple_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  inchworm_control__msg__Thruple__init(message_memory);
}

void Thruple__rosidl_typesupport_introspection_c__Thruple_fini_function(void * message_memory)
{
  inchworm_control__msg__Thruple__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Thruple__rosidl_typesupport_introspection_c__Thruple_message_member_array[3] = {
  {
    "motor1",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inchworm_control__msg__Thruple, motor1),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "motor2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inchworm_control__msg__Thruple, motor2),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "motor3",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inchworm_control__msg__Thruple, motor3),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Thruple__rosidl_typesupport_introspection_c__Thruple_message_members = {
  "inchworm_control__msg",  // message namespace
  "Thruple",  // message name
  3,  // number of fields
  sizeof(inchworm_control__msg__Thruple),
  Thruple__rosidl_typesupport_introspection_c__Thruple_message_member_array,  // message members
  Thruple__rosidl_typesupport_introspection_c__Thruple_init_function,  // function to initialize message memory (memory has to be allocated)
  Thruple__rosidl_typesupport_introspection_c__Thruple_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Thruple__rosidl_typesupport_introspection_c__Thruple_message_type_support_handle = {
  0,
  &Thruple__rosidl_typesupport_introspection_c__Thruple_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_inchworm_control
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, inchworm_control, msg, Thruple)() {
  if (!Thruple__rosidl_typesupport_introspection_c__Thruple_message_type_support_handle.typesupport_identifier) {
    Thruple__rosidl_typesupport_introspection_c__Thruple_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Thruple__rosidl_typesupport_introspection_c__Thruple_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
