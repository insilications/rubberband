#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : rubberband
Version  : 2.0.0
Release  : 312
URL      : file:///aot/build/clearlinux/packages/rubberband/rubberband-v2.0.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/rubberband/rubberband-v2.0.0.tar.gz
Source1  : file:///aot/build/clearlinux/packages/rubberband/car.tar.gz
Summary  : No summary provided
Group    : Development/Tools
License  : GPL-2.0
Requires: rubberband-bin = %{version}-%{release}
Requires: rubberband-data = %{version}-%{release}
Requires: rubberband-lib = %{version}-%{release}
BuildRequires : PyYAML
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : alsa-lib-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : cmake
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expect
BuildRequires : fftw-dev
BuildRequires : fftw-staticdev
BuildRequires : findutils
BuildRequires : flac
BuildRequires : flac-dev
BuildRequires : flac-staticdev
BuildRequires : flex
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-doc
BuildRequires : gcc-go
BuildRequires : gcc-go-lib
BuildRequires : gcc-libs-math
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb-dev
BuildRequires : git
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : gmp-dev
BuildRequires : googletest-dev
BuildRequires : graphviz
BuildRequires : guile
BuildRequires : ladspa_sdk
BuildRequires : ladspa_sdk-dev
BuildRequires : ladspa_sdk-staticdev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libogg-dev
BuildRequires : libogg-staticdev
BuildRequires : libsamplerate-dev
BuildRequires : libsamplerate-staticdev
BuildRequires : libsndfile-dev
BuildRequires : libsndfile-staticdev
BuildRequires : libstdc++
BuildRequires : libunwind-dev
BuildRequires : libvorbis-dev
BuildRequires : libvorbis-staticdev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt
BuildRequires : meson
BuildRequires : mpc-dev
BuildRequires : mpfr-dev
BuildRequires : ncurses
BuildRequires : ncurses-dev
BuildRequires : ninja
BuildRequires : opus
BuildRequires : opus-dev
BuildRequires : opus-staticdev
BuildRequires : pkg-config
BuildRequires : pkgconfig(opus)
BuildRequires : procps-ng
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : sed
BuildRequires : speex-dev
BuildRequires : speex-staticdev
BuildRequires : speexdsp-dev
BuildRequires : speexdsp-staticdev
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : util-linux
BuildRequires : valgrind-dev
BuildRequires : vamp-sdk
BuildRequires : vamp-sdk-dev
BuildRequires : vamp-sdk-staticdev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml
BuildRequires : yaml-cpp
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Rubber Band Library
An audio time-stretching and pitch-shifting library and utility program.

%package bin
Summary: bin components for the rubberband package.
Group: Binaries
Requires: rubberband-data = %{version}-%{release}

%description bin
bin components for the rubberband package.


%package data
Summary: data components for the rubberband package.
Group: Data

%description data
data components for the rubberband package.


%package dev
Summary: dev components for the rubberband package.
Group: Development
Requires: rubberband-lib = %{version}-%{release}
Requires: rubberband-bin = %{version}-%{release}
Requires: rubberband-data = %{version}-%{release}
Provides: rubberband-devel = %{version}-%{release}
Requires: rubberband = %{version}-%{release}

%description dev
dev components for the rubberband package.


%package lib
Summary: lib components for the rubberband package.
Group: Libraries
Requires: rubberband-data = %{version}-%{release}

%description lib
lib components for the rubberband package.


%package staticdev
Summary: staticdev components for the rubberband package.
Group: Default
Requires: rubberband-dev = %{version}-%{release}

%description staticdev
staticdev components for the rubberband package.


