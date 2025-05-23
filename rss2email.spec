Summary:	A python script that converts RSS/Atom newsfeeds to email
Name:		rss2email
Version:	3.14
Release:	3
License:	GPL v2+
Group:		Applications/Networking
Source0:	https://pypi.python.org/packages/source/r/rss2email/%{name}-%{version}.tar.gz
# Source0-md5:	1f8ce06b5f628a2afa73f9d0a01c58d7
URL:		https://pypi.python.org/pypi/rss2email/
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.750
BuildRequires:	sed >= 4.0
Requires:	python3 >= 1:3.6
Requires:	python3-feedparser >= 6
Requires:	python3-html2text
%if %{_ver_ge %py3_ver 3.13}
Requires:	python3-legacy-cgi
%endif
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A python script that converts RSS/Atom newsfeeds to email.

%package -n zsh-completion-rss2email
Summary:	ZSH completion for rss2email
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}

%description -n zsh-completion-rss2email
ZSH completion for rss2email.

%prep
%setup -q

%{__sed} -i -e '1s,^#!.*python,#!%{__python3},' r2e

%build
%{py3_build}

%install
rm -rf $RPM_BUILD_ROOT

%{py3_install}

install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{zsh_compdir}}
cp -p r2e.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p completion/r2e.zsh $RPM_BUILD_ROOT%{zsh_compdir}/_r2e

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README.rst
%attr(755,root,root) %{_bindir}/r2e
%dir %{py3_sitescriptdir}/rss2email
%{py3_sitescriptdir}/rss2email/*.py
%{py3_sitescriptdir}/rss2email/__pycache__
%{py3_sitescriptdir}/rss2email/post_process
%{py3_sitescriptdir}/rss2email-*.egg-info
%{_mandir}/man1/r2e.1*

%files -n zsh-completion-rss2email
%defattr(644,root,root,755)
%{zsh_compdir}/_r2e
