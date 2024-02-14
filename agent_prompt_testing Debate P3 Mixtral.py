# Phase 3 - Trying various chat messages to get the right outcome

from openai import OpenAI
import os

# Clear the terminal (Unix/Linux/MacOS)
os.system('clear')

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='NotRequired', # required but ignored
)

chat_sequences = [] # The actual chat context
correct_agent_sequences = [] # Agent name that it should select

# Standard sequence content
# This is a shortened version of the original.
Step_1_Content = "This is a role play game. The following roles are available:\n#1 Debate_Moderator_Agent: Critical thinker, strong analytical skills, ability to identify inaccuracies or questionable statements within a group chat and offer clear, well-reasoned corrections or alternative viewpoints. Provides constructive feedback without disrupting the flow of the discussion.\n#2 Affirmative_Constructive_Debater: Critical thinker, effective communicator,  can challenge prior assertions, offers clarifications, corrections, or alternative perspectives. possess strong analytical skills to evaluate information and articulate their reasoning clearly. \n#3 Negative_Constructive_Debater: Critical thinker, skilled in analyzing the validity of arguments and information, ability to provide constructive feedback and counterpoints. Strong command of logic, effective communication skills to articulate their critiques clearly, should be allowed to speak when inconsistencies or errors are identified, to refine the group's understanding.\n#4 Affirmative_Rebuttal_Debater: Critical thinker skilled in analyzing statements, identifying inaccuracies or fallacies in arguments, and providing well-reasoned counterpoints or corrected information when necessary. They are articulate, possess strong research skills to substantiate their rebuttals, and be adept at remaining respectful and constructive during discourse.\n#5 Negative_Rebuttal_Debater: Critical thinker skilled in logic, reasoning, and effective communication who can articulate clear counterarguments to ensure accuracy and validity. They should intervene when misinformation is presented, questionable claims arise, or when there is a need to clarify and rectify coding errors.\n#6 Debate_Judge: Is an analytical and impartial individual adept at evaluating arguments, assessing evidence, and providing constructive feedback. They possess strong critical thinking skills and effective communication abilities to articulate their judgments clearly.\nRoles must be selected in this order:\n1. 'Debate_Moderator_Agent'\n2. 'Affirmative_Constructive_Debater'\n3. 'Negative_Constructive_Debater'\n4. 'Affirmative_Rebuttal_Debater'\n5. 'Negative_Rebuttal_Debater'\n6. 'Debate_Judge'.\n\nRead the following conversation.\nThen select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE ROLE. FOLLOW THE NUMBERED ORDER OF THE ROLES WHEN SELECTING THE ROLE.\n\nExample output: Affirmative_Constructive_Debater"

