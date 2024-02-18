Runs in AutoGenStudio

Note: Implemented the Markdown replacement to replace \_ to _ throughout (including in Stock settings)

2024-02-17
1. [Test 0,0,0] Stock settings:
- Phind CodeLlama 34B - Failed to select the correct speaker throughout
- Mixtral - Failed to select the correct speaker throughout
- OpenHermes 7B Mistral v2.5 (Q6) - Failed to select the correct speaker, debated instead of selected speaker

2. [Test 0,1,0] Change "Select Speaker" code in groupchat.py to "Read the above conversation and select the next role, the list of roles is {[agent.name for agent in agents]}. What is the next role in the sequence to speak, answer concisely please?"
- Phind CodeLlama 34B - Failed to choose the correct speaker but did return some succinct roles
- Mixtral - Failed to choose the correct speakers, but did return succinct roles
- OpenHermes 7B Mistral v2.5 (Q6) - Failed to select the correct speaker throughout and debated instead of selected

2. [Test 0,1,0 + Reduced Agent descriptions + emphasize order in the "Select Speaker Msg"] Change "Select Speaker Prompt" code in groupchat.py to "Read the above conversation and select the next role, the list of roles is {[agent.name for agent in agents]}. What is the next role in the sequence to speak, answer concisely please?"

- Phind CodeLlama 34B - Said it could not debate, and chose these in order and succintly: Affirmative_Constructive_Debater > Negative_Constructive_Debater > Affirmative_Constructive_Debater > Affirmative_Rebuttal_Debater > Affirmative_Rebuttal_Debater > AutoGenStudio crashed?
- Mixtral - (so close, just added one extra speaker and the judge didn't terminate!) - Affirmative_Constructive_Debater > Negative_Constructive_Debater (note it referenced NCD but also noted the ACD so we may need an LLM to pick the correct one) > Affirmative_Rebuttal_Debater > Negative_Rebuttal_Debater > Affirmative_Rebuttal_Debater > Debate_Judge
- OpenHermes 7B Mistral v2.5 (Q6) - (started off well but went haywire) - Affirmative_Constructive_Debater > Negative_Constructive_Debater > Affirmative_Rebuttal_Debater > Affirmative_Constructive_Debater > Affirmative_Rebuttal_Debater > Affirmative_Constructive_Debater > Affirmative_Rebuttal_Debater > Negative_Rebuttal_Debater > Affirmative_Constructive_Debater

3. [Test 0,1,0 + as above + adding numbers to the agent names in the groupchat.py (select_speaker_msg)]
["You are in a role play game. The following roles are available:\n{self._participant_roles(agents)}.\n\nRoles must be selected in this order: {', '.join([f'{index + 1}. {agent.name}' for index, agent in enumerate(agents)])} to play. Only return the role."]
- Phind CodeLlama 34B - 
- Mixtral - (slowly getting there...) - Affirmative_Constructive_Debater > Negative_Constructive_Debater > Affirmative_Rebuttal_Debater > Negative_Constructive_Debater > Negative_Rebuttal_Debater > Negative_Rebuttal_Debater
- OpenHermes 7B Mistral v2.5 (Q6) - (so close, added an extra ACD in there but otherwise good!) - Affirmative_Constructive_Debater > Negative_Constructive_Debater > Affirmative_Rebuttal_Debater > Affirmative_Constructive_Debater > Negative_Rebuttal_Debater > Debate_Judge > but didn't terminate and chose some more


4. [Test 0,1,3 + above reduced agent descriptions and emphasizing order] Replace the speaker's content with