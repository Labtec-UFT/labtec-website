import LinkeInIcon from "@assets/svgs/socials/linkedin-in.svg?react"
import InstagramIcon from "@assets/svgs/socials/instagram.svg?react"
import AngleDownIcon from "@assets/svgs/ui/angle-down.svg?react"
import YoutubeIcon from "@assets/svgs/socials/youtube.svg?react"
import { useState, useRef, useEffect } from "react"
import { Link } from 'react-router-dom'

function Divider({ visible }: { visible: boolean }) {
  return (
    <div
      className={`overflow-hidden transition-all duration-200 ${
        visible ? "opacity-100 scale-x-100 my-1" : "opacity-0 scale-x-0 my-0"
      }`}
    >
      <div className="h-px w-full bg-gray-300 origin-left" />
    </div>
  )
}

function Header() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false)
  const [isMobileQuemOpen, setIsMobileQuemOpen] = useState(false)
  const [isMobileServicosOpen, setIsMobileServicosOpen] = useState(false)

  const [isDesktopQuemOpen, setIsDesktopQuemOpen] = useState(false)
  const [isDesktopServicosOpen, setIsDesktopServicosOpen] = useState(false)

  const navRef = useRef<HTMLElement | null>(null)

  useEffect(() => {
    function handlePointerDown(e: PointerEvent) {
      const nav = navRef.current
      if (!nav) return
      const target = e.target as Node | null
      if (target && !nav.contains(target)) {
        setIsDesktopQuemOpen(false)
        setIsDesktopServicosOpen(false)
      }
    }

    document.addEventListener("pointerdown", handlePointerDown)
    return () => document.removeEventListener("pointerdown", handlePointerDown)
  }, [])

  function closeMobileMenu() {
    setIsMobileMenuOpen(false)
    setIsMobileQuemOpen(false)
    setIsMobileServicosOpen(false)
  }

  return (
    <>
      <header className="sticky top-0 left-0 right-0 z-50 bg-white shadow">
        <nav
          ref={navRef}
          className="relative max-w-7xl mx-auto flex items-center justify-between p-4 h-16"
        >
        <Link to="/" aria-label="Ir para a página inicial" className="text-3xl font-black font-nunito-sans">
          LABTEC
        </Link>

        {/* HAMBURGER */}
        <div className="lg:hidden">
          <button
            aria-label="Abrir menu"
            aria-expanded={isMobileMenuOpen}
            onClick={() => setIsMobileMenuOpen(prev => !prev)}
            className="relative w-8 h-8 flex items-center justify-center"
          >
            <span className={`absolute w-6 h-0.5 bg-black transition-all duration-300 ${isMobileMenuOpen ? "rotate-45" : "-translate-y-2"}`} />
            <span className={`absolute w-6 h-0.5 bg-black transition-all duration-300 ${isMobileMenuOpen ? "opacity-0" : ""}`} />
            <span className={`absolute w-6 h-0.5 bg-black transition-all duration-300 ${isMobileMenuOpen ? "-rotate-45" : "translate-y-2"}`} />
          </button>
        </div>

        {/* DESKTOP MENU */}
        <ul className="hidden lg:flex items-center gap-8 text-sm font-semibold text-black">

          {/* QUEM SOMOS */}
          <li
            className="relative"
            onMouseEnter={() => setIsDesktopQuemOpen(true)}
            onMouseLeave={() => setIsDesktopQuemOpen(false)}
          >
            <button
              onClick={() =>
                setIsDesktopQuemOpen(prev => {
                  const next = !prev
                  if (next) setIsDesktopServicosOpen(false)
                  return next
                })
              }
              className="flex items-center gap-1"
            >
              O LABTEC
              <AngleDownIcon className="w-3 h-3" />
            </button>

            <ul
              className={`absolute top-full left-0 w-52 bg-white shadow-md rounded p-2 transition-all duration-200 ${
                isDesktopQuemOpen ? "opacity-100 visible" : "opacity-0 invisible"
              }`}
            >
              <li>
                <a href="/#sobre" className="block px-4 py-2 hover:bg-gray-100">Sobre Nós</a>
              </li>


              <li>
                <a href="/#estrutura" className="block px-4 py-2 hover:bg-gray-100">Estrutura do Laboratório</a>
              </li>

              <Divider visible />
                <li>
                <a href="/#equipe" className="block px-4 py-2 hover:bg-gray-100">Equipe</a>
              </li>

                <Divider visible />
                <li>
                <a href="#" className="block px-4 py-2 hover:bg-gray-100">Liga AutoLab de Robôtica</a>
              </li>
            </ul>
          </li>

          <li><a href="/#projetos">PROJETOS</a></li>
          <li><a href="/#noticias">NOTÍCIAS</a></li>

          {/* SERVIÇOS */}
          <li
            className="relative"
            onMouseEnter={() => setIsDesktopServicosOpen(true)}
            onMouseLeave={() => setIsDesktopServicosOpen(false)}
          >
            <button
              onClick={() =>
                setIsDesktopServicosOpen(prev => {
                  const next = !prev
                  if (next) setIsDesktopQuemOpen(false)
                  return next
                })
              }
              className="flex items-center gap-1"
            >
              SERVIÇOS
              <AngleDownIcon className="w-3 h-3" />
            </button>

            <ul
              className={`absolute top-full left-0 w-40 bg-white shadow-md rounded p-2 transition-all duration-200 ${
                isDesktopServicosOpen ? "opacity-100 visible" : "opacity-0 invisible"
              }`}
            >
              <li>
                <a href="/#servicos" className="block px-4 py-2 hover:bg-gray-100">
                  Impressão 3D
                </a>
              </li>
            </ul>
          </li>

          <li><a href="/contact">CONTATO</a></li>
        </ul>

        {/* SOCIAL */}
        <div className="hidden lg:flex gap-7">
          <LinkeInIcon className="w-5 h-5 hover:cursor-not-allowed" />
          <YoutubeIcon className="w-5 h-5" />
          <InstagramIcon className="w-5 h-5" />
        </div>
      </nav>

      {/* OVERLAY */}
      <div
        className={`fixed inset-0 bg-black/40 z-40 transition-opacity duration-300 lg:hidden ${
          isMobileMenuOpen ? "opacity-100 visible" : "opacity-0 invisible"
        }`}
        onClick={closeMobileMenu}
      />

      {/* DRAWER MOBILE */}
      <div
        className={`fixed top-0 right-0 h-full w-[80%] max-w-sm bg-white z-50 shadow-lg transform transition-transform duration-300 lg:hidden ${
          isMobileMenuOpen ? "translate-x-0" : "translate-x-full"
        }`}
      >
        <div className="flex flex-col h-full p-6 text-sm font-semibold text-gray-800">

          <button onClick={() => setIsMobileQuemOpen(prev => !prev)} className="flex justify-between py-2">
            QUEM SOMOS
            <AngleDownIcon className={`w-3 h-3 ${isMobileQuemOpen ? "rotate-180" : ""}`} />
          </button>

          <Divider visible={isMobileQuemOpen} />

            {isMobileQuemOpen && (
            <div className="pl-3 flex flex-col gap-4 text-gray-600">
              <a href="/#sobre" onClick={closeMobileMenu}>Sobre Nós</a>
              <a href="/#estrutura" onClick={closeMobileMenu}>Estrutura do Laboratório</a>
              <a href="/#equipe" onClick={closeMobileMenu}>Equipe</a>
              <a href="#" onClick={closeMobileMenu}>Liga AutoLab de Robôtica</a>
            </div>
          )}

          <Divider visible />

          <a href="/#projetos" onClick={closeMobileMenu} className="py-2">PROJETOS</a>

          <Divider visible />

          <a href="/#noticias" onClick={closeMobileMenu} className="py-2">NOTÍCIAS</a>

          <Divider visible />

          <button onClick={() => setIsMobileServicosOpen(prev => !prev)} className="flex justify-between py-2">
            SERVIÇOS
            <AngleDownIcon className={`w-3 h-3 ${isMobileServicosOpen ? "rotate-180" : ""}`} />
          </button>

          <Divider visible={isMobileServicosOpen} />

            {isMobileServicosOpen && (
            <div className="pl-3 flex flex-col gap-2 text-gray-600">
              <a href="/#servicos" onClick={closeMobileMenu}>Impressão 3D</a>
            </div>
          )}

          <Divider visible />

          <a href="/contact" onClick={closeMobileMenu} className="py-2">CONTATO</a>

          <div className="mt-auto flex gap-5 pt-6 border-t">
            <LinkeInIcon className="w-5 h-5 hover:cursor-not-allowed" />
            <YoutubeIcon className="w-5 h-5" />
            <InstagramIcon className="w-5 h-5" />
          </div>
        </div>
      </div>
      </header>
    </>
  )
}

export default Header