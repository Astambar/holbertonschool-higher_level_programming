#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_float - affiche des informations de base sur Python
 * concernant l'objet float
 * @p: pointer de PyObject
 */
void print_python_float(PyObject *p)
{
	double d;
	char *string = NULL;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}
	d = ((PyFloatObject *)(p))->ob_fval;
	string = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
	fflush(stdout);
}

/**
 * print_python_bytes -affiche des informations de base sur Python
 * concernant l'objets byte
 * @p: pointer de PyObject
 */
void print_python_bytes(PyObject *p)
{
	size_t i, bytes;
	char *string = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	string = ((PyBytesObject *)(p))->ob_sval;
	bytes = PyBytes_Size(p);
	printf("  size: %ld\n", bytes);
	printf("  trying string: %s\n", string);
	if (bytes >= 10)
		bytes = 10;
	else
		bytes++;
	printf("  first %ld bytes: ", bytes);
	for (i = 0; i < bytes - 1; i++)
		printf("%02hhx ", string[i]);
	printf("%02hhx", string[i]);
	printf("\n");
	fflush(stdout);
}

/**
 * print_python_list - affiche des informations de base sur les listes Python
 * @p: pointer de PyObject
 */
void print_python_list(PyObject *p)
{
	size_t i, allocated, size;
	const char *dataType;
	PyListObject *list;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %li\n", allocated);
	for (i = 0; i < size; i++)
	{
		dataType = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %li: %s\n", i, dataType);
		if (strcmp(dataType, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(dataType, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
	fflush(stdout);}
