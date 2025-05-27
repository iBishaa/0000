#include <vector>
#include <string>
#include <stdexcept>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

std::vector<uint8_t> apply_filter_cpp(
    const std::vector<uint8_t>& image_data,
    int width,
    int height,
    const std::string& filter_name
) {
    if (filter_name != "invert") {
        throw std::runtime_error("Unknown filter: " + filter_name);
    }

    std::vector<uint8_t> result = image_data;

    for (size_t i = 0; i < result.size(); i += 4) {
        result[i] = 255 - result[i];     // R
        result[i + 1] = 255 - result[i + 1]; // G
        result[i + 2] = 255 - result[i + 2]; // B
        // �����-����� (i + 3) �������� ��� ���
    }

    return result;
}

PYBIND11_MODULE(filter, m) {
    m.def("apply_filter_cpp", &apply_filter_cpp,
        "Apply filter to image data",
        py::arg("image_data"),
        py::arg("width"),
        py::arg("height"),
        py::arg("filter_name")
    );
}