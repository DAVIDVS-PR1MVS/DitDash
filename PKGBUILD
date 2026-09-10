# Maintainer: DitPlex Team
pkgname=ditplex-bin
pkgver=1.0.3
pkgrel=1
pkgdesc="Utilitário DitPlex"
arch=('x86_64')
url="https://github.com/DAVIDVS-PR1MVS/DitPlex"
license=('MIT')
depends=('gcc-libs' 'glibc')
provides=('ditplex')
conflicts=('ditplex')
source=("${pkgname}-${pkgver}.pkg.tar.zst::https://github.com/DAVIDVS-PR1MVS/DitPlex/releases/download/v${pkgver}/DitPlex-${pkgver}-1-x86_64.pkg.tar.zst")
sha256sums=('SKIP')

package() {
    cp -r "${srcdir}/usr" "${pkgdir}/"
}