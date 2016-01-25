FROM devries/bottle

RUN apt-get update && apt-get install -y python-qt4 libqt4-webkit xvfb git-core && apt-get install -y build-essential checkinstall && apt-get build-dep imagemagick -y

RUN pip install gevent
RUN pip install python-gyazo
RUN pip install slackweb

RUN mkdir python-webkit2png && git clone https://github.com/adamn/python-webkit2png.git python-webkit2png && cd python-webkit2png && python ./setup.py install

RUN apt-get install -y wget
RUN wget http://www.imagemagick.org/download/ImageMagick.tar.gz
RUN tar xzvf ImageMagick.tar.gz
RUN /ImageMagick-6.9.3-1/configure
RUN make
RUN checkinstall

RUN apt-get install -y fonts-mplus fonts-migmix fonts-ipafont-gothic fonts-ipafont-mincho

EXPOSE 8080

ADD . /app
WORKDIR /app

RUN chown -R apprunner:apprunner /app
#USER apprunner

ENV LDFLAGS -L/usr/local/lib -Wl,-rpath,/usr/local/lib"
ENV LD_LIBRARY_PATH /usr/local/lib

CMD ["gunicorn","-b","0.0.0.0:8080","-w","3","-k","gevent","--log-file","-","--log-level","debug","--access-logfile","-","main_app:app"]
