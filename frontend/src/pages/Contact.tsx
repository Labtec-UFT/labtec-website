import Header from '@components/ui/Header'
import Footer from '@components/ui/Footer'

function Contact() {
  return (
    <>
      <Header />

      <main className="w-full pt-20">
        <section className="flex flex-col items-center gap-12 w-full max-w-4xl mx-auto px-4 sm:px-8 md:px-12">

          <header className="flex flex-col items-center text-center text-slate-900 gap-2">
            <p className="text-lg tracking-tight">
              CONTATO
            </p>
            <h1 className="text-3xl sm:text-4xl font-bold tracking-tight">
              Fale conosco
            </h1>
            <p className="text-gray-600 max-w-xl mt-2 text-sm sm:text-base">
              Entre em contato com o Laboratório de Tecnologias Computacionais para dúvidas, parcerias ou solicitações de serviços.
            </p>
          </header>

          <div className="w-full border-t border-black/20" />

          <div className="w-full bg-white border border-black/10 rounded-3xl p-8 sm:p-10 flex flex-col gap-8">

            <div className="flex flex-col gap-1">
              <span className="text-xs text-gray-500 uppercase tracking-wide">
                Email
              </span>
              <a
                href="mailto:labtec@uft.edu.br"
                className="text-base font-medium text-gray-900 hover:opacity-60 transition"
              >
                labtec@uft.edu.br
              </a>
            </div>

            {/* Divider interno */}
            <div className="w-full border-t border-black/10" />

            {/* Item */}
            <div className="flex flex-col gap-1">
              <span className="text-xs text-gray-500 uppercase tracking-wide">
                Telefone
              </span>
              <a
                href="tel:"
                className="text-base font-medium text-gray-900 hover:opacity-60 transition"
              >
                (63) 99999-9999
              </a>
            </div>

            <div className="w-full border-t border-black/10" />

            <div className="flex flex-col gap-1">
              <span className="text-xs text-gray-500 uppercase tracking-wide">
                Localização
              </span>
              <p className="text-base font-medium text-gray-900">
                Universidade Federal do Tocantins - Campus Palmas
              </p>
                <p className="text-base text-gray-900">
                Av. NS 15 - Plano Diretor Norte, Palmas - TO, 77001-090
              </p>

            </div>

          </div>

        </section>
      </main>

      <Footer />
    </>
  )
}

export default Contact