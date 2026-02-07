from search import search_prompt

def chat():
    while True:
        user_question = input("Faça sua pergunta (ou digite 'sair'): ")
        if user_question.lower() == 'sair':
            break
        
        print(f"PERGUNTA: {user_question}")

        answer = search_prompt(user_question)
        print(f"RESPOSTA: {answer}")

if __name__ == "__main__":
    chat()