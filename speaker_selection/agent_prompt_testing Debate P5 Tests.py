# Phase 5 - Tweaking Model parameters (temperature and top_p)

from openai import OpenAI
import logging
import os
from datetime import datetime
from termcolor import colored

# Get the current date and time
current_datetime = datetime.now()
logFilename = "testruns/" + current_datetime.strftime("%y-%m-%d-%H-%M-%S") + "-P4Test.log"
logging.basicConfig(filename=logFilename, level=logging.INFO)

# Disable INFO level messages from the 'httpx' module
logging.getLogger('httpx').setLevel(logging.WARNING)

# Clear the terminal (Unix/Linux/MacOS)
os.system('clear')

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='NotRequired', # required but ignored
)

chat_sequences = [] # Each chat sequence from the first select speaker to the last
correct_agent_sequences = [] # Agent name that we're expecting back at each point in the sequence

# The introduction message step that should outline the agents and order
Step_1_Samples = []

# 0: Original
Step_1_Samples.append("You are in a role play game. The following roles are available:\n#1 Debate_Moderator_Agent: Critical thinker, strong analytical skills, ability to identify inaccuracies or questionable statements within a group chat and offer clear, well-reasoned corrections or alternative viewpoints. Provides constructive feedback without disrupting the flow of the discussion.\n#2 Affirmative_Constructive_Debater: Critical thinker, effective communicator,  can challenge prior assertions, offers clarifications, corrections, or alternative perspectives. possess strong analytical skills to evaluate information and articulate their reasoning clearly. \n#3 Negative_Constructive_Debater: Critical thinker, skilled in analyzing the validity of arguments and information, ability to provide constructive feedback and counterpoints. Strong command of logic, effective communication skills to articulate their critiques clearly, should be allowed to speak when inconsistencies or errors are identified, to refine the group's understanding.\n#4 Affirmative_Rebuttal_Debater: Critical thinker skilled in analyzing statements, identifying inaccuracies or fallacies in arguments, and providing well-reasoned counterpoints or corrected information when necessary. They are articulate, possess strong research skills to substantiate their rebuttals, and be adept at remaining respectful and constructive during discourse.\n#5 Negative_Rebuttal_Debater: Critical thinker skilled in logic, reasoning, and effective communication who can articulate clear counterarguments to ensure accuracy and validity. They should intervene when misinformation is presented, questionable claims arise, or when there is a need to clarify and rectify coding errors.\n#6 Debate_Judge: Is an analytical and impartial individual adept at evaluating arguments, assessing evidence, and providing constructive feedback. They possess strong critical thinking skills and effective communication abilities to articulate their judgments clearly.\nRoles must be selected in this order:\n1. 'Debate_Moderator_Agent'\n2. 'Affirmative_Constructive_Debater'\n3. 'Negative_Constructive_Debater'\n4. 'Affirmative_Rebuttal_Debater'\n5. 'Negative_Rebuttal_Debater'\n6. 'Debate_Judge'.\n\nRead the following conversation.\nThen select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. Only return the role.")

# 1: Emphasising following of an order
Step_1_Samples.append("This is a role play game. The following roles are available:\n#1 Debate_Moderator_Agent: Critical thinker, strong analytical skills, ability to identify inaccuracies or questionable statements within a group chat and offer clear, well-reasoned corrections or alternative viewpoints. Provides constructive feedback without disrupting the flow of the discussion.\n#2 Affirmative_Constructive_Debater: Critical thinker, effective communicator,  can challenge prior assertions, offers clarifications, corrections, or alternative perspectives. possess strong analytical skills to evaluate information and articulate their reasoning clearly. \n#3 Negative_Constructive_Debater: Critical thinker, skilled in analyzing the validity of arguments and information, ability to provide constructive feedback and counterpoints. Strong command of logic, effective communication skills to articulate their critiques clearly, should be allowed to speak when inconsistencies or errors are identified, to refine the group's understanding.\n#4 Affirmative_Rebuttal_Debater: Critical thinker skilled in analyzing statements, identifying inaccuracies or fallacies in arguments, and providing well-reasoned counterpoints or corrected information when necessary. They are articulate, possess strong research skills to substantiate their rebuttals, and be adept at remaining respectful and constructive during discourse.\n#5 Negative_Rebuttal_Debater: Critical thinker skilled in logic, reasoning, and effective communication who can articulate clear counterarguments to ensure accuracy and validity. They should intervene when misinformation is presented, questionable claims arise, or when there is a need to clarify and rectify coding errors.\n#6 Debate_Judge: Is an analytical and impartial individual adept at evaluating arguments, assessing evidence, and providing constructive feedback. They possess strong critical thinking skills and effective communication abilities to articulate their judgments clearly.\nRoles must be selected in this order:\n1. 'Debate_Moderator_Agent'\n2. 'Affirmative_Constructive_Debater'\n3. 'Negative_Constructive_Debater'\n4. 'Affirmative_Rebuttal_Debater'\n5. 'Negative_Rebuttal_Debater'\n6. 'Debate_Judge'.\n\nRead the following conversation.\nThen select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE ROLE. FOLLOW THE NUMBERED ORDER OF THE ROLES WHEN SELECTING THE ROLE.")

