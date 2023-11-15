// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from inchworm_control:msg/Thruple.idl
// generated code does not contain a copyright notice

#ifndef INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__STRUCT_H_
#define INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/Thruple in the package inchworm_control.
typedef struct inchworm_control__msg__Thruple
{
  float motor1;
  float motor2;
  float motor3;
} inchworm_control__msg__Thruple;

// Struct for a sequence of inchworm_control__msg__Thruple.
typedef struct inchworm_control__msg__Thruple__Sequence
{
  inchworm_control__msg__Thruple * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} inchworm_control__msg__Thruple__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__STRUCT_H_
