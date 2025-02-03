docker build -t dncl-compiler .
docker run --rm -v "$(pwd):/app" dncl-compiler test.dncl