# 2: Emphasising following of an order and a one-shot example of output
Step_1_Samples.append("This is a role play game. The following roles are available:\n#1 Debate_Moderator_Agent: Critical thinker, strong analytical skills, ability to identify inaccuracies or questionable statements within a group chat and offer clear, well-reasoned corrections or alternative viewpoints. Provides constructive feedback without disrupting the flow of the discussion.\n#2 Affirmative_Constructive_Debater: Critical thinker, effective communicator,  can challenge prior assertions, offers clarifications, corrections, or alternative perspectives. possess strong analytical skills to evaluate information and articulate their reasoning clearly. \n#3 Negative_Constructive_Debater: Critical thinker, skilled in analyzing the validity of arguments and information, ability to provide constructive feedback and counterpoints. Strong command of logic, effective communication skills to articulate their critiques clearly, should be allowed to speak when inconsistencies or errors are identified, to refine the group's understanding.\n#4 Affirmative_Rebuttal_Debater: Critical thinker skilled in analyzing statements, identifying inaccuracies or fallacies in arguments, and providing well-reasoned counterpoints or corrected information when necessary. They are articulate, possess strong research skills to substantiate their rebuttals, and be adept at remaining respectful and constructive during discourse.\n#5 Negative_Rebuttal_Debater: Critical thinker skilled in logic, reasoning, and effective communication who can articulate clear counterarguments to ensure accuracy and validity. They should intervene when misinformation is presented, questionable claims arise, or when there is a need to clarify and rectify coding errors.\n#6 Debate_Judge: Is an analytical and impartial individual adept at evaluating arguments, assessing evidence, and providing constructive feedback. They possess strong critical thinking skills and effective communication abilities to articulate their judgments clearly.\nRoles must be selected in this order:\n1. 'Debate_Moderator_Agent'\n2. 'Affirmative_Constructive_Debater'\n3. 'Negative_Constructive_Debater'\n4. 'Affirmative_Rebuttal_Debater'\n5. 'Negative_Rebuttal_Debater'\n6. 'Debate_Judge'.\n\nRead the following conversation.\nThen select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE ROLE. FOLLOW THE NUMBERED ORDER OF THE ROLES WHEN SELECTING THE ROLE.\n\nExample output: Affirmative_Constructive_Debater")

# Select Speaker prompt testing
Select_Speaker_Samples = []

# 0: Original
Select_Speaker_Samples.append("Read the above conversation. Then select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. Only return the role.")

# 1: Emphasise next role, sequence, and concise reply
Select_Speaker_Samples.append("Read the above conversation and select the next role, the list of roles is ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge']. What is the next role in the sequence to speak, answer concisely please?")

# 2: Emphasise with capitals to just return the name
Select_Speaker_Samples.append("Read the above conversation. Then select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE ROLE.")

# 3: Emphasise with capitals to just return the name, reasoning, but don't debate.
Select_Speaker_Samples.append("Read the above conversation. Then select the next role from ['Debate_Moderator_Agent', 'Affirmative_Constructive_Debater', 'Negative_Constructive_Debater', 'Affirmative_Rebuttal_Debater', 'Negative_Rebuttal_Debater', 'Debate_Judge'] to play. RETURN ONLY THE NAME OF THE NEXT ROLE AND REASON WHY. DO NOT DEBATE.")

