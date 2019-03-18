#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-vioplot
Version  : 0.3.0
Release  : 9
URL      : https://cran.r-project.org/src/contrib/vioplot_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vioplot_0.3.0.tar.gz
Summary  : Violin Plot
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-assertthat
Requires: R-cli
Requires: R-markdown
Requires: R-mime
Requires: R-withr
BuildRequires : R-assertthat
BuildRequires : R-cli
BuildRequires : R-markdown
BuildRequires : R-mime
BuildRequires : R-rlang
BuildRequires : R-sm
BuildRequires : R-withr
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n vioplot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552838766

%install
export SOURCE_DATE_EPOCH=1552838766
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vioplot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vioplot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vioplot
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  vioplot || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/vioplot/CITATION
/usr/lib64/R/library/vioplot/COPYRIGHT
/usr/lib64/R/library/vioplot/DESCRIPTION
/usr/lib64/R/library/vioplot/INDEX
/usr/lib64/R/library/vioplot/LICENSE
/usr/lib64/R/library/vioplot/Meta/Rd.rds
/usr/lib64/R/library/vioplot/Meta/features.rds
/usr/lib64/R/library/vioplot/Meta/hsearch.rds
/usr/lib64/R/library/vioplot/Meta/links.rds
/usr/lib64/R/library/vioplot/Meta/nsInfo.rds
/usr/lib64/R/library/vioplot/Meta/package.rds
/usr/lib64/R/library/vioplot/Meta/vignette.rds
/usr/lib64/R/library/vioplot/NAMESPACE
/usr/lib64/R/library/vioplot/NEWS.md
/usr/lib64/R/library/vioplot/R/vioplot
/usr/lib64/R/library/vioplot/R/vioplot.rdb
/usr/lib64/R/library/vioplot/R/vioplot.rdx
/usr/lib64/R/library/vioplot/doc/index.html
/usr/lib64/R/library/vioplot/doc/violin_area.R
/usr/lib64/R/library/vioplot/doc/violin_area.Rmd
/usr/lib64/R/library/vioplot/doc/violin_area.html
/usr/lib64/R/library/vioplot/doc/violin_customisation.R
/usr/lib64/R/library/vioplot/doc/violin_customisation.Rmd
/usr/lib64/R/library/vioplot/doc/violin_customisation.html
/usr/lib64/R/library/vioplot/doc/violin_formulae.R
/usr/lib64/R/library/vioplot/doc/violin_formulae.Rmd
/usr/lib64/R/library/vioplot/doc/violin_formulae.html
/usr/lib64/R/library/vioplot/doc/violin_split.R
/usr/lib64/R/library/vioplot/doc/violin_split.Rmd
/usr/lib64/R/library/vioplot/doc/violin_split.html
/usr/lib64/R/library/vioplot/doc/violin_ylog.R
/usr/lib64/R/library/vioplot/doc/violin_ylog.Rmd
/usr/lib64/R/library/vioplot/doc/violin_ylog.html
/usr/lib64/R/library/vioplot/help/AnIndex
/usr/lib64/R/library/vioplot/help/aliases.rds
/usr/lib64/R/library/vioplot/help/paths.rds
/usr/lib64/R/library/vioplot/help/vioplot.rdb
/usr/lib64/R/library/vioplot/help/vioplot.rdx
/usr/lib64/R/library/vioplot/html/00Index.html
/usr/lib64/R/library/vioplot/html/R.css
/usr/lib64/R/library/vioplot/tests/testthat.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_area.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_customisation.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_formula.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_median.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_na_handle.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_names.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_side.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_unequal_groups.R
/usr/lib64/R/library/vioplot/tests/testthat/test_ylog.R
