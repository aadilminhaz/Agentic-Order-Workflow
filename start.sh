# Install dependencies
#pip install anthropic --break-system-packages
pip install -r requirements.txt 

# Set your API key
export ANTHROPIC_API_KEY='********'

#Run the basic agent
python agent.py

#Run interactive mode
#pyton agent.py interactive