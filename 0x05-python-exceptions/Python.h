#ifndef PYTHON_INFO_H
#define PYTHON_INFO_H

#include <Python.h>

#ifdef __cplusplus
extern "C" {
#endif

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

#ifdef __cplusplus
}
#endif

#endif /* PYTHON_INFO_H */
