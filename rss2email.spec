Summary:	A python script that converts RSS/Atom newsfeeds to email
Name:		rss2email
Version:	3.9
Release:	2
License:	GPL v2+
Group:		Applications/Networking
Source0:	https://pypi.python.org/packages/source/r/rss2email/%{name}-%{version}.tar.gz
Patch0:		%{name}-maildir.patch
# Source0-md5:	23be063b045be29cc4edc76fe6d141ff
URL:		https://pypi.python.org/pypi/rss2email/
BuildRequires:	python3 >= 3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python3 >= 3.2
Requires:	python3-feedparser
Requires:	python3-html2text
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A python script that converts RSS/Atom newsfeeds to email.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,^#!.*python,#!%{__python3},' r2e

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \
	--skip-build

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p r2e.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README
%attr(755,root,root) %{_bindir}/r2e
%dir %{py3_sitescriptdir}/rss2email
%{py3_sitescriptdir}/rss2email/*.py
%{py3_sitescriptdir}/rss2email/__pycache__
%{py3_sitescriptdir}/rss2email/post_process
%{py3_sitescriptdir}/rss2email-*.egg-info
%{_mandir}/man1/r2e.1*
