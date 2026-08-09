import { useRef } from "react";

export default function UploadButton({ onUpload }) {

    const inputRef = useRef();

    return (
        <>
            <button
                onClick={() => inputRef.current.click()}
                className="w-full rounded-lg bg-blue-600 py-2 hover:bg-blue-700"
            >
                Upload PDF
            </button>

            <input
                ref={inputRef}
                type="file"
                accept=".pdf"
                hidden
                onChange={(e) => {

                    if (e.target.files.length > 0) {

                        onUpload(e.target.files[0]);

                    }

                }}
            />
        </>
    );
}