licenses(["notice"])  # Apache 2

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "wamr_lib",
    hdrs = glob(["include/*.h"]),
    defines = [
        "ENVOY_WASM_WAMR",
    ],
    includes = ["include"],
    srcs = glob(["library/libiwasm.so"]),
)