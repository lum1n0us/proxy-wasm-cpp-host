#include "include/proxy-wasm/wasm_vm.h"
#include "wasm_c_api.h"
#include "wasm_export.h"


namespace proxy_wasm {
namespace wamr {

class Wamr : public WasmVm {
public:
  Wamr() {}

  std::string_view runtime() override { return "wamr"; }
};

}
}
