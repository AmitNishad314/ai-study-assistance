import { useState } from "react";

import ChatBox from "../components/ChatBox";
import ChatInput from "../components/ChatInput";
import { streamText } from "../utils/streamText";

import { askQuestion } from "../services/api";
import { useContext } from "react";
import { ChatContext } from "../context/ChatContext";



export default function ChatPage(){

    const {

        messages,
    
        setMessages
    
    } = useContext(ChatContext);
    const [loading,setLoading] = useState(false);

    async function handleSend(question){

        const userMessage={
            role:"user",
            content:question
        };

        setMessages(prev=>[

            ...prev,

            userMessage

        ]);

        try{
            setLoading(true);
            const response = await askQuestion(question);

            console.log("Response:", response);
            console.log("Answer:", response.answer);
            console.log("Sources:", response.sources);
            console.log("Answer type:", typeof response.answer);

            // Empty assistant message
            setMessages(prev => [
            
                ...prev,
            
                {
                    role: "assistant",
                    content: "",
                    sources: response.sources
                }
            
            ]);
            
            // await streamText(
            
            //     response.answer,
            
            //     (partialText) => {
            
            //         setMessages(prev => {
            
            //             const updated = [...prev];
            
            //             updated[updated.length - 1] = {
            
            //                 ...updated[updated.length - 1],
            
            //                 content: partialText
            
            //             };
            
            //             return updated;
            
            //         });
            
            //     }
            
            // );
            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content: response.answer,
                    sources: response.sources
                }
            ]);
            setLoading(false);

        }

        catch{

            setMessages(prev=>[

                ...prev,

                {
                    role:"assistant",
                    content:"Something went wrong."
                }

            ]);

        }

    }

    return (

        <div className="flex flex-col h-full">
    
            <div className="flex-1 overflow-hidden">
    
                <ChatBox
                    messages={messages}
                />
    
            </div>
    
            {
    
                loading &&
    
                <div className="text-gray-500 py-2">
    
                    🤖 AI is thinking...
    
                </div>
    
            }
    
            <ChatInput
                onSend={handleSend}
                disabled={loading}
            />
    
        </div>
    
    );

}