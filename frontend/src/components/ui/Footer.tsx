import LinkeInIcon from "@assets/svgs/socials/linkedin-in.svg?react"
import InstagramIcon from "@assets/svgs/socials/instagram.svg?react"
import YoutubeIcon from "@assets/svgs/socials/youtube.svg?react"

export default function Footer() {
  return (
    <footer className="px-6 mt-20 text-black border-t-2 border-t-gray-200">
      <div className="max-w-7xl mx-auto py-10">

        <h2 className="text-3xl font-bold mb-8">LABTEC</h2>

        <div className="grid gap-12 md:grid-cols-2 lg:grid-cols-5">

          {/* CONTATO (último no mobile, primeiro no desktop) */}
          <section className="flex flex-col gap-4 order-last lg:order-first">
            <div>
              <h3 className="font-bold mb-2">Contato</h3>
              <p>labtec@uft.edu.br</p>
              <a href="https://www.uft.edu.br/" className="hover:text-blue-500">
                www.uft.edu.br
              </a>
            </div>

            <div className="flex gap-5 pt-4 border-t border-black/20">
              <LinkeInIcon className="w-5 h-5 cursor-pointer" />
              <YoutubeIcon className="w-5 h-5 cursor-pointer" />
              <InstagramIcon className="w-5 h-5 cursor-pointer" />
            </div>
          </section>

          {/* LABTEC */}
          <nav className="order-1">
            <h3 className="font-bold mb-2">Labtec</h3>
            <ul className="space-y-1">
              <li><a href="/#sobre">Sobre Nós</a></li>
              <li><a href="/#estrutura">Estrutura</a></li>
              <li><a href="/#equipe">Equipe</a></li>
              <li><a href="/#autolab">AutoLab de Robótica</a></li>
            </ul>
          </nav>

          {/* PROJETOS */}
          <nav className="order-2">
            <h3 className="font-bold mb-2">Projetos</h3>
            <ul className="space-y-1 [&_a:hover]:cursor-not-allowed" title="Essas páginas não estão disponíveis ainda!">
              <li><a href="/#projetos">Impressão 3D</a></li>
              <li><a href="/#projetos">Modelagem</a></li>
              <li><a href="/#projetos">Softwares</a></li>
              <li><a href="/#projetos">Robótica</a></li>
            </ul>
          </nav>

          {/* NOTÍCIAS */}
          <nav className="order-3">
            <h3 className="font-bold mb-2">Notícias</h3>
            <ul className="space-y-1 [&_a:hover]:cursor-not-allowed" title="Essas páginas não estão disponíveis ainda!">
              <li><a href="/#noticias">Últimas Notícias</a></li>
              <li><a href="/#noticias">Destaques</a></li>
              <li><a href="/#noticias">Feed</a></li>
            </ul>
          </nav>

          {/* SERVIÇOS */}
          <nav className="order-4">
            <h3 className="font-bold mb-2">Serviços</h3>
            <ul className="space-y-1 [&_a:hover]:cursor-not-allowed" title="Essas páginas não estão disponíveis ainda!">
              <li><a href="/#servicos">Impressão 3D</a></li>
            </ul>
          </nav>
        </div>
      </div>

      <div className="w-full bg-white">
        <div className="w-full max-w-7xl mx-auto px-4 sm:px-8 md:px-12 lg:px-16 text-center text-xs text-gray-500 py-6">
          {new Date().getFullYear()} LABTEC — Todos os direitos reservados.
        </div>
      </div>
    </footer>
  )
}