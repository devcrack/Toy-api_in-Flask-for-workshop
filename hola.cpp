#include <pybind11/pybind11.h>
#include <string>

using namespace std;

namespace
py = pybind11;

string Saluda(string s) {
  return "Hola desde C++, " + s;
}

//Declaracion de la capsula c++ y Python
PYBIND11_MODULE(hola, m) {
  m.doc() = "Ejemplo modulo con pybind11"; //este comentario es opcional

  m.def("Saluda", &Saluda, "Una función simple que retorna una cadena",
  py::arg("nombre"));
}
