from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    projects_show = [
        {
            "title": "Face-Recognition-Attendance",
            "image": "images/face-recognition.jpg",
            "link": "https://github.com/dhananjay0911/Face_Recognition_Attendance",
            "details": "A Python-based project that uses OpenCV for face detection and recognition, allowing automated attendance marking in an Excel sheet. Includes face data collection, model training, and real-time recognition."
        },
        {
            "title": "Malicious_Link_Checker",
            "image": "images/malicious_link.avif",
            "link": "https://github.com/dhananjay0911/Malicious_Link_Checker",
            "details": "A Python project that detects and identifies potentially malicious URLs. It analyzes website links to determine their safety using machine learning and cybersecurity techniques, ensuring secure browsing."
        },
        {
            "title": "Weather-App",
            "image": "images/WeatherApp.png",
            "link": "https://github.com/dhananjay0911/Weather-App-using-html-css-js",
            "details": "A simple web-based Weather App built using HTML, CSS, and JavaScript. It fetches real-time weather data for any location, displaying temperature, humidity, and conditions in an intuitive interface."
        },
        {
            "title": "Traffic-Sign-Detection-System",
            "image": "images/tf.jpg",
            "link": "https://github.com/dhananjay0911/Traffic-Sign-Detection-System",
            "details": "A Python-based project that utilizes deep learning to detect and classify traffic signs from images or video streams. It helps in improving road safety and assists autonomous driving systems by recognizing signs in real-time."
        },
        {
            "title": "To-Do-List",
            "image": "images/To-do-list.png",
            "link": "https://github.com/dhananjay0911/To-Do-List",
            "details": "A user-friendly To-Do List application built with HTML, CSS, and JavaScript, enabling users to add, edit, and delete tasks. It features a clean interface to help manage daily tasks efficiently."
        },
        {
            "title": "Cracking-a-password-protected-PDF",
            "image": "images/pdf-password.avif",
            "link": "https://github.com/dhananjay0911/Cracking-a-password-protected-PDF",
            "details":"A Python project designed to crack password-protected PDF files using brute force or dictionary attacks. It utilizes libraries like PyPDF2 or pikepdf to test multiple password combinations and unlock secured PDF files."
        },

    ]
    return render(request, "projects.html", {"projects_show": projects_show})

def experience(request):
    experience=[
        {
            "company":"PROWORLD TECHNOLOGY PVT.LTD.",
            "role":"WEB AND SOFTWARE DEVELOPER",
            "link":"https://drive.google.com/file/d/1vRHyZrOkXcwFTBLDRQOI7aGOakWHCKHD/view?usp=drive_link",
            "img": "images/proworld.jpg",
            "details":"""
                
                **ProWorld Technology Pvt. Ltd. (Web and Software Developer)**

                **Location: Nashik, India**
                **Role & Contributions**:
                Built and styled an online bonafide certificate system using HTML, CSS, and JavaScript, reducing manual efforts by 50%.
                Integrated MySQL for real-time and efficient data management, ensuring accurate and customized certificate generation, reducing errors by 15%.
                Enhanced user experience by implementing form validation and dynamic previews, improving user engagement and minimizing input errors by 10%.
                **Learnings**:
                Improved skills in database integration and user experience design.
                Gained experience in building end-to-end web solutions with a focus on efficiency and user engagement.
                
                
            """,
        },
        {
            "company":"UNIFIED MENTOR PVT.LTD.",
            "role":"WEB DEVELOPER",
            "link":"https://drive.google.com/file/d/1KB6FV0Jvpqf3jexwzn7GVDXcw8bkSEEz/view?usp=drive_link",
            "img": "images/unifide.jpeg",
            "details":"""
                **Unified Mentor Pvt. Ltd. (Web Developer)**

                **Location**: Gurugram, India  
                **Role & Contributions**:
                - Developed a responsive clinic appointment website using React.js, CSS, and JavaScript, resulting in a 30% increase in online bookings.
                - Designed reusable React components to enhance scalability and reduce future development time by 40%.
                - Implemented SQL database solutions to improve data retrieval speed by 25%.
                - Applied responsive design principles to ensure compatibility across devices, leading to a 20% improvement in user satisfaction.
                **Learnings**:
                - Mastery in building responsive web applications and database optimization.
                - Experience with reusable component design and performance tuning in React.js.""",
        },

    ]
    return render(request,"experience.html",{"experience":experience})

def Certificate(request):
    Certificate=[
        {
            "title":"Java Certificate",
            "image":"images/javacert.jpg",
        },

        {
            "title":"Advance Java Certificate",
            "image":"images/java2.jpg",
        },

        {
            "title":"Python Certificate",
            "image":"images/Pythoncert.jpg",
        },

        {
            "title":"SQL Certificate",
            "image":"images/SQL.jpg",
        },

        {
            "title":"AWS Certificate",
            "image":"images/AWS.jpg",
        },

        {
            "title":"Cyber-Security Certificate",
            "image":"images/CyberSecurity.jpg",
        },

        {
            "title":"Android Development Certificate",
            "image":"images/AppDev.jpg",
        },
    ]
    return render(request,"Certificate.html",{"Certificate":Certificate})

def Contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            phone_no=form.cleaned_data['phone_no']
            message=form.cleaned_data['message']

            send_mail(
                f'Contact Form Submission from {name}',
                f'Name:{name}\nEmail:{email}\Phone:{phone_no}\Message:{message}',
                'fromdhananjaybamhande@gmail.com',
                [' dhananjaybamhande@gmail.com'],
                fail_silently=False,
            )
            messages.success(request,'Your message has been sent successfully!')
           # return redirect('contact')
    else:
        form=ContactForm()
   
    return render(request,"Contact.html",{'form':form})


def Resume(request):
    return render(request,"Resume.html")