# Interactive Prompt Playground

A user-configurable Streamlit application for testing and comparing OpenAI model outputs with different parameter combinations. Perfect for prompt engineering, parameter tuning, and understanding how various settings affect AI-generated content.

![App UI](AppUI.png)

## 🎯 Features

- **Multi-Model Support**: Test with GPT-3.5-turbo or GPT-4o
- **Parameter Testing**: Experiment with temperature, max tokens, frequency penalty, and presence penalty
- **Real-time Comparison**: View all outputs in an organized table format
- **Reflection Notes**: Built-in text area for documenting observations and insights
- **Custom Prompts**: Configurable system and user prompts
- **Stop Sequences**: Define custom stop sequences for output control

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/haarry9/interactive-prompt-playground.git
cd interactive-prompt-playground
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Running the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📋 Usage

1. **Configure Prompts**: Set your system prompt (AI personality) and user prompt (the question/request)
2. **Select Model**: Choose between GPT-3.5-turbo or GPT-4o
3. **Adjust Parameters**:
   - **Temperature** (0.0-1.5): Controls randomness/creativity
   - **Max Tokens** (10-300): Limits response length
   - **Frequency Penalty** (0.0-2.0): Reduces repetition of frequent tokens
   - **Presence Penalty** (0.0-2.0): Encourages topic diversity
   - **Stop Sequences**: Custom stopping points (optional)
4. **Generate**: Click "Generate" to create a response
5. **Compare Results**: View all outputs in the results table
6. **Document Insights**: Use the reflection area to note observations

## 🔬 Experiment Suggestions

### Recommended Test Values

| Parameter | Test Values |
|-----------|-------------|
| Temperature | 0.0, 0.7, 1.2 |
| Max Tokens | 50, 150, 300 |
| Presence Penalty | 0.0, 1.5 |
| Frequency Penalty | 0.0, 1.5 |

### Sample Prompts

![Output](output.png)

### Reflections

Playing with the OpenAI model parameters in the Interactive Prompt Playground was a cool experience. With gpt-3.5-turbo set to a temperature of 0.0 and token limit at 50, the result was a neat, poetic blurb about iPhone 5, that stopped when hitting the token limit. It was clean and focused but felt like it was holding back. When I bumped the temperature to 0.7, stretched max tokens to 150, and added some frequency and presence penalties, the output for the Tesla Model S5 came alive. It painted a vivid picture of a car that “glides with grace” and “ignites a passion,” showing how a bit of warmth and room to breathe let the model stretch its creative legs, while penalties kept it from rambling.

Then, switching to gpt-4o with a fiery temperature of 1.2, 300 max tokens, and maxed-out penalties, the output turned into something almost magical. The Tesla Model S5 became a “chariot of whispers and wonders,” with poetic flourishes that felt like they were pulled from a dream. It was longer, richer, and packed with imagery—like “cobalt hues reflecting starlight”—that made the car sound like a piece of art. The higher settings and stronger model clearly unleashed a flood of creativity, turning a simple prompt into a story that felt personal and alive. It’s fascinating how these tweaks can transform a few words into something so distinct, like coaxing different voices out of the same instrument.
