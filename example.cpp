#include <pybind11/pybind11.h>

namespace
py = pybind11;

long int mult( int i,long int j) {
  return i * j;
}

PYBIND11_MODULE(example, m) {
  m.doc() = "Ejemplo modulo con pybind11"; //este comentario es opcional

  m.def("Suma", &mult, "Una función simple que suma dos numeros",
  py::arg("i"), py::arg("j"));
}