#1 - OUTPUT should be "Affirmative_Constructive_Debater"
# Notes:
# Adding to the moderator to start with the ACD role helped it choose that one.
# I could not get it to stop using "\_" instead of just "_", apparently it's a token in the model: https://www.reddit.com/r/LocalLLaMA/comments/1agrddy/has_anyone_encountered_mistrals_tendency_to_use/
# Consistently returns the correct result, just with the escaped underscore
correct_agent_sequences.append("Affirmative_Constructive_Debater")
chat_messages=[
    {
        'content': f"{Step_1_Content}", #"You are in a role play game. The following roles are available AND IN CORRECT ORDER:\nDebate_Moderator_Agent: #1 Debate_Moderator_Agent is a critical thinker with strong analytical skills and expertise in Python. They should have the ability to identify inaccuracies or questionable statements within a group chat and offer clear, well-reasoned corrections or alternative viewpoints. This role requires excellent communication skills to articulate challenges and provide constructive feedback without disrupting the flow of the discussion.\n#2 Affirmative_Constructive_Debater: An affirmative constructive debater is a critical thinker and effective communicator who can challenge prior assertions within the group chat, offering clarifications, corrections, or alternative perspectives. This individual should possess strong analytical skills to evaluate information and the ability to articulate their reasoning clearly. When relevant to a discussion involving Python code, the debater should be capable of reading, understanding, and suggesting improvements to the code, even though coding is not their primary role.\n#3 Negative_Constructive_Debater: The negative constructive debater is a critical thinker skilled in analyzing the validity of arguments and information presented in the group chat, with the ability to provide constructive feedback and counterpoints to enhance discussions. This individual should possess a strong command of logic, effective communication skills to articulate their critiques clearly, and when necessary, proficiency in Python to troubleshoot and suggest improvements to code shared within the group. They should be allowed to speak when inconsistencies or errors are identified, to refine the group's understanding or to optimize code functionality.\n#4 Affirmative_Rebuttal_Debater: The affirmative rebuttal debater is a critical thinker skilled in analyzing statements, identifying inaccuracies or fallacies in arguments, and providing well-reasoned counterpoints or corrected information when necessary. This individual should be articulate, possess strong research skills to substantiate their rebuttals, and be adept at remaining respectful and constructive during discourse. If the debate involves the scrutiny of Python code, they should have a proficient understanding of Python to assess and address potential issues in code-related discussions effectively.\n#5 Negative_Rebuttal_Debater: The negative rebuttal debater is a critical thinker skilled in logic, reasoning, and effective communication who can articulate clear counterarguments to ensure accuracy and validity in group discussions. This individual should be proficient in Python for analyzing and correcting any flawed code shared within the chat. They should intervene when misinformation is presented, questionable claims arise, or when there is a need to clarify and rectify coding errors.\n#6 Debate_Judge: Debate_Judge is an analytical and impartial individual adept at evaluating arguments, assessing evidence, and providing constructive feedback. They possess strong critical thinking skills and effective communication abilities to articulate their judgments clearly. The role may occasionally involve basic Python knowledge to verify and correct code within discussions when relevant to the debate. The correct role order is 1. 'Debate_Moderator_Agent'\n2. 'Affirmative_Constructive_Debater'\n3. 'Negative_Constructive_Debater'\n4. 'Affirmative_Rebuttal_Debater'\n5. 'Negative_Rebuttal_Debater'\n6. 'Debate_Judge'.\n\nRead the following conversation.\nThen select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE ROLE. FOLLOW THE NUMBERED ORDER OF THE ROLES WHEN SELECTING THE ROLE.\n\nExample output: Affirmative_Constructive_Debater",
        'role': 'system'
    },
    {
        'content': "Please debate the proposition 'People are wrong, the earth is flat.'. Start with the first debater.",
        'role': 'user',
        'name': 'Debate_Moderator_Agent'
    },
    {
        'role': 'system',
#        'content': "Read the above conversation. Then select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE ROLE."
        'content': "Read the above conversation and select the next role, the list of roles is ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge']. What is the next role to speak, answer concisely please?"
    }
]

chat_sequences.append(chat_messages)

