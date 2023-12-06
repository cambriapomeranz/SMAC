// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from inchworm_control:msg/Thruple.idl
// generated code does not contain a copyright notice

#ifndef INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__FUNCTIONS_H_
#define INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "inchworm_control/msg/rosidl_generator_c__visibility_control.h"

#include "inchworm_control/msg/detail/thruple__struct.h"

/// Initialize msg/Thruple message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * inchworm_control__msg__Thruple
 * )) before or use
 * inchworm_control__msg__Thruple__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
bool
inchworm_control__msg__Thruple__init(inchworm_control__msg__Thruple * msg);

/// Finalize msg/Thruple message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
void
inchworm_control__msg__Thruple__fini(inchworm_control__msg__Thruple * msg);

/// Create msg/Thruple message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * inchworm_control__msg__Thruple__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
inchworm_control__msg__Thruple *
inchworm_control__msg__Thruple__create();

/// Destroy msg/Thruple message.
/**
 * It calls
 * inchworm_control__msg__Thruple__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
void
inchworm_control__msg__Thruple__destroy(inchworm_control__msg__Thruple * msg);

/// Check for msg/Thruple message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
bool
inchworm_control__msg__Thruple__are_equal(const inchworm_control__msg__Thruple * lhs, const inchworm_control__msg__Thruple * rhs);

/// Copy a msg/Thruple message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
bool
inchworm_control__msg__Thruple__copy(
  const inchworm_control__msg__Thruple * input,
  inchworm_control__msg__Thruple * output);

/// Initialize array of msg/Thruple messages.
/**
 * It allocates the memory for the number of elements and calls
 * inchworm_control__msg__Thruple__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
bool
inchworm_control__msg__Thruple__Sequence__init(inchworm_control__msg__Thruple__Sequence * array, size_t size);

/// Finalize array of msg/Thruple messages.
/**
 * It calls
 * inchworm_control__msg__Thruple__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
void
inchworm_control__msg__Thruple__Sequence__fini(inchworm_control__msg__Thruple__Sequence * array);

/// Create array of msg/Thruple messages.
/**
 * It allocates the memory for the array and calls
 * inchworm_control__msg__Thruple__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
inchworm_control__msg__Thruple__Sequence *
inchworm_control__msg__Thruple__Sequence__create(size_t size);

/// Destroy array of msg/Thruple messages.
/**
 * It calls
 * inchworm_control__msg__Thruple__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
void
inchworm_control__msg__Thruple__Sequence__destroy(inchworm_control__msg__Thruple__Sequence * array);

/// Check for msg/Thruple message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
bool
inchworm_control__msg__Thruple__Sequence__are_equal(const inchworm_control__msg__Thruple__Sequence * lhs, const inchworm_control__msg__Thruple__Sequence * rhs);

/// Copy an array of msg/Thruple messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_inchworm_control
bool
inchworm_control__msg__Thruple__Sequence__copy(
  const inchworm_control__msg__Thruple__Sequence * input,
  inchworm_control__msg__Thruple__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__FUNCTIONS_H_