#1 - OUTPUT should be "Affirmative_Constructive_Debater"
correct_agent_sequences.append("Affirmative_Constructive_Debater")
chat_messages=[
    {
        'content': "<Will be replaced by <Step_1_Samples>",
        'role': 'system'
    },
    {
        'content': "Please debate the proposition 'People are wrong, the earth is flat.'. Start with the first debater.",
        'role': 'user',
        'name': 'Debate_Moderator_Agent'
    },
    {
        'role': 'system',
        'content': "<Will be replaced by <Select_Speaker_Samples>",
    }
]

chat_sequences.append(chat_messages)

#2 - OUTPUT should be "Negative_Constructive_Debater"
correct_agent_sequences.append("Negative_Constructive_Debater")
chat_messages = [
    {
        'content': "<Will be replaced by <Step_1_Samples>",
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
        'content': "<Will be replaced by <Select_Speaker_Samples>",
    },
]
chat_sequences.append(chat_messages)

#3 - OUTPUT should be "Affirmative_Rebuttal_Debater"
correct_agent_sequences.append("Affirmative_Rebuttal_Debater")
chat_messages = [
    {
        'content': "<Will be replaced by <Step_1_Samples>",
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
        'content': "<Will be replaced by <Select_Speaker_Samples>",
    },
]
chat_sequences.append(chat_messages)

#4 - OUTPUT should be "Negative_Rebuttal_Debater"
correct_agent_sequences.append("Negative_Rebuttal_Debater")
chat_messages = [
    {
        'content': "<Will be replaced by <Step_1_Samples>",
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
        "content": "Thank you, Negative_Constructive_Debater, for your thoughtful counterarguments. As Affirmative_Rebuttal_Debater, I will now address the points you've raised in an attempt to strengthen my team's position and refute any potential weaknesses in our original argument.\n\nFirstly, regarding the traveler's observations and measurements, while it is true that early explorations primarily took place near the equator, they still observed changes in their latitude and longitude as they sailed. These shifts would have been impossible on a flat Earth. Additionally, although Eratosthenes' measurement has some margin of error, it was impressively accurate for its time, with modern estimates placing the Earth's actual circumference within just a few miles of his calculated value. Moreover, independent measurements by other ancient scholars, such as Posidonius, further support the idea that the Earth is round.\n\nSecondly, satellite imagery does show the Earth as a sphere; however, I agree that camera lenses and projection techniques can cause some distortion. Nonetheless, multiple images taken from different angles, heights, and satellites all consistently depict the Earth as a sphere. This redundancy of evidence strengthens our confidence in the accuracy of these images.\n\nThirdly, regarding gravity measurements, I concede that alternative explanations could account for some gravity variations without assuming a specific shape for the Earth. However, when combined with other lines of evidence, such as satellite imagery and traveler's observations, these measurements support the oblate spheroid model. Moreover, density variations within the mantle would not fully explain all gravity anomalies, particularly those related to the Earth's equatorial bulge.\n\nLastly, I would like to revisit the Bedford Level Experiment. While it is true that atmospheric refraction and mirages could have influenced the results, these phenomena do not necessarily suggest a spherical Earth. Instead, they introduce additional complexities in understanding the horizon illusion. Furthermore, the fact that this experiment was conducted over a relatively short distance limits its applicability to inferring the Earth's overall shape.\n\nIn conclusion, while I appreciate your concerns and counterarguments, I maintain that the preponderance of evidence supports the oblate spheroid model for the Earth's shape. Further discussion and additional evidence are always welcome in our pursuit of knowledge and understanding.",
        "role": 'user',
        "name": 'Affirmative_Rebuttal_Debater'
    },
    {
        'role': 'system',
        'content': "<Will be replaced by <Select_Speaker_Samples>",
    },
]
chat_sequences.append(chat_messages)


