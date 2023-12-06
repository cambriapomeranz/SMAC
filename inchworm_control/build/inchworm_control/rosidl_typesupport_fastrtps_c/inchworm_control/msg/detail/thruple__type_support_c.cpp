// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from inchworm_control:msg/Thruple.idl
// generated code does not contain a copyright notice
#include "inchworm_control/msg/detail/thruple__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "inchworm_control/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "inchworm_control/msg/detail/thruple__struct.h"
#include "inchworm_control/msg/detail/thruple__functions.h"
#include "fastcdr/Cdr.h"

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

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _Thruple__ros_msg_type = inchworm_control__msg__Thruple;

static bool _Thruple__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Thruple__ros_msg_type * ros_message = static_cast<const _Thruple__ros_msg_type *>(untyped_ros_message);
  // Field name: motor1
  {
    cdr << ros_message->motor1;
  }

  // Field name: motor2
  {
    cdr << ros_message->motor2;
  }

  // Field name: motor3
  {
    cdr << ros_message->motor3;
  }

  return true;
}

static bool _Thruple__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Thruple__ros_msg_type * ros_message = static_cast<_Thruple__ros_msg_type *>(untyped_ros_message);
  // Field name: motor1
  {
    cdr >> ros_message->motor1;
  }

  // Field name: motor2
  {
    cdr >> ros_message->motor2;
  }

  // Field name: motor3
  {
    cdr >> ros_message->motor3;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_inchworm_control
size_t get_serialized_size_inchworm_control__msg__Thruple(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Thruple__ros_msg_type * ros_message = static_cast<const _Thruple__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name motor1
  {
    size_t item_size = sizeof(ros_message->motor1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name motor2
  {
    size_t item_size = sizeof(ros_message->motor2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name motor3
  {
    size_t item_size = sizeof(ros_message->motor3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Thruple__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_inchworm_control__msg__Thruple(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_inchworm_control
size_t max_serialized_size_inchworm_control__msg__Thruple(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: motor1
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: motor2
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: motor3
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _Thruple__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_inchworm_control__msg__Thruple(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Thruple = {
  "inchworm_control::msg",
  "Thruple",
  _Thruple__cdr_serialize,
  _Thruple__cdr_deserialize,
  _Thruple__get_serialized_size,
  _Thruple__max_serialized_size
};

static rosidl_message_type_support_t _Thruple__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Thruple,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, inchworm_control, msg, Thruple)() {
  return &_Thruple__type_support;
}

#if defined(__cplusplus)
}
#endif
