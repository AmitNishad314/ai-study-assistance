import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

export default function MainLayout({children}){

    return(

        <div className="flex h-screen">

            <Sidebar/>

            <div className="flex flex-col flex-1">

                <Navbar/>

                <main className="flex-1 overflow-auto p-6 bg-gray-100">

                    {children}

                </main>

            </div>

        </div>

    );

}