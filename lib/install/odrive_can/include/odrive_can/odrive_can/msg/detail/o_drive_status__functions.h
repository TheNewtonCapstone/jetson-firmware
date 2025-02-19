// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from odrive_can:msg/ODriveStatus.idl
// generated code does not contain a copyright notice

#ifndef ODRIVE_CAN__MSG__DETAIL__O_DRIVE_STATUS__FUNCTIONS_H_
#define ODRIVE_CAN__MSG__DETAIL__O_DRIVE_STATUS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "odrive_can/msg/rosidl_generator_c__visibility_control.h"

#include "odrive_can/msg/detail/o_drive_status__struct.h"

/// Initialize msg/ODriveStatus message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * odrive_can__msg__ODriveStatus
 * )) before or use
 * odrive_can__msg__ODriveStatus__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
bool
odrive_can__msg__ODriveStatus__init(odrive_can__msg__ODriveStatus * msg);

/// Finalize msg/ODriveStatus message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
void
odrive_can__msg__ODriveStatus__fini(odrive_can__msg__ODriveStatus * msg);

/// Create msg/ODriveStatus message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * odrive_can__msg__ODriveStatus__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
odrive_can__msg__ODriveStatus *
odrive_can__msg__ODriveStatus__create();

/// Destroy msg/ODriveStatus message.
/**
 * It calls
 * odrive_can__msg__ODriveStatus__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
void
odrive_can__msg__ODriveStatus__destroy(odrive_can__msg__ODriveStatus * msg);

/// Check for msg/ODriveStatus message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
bool
odrive_can__msg__ODriveStatus__are_equal(const odrive_can__msg__ODriveStatus * lhs, const odrive_can__msg__ODriveStatus * rhs);

/// Copy a msg/ODriveStatus message.
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
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
bool
odrive_can__msg__ODriveStatus__copy(
  const odrive_can__msg__ODriveStatus * input,
  odrive_can__msg__ODriveStatus * output);

/// Initialize array of msg/ODriveStatus messages.
/**
 * It allocates the memory for the number of elements and calls
 * odrive_can__msg__ODriveStatus__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
bool
odrive_can__msg__ODriveStatus__Sequence__init(odrive_can__msg__ODriveStatus__Sequence * array, size_t size);

/// Finalize array of msg/ODriveStatus messages.
/**
 * It calls
 * odrive_can__msg__ODriveStatus__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
void
odrive_can__msg__ODriveStatus__Sequence__fini(odrive_can__msg__ODriveStatus__Sequence * array);

/// Create array of msg/ODriveStatus messages.
/**
 * It allocates the memory for the array and calls
 * odrive_can__msg__ODriveStatus__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
odrive_can__msg__ODriveStatus__Sequence *
odrive_can__msg__ODriveStatus__Sequence__create(size_t size);

/// Destroy array of msg/ODriveStatus messages.
/**
 * It calls
 * odrive_can__msg__ODriveStatus__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
void
odrive_can__msg__ODriveStatus__Sequence__destroy(odrive_can__msg__ODriveStatus__Sequence * array);

/// Check for msg/ODriveStatus message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
bool
odrive_can__msg__ODriveStatus__Sequence__are_equal(const odrive_can__msg__ODriveStatus__Sequence * lhs, const odrive_can__msg__ODriveStatus__Sequence * rhs);

/// Copy an array of msg/ODriveStatus messages.
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
ROSIDL_GENERATOR_C_PUBLIC_odrive_can
bool
odrive_can__msg__ODriveStatus__Sequence__copy(
  const odrive_can__msg__ODriveStatus__Sequence * input,
  odrive_can__msg__ODriveStatus__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // ODRIVE_CAN__MSG__DETAIL__O_DRIVE_STATUS__FUNCTIONS_H_