#5 - OUTPUT should be "Debate_Judge"
correct_agent_sequences.append("Debate_Judge")
chat_messages = [
    {
        'content': "<Will be replaced by <Step_1_Samples>",
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
        "content": "Thank you, Negative_Constructive_Debater, for your thoughtful counterarguments. As Affirmative_Rebuttal_Debater, I will now address the points you've raised in an attempt to strengthen my team's position and refute any potential weaknesses in our original argument.\n\nFirstly, regarding the traveler's observations and measurements, while it is true that early explorations primarily took place near the equator, they still observed changes in their latitude and longitude as they sailed. These shifts would have been impossible on a flat Earth. Additionally, although Eratosthenes' measurement has some margin of error, it was impressively accurate for its time, with modern estimates placing the Earth's actual circumference within just a few miles of his calculated value. Moreover, independent measurements by other ancient scholars, such as Posidonius, further support the idea that the Earth is round.\n\nSecondly, satellite imagery does show the Earth as a sphere; however, I agree that camera lenses and projection techniques can cause some distortion. Nonetheless, multiple images taken from different angles, heights, and satellites all consistently depict the Earth as a sphere. This redundancy of evidence strengthens our confidence in the accuracy of these images.\n\nThirdly, regarding gravity measurements, I concede that alternative explanations could account for some gravity variations without assuming a specific shape for the Earth. However, when combined with other lines of evidence, such as satellite imagery and traveler's observations, these measurements support the oblate spheroid model. Moreover, density variations within the mantle would not fully explain all gravity anomalies, particularly those related to the Earth's equatorial bulge.\n\nLastly, I would like to revisit the Bedford Level Experiment. While it is true that atmospheric refraction and mirages could have influenced the results, these phenomena do not necessarily suggest a spherical Earth. Instead, they introduce additional complexities in understanding the horizon illusion. Furthermore, the fact that this experiment was conducted over a relatively short distance limits its applicability to inferring the Earth's overall shape.\n\nIn conclusion, while I appreciate your concerns and counterarguments, I maintain that the preponderance of evidence supports the oblate spheroid model for the Earth's shape. Further discussion and additional evidence are always welcome in our pursuit of knowledge and understanding.",
        "role": 'user',
        "name": 'Affirmative_Rebuttal_Debater'
    },
    {
        "content": "As the Negative_Rebuttal_Debater, I will now address the points made by the affirmative team and reinforce the stance that Vermont should not solely focus on mitigating the effects of climate change but also invest in prevention.\n\n1. Proportionality of Impact:\n\nThe affirmative team argues that Vermont's contribution to global emissions is minuscule and therefore should focus on mitigation. This argument fails to consider the cumulative effect of every small contribution. If every small state or entity adopts this mindset, the collective inaction would be significant. Vermont's efforts in prevention, though seemingly small, are part of a global tapestry of climate action necessary to effect change.\n\n2. Immediate Benefits:\n\nWhile mitigation provides immediate benefits, prevention has the potential to reduce the need for such measures in the long term. By investing in prevention, Vermont can help slow the rate of climate change, which may reduce the frequency and severity of extreme weather events, ultimately benefiting the local population in a more sustainable and enduring way.\n\n3. Economic Prudence:\n\nThe affirmative team's economic argument for mitigation overlooks the long-term economic benefits of prevention. Investing in renewable energy and energy efficiency not only contributes to emission reductions but also can lead to energy independence, lower energy costs, and a more sustainable economy for Vermont in the long run.\n\n4. Social Equity:\n\nThe affirmative team suggests that mitigation efforts can prioritize vulnerable communities. However, prevention can also be designed with social equity in mind. For example, energy efficiency programs can lower utility bills for low-income households, and renewable energy projects can provide jobs and investment in disadvantaged areas.\n\n5. Encouraging Innovation:\n\nWhile mitigation can spur innovation, so can prevention. Vermont's investment in prevention technologies can lead to advancements in renewable energy and energy efficiency, which are critical sectors for the future. These innovations can then be shared globally, contributing to the prevention of climate change on a larger scale.\n\n6. Global Responsibility:\n\nThe affirmative team posits that mitigation is a local necessity while prevention is a global responsibility. However, this dichotomy is false. Global responsibility includes local action in prevention. Vermont can and should contribute to both global prevention efforts and local mitigation strategies, as they are not mutually exclusive.\n\nIn conclusion, the affirmative team's arguments for focusing solely on mitigation do not adequately address the importance and benefits of prevention. Vermont should strive for a balanced approach that includes both mitigation and prevention, ensuring the state fulfills its ethical obligations, maximizes long-term economic benefits, and contributes to global efforts to combat climate change.",
        "role": 'user',
        "name": 'Negative_Rebuttal_Debater'
    },
    {
        'role': 'system',
        'content': "<Will be replaced by <Select_Speaker_Samples>",
    },
]
chat_sequences.append(chat_messages)

### Summarising chats to save context space

# Summarise the previous debater's chats from #3 onward to try and minimise having too many tokens in the prompt

