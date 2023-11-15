// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from inchworm_control:msg/Thruple.idl
// generated code does not contain a copyright notice
#include "inchworm_control/msg/detail/thruple__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
inchworm_control__msg__Thruple__init(inchworm_control__msg__Thruple * msg)
{
  if (!msg) {
    return false;
  }
  // motor1
  // motor2
  // motor3
  return true;
}

void
inchworm_control__msg__Thruple__fini(inchworm_control__msg__Thruple * msg)
{
  if (!msg) {
    return;
  }
  // motor1
  // motor2
  // motor3
}

bool
inchworm_control__msg__Thruple__are_equal(const inchworm_control__msg__Thruple * lhs, const inchworm_control__msg__Thruple * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // motor1
  if (lhs->motor1 != rhs->motor1) {
    return false;
  }
  // motor2
  if (lhs->motor2 != rhs->motor2) {
    return false;
  }
  // motor3
  if (lhs->motor3 != rhs->motor3) {
    return false;
  }
  return true;
}

bool
inchworm_control__msg__Thruple__copy(
  const inchworm_control__msg__Thruple * input,
  inchworm_control__msg__Thruple * output)
{
  if (!input || !output) {
    return false;
  }
  // motor1
  output->motor1 = input->motor1;
  // motor2
  output->motor2 = input->motor2;
  // motor3
  output->motor3 = input->motor3;
  return true;
}

inchworm_control__msg__Thruple *
inchworm_control__msg__Thruple__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  inchworm_control__msg__Thruple * msg = (inchworm_control__msg__Thruple *)allocator.allocate(sizeof(inchworm_control__msg__Thruple), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(inchworm_control__msg__Thruple));
  bool success = inchworm_control__msg__Thruple__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
inchworm_control__msg__Thruple__destroy(inchworm_control__msg__Thruple * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    inchworm_control__msg__Thruple__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
inchworm_control__msg__Thruple__Sequence__init(inchworm_control__msg__Thruple__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  inchworm_control__msg__Thruple * data = NULL;

  if (size) {
    data = (inchworm_control__msg__Thruple *)allocator.zero_allocate(size, sizeof(inchworm_control__msg__Thruple), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = inchworm_control__msg__Thruple__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        inchworm_control__msg__Thruple__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
inchworm_control__msg__Thruple__Sequence__fini(inchworm_control__msg__Thruple__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      inchworm_control__msg__Thruple__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

inchworm_control__msg__Thruple__Sequence *
inchworm_control__msg__Thruple__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  inchworm_control__msg__Thruple__Sequence * array = (inchworm_control__msg__Thruple__Sequence *)allocator.allocate(sizeof(inchworm_control__msg__Thruple__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = inchworm_control__msg__Thruple__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
inchworm_control__msg__Thruple__Sequence__destroy(inchworm_control__msg__Thruple__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    inchworm_control__msg__Thruple__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
inchworm_control__msg__Thruple__Sequence__are_equal(const inchworm_control__msg__Thruple__Sequence * lhs, const inchworm_control__msg__Thruple__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!inchworm_control__msg__Thruple__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
inchworm_control__msg__Thruple__Sequence__copy(
  const inchworm_control__msg__Thruple__Sequence * input,
  inchworm_control__msg__Thruple__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(inchworm_control__msg__Thruple);
    inchworm_control__msg__Thruple * data =
      (inchworm_control__msg__Thruple *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!inchworm_control__msg__Thruple__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          inchworm_control__msg__Thruple__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!inchworm_control__msg__Thruple__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
