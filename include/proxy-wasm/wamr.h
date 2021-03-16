
#pragma once

#include "include/proxy-wasm/wasm_vm.h"

namespace proxy_wasm {

std::unique_ptr<WasmVm> createWamrVm();

} // namespace proxy_wasm
