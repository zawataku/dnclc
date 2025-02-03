#!/bin/bash
docker build -t dncl-compiler .
docker run --rm -v "$(pwd)/test:/test" dncl-compiler /test/test.dncl