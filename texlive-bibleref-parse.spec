Name:		texlive-bibleref-parse
Version:	22054
Release:	2
Summary:	Specify Bible passages in human-readable format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-parse
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-parse.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-parse.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package parses Bible passages that are given in human
readable format. It accepts a wide variety of formats. This
allows for a simpler and more convenient interface to the
functionality of the bibleref package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibleref-parse/bibleref-parse.sty
%doc %{_texmfdistdir}/doc/latex/bibleref-parse/README
%doc %{_texmfdistdir}/doc/latex/bibleref-parse/bibleref-parse.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref-parse/bibleref-parse.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
