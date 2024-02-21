// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from inchworm_control:msg/Tuple.idl
// generated code does not contain a copyright notice
#include "inchworm_control/msg/detail/tuple__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "inchworm_control/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "inchworm_control/msg/detail/tuple__struct.h"
#include "inchworm_control/msg/detail/tuple__functions.h"
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

#include "rosidl_runtime_c/string.h"  // step
#include "rosidl_runtime_c/string_functions.h"  // step

// forward declare type support functions


using _Tuple__ros_msg_type = inchworm_control__msg__Tuple;

static bool _Tuple__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Tuple__ros_msg_type * ros_message = static_cast<const _Tuple__ros_msg_type *>(untyped_ros_message);
  // Field name: step
  {
    const rosidl_runtime_c__String * str = &ros_message->step;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: holding_block
  {
    cdr << (ros_message->holding_block ? true : false);
  }

  return true;
}

static bool _Tuple__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Tuple__ros_msg_type * ros_message = static_cast<_Tuple__ros_msg_type *>(untyped_ros_message);
  // Field name: step
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->step.data) {
      rosidl_runtime_c__String__init(&ros_message->step);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->step,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'step'\n");
      return false;
    }
  }

  // Field name: holding_block
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->holding_block = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_inchworm_control
size_t get_serialized_size_inchworm_control__msg__Tuple(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Tuple__ros_msg_type * ros_message = static_cast<const _Tuple__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name step
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->step.size + 1);
  // field.name holding_block
  {
    size_t item_size = sizeof(ros_message->holding_block);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Tuple__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_inchworm_control__msg__Tuple(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_inchworm_control
size_t max_serialized_size_inchworm_control__msg__Tuple(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: step
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: holding_block
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _Tuple__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_inchworm_control__msg__Tuple(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Tuple = {
  "inchworm_control::msg",
  "Tuple",
  _Tuple__cdr_serialize,
  _Tuple__cdr_deserialize,
  _Tuple__get_serialized_size,
  _Tuple__max_serialized_size
};

static rosidl_message_type_support_t _Tuple__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Tuple,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, inchworm_control, msg, Tuple)() {
  return &_Tuple__type_support;
}

#if defined(__cplusplus)
}
#endif
