from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'Sachin': 'Sachin Ramesh Tendulkar is widely regarded as one of the greatest cricketers in the history of the game. He is often called the "God of Cricket" due to his extraordinary achievements and consistency over a 24-year international career.\n\nHe made his debut at just 16 years old and went on to become the highest run-scorer in both Test and ODI formats. He is the only player to score 100 international centuries.\n\nOne of the most emotional moments of his career was winning the 2011 Cricket World Cup. He retired in 2013, leaving behind a legacy that continues to inspire generations.',

        'Bumrah': 'Jasprit Bumrah is one of the most dangerous fast bowlers in modern cricket. Known for his unique action and pinpoint accuracy, he has become the backbone of India\'s bowling attack.\n\nHe specializes in yorkers, slower balls, and death over bowling, making him extremely difficult to score against.\n\nBumrah has delivered match-winning performances in all formats and is especially impactful in high-pressure situations like ICC tournaments and IPL.',

        'Rohit': 'Rohit Sharma, also known as the "Hitman", is one of the most stylish and destructive batsmen in cricket. He is currently the captain of the Indian cricket team.\n\nHe holds multiple records, including the highest individual score in ODI cricket (264 runs) and multiple double centuries.\n\nRohit is known for his effortless timing and ability to convert starts into big scores, making him one of the most dangerous openers in the world.',

        'Virat': 'Virat Kohli is one of the finest batsmen of the modern era and a former captain of India. He is known for his aggressive mindset, fitness, and consistency across all formats.\n\nKohli is often called the "King of Chase" because of his exceptional ability to perform under pressure while chasing targets.\n\nHe has scored numerous centuries and broken multiple records, making him one of the most celebrated cricketers globally.',

        'Rahul': 'KL Rahul is a technically sound and versatile batsman who can adapt to different roles in the team. He can open the innings, play in the middle order, and also serve as a wicketkeeper.\n\nHe is known for his elegant stroke play and calm temperament.\n\nRahul has played many crucial innings for India and continues to be an important part of the squad across formats.',

        'Rishabh': 'Rishabh Pant is an aggressive and fearless wicketkeeper-batsman known for his attacking style of play. He has changed the way modern wicketkeeper-batsmen approach the game.\n\nPant has delivered several match-winning performances, especially in Test cricket, including historic innings in overseas conditions.\n\nHis ability to take on bowlers and turn games around makes him a valuable player for India.',

        'Dhoni': 'MS Dhoni ".',
        "emp":{
            "ename":"Hemanth",
            "sal":50000
        }
    }

    return render(request, 'index.html', context)


# Here we will be Seeing Howw To Take Input From he User

def Sum_OF_TWO(request,a,b,):
    context={
        'a':a,
        'b':b,
        'c':a+b,
        
    }
    return render(request,'sample2.html',context)


def Even_Or_Not(request,H):
    context={
        'H':H
    }
    return render(request,'sample3.html',context)

#  Here we will Create The Function
def Check_Upper(request,n):
    context={
        'n':n
    }
    return render(request,'sample4.html',context)

def Even_Or_Odd(request,Number):
    context={
        'Number':Number
    }
    return render(request,'sample5.html',context)

def Leap_Year(request,n):
    context={
        'n':n
    }
    return render(request,'sample6.html',context)

def Data(request):
    Emp_Data=[
        {
          'empno':1234,
          'ename':"Hemanth",
          'job':'Clerk'  
            },
        {
            
          'empno':12345,
          'ename':"Rakesh",
          'job':'Manager' },
        {
            
          'empno':123456,
          'ename':"Chandru",
          'job':'Developer' },
        {
            
          'empno':1234567,
          'ename':"Harish",
          'job':'Tester' 
        }
    ]
    context={'employees': Emp_Data}
    return render(request,'Table.html',context)

file=open(r'C:\Users\Heman\OneDrive\Desktop\Django\Templates\captain','r')
json_Data=file.read()
file.close()
import json
py_data=json.loads(json_Data)

def all_recipes(request):
    context={
        'recipes':py_data['recipes']
    }
    
    return render(request,'recipes.html',context)



# def one_Product(request, id):
#     context = {
#         'product': product[id-1]
#     }

# 👉 This is the key idea:

# You already have:

# product = [item1, item2, item3...]

# Now user gives:

# id = 1

# You do:

# product[id-1] → product[0]

# 👉 That gives:

# {"name": "Pizza"}

# product = py_data['recipes']
# means:

# “Extract the list from the dictionary so I can use it easily.”

product=py_data['recipes']
def one_Product(request,id):
    context={
        'product':product[id-1]
    }
    return render(request,'one_Product',context)