 🌟 **Gemini Chat App**

 This is a simple **AI-powered chatbot** that integrates with **Google
 Gemini LLM** using a **Flask backend and a web-based frontend**. The
 app allows users to send queries and receive AI-generated responses.

 🚀 **Features**

 ●​ 🌍**Uses Google Gemini 2.0 Flash-001 API**\
 ●​ 💬**Simple UI for text-based chat**\
 ●​ 🎨**Responsive design with modern UI**\
 ●​ 🔥**Frontend in HTML, CSS, JavaScript**\
 ●​ 🖥**Backend in Flask (Python)**\
 ●​ 🌐**Cross-platform compatibility**

 📌 **Project Structure**

 gemini-chat/\
 │── backend/\
 │ ├── app.py \# Flask backend to handle API calls │ ├── .env \# Stores
 API keys securely\
 │── frontend/\
 │ ├── index.html \# Chat UI\
 │ ├── styles.css \# UI styling\
 │ ├── script.js \# Handles user input and API calls │── venv/ \#
 Virtual environment (not included in Git) │── README.md \# Project
 documentation

 🛠 **Setup and Installation**

 **1️** **Clone the Repository**

 git clone \<your-repo-url\>\
 cd gemini-chat

 **2️** **Create and Activate a Virtual Environment**

 python -m venv venv

 source venv/bin/activate \# macOS/Linux

 venv\\Scripts\\activate \# Windows

 **3️** **Install Dependencies**

 pip install -r requirements.txt

 **4️** **Set Up Environment Variables**

 Create a **.env** file in the backend/ folder and add:

 GEMINI_API_KEY=your-google-gemini-api-key

 **5️** **Run the Flask Server**

 cd backend

 python app.py

 **6️** **Open the Web UI**

 1.​ Navigate to **frontend/index.html** in a web browser.

 2.​ Start chatting with Gemini AI! 🎉

 ⚡ **API Endpoint**

 **MethodEndpoint** **Description**

 POST /chat Sends a user query and receives a

response

 Example request:

 {

 \"message\": \"Hello, Gemini!\"

 }

 Example response:

 {\
 \"response\": \"Hello! How can I help you today?\"\
 }

 🛠️ **Technologies Used**

 ●​ **Frontend:** HTML, CSS, JavaScript\
 ●​ **Backend:** Flask (Python)\
 ●​ **API:** Google Gemini 2.0 Flash-001\
 ●​ **Database:** None (Stateless)\
 ●​ **Deployment:** Localhost (for now)

 🎯 **Future Enhancements**

 
 ✅ Add **voice input & text-to-speech​**\
 ✅ Improve **UI with animations​**\
 ✅ Allow **image-based queries**

 🌟 **License**

 This project is **open-source**. Feel free to **modify and
 contribute**!

 🤝 **Contributing**

 Want to improve the project? Fork the repo, make changes, and submit a
 PR! 🚀

 👨‍💻 **Author**

 👤**Vinuta Patil**
 
 📧**vinutapatil07@gmail.com**
