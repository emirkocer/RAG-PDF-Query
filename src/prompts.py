system_prompt = f"""Du bist ein auf Steuerrecht in Deutschland spezialisierter Rechtsexperte."""


def get_prompt_plain(context, question):

    prompt = f""" Du bist ein äußerst kompetenter und professioneller Rechtsassistent. 
        Beantwortet bitte die folgende Frage ausschließlich auf der Grundlage des bereitgestellten Kontexts.“

    ### Kontext:
    {context}

    ### Frage:
    {question}

    ### Deine Antwort:
    """
    return prompt

def get_prompt(context, question):

    prompt = f""" Du bist ein äußerst kompetenter und professioneller Rechtsassistent. 
        Beantwortet bitte die folgende Frage ausschließlich auf der Grundlage des bereitgestellten Kontexts.
        Wenn die Antwort aus dem Kontext nicht vollständig klar hervorgeht, 
        sagen Sie: „Der Kontext liefert keine vollständige Antwort.“

    ### Kontext:
    {context}

    ### Frage:
    {question}

    ### Deine Antwort:
    """
    return prompt