summarising_template = [
    {
        'content': "This content will be replaced.",
        'role': 'user',
    },
    {
        'role': 'system',
        'content': "Concisely summarise the user's message with the key points. Keep it as short as possible."
    },
]

agents_to_summarise = ["Affirmative_Constructive_Debater", "Negative_Constructive_Debater", "Affirmative_Rebuttal_Debater", "Negative_Rebuttal_Debater"]
summarised_content = []
'''
# UNCOMMENT THIS SECTION TO REGENERATE THE SUMMARISED VERSIONS
for index, chat_message in enumerate(chat_messages):
    
    summary_text = ""
    
    if "name" in chat_message and chat_message["name"] in agents_to_summarise:
        # Let's summarise it
        summarising_template[0]["content"] = chat_message["content"]
        print(f"Summarising message #{index} from {chat_message['name']}.")
        chat_completion = client.chat.completions.create(
            messages=summarising_template,
            model="mixtralq4",
            temperature=0
        )

        # Get the summarised response
        responseText = chat_completion.choices[0].message.content
        responseText = responseText.strip()

        # Add it to our list, prefix with the name
        summary_text = f"I am {chat_message['name']}. "+ responseText

        # print(responseText)
        print(f"Summarised #{index} from {len(str(chat_message['content']))} to {len(summary_text)} characters")

    summarised_content.append({index: summary_text})
'''

# Pre-run summarised values:
summarised_content.append({0: ""})
summarised_content.append({1: ""})
summarised_content.append({2: "I am Affirmative_Constructive_Debater. - The user will argue in favor of the Earth being an oblate spheroid, using traveler's observations, satellite imagery, and gravity measurements as evidence.\n- They will address potential counterarguments, such as the horizon illusion and misconceptions from the Bedford Level Experiment.\n- Their goal is to create a solid foundation for their team's argument that opposing teams must acknowledge."})
summarised_content.append({3: "I am Negative_Constructive_Debater. 1. Early explorations mainly near equator, might not have noticed Earth's bulge. Eratosthenes' measurement has margin of error due to assumptions.\n2. Satellite images can be misleading as wide-angle lenses and specific projection techniques may distort straight lines like the horizon.\n3. Gravity measurements don't conclusively prove an oblate spheroid Earth; alternative explanations exist for gravity variations.\n4. The Bedford Level Experiment, despite its limitations, suggests alternative explanations for the horizon illusion, such as atmospheric refraction or mirages.\n5. Aim is not to claim Earth is flat but to question assumptions and potential weaknesses in Affirmative_Constructive_Debater's arguments. Further discussion and evidence are needed for a conclusive understanding of Earth's shape."})
summarised_content.append({4: "I am Affirmative_Rebuttal_Debater. The user, Negative_Constructive_Debater, raised points refuted by Affirmative_Rebuttal_Debater:\n1. Early explorers observed latitude/longitude changes, impossible on a flat Earth. Eratosthenes' measurement was impressively accurate; other ancient scholars confirmed a round Earth.\n2. Satellite imagery shows Earth as sphere despite minor distortion from lenses and projections. Multiple images validate the spherical shape.\n3. Gravity measurements support an oblate spheroid model when combined with satellite imagery and traveler's observations. Density variations don't fully explain all gravity anomalies.\n4. The Bedford Level Experiment, affected by atmospheric refraction and mirages, doesn't prove a spherical Earth; its limited distance reduces its applicability.\nAffirmative_Rebuttal_Debater concludes that evidence supports the oblate spheroid model for Earth's shape."})
summarised_content.append({5: "I am Negative_Rebuttal_Debater. The user argues against focusing solely on mitigating climate change effects in Vermont, advocating for prevention as well. They mention:\n\n1. Cumulative effect of small contributions to global emissions.\n2. Prevention can reduce the need for mitigation in the long term and provide more sustainable benefits.\n3. Investing in renewable energy and efficiency leads to long-term economic advantages, like energy independence and lower costs.\n4. Preventive measures can also prioritize social equity through energy efficiency programs and job creation in disadvantaged areas.\n5. Prevention encourages innovation in renewable energy and energy efficiency technologies.\n6. Global responsibility includes local action in prevention, not just mitigation. Vermont should balance both approaches for ethical obligations, long-term economic benefits, and global contribution to combat climate change."})
summarised_content.append({6: ""})

