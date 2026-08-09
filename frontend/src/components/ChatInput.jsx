import { useState } from "react";

export default function ChatInput({ onSend }) {

    const [question, setQuestion] = useState("");

    function send() {

        if (!question.trim()) return;

        onSend(question);

        setQuestion("");

    }

    return (

        <div className="flex gap-2">

            <input
                value={question}
                onChange={(e)=>setQuestion(e.target.value)}
                onKeyDown={(e)=>{

                    if(e.key==="Enter"){

                        send();

                    }

                }}
                className="flex-1 border rounded-lg p-3"
                placeholder="Ask something..."
            />

            <button
                onClick={send}
                className="bg-blue-600 text-white px-6 rounded-lg"
            >
                Send
            </button>

        </div>

    );

}