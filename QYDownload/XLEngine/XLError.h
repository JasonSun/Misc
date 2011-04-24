#pragma once

#define XL_SUCCESS                     0
#define XL_ERROR_FAIL                  0x10000000

// Not initialize
#define XL_ERROR_UNINITAILIZE          XL_ERROR_FAIL+1

// Unsupported protocol, HTTP only as far
#define XL_ERROR_UNSPORTED_PROTOCOL    XL_ERROR_FAIL+2

// Fail to init icon
#define XL_ERROR_INIT_TASK_TRAY_ICON_FAIL  XL_ERROR_FAIL+3

// Fail to add icon
#define XL_ERROR_ADD_TASK_TRAY_ICON_FAIL   XL_ERROR_FAIL+4

// Null pointer
#define XL_ERROR_POINTER_IS_NULL    XL_ERROR_FAIL+5

// Null string
#define XL_ERROR_STRING_IS_EMPTY    XL_ERROR_FAIL+6

// Stored path not include filename
#define XL_ERROR_PATH_DONT_INCLUDE_FILENAME    XL_ERROR_FAIL+7

// Fail to create directory
#define XL_ERROR_CREATE_DIRECTORY_FAIL    XL_ERROR_FAIL+8

// Memory is not enough
#define XL_ERROR_MEMORY_ISNT_ENOUGH    XL_ERROR_FAIL+9

// Invalid arguments
#define XL_ERROR_INVALID_ARG    XL_ERROR_FAIL+10

// Task not exist
#define XL_ERROR_TASK_DONT_EXIST    XL_ERROR_FAIL+11

// Invalid file name
#define XL_ERROR_FILE_NAME_INVALID   XL_ERROR_FAIL+12

// Not implement
#define XL_ERROR_NOTIMPL    XL_ERROR_FAIL+13

// Max task numbers reached can not create new task
#define XL_ERROR_TASKNUM_EXCEED_MAXNUM    XL_ERROR_FAIL+14

// Invalid task type
#define XL_ERROR_INVALID_TASK_TYPE    XL_ERROR_FAIL+15

// File already exist
#define XL_ERROR_FILE_ALREADY_EXIST   XL_ERROR_FAIL+16

// File not exist
#define XL_ERROR_FILE_DONT_EXIST      XL_ERROR_FAIL+17

// Fail to read configuration file
#define XL_ERROR_READ_CFG_FILE_FAIL   XL_ERROR_FAIL+18

// Fail to write configuration file
#define XL_ERROR_WRITE_CFG_FILE_FAIL   XL_ERROR_FAIL+19

// Can not continue task
#define XL_ERROR_CANNOT_CONTINUE_TASK  XL_ERROR_FAIL+20

// Can not pause task
#define XL_ERROR_CANNOT_PAUSE_TASK  XL_ERROR_FAIL+21

// Small buffer to use
#define XL_ERROR_BUFFER_TOO_SMALL   XL_ERROR_FAIL+22

// Init download engine exit before uninit download engine
#define XL_ERROR_INIT_THREAD_EXIT_TOO_EARLY XL_ERROR_FAIL+23
