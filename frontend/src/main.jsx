import React from "react";
import ReactDOM from "react-dom/client";
import { Toaster } from "react-hot-toast";
import ChatProvider from "./context/ChatContext";

import "./styles/global.css";

import App from "./App";

ReactDOM.createRoot(
  document.getElementById("root")
).render(
  <React.StrictMode>
      <>
    

     <ChatProvider>
     <Toaster position="top-right" />
      <App />

     </ChatProvider>
     </>
  </React.StrictMode>
);