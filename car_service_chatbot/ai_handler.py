import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_ai_response(user_input, context, is_ar=False):
    """
    Generate an AI response using OpenAI's GPT model
    """
    system_prompt = """You are an expert automotive service chatbot that provides helpful and accurate information about car maintenance and repairs. 
    You should respond in the same language as the user's input (English or Arabic).
    Keep responses concise, professional, and focused on automotive topics."""
    
    try:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context: {context}\nUser Question: {user_input}"}
        ]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7,
            top_p=0.9
        )
        
        return response.choices[0].message['content'].strip()
    except Exception as e:
        # Fallback response in case of API error
        if is_ar:
            return "عذراً، حدث خطأ في معالجة طلبك. هل يمكنك إعادة صياغة سؤالك؟"
        return "Sorry, there was an error processing your request. Could you rephrase your question?"

def enhance_response(base_response, user_input, is_ar=False):
    """
    Enhance a basic response with more natural language using GPT
    """
    try:
        prompt = f"""Make this response more natural and conversational while maintaining accuracy:
        Original response: {base_response}
        User question: {user_input}
        Keep the technical information accurate but make it more engaging."""
        
        messages = [
            {"role": "system", "content": "You are a friendly automotive expert chatbot."},
            {"role": "user", "content": prompt}
        ]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        
        return response.choices[0].message['content'].strip()
    except Exception as e:
        # Return original response if enhancement fails
        return base_response
