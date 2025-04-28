# Categorizes the user query into a specific intent using an LLM model.
def intent_categorizer(query, llm, model_name, instruction):

    full_query = f"\nUser: {query}"

    messages = [
        {"role": "system", "content": f"{instruction}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result

# Handles user queries related to healthcare.
def call_admin_healthcare():
    return print("Hello, I'm admin from ABC company who will answer questions about healthcare.")

# Handles user queries related to legal matters.
def call_admin_legal():
    return print("Hello, I'm admin of ABC company who will answer questions about legal.")

# Handles user queries related to education topics.
def call_admin_education():
    return print("Hello, I'm admin of ABC company who will answer questions about education.")

# Handles user queries that do not fit predefined intents.
def call_admin_others():
    return print("Hello, I'm admin of ABC company.")