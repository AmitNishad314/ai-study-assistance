import { createContext } from "react";
import useLocalStorage from "../hooks/useLocalStorage";

export const ChatContext = createContext();

export default function ChatProvider({ children }) {

    const [messages, setMessages] = useLocalStorage(
        "chat-history",
        []
    );

    return (

        <ChatContext.Provider
            value={{
                messages,
                setMessages
            }}
        >

            {children}

        </ChatContext.Provider>

    );

}