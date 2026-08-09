import MessageBubble from "./MessageBubble";

export default function ChatBox({

    messages

}){

    return(

        <div
            className="flex-1 overflow-y-auto space-y-4"
        >

            {
                messages.map((msg,index)=>(

                    <MessageBubble

                        key={index}

                        role={msg.role}

                        content={msg.content}

                    />

                ))
            }

        </div>

    );

}