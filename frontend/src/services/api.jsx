import axios from "axios";

const api = axios.create({

    baseURL: "http://127.0.0.1:8000",

});

export async function uploadPDF(file){

    const formData = new FormData();

    formData.append("file",file);

    const response = await api.post(

        "/upload",

        formData

    );

    return response.data;

}

export async function getDocuments(){

    const response = await api.get(

        "/documents"

    );

    return response.data;

}

export async function deleteDocument(documentId){

    const response = await api.delete(
        `/documents/${documentId}`
    );

    return response.data;

}
export async function askQuestion(question){

    const response = await api.post(
        "/chat",
        {
            question
        }
    );

    return response.data;

}

export default api;