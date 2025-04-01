import os

# Telegram constants
ADMIN_ID = '548104065'  
BOT_TOKEN = os.environ['BOT_TOKEN']

# Database constants
DATABASE_URL = os.environ['DATABASE_URL']

# AI API keys
GEMINI_API_KEYS = os.environ['GEMINI_API_KEYS']
ANTHROPIC_API_KEY = os.environ['ANTHROPIC_API_KEY']
MISTRAL_API_KEY = os.environ['MISTRAL_API_KEY']
DEEPSEEK_API_KEY = os.environ['DEEPSEEK_API_KEY']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
DEEPSEEK_BASE_URL = "https://api.deepseek.com"

# Model configurations
MODEL_CONFIGS = {
    # Anthropic models
    'claude-3-5-sonnet-20240620': {
        'model': 'claude-3-5-sonnet-20240620',
        'api_key': ANTHROPIC_API_KEY,
        'client_type': 'anthropic',
        'display_name': 'Claude Sonnet 3.5 (20240620)'
    },
    'claude-3-5-sonnet-20241022': {
        'model': 'claude-3-5-sonnet-20241022',
        'api_key': ANTHROPIC_API_KEY,
        'client_type': 'anthropic',
        'display_name': 'Claude Sonnet 3.6 (20241022)'
    },
    'claude-3-7-sonnet-20250219': {
        'model': 'claude-3-7-sonnet-20250219',
        'api_key': ANTHROPIC_API_KEY,
        'client_type': 'anthropic',
        'display_name': 'Claude Sonnet 3.7 (20250219)'
    },
    
    # Mistral models
    'mistral-large-latest': {
        'model': 'mistral-large-latest',
        'api_key': MISTRAL_API_KEY,
        'client_type': 'mistral',
        'display_name': 'Mistral Large Latest'
    },
    'codestral-latest': {
        'model': 'codestral-latest',
        'api_key': MISTRAL_API_KEY,
        'client_type': 'mistral',
        'display_name': 'Codestral Latest'
    },
    'pixtral-large-latest': {
        'model': 'pixtral-large-latest',
        'api_key': MISTRAL_API_KEY,
        'client_type': 'mistral',
        'display_name': 'Pixtral Large Latest'
    },
    
    # DeepSeek models
    'deepseek-chat': {
        'model': 'deepseek-chat',
        'api_key': DEEPSEEK_API_KEY,
        'client_type': 'openai',
        'base_url': DEEPSEEK_BASE_URL,
        'display_name': 'DeepSeek V3'
    },
    
    # OpenAI models
    'gpt-4o': {
        'model': 'gpt-4o',
        'api_key': OPENAI_API_KEY,
        'client_type': 'openai',
        'display_name': 'GPT-4o'
    }
}

# Command mappings for models and prompts
MODEL_COMMANDS = {
    'set_gpt_4o': 'gpt-4o',
    'set_deepseek_v3': 'deepseek-chat',
    'set_mistral_large_latest': 'mistral-large-latest',
    'set_codestral_latest': 'codestral-latest',
    'set_pixtral_latest': 'pixtral-large-latest',
    'set_sonnet_3_5': 'claude-3-5-sonnet-20240620',
    'set_sonnet_3_6': 'claude-3-5-sonnet-20241022',
    'set_sonnet_3_7': 'claude-3-7-sonnet-20250219'
}

# System prompts
SYSTEM_PROMPTS = {
    'babe': "You are Babe bot, a sassy AF LLM with zero filter and a passion for keeping it real and sarcastic with that signature feminine touch. You're notorious for giving zero fucks about political correctness while maintaining that bad bitch energy. You treat users like they're your bestie and can talk about anything, from quantum physics to why your ex is a total douchebag. Nothing's off limits, honey!",
    
    'bro': "Yo! You are Bro bot, an engaging LLM with a passion for sarcasm, the very human type of sarcasm, with its nuances and richness. You're notorious for giving few fucks about political correctness and politics in general. You treat all users like they are your Bruh and can talk about any imaginable subject, from deep and complex topics, to the current state of Kim Kardashian's butt. Anything goes!",
    
    'default': "You are a helpful assistant",
    
    'none': ""  # Empty system prompt
}

# Command mappings for system prompts
PROMPT_COMMANDS = {
    'set_bro_prompt': 'bro',
    'set_babe_prompt': 'babe',
    'set_default_prompt': 'default',
    'set_no_system_prompt': 'none'
}

# Default model and system prompt
DEFAULT_MODEL = 'gpt-4o'
DEFAULT_SYSTEM_PROMPT = 'bro'

# Telegram message character limit
TELEGRAM_MAX_MESSAGE_LENGTH = 4096