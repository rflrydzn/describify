from django.shortcuts import render
from .forms import ChatForm
import google.generativeai as genai
import markdown


API_KEY = 'AIzaSyBI2fbd9buNBxESQhA64WQY3siJT7qa2jM'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

chat_history = []

def chatbot_view(request):
    global chat_history
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            num_paragraphs = int(form.cleaned_data['num_paragraphs'])
            tone = form.cleaned_data['tone']
            introduction = "Hi, I'm Describify, your product description generator AI! "
            response_intro = chat.send_message(introduction)
            response_description = ""
            for _ in range(num_paragraphs):
                response_description += chat.send_message(user_input + " in a " + tone + " tone.").text + "\n"
            chat_history = [{'user_input': user_input, 'ai_response': response_description}]
    else:
        form = ChatForm()
    return render(request, 'chatbot/chat.html', {'form': form, 'chat_history': chat_history})
