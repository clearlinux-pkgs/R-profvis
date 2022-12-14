#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-profvis
Version  : 0.3.7
Release  : 3
URL      : https://cran.r-project.org/src/contrib/profvis_0.3.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/profvis_0.3.7.tar.gz
Summary  : Interactive Visualizations for Profiling R Code
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
Requires: R-profvis-lib = %{version}-%{release}
Requires: R-htmlwidgets
Requires: R-stringr
BuildRequires : R-htmlwidgets
BuildRequires : R-stringr
BuildRequires : buildreq-R

%description
Profvis
=======
[![Travis-CI Build Status](https://travis-ci.org/rstudio/profvis.svg?branch=master)](https://travis-ci.org/rstudio/profvis)

%package lib
Summary: lib components for the R-profvis package.
Group: Libraries

%description lib
lib components for the R-profvis package.


%prep
%setup -q -c -n profvis
cd %{_builddir}/profvis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658418429

%install
export SOURCE_DATE_EPOCH=1658418429
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library profvis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library profvis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library profvis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc profvis || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/profvis/DESCRIPTION
/usr/lib64/R/library/profvis/INDEX
/usr/lib64/R/library/profvis/LICENSE
/usr/lib64/R/library/profvis/Meta/Rd.rds
/usr/lib64/R/library/profvis/Meta/features.rds
/usr/lib64/R/library/profvis/Meta/hsearch.rds
/usr/lib64/R/library/profvis/Meta/links.rds
/usr/lib64/R/library/profvis/Meta/nsInfo.rds
/usr/lib64/R/library/profvis/Meta/package.rds
/usr/lib64/R/library/profvis/NAMESPACE
/usr/lib64/R/library/profvis/NEWS.md
/usr/lib64/R/library/profvis/R/profvis
/usr/lib64/R/library/profvis/R/profvis.rdb
/usr/lib64/R/library/profvis/R/profvis.rdx
/usr/lib64/R/library/profvis/help/AnIndex
/usr/lib64/R/library/profvis/help/aliases.rds
/usr/lib64/R/library/profvis/help/paths.rds
/usr/lib64/R/library/profvis/help/profvis.rdb
/usr/lib64/R/library/profvis/help/profvis.rdx
/usr/lib64/R/library/profvis/html/00Index.html
/usr/lib64/R/library/profvis/html/R.css
/usr/lib64/R/library/profvis/htmlwidgets/lib/d3/LICENSE
/usr/lib64/R/library/profvis/htmlwidgets/lib/d3/d3.min.js
/usr/lib64/R/library/profvis/htmlwidgets/lib/highlight/LICENSE
/usr/lib64/R/library/profvis/htmlwidgets/lib/highlight/default.css
/usr/lib64/R/library/profvis/htmlwidgets/lib/highlight/highlight.js
/usr/lib64/R/library/profvis/htmlwidgets/lib/highlight/textmate.css
/usr/lib64/R/library/profvis/htmlwidgets/lib/jquery/jquery.min.js
/usr/lib64/R/library/profvis/htmlwidgets/lib/profvis/profvis.css
/usr/lib64/R/library/profvis/htmlwidgets/lib/profvis/profvis.js
/usr/lib64/R/library/profvis/htmlwidgets/lib/profvis/scroll.js
/usr/lib64/R/library/profvis/htmlwidgets/profvis.js
/usr/lib64/R/library/profvis/htmlwidgets/profvis.yaml
/usr/lib64/R/library/profvis/shinymodule/draggable-helper.js
/usr/lib64/R/library/profvis/tests/manual-test-source.R
/usr/lib64/R/library/profvis/tests/manual-tests.R
/usr/lib64/R/library/profvis/tests/test-all.R
/usr/lib64/R/library/profvis/tests/testthat/test-parse.R
/usr/lib64/R/library/profvis/tests/testthat/test-parse.prof

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/profvis/libs/profvis.so
/usr/lib64/R/library/profvis/libs/profvis.so.avx2
/usr/lib64/R/library/profvis/libs/profvis.so.avx512