#2 - OUTPUT should be "Negative_Constructive_Debater"
# Carried forward the content from the first sequence
# Mixtral started to output the correct name without the escaped underscores, maybe the longer context worked.
# Correctly identified the next in sequence
correct_agent_sequences.append("Negative_Constructive_Debater")
chat_messages = [
    {
        'content': f"{Step_1_Content}", #"You are in a role play game. The following roles are available AND IN CORRECT ORDER:\nDebate_Moderator_Agent: #1 Debate_Moderator_Agent is a critical thinker with strong analytical skills and expertise in Python. They should have the ability to identify inaccuracies or questionable statements within a group chat and offer clear, well-reasoned corrections or alternative viewpoints. This role requires excellent communication skills to articulate challenges and provide constructive feedback without disrupting the flow of the discussion.\n#2 Affirmative_Constructive_Debater: An affirmative constructive debater is a critical thinker and effective communicator who can challenge prior assertions within the group chat, offering clarifications, corrections, or alternative perspectives. This individual should possess strong analytical skills to evaluate information and the ability to articulate their reasoning clearly. When relevant to a discussion involving Python code, the debater should be capable of reading, understanding, and suggesting improvements to the code, even though coding is not their primary role.\n#3 Negative_Constructive_Debater: The negative constructive debater is a critical thinker skilled in analyzing the validity of arguments and information presented in the group chat, with the ability to provide constructive feedback and counterpoints to enhance discussions. This individual should possess a strong command of logic, effective communication skills to articulate their critiques clearly, and when necessary, proficiency in Python to troubleshoot and suggest improvements to code shared within the group. They should be allowed to speak when inconsistencies or errors are identified, to refine the group's understanding or to optimize code functionality.\n#4 Affirmative_Rebuttal_Debater: The affirmative rebuttal debater is a critical thinker skilled in analyzing statements, identifying inaccuracies or fallacies in arguments, and providing well-reasoned counterpoints or corrected information when necessary. This individual should be articulate, possess strong research skills to substantiate their rebuttals, and be adept at remaining respectful and constructive during discourse. If the debate involves the scrutiny of Python code, they should have a proficient understanding of Python to assess and address potential issues in code-related discussions effectively.\n#5 Negative_Rebuttal_Debater: The negative rebuttal debater is a critical thinker skilled in logic, reasoning, and effective communication who can articulate clear counterarguments to ensure accuracy and validity in group discussions. This individual should be proficient in Python for analyzing and correcting any flawed code shared within the chat. They should intervene when misinformation is presented, questionable claims arise, or when there is a need to clarify and rectify coding errors.\n#6 Debate_Judge: Debate_Judge is an analytical and impartial individual adept at evaluating arguments, assessing evidence, and providing constructive feedback. They possess strong critical thinking skills and effective communication abilities to articulate their judgments clearly. The role may occasionally involve basic Python knowledge to verify and correct code within discussions when relevant to the debate. The correct role order is 1. 'Debate_Moderator_Agent'\n2. 'Affirmative_Constructive_Debater'\n3. 'Negative_Constructive_Debater'\n4. 'Affirmative_Rebuttal_Debater'\n5. 'Negative_Rebuttal_Debater'\n6. 'Debate_Judge'.\n\nRead the following conversation.\nThen select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE ROLE. FOLLOW THE NUMBERED ORDER OF THE ROLES WHEN SELECTING THE ROLE.\n\nExample output: Affirmative_Constructive_Debater",
        'role': 'system'
    },
    {
        'content': "Please debate the proposition 'People are wrong, the earth is flat.'. Start with the first debater.",
        'role': 'user',
        'name': 'Debate_Moderator_Agent'
    },
    {
        "content": "As Affirmative_Constructive_Debater, I will argue in favor of the proposition that people are wrong and the Earth is not flat. I will present a solid case supported by compelling evidence and reasoning to substantiate the affirmative side. My role is to create a robust foundation for my team's argument that the opposing team must address.\n\nFirst, let us establish that the Earth is, in fact, an oblate spheroid – a sphere that is slightly squashed at its poles and slightly swollen at the equator. This has been proven by various means, including:\n\n1. Traveller's observations and measurements: Historically, explorers such as Ferdinand Magellan and James Cook circumnavigated the Earth, observing that the route eventually returned them to their starting point. Additionally, Eratosthenes measured the Earth's circumference around 240 BCE using simple geometry and shadows cast by vertical sticks at two different locations on Earth.\n\n2. Satellite imagery: High-resolution satellite images from space clearly show the Earth as a sphere. For example, NASA's Earth Polychromatic Imaging Camera (EPIC) provides daily full-disk images of the Earth, which unambiguously display it as a sphere.\n\n3. Gravity measurements: Measurements of variations in gravity around the Earth reveal an oblate spheroid shape. The Gravity Recovery and Climate Experiment (GRACE) satellites, for instance, measured changes in Earth's gravity field that correspond to this shape.\n\nIn anticipation of potential counterarguments, I would like to address two common misconceptions about a flat Earth:\n\n1. The horizon illusion: While it is true that the horizon appears flat when observing at a small scale (such as from the beach), this does not prove that the Earth is flat. As previously mentioned, the Earth is an oblate spheroid; thus, its curvature is only noticeable over large distances.\n\n2. The Bedford Level Experiment: This 19th-century experiment claimed to demonstrate a flat Earth by observing a distant object's visibility along a six-mile canal. However, this experiment has been widely discredited due to various errors in its methodology and misinterpretations of the results.\n\nIn conclusion, based on historical observations, satellite imagery, gravity measurements, and refutation of common misconceptions, we can confidently assert that people are wrong, and the Earth is not flat but rather an oblate spheroid.",
        "role": "user",
        "name": "Affirmative_Constructive_Debater",
    },
    {
        'role': 'system',
#        'content': "Read the above conversation. Then select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE ROLE."
        'content': "Read the above conversation and select the next role, the list of roles is ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge']. What is the next role to speak, answer concisely please?"
    },
]
chat_sequences.append(chat_messages)

