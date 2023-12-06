// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from inchworm_control:msg/Thruple.idl
// generated code does not contain a copyright notice

#ifndef INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__STRUCT_HPP_
#define INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__inchworm_control__msg__Thruple __attribute__((deprecated))
#else
# define DEPRECATED__inchworm_control__msg__Thruple __declspec(deprecated)
#endif

namespace inchworm_control
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Thruple_
{
  using Type = Thruple_<ContainerAllocator>;

  explicit Thruple_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->motor1 = 0.0f;
      this->motor2 = 0.0f;
      this->motor3 = 0.0f;
    }
  }

  explicit Thruple_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->motor1 = 0.0f;
      this->motor2 = 0.0f;
      this->motor3 = 0.0f;
    }
  }

  // field types and members
  using _motor1_type =
    float;
  _motor1_type motor1;
  using _motor2_type =
    float;
  _motor2_type motor2;
  using _motor3_type =
    float;
  _motor3_type motor3;

  // setters for named parameter idiom
  Type & set__motor1(
    const float & _arg)
  {
    this->motor1 = _arg;
    return *this;
  }
  Type & set__motor2(
    const float & _arg)
  {
    this->motor2 = _arg;
    return *this;
  }
  Type & set__motor3(
    const float & _arg)
  {
    this->motor3 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    inchworm_control::msg::Thruple_<ContainerAllocator> *;
  using ConstRawPtr =
    const inchworm_control::msg::Thruple_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<inchworm_control::msg::Thruple_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<inchworm_control::msg::Thruple_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      inchworm_control::msg::Thruple_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<inchworm_control::msg::Thruple_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      inchworm_control::msg::Thruple_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<inchworm_control::msg::Thruple_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<inchworm_control::msg::Thruple_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<inchworm_control::msg::Thruple_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__inchworm_control__msg__Thruple
    std::shared_ptr<inchworm_control::msg::Thruple_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__inchworm_control__msg__Thruple
    std::shared_ptr<inchworm_control::msg::Thruple_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Thruple_ & other) const
  {
    if (this->motor1 != other.motor1) {
      return false;
    }
    if (this->motor2 != other.motor2) {
      return false;
    }
    if (this->motor3 != other.motor3) {
      return false;
    }
    return true;
  }
  bool operator!=(const Thruple_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Thruple_

// alias to use template instance with default allocator
using Thruple =
  inchworm_control::msg::Thruple_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace inchworm_control

#endif  // INCHWORM_CONTROL__MSG__DETAIL__THRUPLE__STRUCT_HPP_
