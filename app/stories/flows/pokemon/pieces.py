from pieces_copilot_sdk import PiecesClient

# Create an instance of PiecesClient
pieces_client = PiecesClient(
    config={
        'baseUrl': 'http://localhost:1000'
    }
)

# 1. Create a new conversation
conversation_response = pieces_client.create_conversation(
    props={
        "name": "Test Conversation",
        "firstMessage": "Hello, how can I use the API?"
    }
)

# Check if the conversation was created successfully
if conversation_response:
    print("Conversation Created:", conversation_response['conversation'].id)
    print("First Message Response:", conversation_response['answer']['text'])

    # 2. Get the created conversation details
    conversation_id = conversation_response['conversation'].id
    conversation_details = pieces_client.get_conversation(
        conversation_id=conversation_id,
        include_raw_messages=True
    )

    # Access the conversation name using the key
    print("Conversation Name:", conversation_details.get('name'))

    # 3. Ask a question within the created conversation
    question_response = pieces_client.prompt_conversation(
        message="Can you give me an example code snippet?",
        conversation_id=conversation_id
    )
    print("Question Response:", question_response['text'])

# 4. Retrieve all conversations and print their names
all_conversations = pieces_client.get_conversations()
for conversation in all_conversations:
    print("Conversation Name:", conversation.name)

# 5. Get user profile picture
profile_picture = pieces_client.get_user_profile_picture()
print("User Profile Picture URL:", profile_picture)

# 6. Ask a question
question = "What is Pieces for Developer?"
response = pieces_client.ask_question(question)
print("Question Response:", response)