%prep
%setup -q -n rubberband
cd %{_builddir}
mkdir -p car.tar
cd car.tar
tar xf %{_sourcedir}/car.tar.gz
cd %{_builddir}/rubberband
mkdir -p sample
cp -a %{_builddir}/car.tar/* %{_builddir}/rubberband/sample

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640835397
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
unset ASFLAGS
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage -fprofile-partial-training -fprofile-correction -freorder-functions --coverage -lgcov"
export CFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export ASMFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export CXXFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LDFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LIBS_GENERATE="-lgcov"
## pgo use
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize -fopt-info-vec
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export PGO_USE="-Wmissing-profile -Wcoverage-mismatch -fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-partial-training -fprofile-correction -freorder-functions"
export CFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export ASMFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/gbm:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/gbm:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=1
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
export ASMFLAGS="${ASMFLAGS_GENERATE}"
export LIBS="${LIBS_GENERATE}"
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" LIBS="$LIBS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both  -Ddefault_library=both \
-Dfft=fftw \
-Dresampler=libsamplerate builddir
## make_prepend content
# sd "/usr/lib64/libfftw3.so" -- "-Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libfftw3.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive" $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libfftw3\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libfftw3.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
# sd "/usr/lib64/libsamplerate.so" -- "-Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsamplerate.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive" $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libsamplerate\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsamplerate.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
# sd "/usr/lib64/libsndfile.so" -- "-Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsndfile.a,/usr/lib64/libFLAC.a,/usr/lib64/libopus.a,/usr/lib64/libvorbis.a,/usr/lib64/libvorbisenc.a,/usr/lib64/libvorbisfile.a,/usr/lib64/libogg.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive" $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libsndfile\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsndfile.a,/usr/lib64/libFLAC.a,/usr/lib64/libopus.a,/usr/lib64/libvorbis.a,/usr/lib64/libvorbisenc.a,/usr/lib64/libvorbisfile.a,/usr/lib64/libogg.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
## make_prepend end
ninja --verbose %{?_smp_mflags} -C builddir

## profile_payload start
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
meson test --verbose --num-processes 1 -C builddir || :
pushd builddir/
./rubberband --threads -t 1.5 -p 2.0 ../sample/otter.wav ../sample/otter2.wav
./rubberband --threads -c 1 -t 1.5 -p 2.0 ../sample/otter.wav ../sample/otter3.wav
./rubberband --threads -c 6 -t 2.5 -p 2.0 ../sample/otter.wav ../sample/otter4.wav
./rubberband --threads --realtime --pitch-hq -t 1.5 -p 2.0 ../sample/otter.wav ../sample/otter5.wav
./rubberband --threads -c 0 --smoothing --window-long -t 1.5 -p 2.0 ../sample/otter.wav ../sample/otter6.wav
popd
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/gbm:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/gbm:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
## profile_payload end
find builddir/ -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print  || :
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
export ASMFLAGS="${ASMFLAGS_USE}"
export LIBS="${LIBS_USE}"
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" LIBS="$LIBS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both -Ddefault_library=both \
-Dfft=fftw \
-Dresampler=libsamplerate  builddir
## make_prepend content
# sd "/usr/lib64/libfftw3.so" -- "-Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libfftw3.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive" $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libfftw3\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libfftw3.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
# sd "/usr/lib64/libsamplerate.so" -- "-Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsamplerate.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive" $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libsamplerate\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsamplerate.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
# sd "/usr/lib64/libsndfile.so" -- "-Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsndfile.a,/usr/lib64/libFLAC.a,/usr/lib64/libopus.a,/usr/lib64/libvorbis.a,/usr/lib64/libvorbisenc.a,/usr/lib64/libvorbisfile.a,/usr/lib64/libogg.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive" $(fd -uu --glob *.ninja)
sd '(LINK_ARGS.+)(\s/usr/lib64/libsndfile\.so)' -- '$1 -Wl,--whole-archive,--as-needed,--allow-multiple-definition,/usr/lib64/libsndfile.a,/usr/lib64/libFLAC.a,/usr/lib64/libopus.a,/usr/lib64/libvorbis.a,/usr/lib64/libvorbisenc.a,/usr/lib64/libvorbisfile.a,/usr/lib64/libogg.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive' $(fd -uu --glob *.ninja)
## make_prepend end
ninja --verbose %{?_smp_mflags} -C builddir
fi

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rubberband

%files data
%defattr(-,root,root,-)
/usr/share/ladspa/rdf/ladspa-rubberband.rdf

%files dev
%defattr(-,root,root,-)
/usr/include/rubberband/RubberBandStretcher.h
/usr/include/rubberband/rubberband-c.h
/usr/lib64/ladspa/ladspa-rubberband.cat
/usr/lib64/ladspa/ladspa-rubberband.so
/usr/lib64/librubberband.so
/usr/lib64/pkgconfig/rubberband.pc
/usr/lib64/vamp/vamp-rubberband.cat
/usr/lib64/vamp/vamp-rubberband.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/librubberband.so.2
/usr/lib64/librubberband.so.2.1.5

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/librubberband.a
