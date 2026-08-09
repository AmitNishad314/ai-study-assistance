import ReactMarkdown from "react-markdown";

export default function MessageBubble({

    role,

    content,

    sources=[]

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
                className={`max-w-3xl w-fit rounded-xl p-4 ${
                    user
                    ? "bg-blue-600 text-white"
                    : "bg-white border border-gray-200 shadow-md"
                }`}
            >

                <ReactMarkdown>

                    {content}

                </ReactMarkdown>

                {

                    !user &&

                    sources.length>0 &&(

                        <>

                            <hr className="my-4"/>

                            <h4 className="font-semibold text-sm">

                                Sources

                            </h4>

                            <div className="mt-2 space-y-2">

                                {

                                    sources.map((source,index)=>(

                                        <div
                                            key={index}
                                            className="text-sm text-gray-600 bg-gray-100 rounded p-2"
                                        >

                                            📄 {source.filename}

                                            {" "}

                                            Page {source.page}

                                        </div>

                                    ))

                                }

                            </div>

                        </>

                    )

                }

            </div>

        </div>

    );

}