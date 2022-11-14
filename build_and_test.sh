#!/bin/bash

#bazel build --define engine=v8 --config=clang -- //test:runtime_test
#bazel build --define engine=wasmtime --config=clang -- //test:runtime_test
#bazel build --define engine=wasmedge --config=clang //test:runtime_test
#bazel build --define engine=wavm --config=clang //test:runtime_test
bazel build -c dbg --define engine=wamr --config=clang -- //test:runtime_test
