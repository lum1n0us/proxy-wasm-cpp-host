#!/bin/bash
# --memory=7G --cpus=2 \
docker run -it \
    --security-opt seccomp=unconfined --cap-add=SYS_PTRACE \
    --mount type=bind,src=$(pwd),dst=/workspaces \
    --env PATH="/opt/llvm/bin:$PATH" \
    --workdir /workspaces \
    envoyproxy/envoy-build-ubuntu:0a02a76af5951bf7f4c7029c0ea6d29d96c0f682 \
    /bin/bash