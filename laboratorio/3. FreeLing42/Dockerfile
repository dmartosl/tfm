FROM ubuntu:bionic

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y locales && \
    locale-gen en_US.UTF-8 && \
    apt-get install -y --no-install-recommends build-essential libboost-all-dev wget swig python3 python3-dev cmake && \
    apt-get clean && \
    wget -O /tmp/FreeLing-src-4.2.tar.gz https://github.com/TALP-UPC/FreeLing/releases/download/4.2/FreeLing-src-4.2.tar.gz --no-check-certificate && \
    wget -O /tmp/FreeLing-langs-src-4.2.tar.gz https://github.com/TALP-UPC/FreeLing/releases/download/4.2/FreeLing-langs-src-4.2.tar.gz --no-check-certificate && \
    cd /tmp && \
    tar -xzvf FreeLing-src-4.2.tar.gz && \
    tar -xzvf FreeLing-langs-src-4.2.tar.gz && \
    cd /tmp/FreeLing-4.2 && \
    mkdir build && \
    cd build && \
    cmake .. -DPYTHON3_API=ON && \
    make install && \
    rm -rf /tmp/FreeLing-src-4.2.tar.gz /tmp/FreeLing-langs-src-4.2.tar.gz /tmp/FreeLing-4.2

ENV FREELINGDIR /usr/local
ENV FREELINGSHARE $FREELINGDIR/share/freeling

#COPY . /config
#ENTRYPOINT [ "analyze", "--flush", "-f /config/es.cfg", "--ftok /config/tokenizer.dat", "--fsplit /config/splitter.dat", "--floc /config/singlewords.dat", "--usr --fmap /config/usermap.dat", "--noquant" ]

# docker build -t freeling4-2:1.0.0 .
# echo 'Esto es una prueba.' | python3 $FREELINGSHARE/APIs/python3/sample.py
# wget https://raw.githubusercontent.com/dmartosl/tfm/master/data/SPACCC/corpus/S0004-06142005000400011-1.txt --no-check-certificate
# python3 $FREELINGSHARE/APIs/python3/sample.py < S0004-06142005000400011-1.txt