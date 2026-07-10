%global tl_name bashful
%global tl_revision 25597

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.93
Release:	%{tl_revision}.1
Summary:	Invoke bash commands from within LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bashful
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bashful.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bashful.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes it possible to execute Unix bash shell scripts from
within LaTeX. The main application is in writing computer-science texts,
in which you want to make sure the programs listed in the document are
executed directly from the input. The package may use other Unix shells
than bash, but does not work without modification in a Windows
environment. The package requires the -shell-escape flag when LaTeX is
processing your document.

