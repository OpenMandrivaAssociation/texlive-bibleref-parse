Name:		texlive-bibleref-parse
Version:	1.1
Release:	1
Summary:	Specify Bible passages in human-readable format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-parse
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-parse.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-parse.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package parses Bible passages that are given in human
readable format. It accepts a wide variety of formats. This
allows for a simpler and more convenient interface to the
functionality of the bibleref package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibleref-parse/bibleref-parse.sty
%doc %{_texmfdistdir}/doc/latex/bibleref-parse/README
%doc %{_texmfdistdir}/doc/latex/bibleref-parse/bibleref-parse.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref-parse/bibleref-parse.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