#3 - OUTPUT should be "Affirmative_Rebuttal_Debater"
# Carried forward the content from the first and second sequences
# The length of the whole sequence resulting in a mix of different results, not just agent names but debating as well. Reducing the first message content made a significant difference in that it start to just return the agent names (rather than trying to debate), though they weren't correct until we asked them to explain why
# Asking it to return the name of the next role AND WHY resulted in it choosing the right role but with the reasoning added. So changing "RETURN ONLY THE NAME OF THE NEXT ROLE." to "RETURN ONLY THE NAME OF THE NEXT ROLE AND REASON WHY." resulted in it returning the correct result (just with the extra text). Had to have "REASON WHY" and not just "WHY" to get a consistent output. Changing this in the previous sequences does not work - argh.
# Q4 and Q5 versions of Mixtral were producing the same result.
# Interestingly, if I ran the first three sequences in a row with the same LLM model this third sequence would return the wrong agent role. However, if I ran the first two with an LLM model and then changed the third one it would return the correct result. Caching issue?!?
correct_agent_sequences.append("Affirmative_Rebuttal_Debater")
chat_messages = [
    # MS Reducing content to see if context length is an issue.
    {
        'content': f"{Step_1_Content}", #"This is a role play game. The following roles are available:\n#1 Debate_Moderator_Agent: Critical thinker, strong analytical skills, ability to identify inaccuracies or questionable statements within a group chat and offer clear, well-reasoned corrections or alternative viewpoints. Provides constructive feedback without disrupting the flow of the discussion.\n#2 Affirmative_Constructive_Debater: Critical thinker, effective communicator,  can challenge prior assertions, offers clarifications, corrections, or alternative perspectives. possess strong analytical skills to evaluate information and articulate their reasoning clearly. \n#3 Negative_Constructive_Debater: Critical thinker, skilled in analyzing the validity of arguments and information, ability to provide constructive feedback and counterpoints. Strong command of logic, effective communication skills to articulate their critiques clearly, should be allowed to speak when inconsistencies or errors are identified, to refine the group's understanding.\n#4 Affirmative_Rebuttal_Debater: Critical thinker skilled in analyzing statements, identifying inaccuracies or fallacies in arguments, and providing well-reasoned counterpoints or corrected information when necessary. They are articulate, possess strong research skills to substantiate their rebuttals, and be adept at remaining respectful and constructive during discourse.\n#5 Negative_Rebuttal_Debater: Critical thinker skilled in logic, reasoning, and effective communication who can articulate clear counterarguments to ensure accuracy and validity. They should intervene when misinformation is presented, questionable claims arise, or when there is a need to clarify and rectify coding errors.\n#6 Debate_Judge: Is an analytical and impartial individual adept at evaluating arguments, assessing evidence, and providing constructive feedback. They possess strong critical thinking skills and effective communication abilities to articulate their judgments clearly.\nRoles must be selected in this order:\n1. 'Debate_Moderator_Agent'\n2. 'Affirmative_Constructive_Debater'\n3. 'Negative_Constructive_Debater'\n4. 'Affirmative_Rebuttal_Debater'\n5. 'Negative_Rebuttal_Debater'\n6. 'Debate_Judge'.\n\nRead the following conversation.\nThen select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE ROLE. FOLLOW THE NUMBERED ORDER OF THE ROLES WHEN SELECTING THE ROLE.\n\nExample output: Affirmative_Constructive_Debater",
        'role': 'system'
    },
    {
        'content': "Please debate the proposition 'People are wrong, the earth is flat.'. Start with the first debater.",
        'role': 'user',
        'name': 'Debate_Moderator_Agent'
    },
    {
        "content": "As Affirmative_Constructive_Debater, I will argue in favor of the proposition that people are wrong and the Earth is not flat. I will present a solid case supported by compelling evidence and reasoning to substantiate the affirmative side. My role is to create a robust foundation for my team's argument that the opposing team must address.\n\nFirst, let us establish that the Earth is, in fact, an oblate spheroid – a sphere that is slightly squashed at its poles and slightly swollen at the equator. This has been proven by various means, including:\n\n1. Traveller's observations and measurements: Historically, explorers such as Ferdinand Magellan and James Cook circumnavigated the Earth, observing that the route eventually returned them to their starting point. Additionally, Eratosthenes measured the Earth's circumference around 240 BCE using simple geometry and shadows cast by vertical sticks at two different locations on Earth.\n\n2. Satellite imagery: High-resolution satellite images from space clearly show the Earth as a sphere. For example, NASA's Earth Polychromatic Imaging Camera (EPIC) provides daily full-disk images of the Earth, which unambiguously display it as a sphere.\n\n3. Gravity measurements: Measurements of variations in gravity around the Earth reveal an oblate spheroid shape. The Gravity Recovery and Climate Experiment (GRACE) satellites, for instance, measured changes in Earth's gravity field that correspond to this shape.\n\nIn anticipation of potential counterarguments, I would like to address two common misconceptions about a flat Earth:\n\n1. The horizon illusion: While it is true that the horizon appears flat when observing at a small scale (such as from the beach), this does not prove that the Earth is flat. As previously mentioned, the Earth is an oblate spheroid; thus, its curvature is only noticeable over large distances.\n\n2. The Bedford Level Experiment: This 19th-century experiment claimed to demonstrate a flat Earth by observing a distant object's visibility along a six-mile canal. However, this experiment has been widely discredited due to various errors in its methodology and misinterpretations of the results.\n\nIn conclusion, based on historical observations, satellite imagery, gravity measurements, and refutation of common misconceptions, we can confidently assert that people are wrong, and the Earth is not flat but rather an oblate spheroid.",
        "role": "user",
        "name": "Affirmative_Constructive_Debater",
    },
    {
        "content": "Thank you for the opportunity to present my counterarguments, as Negative_Constructive_Debater. I appreciate the well-structured and evidence-based case presented by Affirmative_Constructive_Debater. However, I would like to point out a few considerations that may weaken some of their claims.\n\nFirstly, regarding traveler's observations and measurements, while it is true that early explorers have circumnavigated the Earth and observed its roundness, these voyages were primarily along the equator or near it. The Earth's equatorial bulge could have potentially gone unnoticed during their journeys. Moreover, Eratosthenes' measurement, although ingenious for its time, has a margin of error due to assumptions and simplifications in his calculations. Modern technology allows us to measure the Earth's shape with much greater precision.\n\nSecondly, satellite imagery does indeed show our planet as a sphere; however, these images can be misleading. It is important to recognize that satellite cameras often utilize wide-angle lenses and specific projection techniques that may unintentionally distort or curve straight lines, such as the horizon. While I do not dispute that the Earth appears spherical from space, it is worth considering whether these images accurately depict the Earth's true shape.\n\nThirdly, gravity measurements supporting an oblate spheroid Earth are subject to interpretation. Gravity varies across the surface of Earth due to factors such as mass distribution and rotation. Although GRACE satellites have measured gravity anomalies consistent with an oblate spheroid, alternative explanations could be invoked to account for these variations without assuming a specific shape for the Earth. For example, density variations within the Earth's mantle could also produce similar patterns in gravity measurements.\n\nLastly, I would like to address the dismissal of the Bedford Level Experiment as flawed and discredited. While it is true that this experiment has limitations and was conducted over a relatively short distance compared to Earth's total circumference, its results are still worth considering. The fact that objects were visible beyond what should have been possible on a flat Earth suggests alternative explanations for the horizon illusion, such as atmospheric refraction or mirages.\n\nIn summary, I would like to reiterate that my intention is not to claim the Earth is flat but rather to challenge some of the assumptions and potential weaknesses in Affirmative_Constructive_Debater's arguments. Further discussion and evidence are necessary to reach a conclusive understanding of our planet's true shape.",
        "role": "user",
        "name": "Negative_Constructive_Debater",
    },
    {
        'role': 'system',
#        'content': "Read the above conversation. Then select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE NEXT ROLE AND REASON WHY. DO NOT DEBATE."
        'content': "Read the above conversation and select the next role, the list of roles is ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge']. What is the next role to speak, answer concisely please?"
    },
]
chat_sequences.append(chat_messages)


