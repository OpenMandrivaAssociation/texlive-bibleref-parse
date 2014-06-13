# revision 22054
# category Package
# catalog-ctan /macros/latex/contrib/bibleref-parse
# catalog-date 2011-04-11 08:43:57 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-bibleref-parse
Version:	1.1
Release:	7
Summary:	Specify Bible passages in human-readable format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-parse
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-parse.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-parse.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 749691
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 717937
- texlive-bibleref-parse
- texlive-bibleref-parse
- texlive-bibleref-parse
- texlive-bibleref-parse
- texlive-bibleref-parse

