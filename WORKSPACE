workspace(name = "proxy_wasm_cpp_host")

load("@proxy_wasm_cpp_host//bazel:repositories.bzl", "proxy_wasm_cpp_host_repositories")

proxy_wasm_cpp_host_repositories()

# load("@rules_python//python:repositories.bzl", "py_repositories")
# py_repositories()

load("@proxy_wasm_cpp_host//bazel:dependencies.bzl", "proxy_wasm_cpp_host_dependencies")

proxy_wasm_cpp_host_dependencies()

load("@fuzzing_py_deps//:requirements.bzl", "install_deps")

install_deps()

# # FIXME
# load("@v8_python_deps//:requirements.bzl", "install_deps")

# install_deps()

load("@proxy_wasm_cpp_sdk//bazel:repositories.bzl", "proxy_wasm_cpp_sdk_repositories")

proxy_wasm_cpp_sdk_repositories()

load("@proxy_wasm_cpp_sdk//bazel:dependencies.bzl", "proxy_wasm_cpp_sdk_dependencies")

proxy_wasm_cpp_sdk_dependencies()

load("@proxy_wasm_cpp_sdk//bazel:dependencies_extra.bzl", "proxy_wasm_cpp_sdk_dependencies_extra")

proxy_wasm_cpp_sdk_dependencies_extra()
