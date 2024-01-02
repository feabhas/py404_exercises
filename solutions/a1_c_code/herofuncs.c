#include <Python.h>

double hero(double value);

static PyObject *herofuncs_hero(PyObject *self, PyObject *args) {
   double value;

   if (!PyArg_ParseTuple(args, "d", &value)) {
      return NULL;
   }
   return Py_BuildValue("d", hero(value));
}

static PyMethodDef herofuncs_funcs[] = {
    {"hero", (PyCFunction)herofuncs_hero, METH_VARARGS, "Hero's formula for root"},
    {NULL}
};

static struct PyModuleDef herofuncs_module = {
   PyModuleDef_HEAD_INIT,
   "herofuncs",   
   "Hero - functions",
   -1,       
   herofuncs_funcs
};

PyMODINIT_FUNC PyInit_herofuncs(void)
{
    return PyModule_Create(&herofuncs_module);
}

