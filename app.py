from flask import Flask,render_template

app = Flask(__name__)

COURSES=[
{
    'id':1,
    'title':'Data Science',
    'description':'Master the fundamentals of data science with our online course. Learn data analysis, machine learning, and statistical modeling using Python, R, and SQL. Perfect for beginners and professionals, this course offers video lectures and hands-on projects to build practical skills for a successful career in data science.'  
},
{
    'id':2,
    'title':'Full Stack Developar',
    'description':'Become a versatile Full Stack Developer with our in-depth course. Learn to build dynamic web applications from front to back using HTML, CSS, JavaScript, and popular frameworks like React and Node.js. Gain hands-on experience with databases, APIs, and deployment. Ideal for beginners and professionals looking to enhance their skills, this course prepares you for a thriving career in web development.'
},
{
    'id':3,
    'title':'Devops',
    'description':'Accelerate your career with our DevOps course. Learn essential tools and practices like CI/CD, automation, containerization with Docker, and orchestration with Kubernetes. Gain hands-on experience in bridging the gap between development and operations, ensuring efficient and reliable software delivery. Perfect for IT professionals and developers aiming to enhance their skills and streamline workflows.'
},
{
    'id':4,
    'title':'Web 3.0',
    'description':'Dive into the future of the internet with our Web 3.0 course. Explore blockchain technology, decentralized applications (dApps), and smart contracts. Gain hands-on experience with Ethereum, Solidity, and Web3.js. Ideal for developers and tech enthusiasts looking to advance their skills in the next generation of web technologies.'  
}
]

@app.route("/")
def hello_world():
    return render_template("home.html",courses=COURSES)

if(__name__)=="__main__":
    app.run(host="0.0.0.0", debug=True)