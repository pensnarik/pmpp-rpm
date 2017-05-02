FROM centos:7

RUN yum update -y && yum install -y wget \
    rpm-build \
    redhat-rpm-config \
    gcc \
    make

RUN yum install -y https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm

RUN yum install -y postgresql96-server \
    postgresql96-devel \
    postgresql96-contrib \
    openssl-devel \
    flex \
    bison

RUN find / -name "libpq*"

ENV PATH $PATH:/usr/pgsql-9.6/bin
ENV LIBPQ_DIR /usr/pgsql-9.6/
ENV LIBRARY_PATH /usr/pgsql-9.6/lib
ENV PG_CPPFLAGS -I/usr/pghttp://termbin.com/29qysql-9.6/include
ENV PKG_CONFIG_PATH /usr/pgsql-9.6/lib/pkgconfig
ENV SHLIB_LINK -L/usr/pgsql-9.6/lib -lpq

ENV PMPP_VERSION master

RUN echo $PKG_CONFIG_PATH

COPY rpmbuild /rpmbuild
WORKDIR /rpmbuild/SOURCES
RUN wget "https://github.com/moat/pmpp/archive/$PMPP_VERSION.zip"
WORKDIR /rpmbuild/SPECS
RUN rpmbuild -ba pmpp.spec
