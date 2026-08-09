import { Trash2 } from "lucide-react";

export default function DocumentCard({

    document,

    onDelete

}){

    return(

        <div className="bg-slate-800 rounded-lg p-3">

            <div className="flex justify-between items-center">

                <div>

                    <p className="font-semibold">

                        📄 {document.filename}

                    </p>

                    <p className="text-sm text-gray-400">

                        {document.chunks} chunks

                    </p>

                </div>

                <button
                    onClick={()=>onDelete(document.document_id)}
                >

                    <Trash2
                        size={18}
                        className="text-red-400 hover:text-red-600"
                    />

                </button>

            </div>

        </div>

    );

}