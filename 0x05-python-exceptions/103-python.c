#include <stdio.h>
#include <Python.h>
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
* print_python_list - Prints info about Python lists.
* @p: Python object.
*/
void print_python_list(PyObject *p)
{
	int i;

	puts("[*] Python list info");
	if (!PyList_Check(p))
	{
		puts("  [ERROR] Invalid List Object");
		return;
	}
	printf("[*] Size of the Python List = %d\n", (int)((PyVarObject *)(p))
->ob_size);
	printf("[*] Allocated = %d\n", (int)(((PyListObject *)p)->allocated));
	for (i = 0; i < (int)((PyVarObject *)(p))->ob_size; i++)
	{
		printf("Element %d: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
		if (!strcmp(PyList_GET_ITEM(p, i)->ob_type->tp_name, "bytes"))
			print_python_bytes(PyList_GET_ITEM(p, i));
		if (!strcmp(PyList_GET_ITEM(p, i)->ob_type->tp_name, "float"))
			print_python_float(PyList_GET_ITEM(p, i));
	}

}
/**
* print_python_bytes - Prints info about Python Bytes.
* @p: Python object.
*/
void print_python_bytes(PyObject *p)
{
	int bytes_to_show, i;

	puts("[.] bytes object info");
	if (!PyBytes_Check(p))
	{
		puts("  [ERROR] Invalid Bytes Object");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	if (PyBytes_Size(p) > 0)
	{
		printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
		bytes_to_show = PyBytes_Size(p) + 1;
		if (bytes_to_show > 10)
			bytes_to_show = 10;
		printf("  first %d bytes:", bytes_to_show);
		for (i = 0; i < bytes_to_show; i++)
		{
			printf(" %02x", (unsigned char)*(((PyBytesObject *)p)->ob_sval + i));
		}
		puts("");
	}
}
/**
* print_python_float - Prints info about a float.
* @p: Pointer to PyObject.
*/
void print_python_float(PyObject *p)
{
	puts("[.] float object info");
	if (!PyFloat_Check(p))
	{
		puts("  [ERROR] Invalid Float Object");
		return;
	}
	printf("  value: %.16g\n", PyFloat_AsDouble(p));
}
