import Header from "@components/ui/Header.tsx";

import Background from "@assets/svgs/background/void.svg?react"

function Project(){
    return(
        <>
           <Header />

           <div className="h-106 w-screen relative overflow-hidden">
               <Background className="absolute inset-0 w-full h-full object-cover" />
           </div>
        </>
    )
}


export default Project