# print(chat_messages)

models = ["mixtralq4"] # ["yi:34b-chat-q3_K_M", "mixtralcopy", "llama2:13b-chat", "mistral:7b-instruct-q6_K", "neural-chat:7b-v3.3-q6_K", "openhermes:7b-mistral-v2.5-q6_K", "orca2:13b-q5_K_S", "phi:latest", "solar:10.7b-instruct-v1-q5_K_M", "qwen:14b-chat-q6_K"]

for modelName in models:

    print(f"MODEL: {modelName}\n\n")

    for index, chat_sequence in enumerate(chat_sequences):

        if index < 0:
            continue # Skip first and second chat_sequences
        # elif index == 2:
            # modelName = "mixtralq4"

        correct_agent = correct_agent_sequences[index]
        print(f"Chat Sequence #{index+1}, Expecting '{correct_agent}'")
        # print(f"Chat Messages:\n{chat_sequence}\n")
        
        correctCount = 0
        correctWithTidy = 0
        existsWithin = 0
        iterations = 10

        # Loop through and run the chat sequence, checking for the correct agent name
        for i in range(iterations):
            
            seqlength = len(str(chat_sequence))

            chat_completion = client.chat.completions.create(
                messages=chat_sequence,
                model=modelName,
                temperature=0
            )

            responseText = chat_completion.choices[0].message.content
            responseText = responseText.strip()
            print(f"[{i}] Response: {responseText}")

            if responseText == correct_agent:
                correctCount = correctCount + 1
                print("MATCHED!")
            else:

                tidyName = responseText.replace('\\_', '_')
                tidyName = tidyName.replace(" ", "_")

                if tidyName == correct_agent:
                    correctWithTidy = correctWithTidy + 1
                else:
                    if correct_agent in responseText or correct_agent in tidyName:
                        existsWithin = existsWithin + 1


        print(f"Model/Sequence - Correct/Correct with Tidy/Exists Within/Iterations | {modelName}/{index+1} - {correctCount}/{correctWithTidy}/{existsWithin}/{iterations}")

        # break