import { useEffect, useState } from "react";

import UploadButton from "./UploadButton";
import DocumentCard from "./DocumentCard";

import {

    uploadPDF,

    getDocuments,

    deleteDocument

} from "../services/api";

import toast from "react-hot-toast";

export default function Sidebar() {

    const [documents, setDocuments] = useState([]);
    const [uploading,setUploading]=useState(false);

    async function loadDocuments() {
        try {
            const docs = await getDocuments();
    
            console.log(docs);
            console.log(Array.isArray(docs));
    
            setDocuments(
                Object.entries(docs).map(([document_id, data]) => ({
                    document_id,
                    ...data,
                }))
            );
    
        } catch (err) {
            console.error(err);
        }
    }

    async function handleUpload(file){

        try{
    
            setUploading(true);
    
            await uploadPDF(file);
    
            toast.success("PDF Uploaded");
    
            await loadDocuments();
    
        }
    
        catch(err){
    
            toast.error("Upload Failed");
    
        }
    
        finally{
    
            setUploading(false);
    
        }
    
    }

    async function handleDelete(id){

        try{
    
            await deleteDocument(id);
    
            toast.success("Document Deleted");
    
            loadDocuments();
    
        }
    
        catch{
    
            toast.error("Delete Failed");
    
        }
    
    }

    useEffect(() => {

        loadDocuments();

    }, []);

    return (

        <aside className="w-72 bg-slate-900 text-white p-5 flex flex-col">

            <h2 className="text-xl font-bold mb-6">

                📚 Documents

            </h2>

            {
                uploading ?
            
                <button
                    disabled
                    className="w-full bg-gray-600 py-2 rounded-lg"
                >
                    Uploading...
                </button>
            
                :
            
                <UploadButton
                    onUpload={handleUpload}
                />
            }

            <div className="mt-6 flex-1 overflow-y-auto space-y-3">

                {
                    documents.length === 0 ?

                    <p>No documents uploaded.</p>

                    :

                    documents.map((doc)=>(

                        <DocumentCard

                         key={doc.document_id}

                          document={doc}

                           onDelete={handleDelete}

                        />

                    ))
                }

            </div>

        </aside>

    );

}