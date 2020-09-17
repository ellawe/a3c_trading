FROM linuxmintd/mint19.3-amd64
RUN sudo apt-get -y update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev python3-setuptools
RUN pip3 -q install pip --upgrade
RUN mkdir src
WORKDIR src/
COPY . .
RUN pip3 install -r requirements.txt
#RUN pip3 install jupyter notebook
#RUN pip3 install runipy
#ENV TINI_VERSION v0.6.0
#CMD runipy test_trading.ipynb
CMD ["python3","test_trading.py"]