import ReactMarkdown from "react-markdown";

export default function MessageBubble({

    role,

    content

}){

    const user = role==="user";

    return(

        <div
            className={`flex ${
                user
                ? "justify-end"
                : "justify-start"
            }`}
        >

            <div
                className={`max-w-3xl rounded-xl p-4 ${
                    user
                    ? "bg-blue-600 text-white"
                    : "bg-white border"
                }`}
            >

                <ReactMarkdown>

                    {content}

                </ReactMarkdown>

            </div>

        </div>

    );

}