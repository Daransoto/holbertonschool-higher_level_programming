#include <stdio.h>
#include <Python.h>
#include <string.h>
/**
* print_python_list - Prints info about Python lists.
* @p: Python object.
*/
void print_python_list(PyObject *p)
{
	long i;

	puts("[*] Python list info");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", (((PyListObject *)p)->allocated));
	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %ld: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);

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
	printf("  trying string: %s\n", PyBytes_AsString(p));
	bytes_to_show = PyBytes_Size(p) + 1;
	if (bytes_to_show > 10)
		bytes_to_show = 10;
	printf("  first %d bytes:", bytes_to_show);
	for (i = 0; i < bytes_to_show; i++)
	{
		printf(" %02x", (unsigned char)*(PyBytes_AsString(p) + i));
	}
	puts("");
}
