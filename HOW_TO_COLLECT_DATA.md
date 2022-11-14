
## Get envoy-dev image

```
$ docker pull envoyproxy/envoy-build-ubuntu:0a02a76af5951bf7f4c7029c0ea6d29d96c0f682
```

## Enter into the compilation environment

```
$  ./run_envoy_dev_docker.sh
```

Use `--env http_proxy=xxxxx` to setup proxy configuration in the container

All below operations are in the docker container

## Compile or Test

```
$ ./build_and_test.sh
```

`bazel build` generates the target

`basel test` run specific tests

`--define engine=wamr` is used to enable one Wasm Runtime. All possible options are: `v8`, `wasmtime`, `wamr`, `wasmedge`, `wavm`

## Run manually and record output

```
$ ./bazel_bin/test/runtime_test --gtest_filter=*BasicVM* | tee runtime_test.log
```

## Analyse data

```
$ python3 process_log.py runtime_test.log | tee report.md
```

The output is a table in Markdown style
