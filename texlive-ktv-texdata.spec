%global tl_name ktv-texdata
%global tl_revision 27369

Name:		texlive-%{tl_name}
Epoch:		1
Version:	05.34
Release:	%{tl_revision}.1
Summary:	Extract subsets of documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ktv-texdata
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ktv-texdata.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ktv-texdata.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ktv-texdata.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines an exercice environment which numbers every
exercise, and a command \get to extract a collection whose argument is a
comma-separated set of exercise index numbers. While the package was
designed for teachers constructing tables of exercises, it plainly has
more general application.

