from langchain_core.output_parsers import StrOutputParser

from app.llm.langchain_llm import llm
from app.prompts.chat_prompt import chat_prompt

parser = StrOutputParser()

chain = chat_prompt | llm | parser


class ChatService:

    def ask(self, question: str):

        return chain.invoke(
            {
                "question": question
            }
        )