#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-user_agents
Version  : 2.2.0
Release  : 36
URL      : https://files.pythonhosted.org/packages/e3/e1/63c5bfb485a945010c8cbc7a52f85573561737648d36b30394248730a7bc/user-agents-2.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e3/e1/63c5bfb485a945010c8cbc7a52f85573561737648d36b30394248730a7bc/user-agents-2.2.0.tar.gz
Summary  : A library to identify devices (phones, tablets) and their capabilities by parsing browser user agent strings.
Group    : Development/Tools
License  : MIT
Requires: pypi-user_agents-license = %{version}-%{release}
Requires: pypi-user_agents-python = %{version}-%{release}
Requires: pypi-user_agents-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ua_parser)

%description
==================

%package license
Summary: license components for the pypi-user_agents package.
Group: Default

%description license
license components for the pypi-user_agents package.


%package python
Summary: python components for the pypi-user_agents package.
Group: Default
Requires: pypi-user_agents-python3 = %{version}-%{release}

%description python
python components for the pypi-user_agents package.


%package python3
Summary: python3 components for the pypi-user_agents package.
Group: Default
Requires: python3-core
Provides: pypi(user_agents)
Requires: pypi(ua_parser)

%description python3
python3 components for the pypi-user_agents package.


%prep
%setup -q -n user-agents-2.2.0
cd %{_builddir}/user-agents-2.2.0
pushd ..
cp -a user-agents-2.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656363779
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-user_agents
cp %{_builddir}/user-agents-2.2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-user_agents/67889d1b621a75a20266ff60118d4e11f734f7db
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-user_agents/67889d1b621a75a20266ff60118d4e11f734f7db

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
