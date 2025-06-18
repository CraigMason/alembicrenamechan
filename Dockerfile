FROM alpine:latest

RUN apk add openexr git cmake build-base zlib-dev bzip2-dev gdbm libbz2 libcrypto3 libexpat libffi-dev libncursesw libpanelw openssl-dev mpdecimal musl readline sqlite-libs xz-libs zlib

WORKDIR /root

RUN git clone --depth 1 --branch 3.11 https://github.com/python/cpython.git \
    && cd cpython && ./configure --enable-shared && make -j 8 && make install \
    && python3 -m ensurepip --upgrade \
    && python3 -m pip install setuptools numpy==1.26.0 \
    && cd .. && rm -rf cpython

RUN wget https://github.com/boostorg/boost/releases/download/boost-1.83.0/boost-1.83.0.tar.gz && tar -xzvf boost-1.83.0.tar.gz \
    && cd boost-1.83.0 && ./bootstrap.sh --with-libraries=program_options,python --with-python=/usr/local/bin/python3 && ./b2 install \
    && cd /root && rm -rf boost-1.83.0.tar.gz && rm -rf boost-1.83.0

RUN git clone --depth 1 --branch v3.1.9 https://github.com/AcademySoftwareFoundation/Imath \
    && cd Imath && mkdir build && cd build && cmake -DPYTHON=ON .. && cmake --build . --target install --config Release \
    && cd /root && rm -rf Imath

RUN cd /root && git clone --depth 1 --branch 1.8.8 https://github.com/alembic/alembic.git \
    && cd /root/alembic && mkdir build && cd build && cmake -DUSE_BINARIES=ON -DUSE_TESTS=OFF -DUSE_PYALEMBIC=ON .. && cmake --build . --target install \
    && cd /root && rm -rf alembic

RUN git clone https://github.com/PeterShinners/cask.git && cd cask && python3 setup.py install \
    && cd /root && rm -rf cask

COPY abcrenamechan.py /usr/local/bin/abcrenamechan
RUN chmod +x /usr/local/bin/abcrenamechan

WORKDIR /app
