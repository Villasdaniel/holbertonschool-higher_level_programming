#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - print a list from python to c
 * @p: pointer to list structure
 */
void print_python_list_info(PyObject *p)
{
	int i = 0;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
