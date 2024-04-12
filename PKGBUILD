# Maintainer: Joar Heimonen <joarheimonen@live.no>
# Note: This is only an install script for Yuma123, not the actual project itself.

pkgname=yuma123
pkgver=1
pkgrel=1
pkgdesc="Package description for yuma123"
arch=('x86_64')
url="https://github.com/vlvassilev/yuma123"
#license=('GPL3')

#depends=('vi' 'ffmpeg')
#makedepends=('qt5-tools')

#source=("https://github.com/[your package].tar.gz")

#sha512sums=("[paste sha512sum output]")


build() {
  cd "$srcdir"
  # Your build
   cd "$srcdir/yuma123"
   make DESTDIR="${pkgdir}" install
   mv "${pkgdir}/usr/sbin" "${pkgdir}/usr/bin"
 }

package() {

  # Create necessary directories
  #install -d "$pkgdir/usr/bin"


  # Install additional files
  #install -m644 usr/share/[package name]/[folder name]/* "$pkgdir/usr/share/[package name]/[folder name]"

  # Change ownership
  #chown -R "$USER:$USER" "$pkgdir/usr/share/[your package]"

}
