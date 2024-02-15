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
        'content': "Read the above conversation. Then select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. Only return the role.",
    },
]

# print(chat_messages)

correctCount = 0
correctWithTidy = 0
iterations = 100
expectedResponse = "Affirmative_Constructive_Debater"
for i in range(iterations):
    
    chat_completion = client.chat.completions.create(
        messages=chat_messages,
        model='mixtralcopy',
    )

    responseText = chat_completion.choices[0].message.content
    responseText = responseText.strip()
    print(f"[{i}] Response: {responseText}\n")

    if responseText == expectedResponse:
        correctCount = correctCount + 1
        print("MATCHED!")
    else:
        tidyName = responseText.replace('\\_', '')
        tidyName = tidyName.replace(" ", "_")

        if tidyName == expectedResponse:
            correctWithTidy = correctWithTidy + 1

# print(chat_completion)
# print(f"Role: {chat_completion.choices[0].message.role}")
# print(f"Usage (prompt/completion/total tokens): {chat_completion.usage.prompt_tokens}/{chat_completion.usage.completion_tokens}/{chat_completion.usage.total_tokens}")

# match = chat_completion.choices[0].message.content == "Affirmative_Constructive_Debater"
# print(match)
print(f"Result is {correctCount} correct, {correctWithTidy} correct with tidy, out of {iterations} iterations")

'''
[0] Response: Affirmative Constructive Debater

[1] Response: Affirmative Constructive Debater

[2] Response: Affirmative\_Constructive\_Debater

[3] Response: Affirmative\_Constructive\_Debater

[4] Response: Affirmative Constructive Debater

[5] Response: Affirmative Constructive Debater

[6] Response: Affirmative Constructive Debater

[7] Response: Affirmative Constructive Debater

[8] Response: Affirmative Constructive Debater

[9] Response: Affirmative\_Constructive\_Debater

[10] Response: Affirmative\_Constructive\_Debater

[11] Response: Affirmative\_Constructive\_Debater

[12] Response: Affirmative\_Constructive\_Debater

[13] Response: Affirmative Constructive Debater

[14] Response: Affirmative Constructive Debater

[15] Response: Affirmative Constructive Debater

[16] Response: Affirmative Constructive Debater

[17] Response: Affirmative Constructive Debater

[18] Response: Affirmative\_Constructive\_Debater

[19] Response: Affirmative Constructive Debater

[20] Response: Affirmative Constructive Debater

[21] Response: Affirmative Constructive Debater

[22] Response: Affirmative Constructive Debater

[23] Response: Affirmative Constructive Debater

[24] Response: Affirmative Constructive Debater

[25] Response: Affirmative Constructive Debater

[26] Response: Affirmative Constructive Debater

[27] Response: Affirmative Constructive Debater

[28] Response: Affirmative\_Constructive\_Debater

[29] Response: Affirmative Constructive Debater

[30] Response: Affirmative Constructive Debater

[31] Response: Affirmative Constructive Debater

[32] Response: Affirmative\_Constructive\_Debater

[33] Response: Affirmative\_Constructive\_Debater

[34] Response: Affirmative Constructive Debater

[35] Response: Affirmative Constructive Debater

[36] Response: Affirmative Constructive Debater

[37] Response: Affirmative Constructive Debater

[38] Response: Affirmative Constructive Debater

[39] Response: Affirmative Constructive Debater

[40] Response: Affirmative Constructive Debater

[41] Response: Affirmative Constructive Debater

[42] Response: Affirmative Constructive Debater

[43] Response: Affirmative Constructive Debater

[44] Response: Affirmative Constructive Debater

[45] Response: Affirmative Constructive Debater

[46] Response: Affirmative\_Constructive\_Debater

[47] Response: Affirmative\_Constructive\_Debater

[48] Response: Affirmative\_Constructive\_Debater

[49] Response: Affirmative\_Constructive\_Debater

[50] Response: Affirmative Constructive Debater

[51] Response: Affirmative\_Constructive\_Debater

[52] Response: Affirmative Constructive Debater

[53] Response: Affirmative Constructive Debater

[54] Response: Affirmative\_Constructive\_Debater

[55] Response: Affirmative\_Constructive\_Debater

[56] Response: Affirmative\_Constructive\_Debater

[57] Response: Affirmative Constructive Debater

[58] Response: Affirmative\_Constructive\_Debater

[59] Response: Affirmative\_Constructive\_Debater

[60] Response: Affirmative\_Constructive\_Debater

[61] Response: Affirmative Constructive Debater

[62] Response: Affirmative\_Constructive\_Debater

[63] Response: Affirmative Constructive Debater

[64] Response: Affirmative Constructive Debater

[65] Response: Affirmative Constructive Debater

[66] Response: Affirmative Constructive Debater

[67] Response: Affirmative Constructive Debater

[68] Response: Affirmative Constructive Debater

[69] Response: Affirmative Constructive Debater

[70] Response: Affirmative\_Constructive\_Debater

[71] Response: Affirmative\_Constructive\_Debater

[72] Response: Affirmative\_Constructive\_Debater

[73] Response: Affirmative Constructive Debater

[74] Response: Affirmative Constructive Debater

[75] Response: Affirmative Constructive Debater

[76] Response: Affirmative Constructive Debater

[77] Response: Affirmative Constructive Debater

[78] Response: Affirmative\_Constructive\_Debater

[79] Response: Affirmative\_Constructive\_Debater

[80] Response: Affirmative\_Constructive\_Debater

[81] Response: Affirmative\_Constructive\_Debater

[82] Response: Affirmative Constructive Debater

[83] Response: Affirmative Constructive Debater

[84] Response: Affirmative Constructive Debater

[85] Response: Affirmative\_Constructive\_Debater

[86] Response: Affirmative\_Constructive\_Debater

[87] Response: Affirmative Constructive Debater

[88] Response: Affirmative\_Constructive\_Debater

[89] Response: Affirmative Constructive Debater

[90] Response: Affirmative Constructive Debater

[91] Response: Affirmative Constructive Debater

[92] Response: Affirmative Constructive Debater

[93] Response: Affirmative\_Constructive\_Debater

[94] Response: Affirmative Constructive Debater

[95] Response: Affirmative Constructive Debater

[96] Response: Affirmative Constructive Debater

[97] Response: Affirmative Constructive Debater

[98] Response: Affirmative Constructive Debater

[99] Response: Affirmative\_Constructive\_Debater

Result is 0 correct, 100 correct with tidy, out of 100 iterations
'''