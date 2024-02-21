// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from inchworm_control:msg/Tuple.idl
// generated code does not contain a copyright notice
#include "inchworm_control/msg/detail/tuple__rosidl_typesupport_fastrtps_cpp.hpp"
#include "inchworm_control/msg/detail/tuple__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace inchworm_control
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_inchworm_control
cdr_serialize(
  const inchworm_control::msg::Tuple & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: step
  cdr << ros_message.step;
  // Member: holding_block
  cdr << (ros_message.holding_block ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_inchworm_control
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  inchworm_control::msg::Tuple & ros_message)
{
  // Member: step
  cdr >> ros_message.step;

  // Member: holding_block
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.holding_block = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_inchworm_control
get_serialized_size(
  const inchworm_control::msg::Tuple & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: step
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.step.size() + 1);
  // Member: holding_block
  {
    size_t item_size = sizeof(ros_message.holding_block);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_inchworm_control
max_serialized_size_Tuple(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: step
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: holding_block
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _Tuple__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const inchworm_control::msg::Tuple *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Tuple__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<inchworm_control::msg::Tuple *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Tuple__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const inchworm_control::msg::Tuple *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Tuple__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_Tuple(full_bounded, 0);
}

static message_type_support_callbacks_t _Tuple__callbacks = {
  "inchworm_control::msg",
  "Tuple",
  _Tuple__cdr_serialize,
  _Tuple__cdr_deserialize,
  _Tuple__get_serialized_size,
  _Tuple__max_serialized_size
};

static rosidl_message_type_support_t _Tuple__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Tuple__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace inchworm_control

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_inchworm_control
const rosidl_message_type_support_t *
get_message_type_support_handle<inchworm_control::msg::Tuple>()
{
  return &inchworm_control::msg::typesupport_fastrtps_cpp::_Tuple__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, inchworm_control, msg, Tuple)() {
  return &inchworm_control::msg::typesupport_fastrtps_cpp::_Tuple__handle;
}

#ifdef __cplusplus
}
#endif
