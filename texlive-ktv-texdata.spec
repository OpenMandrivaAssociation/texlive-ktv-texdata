Name:		texlive-ktv-texdata
Version:	27369
Release:	1
Summary:	Extract subsets of documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ktv-texdata
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ktv-texdata.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ktv-texdata.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ktv-texdata.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines an exercice environment which numbers every
exercise, and a command \get to extract a collection whose
argument is a comma-separated set of exercise index numbers.
While the package was designed for teachers constructing tables
of exercises, it plainly has more general application.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ktv-texdata/ktv-buildnum.sty
%{_texmfdistdir}/tex/latex/ktv-texdata/ktv-texdata.sty
%doc %{_texmfdistdir}/doc/latex/ktv-texdata/README
%doc %{_texmfdistdir}/doc/latex/ktv-texdata/README.txt.doc
%doc %{_texmfdistdir}/doc/latex/ktv-texdata/ktv-data.tex
%doc %{_texmfdistdir}/doc/latex/ktv-texdata/ktv-test.KTVhint
%doc %{_texmfdistdir}/doc/latex/ktv-texdata/ktv-test.tex
%doc %{_texmfdistdir}/doc/latex/ktv-texdata/ktv-texdata.ktvnum
%doc %{_texmfdistdir}/doc/latex/ktv-texdata/ktv-texdata.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ktv-texdata/ktv-texdata.dtx
%doc %{_texmfdistdir}/source/latex/ktv-texdata/ktv-texdata.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
