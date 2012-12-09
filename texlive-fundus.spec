# revision 18146
# category Package
# catalog-ctan /macros/latex/contrib/gene/fundus
# catalog-date 2008-09-12 11:49:08 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-fundus
Version:	20080912
Release:	2
Summary:	Providing LaTeX access to various font families
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gene/fundus
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Fonts supported are Peter Vanroose's calligra and handwriting
fonts, the Washington University cyrillic fonts, the la and lla
children's handwriting fonts, the Computer Modern outline
fonts, various 'Star Trek' fonts, Sutterlin and schwell
handwriting fonts, the twcal calligraphic fonts, and the va
handwriting fonts. Note that the Washington University fonts
are now officially supported by LaTeX, as the OT2 encoding.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fundus/calligra.sty
%{_texmfdistdir}/tex/latex/fundus/cyr.sty
%{_texmfdistdir}/tex/latex/fundus/la.sty
%{_texmfdistdir}/tex/latex/fundus/ot1ocm.fd
%{_texmfdistdir}/tex/latex/fundus/ot1ocmss.fd
%{_texmfdistdir}/tex/latex/fundus/ot1ocmtt.fd
%{_texmfdistdir}/tex/latex/fundus/pvscript.sty
%{_texmfdistdir}/tex/latex/fundus/startrek.sty
%{_texmfdistdir}/tex/latex/fundus/suetterl.sty
%{_texmfdistdir}/tex/latex/fundus/twcal.sty
%{_texmfdistdir}/tex/latex/fundus/va.sty
%doc %{_texmfdistdir}/doc/latex/fundus/doc/calligra.pdf
%doc %{_texmfdistdir}/doc/latex/fundus/doc/la.pdf
%doc %{_texmfdistdir}/doc/latex/fundus/doc/outline.pdf
%doc %{_texmfdistdir}/doc/latex/fundus/doc/twcal.pdf
%doc %{_texmfdistdir}/doc/latex/fundus/startrek.map
%doc %{_texmfdistdir}/doc/latex/fundus/stclass.zip
%doc %{_texmfdistdir}/doc/latex/fundus/stmov.zip
%doc %{_texmfdistdir}/doc/latex/fundus/tngcril.zip
%doc %{_texmfdistdir}/doc/latex/fundus/tngmon.zip
%doc %{_texmfdistdir}/doc/latex/fundus/tngtit.zip
#- source
%doc %{_texmfdistdir}/source/latex/fundus/calligra.dtx
%doc %{_texmfdistdir}/source/latex/fundus/calligra.ins
%doc %{_texmfdistdir}/source/latex/fundus/la.dtx
%doc %{_texmfdistdir}/source/latex/fundus/la.ins
%doc %{_texmfdistdir}/source/latex/fundus/outline.dtx
%doc %{_texmfdistdir}/source/latex/fundus/outline.ins
%doc %{_texmfdistdir}/source/latex/fundus/pvscript.dtx
%doc %{_texmfdistdir}/source/latex/fundus/pvscript.ins
%doc %{_texmfdistdir}/source/latex/fundus/startrek.dtx
%doc %{_texmfdistdir}/source/latex/fundus/startrek.ins
%doc %{_texmfdistdir}/source/latex/fundus/suetterl.dtx
%doc %{_texmfdistdir}/source/latex/fundus/suetterl.ins
%doc %{_texmfdistdir}/source/latex/fundus/twcal.dtx
%doc %{_texmfdistdir}/source/latex/fundus/twcal.ins
%doc %{_texmfdistdir}/source/latex/fundus/va.dtx
%doc %{_texmfdistdir}/source/latex/fundus/va.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080912-2
+ Revision: 752177
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080912-1
+ Revision: 718515
- texlive-fundus
- texlive-fundus
- texlive-fundus
- texlive-fundus

