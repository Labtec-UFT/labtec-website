import './App.css'
import { useEffect, useState } from 'react'
import Header from '@components/ui/Header'
import Footer from '@components/ui/Footer'

function App() {
  type Member = { id: number; name: string; role: string; avatar?: string; course?: string }
  const [team, setTeam] = useState<Member[]>([])

  useEffect(() => {
    fetch('/team.json')
      .then((res) => {
        if (!res.ok) throw new Error('Network response was not ok')
        return res.json()
      })
      .then((data: Member[]) => setTeam(data))
      .catch((err) => {
        console.error('Failed to load team.json', err)
      })
  }, [])

  return (
    <>
      <Header />

      <div className="w-full h-96 bg-black flex items-center">
        <div className="w-full max-w-7xl mx-auto px-4 sm:px-8 md:px-12 lg:px-16">
          <p className="text-4xl sm:text-5xl md:text-6xl font-bold text-white opacity-15">
            BANNER
          </p>
        </div>
      </div>

      <main className="w-full pt-14">
        <div className="flex flex-col gap-24 w-full max-w-7xl mx-auto px-4 sm:px-8 md:px-12 lg:px-16">

          <section id="sobre" className="flex flex-col items-center gap-12 w-full" style={{ scrollMarginTop: '100px' }}>
            <header className="flex flex-col items-center text-center text-slate-900 gap-2">
              <p className="text-lg leading-7 tracking-tight">
                SOBRE NÓS
              </p>
              <h2 id="missao" className="text-2xl font-bold leading-8 tracking-tight" style={{ scrollMarginTop: '64px' }}>
                NOSSA MISSÃO
              </h2>
            </header>

            <div className="w-full border-t border-black/20" />

            <div className="grid md:grid-cols-2 gap-12 w-full items-center" id="sobre">

              <div className="w-full">
                <div className="w-full h-50 sm:h-75 md:h-105 bg-gray-200 rounded-3xl" />
              </div>

              <div className="text-gray-700 text-base leading-relaxed">
                <p>
                  O <b> Laboratório de Tecnologias Computacionais (LABTEC)</b> da <b>Universidade Federal do Tocantins</b> é um espaço dedicado ao desenvolvimento de soluções tecnológicas, com foco em fabricação digital, prototipagem e aplicação prática do conhecimento em computação. Integrado ao curso de Ciência da Computação, o laboratório promove a transformação de ideias em projetos reais.
                </p>
                <p className="mt-4">
                  Sua atuação conecta ensino, pesquisa e extensão, incentivando a criatividade, o pensamento computacional e a construção de soluções que geram impacto dentro e fora da universidade. Por meio de projetos educacionais, tecnológicos e sociais, o Labtec contribui para tornar a tecnologia mais acessível e relevante para a comunidade.
                </p>
              </div>

            </div>
          </section>

          <article id="estrutura" className="flex flex-col items-center gap-12 w-full" style={{ scrollMarginTop: '100px' }}>

            <header className="flex flex-col items-center text-center text-slate-900 gap-2">
              <p className="text-lg leading-7 tracking-tight">
                ESTRUTURA
              </p>
              <h2 className="text-2xl font-bold leading-8 tracking-tight">
                NOSSO ESPAÇO
              </h2>
            </header>

            <div className="w-full border-t border-black/20" />

            <div className="flex flex-col md:flex-row gap-16 w-full items-start">

              <div className="flex flex-col gap-16 w-full md:flex-1">

                <div className="flex flex-col gap-6">
                  <div className="flex flex-col gap-2 text-gray-800">
                    <h3 className="text-base font-semibold">
                      Sala de Reuniões
                    </h3>
                    <p className="text-sm">
                      Espaço confortável para reuniões e apresentações
                    </p>
                  </div>
                  <div className="bg-gray-100 h-48 sm:h-64 md:h-80 rounded-3xl" />
                </div>

                <div className="flex flex-col gap-6">
                  <div className="flex flex-col gap-2 text-gray-800">
                    <h3 className="text-base font-semibold">
                      Laboratório
                    </h3>
                    <p className="text-sm">
                      Equipado com impressoras 3D
                    </p>
                  </div>
                  <div className="bg-gray-100 h-48 sm:h-64 md:h-80 rounded-3xl" />
                </div>

              </div>

              <div className="flex flex-col gap-16 w-full md:flex-1">

                <div className="flex flex-col gap-6">
                  <div className="flex flex-col gap-2 text-gray-800">
                    <h3 className="text-base font-semibold">
                      Área de Trabalho
                    </h3>
                    <p className="text-sm">
                      Mesas e estações para colaboração diária
                    </p>
                  </div>
                  <div className="bg-gray-100 h-64 sm:h-80 md:h-104 rounded-3xl" />
                </div>

                <div className="flex flex-col gap-6">
                  <div className="flex flex-col gap-2 text-gray-800">
                    <h3 className="text-base font-semibold">
                      Espaço Comum
                    </h3>
                    <p className="text-sm">
                      Área para descanso e interação rápida
                    </p>
                  </div>
                  <div className="bg-gray-100 h-48 sm:h-64 md:h-72 rounded-3xl" />
                </div>

              </div>
            </div>
          </article>

          <section id="equipe" className="flex flex-col items-center gap-12 w-full" style={{ scrollMarginTop: '100px' }}>
            <header className="flex flex-col items-center text-center text-slate-900 gap-2">
              <p className="text-lg leading-7 tracking-tight">
                EQUIPE
              </p>
              <h2 className="text-2xl font-bold leading-8 tracking-tight">
                NOSSO TIME
              </h2>
            </header>

            <div className="w-full border-t border-black/20" />

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-10 w-full">

              {(((team.length ? team : Array.from({ length: 6 }, (_, i) => ({
                id: i + 1,
                name: 'Nome do Integrante',
                role: 'Função ou área',
                avatar: undefined,
                course: undefined,
              }))) as Member[])).map((member) => (
                <div key={member.id} className="flex flex-col gap-4 items-center text-center group transition-transform duration-300 transform hover:-translate-y-1 hover:scale-105">
                  {member.avatar ? (
                    <img
                      src={member.avatar}
                      alt={member.name}
                      className="w-32 h-32 object-cover rounded-full transition-transform duration-300 group-hover:scale-105 ring-2 ring-transparent group-hover:ring-black/10"
                    />
                  ) : (
                    <div className="w-32 h-32 bg-gray-200 rounded-full" />
                  )}

                  <div className="mt-2">
                    <h3 className="text-sm font-semibold text-gray-900 group-hover:text-slate-900">{member.name}</h3>
                    <p className="text-xs text-gray-500">{member.role}{member.course ? ` - ${member.course}` : ''}</p>
                  </div>
                </div>
              ))}

            </div>
          </section>
        </div>
      </main>

      <div className="w-full mt-20 bg-black flex items-center py-16">
        <div className="w-full max-w-7xl mx-auto px-4 sm:px-8 md:px-12 lg:px-16 flex flex-col gap-6">

          <div>
            <h3 className="text-3xl sm:text-5xl md:text-5xl font-bold text-white">
              Dê vida às suas ideias
            </h3>
            <p className="text-white mt-2 text-lg">
              Envie seu projeto e nós cuidamos da impressão 3D para você.
            </p>
          </div>

          <button
            className="group relative flex items-center justify-center w-75 h-12.5 active:scale-95 transition-transform"
            type="button"
          >
            <div className="absolute inset-0 pointer-events-none transition-opacity duration-1200 opacity-100 group-hover:opacity-0 bg-[radial-gradient(15%_50%_at_50%_100%,white_0%,transparent_100%)] blur-[15px] rounded-md" />
            <div className="absolute inset-0 pointer-events-none transition-opacity duration-1200 opacity-0 group-hover:opacity-100 bg-[radial-gradient(60%_50%_at_50%_100%,white_0%,transparent_100%)] blur-[18px] rounded-md" />
            <div className="absolute inset-0 pointer-events-none transition-opacity duration-1200 opacity-100 group-hover:opacity-0 bg-[radial-gradient(10%_50%_at_50%_100%,white_0%,transparent_100%)] rounded-md" />
            <div className="absolute inset-0 pointer-events-none transition-opacity duration-1200 opacity-0 group-hover:opacity-100 bg-[radial-gradient(60%_50%_at_50%_100%,white_0%,transparent_100%)] rounded-md" />

            <div className="absolute inset-px rounded-[7px] bg-white z-10" />

            <span className="relative z-20 text-black text-sm font-medium tracking-wide">
              Fazer Orçamento
            </span>
          </button>
        </div>
      </div>

      <Footer />
    </>
  )
}

export default App