FROM ubuntu:22.04

MAINTAINER sourish <sourishonax@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive

# Add user
RUN adduser --quiet  kubex && usermod -a -G audio,video kubex

# This fix: libGL error: No matching fbConfigs or visuals found
ENV LIBGL_ALWAYS_INDIRECT=1
ENV NO_AT_BRIDGE=1
# Install Python 3, PyQt5
RUN apt-get update

RUN apt-get install -y python3-pip

RUN apt install -y shellinabox

RUN apt-get install -y python3-pyqt5

RUN apt-get install -y sshpass

RUN apt-get install -y nano

RUN apt-get install -y net-tools

RUN pip install pawk
RUN apt-get install -y gnome-terminal
RUN apt-get install -y python3-pyqt5.qtwebengine
RUN apt-get install -y python3-pyqt5.qtopengl
RUN apt-get install -y python3-pyqt5.qtquick
RUN apt-get install -y dbus-x11
RUN apt-get install -y apt-transport-https
RUN apt-get install -y ca-certificates
RUN apt-get install -y curl
RUN apt-get install -y gnupg
RUN pip install PyYAML
RUN apt install -y dconf-cli



WORKDIR /home/kubex/

COPY . .

RUN chown -R kubex:kubex /home/kubex


