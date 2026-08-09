import { useState } from "react";

export default function ChatInput({ onSend ,disabled }) {

    const [question, setQuestion] = useState("");

    function send() {

        if (!question.trim()) return;

        onSend(question);

        setQuestion("");

    }

    return (

        <div className="flex gap-3 border-t pt-4">
    
            <input
                value={question}
                onChange={(e)=>setQuestion(e.target.value)}
                disabled={disabled}
                onKeyDown={(e)=>{
    
                    if(e.key==="Enter"){
    
                        send();
    
                    }
    
                }}
                placeholder="Ask anything about your documents..."
                className="flex-1 rounded-xl border px-5 py-3 outline-none focus:ring-2 focus:ring-blue-500"
            />
    
            <button
                onClick={send}
                disabled={disabled}
                className="rounded-xl bg-blue-600 px-6 text-white hover:bg-blue-700"
            >
    
                {disabled ? "Thinking..." : "Send"}
    
            </button>
    
        </div>
    
    );

}