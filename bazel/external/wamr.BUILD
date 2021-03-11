licenses(["notice"])  # Apache 2

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "wamr_lib",
    hdrs = glob(["include/*.h"]),
    includes = ["include"],
    srcs = glob(["library/linux-classic_interp-multi_module/libiwasm.so"]),
)
