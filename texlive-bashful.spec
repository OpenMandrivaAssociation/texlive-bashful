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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes it possible to execute Unix bash shell scripts from
within LaTeX. The main application is in writing computer-science texts,
in which you want to make sure the programs listed in the document are
executed directly from the input. The package may use other Unix shells
than bash, but does not work without modification in a Windows
environment. The package requires the -shell-escape flag when LaTeX is
processing your document.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bashful
%dir %{_datadir}/texmf-dist/tex/latex/bashful
%doc %{_datadir}/texmf-dist/doc/latex/bashful/Makefile
%doc %{_datadir}/texmf-dist/doc/latex/bashful/README
%doc %{_datadir}/texmf-dist/doc/latex/bashful/bashful.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bashful/bashful.tex
%{_datadir}/texmf-dist/tex/latex/bashful/bashful.sty
