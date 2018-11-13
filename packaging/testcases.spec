Name:      nnsuite-testcases
Summary:   Testcases of nnsuite for CI testing
Version:   1.0.0
Release:   1rc1
Group:     Development/Tools
Packager:  MyungJoo Ham <myungjoo.ham@samsung.com>
License:   Apache-2.0
Source0:   nnsuite-testcases-%{version}.tar.gz
BuildArch: noarch

%description
This package is set of testcases and neural network models for nnsuite packages.
If the test cases (usually the network models) are too large to be included
in a source code repo of a nnsuite package, they can be located in this package.
For testing in CI, the CI system may install this package in its sandbox.
For testing in OBS/GBS, the packager may "BuildRequires: nnsuite-testcases" to
have this package available in their OBS/GBS process.

The test cases and models are installed at /usr/{lib or lib64}/nnsuite/testcases/

%define installpath %{_libdir}/nnsuite/testcases

%prep
%setup -q

%build
# DO NOTHING

%install

mkdir -p %{buildroot}%{installpath}/models

# list files to be installed.

# 1. DL NN Models
cp -R DeepLearningModels/* %{buildroot}%{installpath}/models/

%files
%defattr(644,root,root,755)
%{installpath}/*

%changelog
* Fri Nov 02 2018 MyungJoo Ham <myungjoo.ham@samsung.com>
- Packaged for the first time.