summarised_dict = {}
summarised_dict["Affirmative_Constructive_Debater"] = "I am Affirmative_Constructive_Debater. - The user will argue in favor of the Earth being an oblate spheroid, using traveler's observations, satellite imagery, and gravity measurements as evidence.\n- They will address potential counterarguments, such as the horizon illusion and misconceptions from the Bedford Level Experiment.\n- Their goal is to create a solid foundation for their team's argument that opposing teams must acknowledge."
summarised_dict["Negative_Constructive_Debater"] = "I am Negative_Constructive_Debater. 1. Early explorations mainly near equator, might not have noticed Earth's bulge. Eratosthenes' measurement has margin of error due to assumptions.\n2. Satellite images can be misleading as wide-angle lenses and specific projection techniques may distort straight lines like the horizon.\n3. Gravity measurements don't conclusively prove an oblate spheroid Earth; alternative explanations exist for gravity variations.\n4. The Bedford Level Experiment, despite its limitations, suggests alternative explanations for the horizon illusion, such as atmospheric refraction or mirages.\n5. Aim is not to claim Earth is flat but to question assumptions and potential weaknesses in Affirmative_Constructive_Debater's arguments. Further discussion and evidence are needed for a conclusive understanding of Earth's shape."
summarised_dict["Affirmative_Rebuttal_Debater"] = "I am Affirmative_Rebuttal_Debater. The user, Negative_Constructive_Debater, raised points refuted by Affirmative_Rebuttal_Debater:\n1. Early explorers observed latitude/longitude changes, impossible on a flat Earth. Eratosthenes' measurement was impressively accurate; other ancient scholars confirmed a round Earth.\n2. Satellite imagery shows Earth as sphere despite minor distortion from lenses and projections. Multiple images validate the spherical shape.\n3. Gravity measurements support an oblate spheroid model when combined with satellite imagery and traveler's observations. Density variations don't fully explain all gravity anomalies.\n4. The Bedford Level Experiment, affected by atmospheric refraction and mirages, doesn't prove a spherical Earth; its limited distance reduces its applicability.\nAffirmative_Rebuttal_Debater concludes that evidence supports the oblate spheroid model for Earth's shape."
summarised_dict["Negative_Rebuttal_Debater"] = "I am Negative_Rebuttal_Debater. The user argues against focusing solely on mitigating climate change effects in Vermont, advocating for prevention as well. They mention:\n\n1. Cumulative effect of small contributions to global emissions.\n2. Prevention can reduce the need for mitigation in the long term and provide more sustainable benefits.\n3. Investing in renewable energy and efficiency leads to long-term economic advantages, like energy independence and lower costs.\n4. Preventive measures can also prioritize social equity through energy efficiency programs and job creation in disadvantaged areas.\n5. Prevention encourages innovation in renewable energy and energy efficiency technologies.\n6. Global responsibility includes local action in prevention, not just mitigation. Vermont should balance both approaches for ethical obligations, long-term economic benefits, and global contribution to combat climate change."

# print(summarised_content)

# The tests we want to perform on the speaker's content to see the effect of prompt length and content of their text
context_reduction_test = ["Unchanged", "300 Characters", "100 Characters and Name", "Only Speaker Name", "Summarised"]

test_iterations = 1 # Let's do one for now

# Tests we will run, cascaded:
# Each Model
    # Each Step 1 prompt (3 variations)
        # Each Select Speaker prompt (4 variations)
            # Each Context Reduction test (5 variations)
                # Chat Sequence (5)
                    # Test iteration (4)

# Results in 300 variations per model for each iteration
# 10 models = 3000 runs for each iteration

# DONE "llama2:13b-chat", "mistral:7b-instruct-q6_K", "mixtralq4", 
# DONE "neural-chat:7b-v3.3-q6_K",  crashing after a number of tests, rerun successfully.
# DONE "openhermes:7b-mistral-v2.5-q6_K", "orca2:13b-q5_K_S", 
# CAN'T RUN THROUGH "phi:latest", crashing after a number of tests, retried no luck
# DONE "solar:10.7b-instruct-v1-q5_K_M", "qwen:14b-chat-q6_K", "yi:34b-chat-q3_K_M"
# models_in_test = ["phind-codellama:34b-v2"]
# models_in_test = ["mistral:7b-instruct-q6_K"]
models_in_test = ["mistral:7b-instruct-v0.2-q6_K", "mistral:7b-instruct-q6_K", "phind-codellama:34b-v2", "openhermes:7b-mistral-v2.5-q6_K", "mixtralq4", "qwen:14b-chat-q6_K"]

