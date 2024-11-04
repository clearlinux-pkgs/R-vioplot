#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v13
# autospec commit: 2659038
#
Name     : R-vioplot
Version  : 0.5.0
Release  : 49
URL      : https://cran.r-project.org/src/contrib/vioplot_0.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vioplot_0.5.0.tar.gz
Summary  : Violin Plot
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-vioplot-license = %{version}-%{release}
Requires: R-sm
Requires: R-zoo
BuildRequires : R-sm
BuildRequires : R-zoo
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package license
Summary: license components for the R-vioplot package.
Group: Default

%description license
license components for the R-vioplot package.


%prep
%setup -q -n vioplot
pushd ..
cp -a vioplot buildavx2
popd
pushd ..
cp -a vioplot buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720458363

%install
export SOURCE_DATE_EPOCH=1720458363
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-vioplot
cp %{_builddir}/vioplot/inst/COPYRIGHT %{buildroot}/usr/share/package-licenses/R-vioplot/330a83cc67cff3f1bfb60cacef037400e8684497 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/vioplot/doc/histogram_customisation.R
/usr/lib64/R/library/vioplot/doc/histogram_customisation.Rmd
/usr/lib64/R/library/vioplot/doc/histogram_customisation.html
/usr/lib64/R/library/vioplot/doc/histogram_formulae.R
/usr/lib64/R/library/vioplot/doc/histogram_formulae.Rmd
/usr/lib64/R/library/vioplot/doc/histogram_formulae.html
/usr/lib64/R/library/vioplot/doc/index.html
/usr/lib64/R/library/vioplot/doc/overlaying_annotations.R
/usr/lib64/R/library/vioplot/doc/overlaying_annotations.Rmd
/usr/lib64/R/library/vioplot/doc/overlaying_annotations.html
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
/usr/lib64/R/library/vioplot/tests/testthat/Rplots.pdf
/usr/lib64/R/library/vioplot/tests/testthat/test_histoplot_customisation.R
/usr/lib64/R/library/vioplot/tests/testthat/test_histoplot_formula.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_area.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_classes.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_customisation.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_formula.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_median.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_na_handle.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_names.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_side.R
/usr/lib64/R/library/vioplot/tests/testthat/test_violin_unequal_groups.R
/usr/lib64/R/library/vioplot/tests/testthat/test_ylog.R

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-vioplot/330a83cc67cff3f1bfb60cacef037400e8684497
