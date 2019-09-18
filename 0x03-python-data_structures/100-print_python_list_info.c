#include <stdio.h>
#include <Python.h>
#include <string.h>
void print_python_list_info(PyObject *p)
{
	int i;
	char type[6];

	type[5] = '\0';
	printf("[*] Size of the Python List = %d\n", (int)PyList_Size(p));
	printf("[*] Allocated =  %d\n", (int)(Py_SIZE(p)));
	for (i = 0; i < (int)PyList_Size(p); i++)
	{
		if(!strcmp("I", (char *)Py_TYPE(PyList_GetItem(p, i))))
		{
			strcpy(type, "str");
		}
		else if (!strcmp("C", (char *)Py_TYPE(PyList_GetItem(p, i))))
		{
			strcpy(type, "int");
		}
		else if (!strcmp("3", (char *)Py_TYPE(PyList_GetItem(p, i))))
		{
			strcpy(type, "float");
		}
		else if (!strcmp("9", (char *)Py_TYPE(PyList_GetItem(p, i))))
		{
			strcpy(type, "tuple");
		}
		else if (!strcmp("'", (char *)Py_TYPE(PyList_GetItem(p, i))))
		{
			strcpy(type, "list");
		}
		printf("Element %d: %s\n", i, type);
	}
	
}
