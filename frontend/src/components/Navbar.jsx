export default function Navbar(){

    return(

        <header className="h-16 border-b bg-white flex items-center justify-between px-6">

            <h1 className="text-2xl font-bold">

                AI Document Assistant

            </h1>

            <span className="text-sm text-gray-500">

                Powered by Gemini

            </span>
            <button

               onClick={() => {
            
                   localStorage.removeItem("chat-history");
            
                   window.location.reload();
            
               }}
            
               className="rounded bg-red-500 px-3 py-2 text-white"
            
            >
            
               Clear Chat
            
             </button>

        </header>

    );

}