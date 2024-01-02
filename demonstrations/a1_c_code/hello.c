#include <Python.h>


static PyObject *hello_greet(PyObject *self, PyObject *args) {
   char *name;
   char buffer[255];

   if (!PyArg_ParseTuple(args, "s", &name)) {
      return NULL;
   }
   strcpy(buffer, "hello ");
   strcat(buffer, name);
   return Py_BuildValue("s", buffer);
}

static PyMethodDef hello_funcs[] = {
    {"greet", (PyCFunction)hello_greet, METH_VARARGS, "Greet by name"},
    {NULL}
};

static struct PyModuleDef hello_module = {
   PyModuleDef_HEAD_INIT,
   "hello",   
   "Extension - argument passing example",
   -1,       
   hello_funcs
};

PyMODINIT_FUNC PyInit_hello(void)
{
    return PyModule_Create(&hello_module);
}

