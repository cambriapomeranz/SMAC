// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from inchworm_control:msg/Tuple.idl
// generated code does not contain a copyright notice

#ifndef INCHWORM_CONTROL__MSG__DETAIL__TUPLE__STRUCT_H_
#define INCHWORM_CONTROL__MSG__DETAIL__TUPLE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'step'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/Tuple in the package inchworm_control.
typedef struct inchworm_control__msg__Tuple
{
  rosidl_runtime_c__String step;
  bool holding_block;
} inchworm_control__msg__Tuple;

// Struct for a sequence of inchworm_control__msg__Tuple.
typedef struct inchworm_control__msg__Tuple__Sequence
{
  inchworm_control__msg__Tuple * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} inchworm_control__msg__Tuple__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INCHWORM_CONTROL__MSG__DETAIL__TUPLE__STRUCT_H_
