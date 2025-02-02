Name:		texlive-bashful
Version:	25597
Release:	2
Summary:	Invoke bash commands from within LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bashful
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bashful.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bashful.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes it possible to execute Unix bash shell
scripts from within LaTeX. The main application is in writing
computer-science texts, in which you want to make sure the
programs listed in the document are executed directly from the
input. The package may use other Unix shells than bash, but
does not work without modification in a Windows environment.
The package requires the -shell-escape flag when LaTeX is
processing your document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bashful/bashful.sty
%doc %{_texmfdistdir}/doc/latex/bashful/Makefile
%doc %{_texmfdistdir}/doc/latex/bashful/README
%doc %{_texmfdistdir}/doc/latex/bashful/bashful.pdf
%doc %{_texmfdistdir}/doc/latex/bashful/bashful.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
