// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from inchworm_control:msg/Tuple.idl
// generated code does not contain a copyright notice
#include "inchworm_control/msg/detail/tuple__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `step`
#include "rosidl_runtime_c/string_functions.h"

bool
inchworm_control__msg__Tuple__init(inchworm_control__msg__Tuple * msg)
{
  if (!msg) {
    return false;
  }
  // step
  if (!rosidl_runtime_c__String__init(&msg->step)) {
    inchworm_control__msg__Tuple__fini(msg);
    return false;
  }
  // holding_block
  return true;
}

void
inchworm_control__msg__Tuple__fini(inchworm_control__msg__Tuple * msg)
{
  if (!msg) {
    return;
  }
  // step
  rosidl_runtime_c__String__fini(&msg->step);
  // holding_block
}

bool
inchworm_control__msg__Tuple__are_equal(const inchworm_control__msg__Tuple * lhs, const inchworm_control__msg__Tuple * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // step
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->step), &(rhs->step)))
  {
    return false;
  }
  // holding_block
  if (lhs->holding_block != rhs->holding_block) {
    return false;
  }
  return true;
}

bool
inchworm_control__msg__Tuple__copy(
  const inchworm_control__msg__Tuple * input,
  inchworm_control__msg__Tuple * output)
{
  if (!input || !output) {
    return false;
  }
  // step
  if (!rosidl_runtime_c__String__copy(
      &(input->step), &(output->step)))
  {
    return false;
  }
  // holding_block
  output->holding_block = input->holding_block;
  return true;
}

inchworm_control__msg__Tuple *
inchworm_control__msg__Tuple__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  inchworm_control__msg__Tuple * msg = (inchworm_control__msg__Tuple *)allocator.allocate(sizeof(inchworm_control__msg__Tuple), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(inchworm_control__msg__Tuple));
  bool success = inchworm_control__msg__Tuple__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
inchworm_control__msg__Tuple__destroy(inchworm_control__msg__Tuple * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    inchworm_control__msg__Tuple__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
inchworm_control__msg__Tuple__Sequence__init(inchworm_control__msg__Tuple__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  inchworm_control__msg__Tuple * data = NULL;

  if (size) {
    data = (inchworm_control__msg__Tuple *)allocator.zero_allocate(size, sizeof(inchworm_control__msg__Tuple), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = inchworm_control__msg__Tuple__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        inchworm_control__msg__Tuple__fini(&data[i - 1]);
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
inchworm_control__msg__Tuple__Sequence__fini(inchworm_control__msg__Tuple__Sequence * array)
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
      inchworm_control__msg__Tuple__fini(&array->data[i]);
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

inchworm_control__msg__Tuple__Sequence *
inchworm_control__msg__Tuple__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  inchworm_control__msg__Tuple__Sequence * array = (inchworm_control__msg__Tuple__Sequence *)allocator.allocate(sizeof(inchworm_control__msg__Tuple__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = inchworm_control__msg__Tuple__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
inchworm_control__msg__Tuple__Sequence__destroy(inchworm_control__msg__Tuple__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    inchworm_control__msg__Tuple__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
inchworm_control__msg__Tuple__Sequence__are_equal(const inchworm_control__msg__Tuple__Sequence * lhs, const inchworm_control__msg__Tuple__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!inchworm_control__msg__Tuple__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
inchworm_control__msg__Tuple__Sequence__copy(
  const inchworm_control__msg__Tuple__Sequence * input,
  inchworm_control__msg__Tuple__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(inchworm_control__msg__Tuple);
    inchworm_control__msg__Tuple * data =
      (inchworm_control__msg__Tuple *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!inchworm_control__msg__Tuple__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          inchworm_control__msg__Tuple__fini(&data[i]);
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
    if (!inchworm_control__msg__Tuple__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
