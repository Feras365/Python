# ZekaChat
    #### Video Demo:  <https://youtu.be/EIw4Xw9PMGw?feature=shared>
    #### Description:
    ZekaChat is a self-learning chatbot built using Python and CSV-based memory storage. Unlike traditional chatbots that only respond with predefined answers, ZekaChat learns and remembers new responses based on user interactions, making it smarter over time. This project demonstrates the principles of artificial intelligence, file handling, and interactive programming in a simple yet effective way.
    The chatbot continuously adapts and enhances its knowledge, ensuring that it provides better responses with every interaction. It maintains a history of user conversations, allowing it to retrieve relevant answers for repeated queries. This makes ZekaChat an ideal learning-based AI assistant that gets better over time.
    Unlike many chatbots that require complex machine learning models, ZekaChat achieves intelligence through structured data storage and retrieval, making it lightweight and efficient. By using a simple CSV file (AI.csv), it mimics human memory, offering a straightforward yet powerful implementation of an AI-driven chatbot. Future enhancements can include integration with NLP models, databases, and web interfaces to expand its capabilities.


    ### Files In Project
    project.py – The main chatbot program.
    test_project.py – Unit tests to validate chatbot functions.
    AI.csv – Memory storage file where learned responses are saved.
    README.md – Documentation for the project.

    ###Feature
   ✅ Remembers Conversations – Stores user queries and responses in AI.csv for future reference.
   ✅ Retrieves Known Answers – Checks if a question has been asked before and provides a response.
   ✅ Learns New Responses – If the chatbot doesn’t know an answer, it asks the user and stores it for future use.
   ✅ Simple and Lightweight – Uses only Python’s built-in csv module, making it easy to run without external dependencies.
   ✅ Command-Line Interface (CLI) – Runs in the terminal with a simple text-based interaction.

     ### How It Works
     User inputs a question.
     The chatbot checks its memory (AI.csv) to see if it knows the answer.
     If the answer exists, it retrieves and responds.
     If not found, it asks the user for the correct response and saves it.
     The chatbot continuously learns and improves over multiple interactions.
     ####Future Enhancements

     ✔ Integrate Natural Language Processing (NLP) – Improve chatbot intelligence with NLTK or spaCy.✔
     Use a Database Instead of CSV – Store chatbot memory in an SQLite or MongoDB database for better efficiency.✔
      Develop a Web Interface – Convert ZekaChat into a Flask/Django-based chatbot accessible via a browser.✔ Voice Interaction Support – Add speech-to-text and text-to-speech features to make it voice-interactive.
      ZekaChat is a great foundational AI project for understanding interactive chat systems, file handling, and machine learning principles. Start using ZekaChat today and watch it grow smarter with every conversation! 🚀
