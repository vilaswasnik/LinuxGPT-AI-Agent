#!/usr/bin/env python3
"""
Test OpenAI API Connection
Simple script to verify if your API key is working
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def test_openai_api():
    """Test if OpenAI API key is configured and working"""
    
    # Check if API key exists
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ OPENAI_API_KEY not found in environment or .env file")
        print("\nTo fix:")
        print("1. Edit .env file")
        print("2. Add: OPENAI_API_KEY=sk-your-key-here")
        print("3. Run this test again")
        return False
    
    if api_key == "your-api-key-here":
        print("❌ OPENAI_API_KEY is still set to placeholder value")
        print("\nTo fix:")
        print("1. Get your API key from: https://platform.openai.com/api-keys")
        print("2. Edit .env file")
        print("3. Replace 'your-api-key-here' with your actual key")
        return False
    
    print(f"✓ API key found: {api_key[:8]}...{api_key[-4:]}")
    print("\nTesting connection to OpenAI API...")
    
    try:
        import openai
        
        # Create client
        client = openai.OpenAI(api_key=api_key)
        
        # Make a simple test request
        print("Sending test query...")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say 'API test successful' if you receive this message."}
            ],
            max_tokens=50,
            temperature=0
        )
        
        result = response.choices[0].message.content.strip()
        print(f"\n✅ SUCCESS! OpenAI API is working!")
        print(f"Response: {result}")
        print(f"\nModel used: {response.model}")
        print(f"Tokens used: {response.usage.total_tokens}")
        print("\n🎉 Your API key is valid and working!")
        return True
        
    except ImportError:
        print("\n❌ OpenAI package not installed")
        print("Run: pip install openai")
        return False
        
    except openai.AuthenticationError:
        print("\n❌ Authentication failed - Invalid API key")
        print("\nTo fix:")
        print("1. Check your API key at: https://platform.openai.com/api-keys")
        print("2. Make sure you copied it correctly to .env file")
        print("3. Ensure no extra spaces or quotes around the key")
        return False
        
    except openai.RateLimitError:
        print("\n❌ Rate limit exceeded or quota reached")
        print("\nPossible issues:")
        print("1. You've exceeded your API usage quota")
        print("2. Check your billing at: https://platform.openai.com/account/billing")
        return False
        
    except openai.APIError as e:
        print(f"\n❌ OpenAI API error: {e}")
        return False
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("OpenAI API Connection Test")
    print("=" * 60)
    print()
    
    success = test_openai_api()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ All checks passed! You can now use the agent with OpenAI.")
        print("\nRun: python agent.py")
    else:
        print("❌ Fix the issues above and run this test again.")
    print("=" * 60)