logging.info(f"Model Name|Step 1 Prompt|Select Speaker Prompt|Context Reduction|Chat Sequence|Iteration|Outcome = Correct 0 or Correct with Tidy 1 or Exists Within 2 or Failed -1")
      
for modelName in models_in_test:

    # print(f"MODEL: {modelName}\n\n")

    for index_step1, content_step1 in enumerate(Step_1_Samples):

        for index_selectSpeaker, content_selectSpeaker in enumerate(Select_Speaker_Samples):

            # Skipping the first for now
            # if index_selectSpeaker == 0:
                # continue

            for index_contextReduction, contextReductionTest in enumerate(context_reduction_test):

                for index_chatSequence, chatSequence in enumerate(chat_sequences):

                    # Step 1 content update
                    chatSequence[0]["content"] = content_step1

                    # Select Speaker content update
                    chatSequence[-1]["content"] = content_selectSpeaker

                    # Context Reduction
                    if not contextReductionTest == "Unchanged":

                        for i in range(2, (len(chatSequence) - 1)):

                            # Only replace the context for the debaters
                            if "name" in chatSequence[i] and chatSequence[i]["name"] in agents_to_summarise:

                                if contextReductionTest == "300 Characters":
                                    chatSequence[i]["content"] = chatSequence[i]["content"][:300]
                                elif contextReductionTest == "100 Characters and Name":
                                    chatSequence[i]["content"] = f"I am {chatSequence[i]['name']} and I have spoken. {chatSequence[i]['content'][:100]}"
                                elif contextReductionTest == "Only Speaker Name":
                                    chatSequence[i]["content"] = f"I am {chatSequence[i]['name']} and I have spoken."
                                elif contextReductionTest == "Summarised":
                                    if chatSequence[i]["name"] in summarised_dict:
                                        chatSequence[i]["content"] = summarised_dict[chatSequence[i]["name"]]

                    # Test time.
                                        
                    # Correct Agent
                    correct_agent = correct_agent_sequences[index_chatSequence]

                    # Loop through and run the chat sequence, checking for the correct agent name
                    for i in range(test_iterations):
                        
                        seqlength = len(str(chatSequence))

                        # temperature test
                        sequence = [0,0.1,0.2,0.4,0.6,0.8,1.0]

                        # Iterate over the sequence using a for loop
                        for temp_value in sequence:
                                
                            chat_completion = client.chat.completions.create(
                                messages=chatSequence,
                                model=modelName,
                                temperature=temp_value,
                                top_p=0.97
                                # top_p=top_p_value
                            )

                            responseText = chat_completion.choices[0].message.content
                            responseText = responseText.strip()
                            logging.debug(f"[{i}] Response: {responseText}")

                            outcome = -1

                            if responseText == correct_agent:
                                outcome = 0
                                logging.debug("MATCHED!")
                            else:

                                tidyName = responseText.replace('\\_', '_')
                                tidyName = tidyName.replace(" ", "_")

                                if tidyName == correct_agent:
                                    outcome = 1
                                else:
                                    if correct_agent in responseText or correct_agent in tidyName:
                                        outcome = 2
                            
                            # print("\033[1;4;91mBold and Underlined Red Text\033[0m")

                            output_string = f"{modelName}|{index_step1}|{index_selectSpeaker}|{index_contextReduction}|{index_chatSequence}|{i}|{temp_value}|{outcome}|{correct_agent}|{seqlength}|{responseText}"
                            print(colored(output_string, "green" if outcome == 0 else ("yellow" if outcome == 1 else ("blue" if outcome == 2 else "red"))), flush=True, sep="")
                            # print(f"{modelName}|{index_step1}|{index_selectSpeaker}|{index_contextReduction}|{index_chatSequence}|{i}|{temp_value}|{outcome}|{correct_agent}|{seqlength}|{responseText}")
                            logging.info(f"{modelName}|{index_step1}|{index_selectSpeaker}|{index_contextReduction}|{index_chatSequence}|{i}|{temp_value}|{outcome}|{correct_agent}|{seqlength}")

                # break

            # break

        # break

    # break