import { useEffect, useRef } from "react";
import MessageBubble from "./MessageBubble";

export default function ChatBox({ messages }) {

    const bottomRef = useRef(null);

    useEffect(() => {

        bottomRef.current?.scrollIntoView({
            behavior: "smooth"
        });

    }, [messages]);

    return (

        <div className="flex-1 overflow-y-auto space-y-5">

            {
                messages.map((msg, index) => (

                    <MessageBubble
                        key={index}
                        role={msg.role}
                        content={msg.content}
                        sources={msg.sources}
                    />

                ))
            }

            <div ref={bottomRef} />

        </div>

    );

}