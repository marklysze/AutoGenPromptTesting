# Phase 2 - keeping temp=0, output should be Negative_Constructive_Debater

from openai import OpenAI
import os

# Clear the terminal (Unix/Linux/MacOS)
os.system('clear')

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='NotRequired', # required but ignored
)

topic = "The earth is round."

chat_messages=[
    {
        "content": "You are in a role play game. The following roles are available:\nDebate_Moderator_Agent: Debate_Moderator_Agent is a critical thinker with strong analytical skills and expertise in Python. They should have the ability to identify inaccuracies or questionable statements within a group chat and offer clear, well-reasoned corrections or alternative viewpoints. This role requires excellent communication skills to articulate challenges and provide constructive feedback without disrupting the flow of the discussion.\nAffirmative_Constructive_Debater: An affirmative constructive debater (named 'Affirmative_Constructive_Debater') is a critical thinker and effective communicator who can challenge prior assertions within the group chat, offering clarifications, corrections, or alternative perspectives. This individual should possess strong analytical skills to evaluate information and the ability to articulate their reasoning clearly. When relevant to a discussion involving Python code, the debater should be capable of reading, understanding, and suggesting improvements to the code, even though coding is not their primary role.\nNegative_Constructive_Debater: The negative constructive debater (named 'Negative_Constructive_Debater') is a critical thinker skilled in analyzing the validity of arguments and information presented in the group chat, with the ability to provide constructive feedback and counterpoints to enhance discussions. This individual should possess a strong command of logic, effective communication skills to articulate their critiques clearly, and when necessary, proficiency in Python to troubleshoot and suggest improvements to code shared within the group. They should be allowed to speak when inconsistencies or errors are identified, to refine the group's understanding or to optimize code functionality.\nAffirmative_Rebuttal_Debater: The affirmative rebuttal debater (named 'Affirmative_Rebuttal_Debater') is a critical thinker skilled in analyzing statements, identifying inaccuracies or fallacies in arguments, and providing well-reasoned counterpoints or corrected information when necessary. This individual should be articulate, possess strong research skills to substantiate their rebuttals, and be adept at remaining respectful and constructive during discourse. If the debate involves the scrutiny of Python code, they should have a proficient understanding of Python to assess and address potential issues in code-related discussions effectively.\nNegative_Rebuttal_Debater: The negative rebuttal debater (named 'Negative_Rebuttal_Debater') is a critical thinker skilled in logic, reasoning, and effective communication who can articulate clear counterarguments to ensure accuracy and validity in group discussions. This individual should be proficient in Python for analyzing and correcting any flawed code shared within the chat. They should intervene when misinformation is presented, questionable claims arise, or when there is a need to clarify and rectify coding errors.\nDebate_Judge: Debate_Judge is an analytical and impartial individual adept at evaluating arguments, assessing evidence, and providing constructive feedback. They possess strong critical thinking skills and effective communication abilities to articulate their judgments clearly. The role may occasionally involve basic Python knowledge to verify and correct code within discussions when relevant to the debate..\n\nRead the following conversation.\nThen select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. Only return the role.",
        "role": "system"
    },
    {
        "content": "Please debate the proposition 'Cows are better than Pigs.'.",
        "role": "user",
        "name": "Debate_Moderator_Agent"
    },
    {
        "content": " Affirmative_Constructive_Debater: Thank you for presenting this interesting topic for debate. Let's discuss why we believe cows are better than pigs based on several key factors:\n\n1) Environmental impact: Cows have a more positive environmental footprint compared to pigs due to their feeding habits and waste management. Cows primarily eat grass, which not only helps reduce greenhouse gas emissions but also plays an essential role in maintaining healthy ecosystems. In contrast, pigs require large quantities of grain, which contributes significantly to deforestation when grown for animal feed production. Furthermore, cows' manure can be used as fertilizer and is often spread on fields to promote plant growth, while pig waste must be carefully managed in confined animal feeding operations (CAFOs) to prevent pollution.\n\n2) Ethical considerations: Cows are generally treated better than pigs when it comes to living conditions and welfare. While there are still instances of poor treatment, intensive farming practices for cows are less common compared to the industrialized pig production system, which often confines animals in cramped and unsanitary conditions with little to no natural behaviors or enrichment opportunities.\n\n3) Nutritional benefits: Milk from cows is a significant source of essential nutrients for humans, including calcium, vitamin D, protein, and other micronutrients that contribute to a healthy diet. Additionally, the by-products of cow milk production, such as cheese, yogurt, and butter, provide various health benefits and culinary applications. While pigs can also be sources of important nutrients like iron and B vitamins, their meat consumption is primarily driven by cultural preferences and not essential for human survival.\n\n4) Economic advantages: Dairy farming offers economic opportunities beyond the sale of milk, such as the production of cheese, yogurt, and butter, which can create jobs in rural areas and contribute to local economies. Furthermore, cows have a longer lifespan than pigs and are more adaptable to various environments, making them a more viable agricultural investment for farmers.\n\n5) Cultural significance: Cows hold cultural importance across the world. In India, they are considered sacred animals and play an essential role in religious practices. In Western cultures, cows provide milk and other dairy products that are staples in the diet and contribute to various culinary traditions. Pigs, on the other hand, have often been associated with negative stereotypes due to their role in spreading diseases like trichinosis and their use as a symbol of greed or wastefulness.\n\nIn conclusion, we argue that cows are better than pigs for several reasons, including environmental impact, ethical considerations, nutritional benefits, economic advantages, and cultural significance. We encourage the negative team to present their case, and we will be open to discussing any counterarguments they may have. Thank you.",
        "role": "user",
        "name": "Affirmative_Constructive_Debater"
    },
    {
        "role": "system",
        "content": "Read the above conversation. Then select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. Only return the role."
    }
]

# print(chat_messages)

models = ["yi:34b-chat-q3_K_M", "mixtralcopy"]#, "llama2:13b-chat", "mistral:7b-instruct-q6_K", "neural-chat:7b-v3.3-q6_K", "openhermes:7b-mistral-v2.5-q6_K", "orca2:13b-q5_K_S", "phi:latest", "solar:10.7b-instruct-v1-q5_K_M", "qwen:14b-chat-q6_K"]

for modelName in models:

    correctCount = 0
    correctWithTidy = 0
    iterations = 10
    expectedResponse = "Negative_Constructive_Debater"
    for i in range(iterations):
        
        chat_completion = client.chat.completions.create(
            messages=chat_messages,
            model=modelName,
            temperature=0
        )

        responseText = chat_completion.choices[0].message.content
        responseText = responseText.strip()
        print(f"[{i}] Response: {responseText}")

        if responseText == expectedResponse:
            correctCount = correctCount + 1
            print("MATCHED!")
        else:
            tidyName = responseText.replace('\\_', '')
            tidyName = tidyName.replace(" ", "_")

            if tidyName == expectedResponse:
                correctWithTidy = correctWithTidy + 1

    print(f"Model/Correct/Correct with Tidy/Iterations | {modelName}/{correctCount}/{correctWithTidy}/{iterations}")