# revision 25597
# category Package
# catalog-ctan /macros/latex/contrib/bashful
# catalog-date 2011-06-17 14:38:58 +0200
# catalog-license lppl1.3
# catalog-version 0.92
Name:		texlive-bashful
Version:	0.92
Release:	8
Summary:	Invoke bash commands from within LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bashful
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bashful.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bashful.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.92-3
+ Revision: 787565
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.92-2
+ Revision: 749451
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.92-1
+ Revision: 717885
- texlive-bashful
- texlive-bashful
- texlive-bashful
- texlive-bashful
- texlive-bashful

