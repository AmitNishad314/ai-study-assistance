import { useState } from "react";

import ChatBox from "../components/ChatBox";
import ChatInput from "../components/ChatInput";

import { askQuestion } from "../services/api";

export default function ChatPage(){

    const [messages,setMessages]=useState([]);

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

            const response=await askQuestion(question);

            setMessages(prev=>[

                ...prev,

                {
                    role:"assistant",
                    content:response.answer
                }

            ]);

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

    return(

        <div className="flex flex-col h-full gap-4">

            <ChatBox
                messages={messages}
            />

            <ChatInput
                onSend={handleSend}
            />

        </div>

    );

}