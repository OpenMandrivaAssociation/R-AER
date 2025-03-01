%bcond_with bootstrap
%global packname  AER
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1_9
Release:          3
Summary:          Applied Econometrics with R
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-9.tar.gz
Requires:         R-stats R-car R-Formula R-lmtest R-sandwich R-strucchange
Requires:         R-survival R-zoo R-stats
%if %{with bootstrap}
Requires:         R-boot R-dynlm R-effects R-foreign R-ineq R-KernSmooth
Requires:         R-lattice R-MASS R-nlme R-nnet R-np R-plm R-pscl R-quantreg
Requires:         R-ROCR R-sampleSelection R-scatterplot3d R-systemfit R-rgl
Requires:         R-truncreg R-tseries R-urca
%else
Requires:         R-boot R-dynlm R-effects R-foreign R-ineq R-KernSmooth
Requires:         R-lattice R-MASS R-mlogit R-nlme R-nnet R-np R-plm R-pscl
Requires:         R-quantreg R-ROCR R-sampleSelection R-scatterplot3d
Requires:         R-systemfit R-rgl R-truncreg R-tseries R-urca
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-car
BuildRequires:    R-Formula R-lmtest R-sandwich R-strucchange R-survival R-zoo
BuildRequires:    R-stats
%if %{with bootstrap}
BuildRequires:    R-boot R-dynlm R-effects R-foreign R-ineq R-KernSmooth
BuildRequires:    R-lattice R-MASS R-nlme R-nnet R-np R-plm R-pscl R-quantreg
BuildRequires:    R-ROCR R-sampleSelection R-scatterplot3d R-systemfit R-rgl
BuildRequires:    R-truncreg R-tseries R-urca
%else
BuildRequires:    R-boot R-dynlm R-effects R-foreign R-ineq R-KernSmooth
BuildRequires:    R-lattice R-MASS R-mlogit R-nlme R-nnet R-np R-plm R-pscl
BuildRequires:    R-quantreg R-ROCR R-sampleSelection R-scatterplot3d
BuildRequires:    R-systemfit R-rgl R-truncreg R-tseries R-urca
%endif

%description
Functions, data sets, examples, demos, and vignettes for the book
Christian Kleiber and Achim Zeileis (2008), Applied Econometrics with R,
Springer-Verlag, New York. ISBN 978-0-387-77316-2. (See the vignette for a
package overview.)

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
if [ x$DISPLAY != x ];	then %{_bindir}/R CMD check %{packname}
else			true
fi
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
