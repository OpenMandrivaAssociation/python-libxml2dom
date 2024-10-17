%define oname libxml2dom
%define name python-%oname

Summary:	A traditional DOM wrapper around the Python bindings for libxml2
Name:		%{name}
Version:	0.5
Release:	3
Source0:	https://files.pythonhosted.org/packages/35/92/fbf67a6eb368faab70a2ec6473f5f370a868e766e20eb0e10678e97ae75f/libxml2dom-0.5.tar.bz2
License:	LGPLv3+
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch
URL:		https://www.boddie.org.uk/python/libxml2dom.html
BuildRequires:	python-devel libxml2-python
Requires:	libxml2-python

%description
The libxml2dom package provides a traditional DOM wrapper around the
Python bindings for libxml2. In contrast to the standard libxml2 bindings,
libxml2dom provides an API reminiscent of minidom, pxdom and other
Python-based and Python-related XML toolkits. Performance is fairly
respectable since libxml2dom makes direct use of libxml2mod - the
low-level wrapping of libxml2 for Python. Moreover, serialisation of
documents is much faster than many other toolkits because libxml2dom
can make direct use of libxml2 rather than employing Python-level
mechanisms to visit and serialise nodes.

%prep
%setup -q -n %oname-%version

%build
python setup.py build

%install
rm -rf %buildroot
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt docs/COPYING.txt docs/libxml2macro.html docs/NOTES_libxml2macro.txt docs/styles.css
%{_bindir}/libxml2macro.py
%py_puresitedir/%oname/
%py_puresitedir/*.egg-info



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.4.7-3mdv2010.0
+ Revision: 442275
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.4.7-2mdv2009.1
+ Revision: 323753
- rebuild

* Wed Dec 10 2008 Nicolas Vigier <nvigier@mandriva.com> 0.4.7-1mdv2009.1
+ Revision: 312514
- import python-libxml2dom


