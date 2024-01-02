#include <Python.h>

static PyObject* helloworld_message(PyObject* self)
{
    return Py_BuildValue("s", "Hello from a Python extension");
}

static PyMethodDef helloworld_funcs[] = {
    {"message", (PyCFunction)helloworld_message, METH_NOARGS, "Hello World Example"}, 
    {NULL} 
};

static struct PyModuleDef helloworld_module = {
   PyModuleDef_HEAD_INIT,
   "helloworld",   
   "Extension - simple example",
   -1,       
   helloworld_funcs
};

PyMODINIT_FUNC PyInit_helloworld(void)
{
    return PyModule_Create(&helloworld_module);
}


