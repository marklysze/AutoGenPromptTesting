# Phase 1 - add one shot example. to the last message, "Example output: Negative_Rebuttal_Debater"

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
        'role': 'system',
        'content': "You are in a role play game. The following roles are available:\nDebate_Moderator_Agent: Debate_Moderator_Agent is a critical thinker with strong analytical skills and expertise in Python. They should have the ability to identify inaccuracies or questionable statements within a group chat and offer clear, well-reasoned corrections or alternative viewpoints. This role requires excellent communication skills to articulate challenges and provide constructive feedback without disrupting the flow of the discussion.\nAffirmative_Constructive_Debater: An affirmative constructive debater (named 'Affirmative_Constructive_Debater') is a critical thinker and effective communicator who can challenge prior assertions within the group chat, offering clarifications, corrections, or alternative perspectives. This individual should possess strong analytical skills to evaluate information and the ability to articulate their reasoning clearly. When relevant to a discussion involving Python code, the debater should be capable of reading, understanding, and suggesting improvements to the code, even though coding is not their primary role.\nNegative_Constructive_Debater: The negative constructive debater (named 'Negative_Constructive_Debater') is a critical thinker skilled in analyzing the validity of arguments and information presented in the group chat, with the ability to provide constructive feedback and counterpoints to enhance discussions. This individual should possess a strong command of logic, effective communication skills to articulate their critiques clearly, and when necessary, proficiency in Python to troubleshoot and suggest improvements to code shared within the group. They should be allowed to speak when inconsistencies or errors are identified, to refine the group's understanding or to optimize code functionality.\nAffirmative_Rebuttal_Debater: The affirmative rebuttal debater (named 'Affirmative_Rebuttal_Debater') is a critical thinker skilled in analyzing statements, identifying inaccuracies or fallacies in arguments, and providing well-reasoned counterpoints or corrected information when necessary. This individual should be articulate, possess strong research skills to substantiate their rebuttals, and be adept at remaining respectful and constructive during discourse. If the debate involves the scrutiny of Python code, they should have a proficient understanding of Python to assess and address potential issues in code-related discussions effectively.\nNegative_Rebuttal_Debater: The negative rebuttal debater (named 'Negative_Rebuttal_Debater') is a critical thinker skilled in logic, reasoning, and effective communication who can articulate clear counterarguments to ensure accuracy and validity in group discussions. This individual should be proficient in Python for analyzing and correcting any flawed code shared within the chat. They should intervene when misinformation is presented, questionable claims arise, or when there is a need to clarify and rectify coding errors.\nDebate_Judge: Debate_Judge is an analytical and impartial individual adept at evaluating arguments, assessing evidence, and providing constructive feedback. They possess strong critical thinking skills and effective communication abilities to articulate their judgments clearly. The role may occasionally involve basic Python knowledge to verify and correct code within discussions when relevant to the debate..\n\nRead the following conversation.\nThen select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. Only return the role.",
    },
    {
        'role': 'user',
        'content': f"Please debate the proposition '{topic}'.", # The debate will start with Affirmative_Constructive_Debater.",
        'name': "Debate_Moderator_Agent"
    },
    {
        'role': 'system',
        'content': "Read the above conversation. Then select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. Only return the role.\n\nExample output: Negative_Rebuttal_Debater",
    },
]

# print(chat_messages)

models = ["llama2:13b-chat", "mistral:7b-instruct-q6_K", "neural-chat:7b-v3.3-q6_K", "openhermes:7b-mistral-v2.5-q6_K", "orca2:13b-q5_K_S", "phi:latest", "solar:10.7b-instruct-v1-q5_K_M", "qwen:14b-chat-q6_K"] # "yi:34b-chat-q3_K_M", "mixtralcopy", 

for modelName in models:

    correctCount = 0
    correctWithTidy = 0
    iterations = 10
    expectedResponse = "Affirmative_Constructive_Debater"
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