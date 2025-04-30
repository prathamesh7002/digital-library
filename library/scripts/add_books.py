from library.models import Book

books = [
    {
        'title': 'Introduction to Compiler Design',
        'author': 'Torben Ægidius Mogensen',
        'subject': 'compiler_design',
        'description': 'A comprehensive guide to compiler design, covering lexical analysis, parsing, and code generation.'
    },
    {
        'title': 'Web Coding & Development All-in-One For Dummies',
        'author': 'Paul McFedries',
        'subject': 'web_programming',
        'description': 'An all-in-one guide covering HTML, CSS, JavaScript, and web development best practices.'
    },
    {
        'title': 'Data Structures and Algorithms in Python',
        'author': 'Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser',
        'subject': 'data_structure',
        'description': 'An introduction to data structures and algorithms using Python, with practical examples and exercises.'
    },
    {
        'title': 'Digital Techniques and Microprocessor Systems',
        'author': 'Ian Robertson Sinclair, Geoffrey E. Lewis',
        'subject': 'digital_technique',
        'description': 'A detailed study of digital techniques and microprocessor systems, including practical applications.'
    },
    {
        'title': 'Essential Computer Hardware: The Illustrated Guide',
        'author': 'Kevin Wilson',
        'subject': 'computer_hardware',
        'description': 'An illustrated guide to understanding the basics of computer hardware components and functions.'
    },
    {
        'title': 'Mechanics for Engineers: Statics',
        'author': 'Ferdinand P. Beer, E. Russell Johnston Jr.',
        'subject': 'mechanics',
        'description': 'A textbook on statics, providing a comprehensive introduction to mechanics for engineering students.'
    },
    {
        'title': 'Machine Learning Fundamentals: A Concise Introduction',
        'author': 'Hui Jiang',
        'subject': 'machine_learning',
        'description': 'An introduction to machine learning concepts, models, and applications, suitable for beginners.'
    },
    {
        'title': 'Python for Data Analysis',
        'author': 'Wes McKinney',
        'subject': 'data_analytics',
        'description': 'Learn data analysis using Python, with a focus on pandas, NumPy, and data visualization techniques.'
    },
    {
        'title': 'Software Engineering: A Practitioner\'s Approach',
        'author': 'Roger S. Pressman',
        'subject': 'software_engineering',
        'description': 'A guide to software engineering principles, methodologies, and best practices for practitioners.'
    },
    {
        'title': 'Mathematics 1',
        'author': 'Jenelle Motita, Jan Cherry San Juan, Leslie Pearl Castillo, Jam Sy',
        'subject': 'maths1',
        'description': 'Mathematics for first-year students, covering fundamental concepts and problem-solving techniques.'
    },
    {
        'title': 'Pure Mathematics 2',
        'author': 'L Bostock',
        'subject': 'maths2',
        'description': 'Advanced mathematics for second-year students, focusing on pure mathematics topics.'
    },
    {
        'title': 'Physics for Engineers and Scientists',
        'author': 'Hans Ohanian',
        'subject': 'physics',
        'description': 'Physics concepts for engineering students, with a focus on applications and problem-solving.'
    },
    {
        'title': 'Basic Chemistry',
        'author': 'Steven S. Zumdahl, Donald J. DeCoste',
        'subject': 'chemistry',
        'description': 'Basic concepts of chemistry, including atomic structure, bonding, and chemical reactions.'
    },
    {
        'title': 'Introduction to Artificial Intelligence',
        'author': 'Wolfgang Ertel',
        'subject': 'introduction_to_ai',
        'description': 'A beginner\'s guide to artificial intelligence, covering fundamental concepts and techniques.'
    },
    {
        'title': 'RDBMS In-Depth: Mastering SQL and PL/SQL Concepts',
        'author': 'Dr. Madhavi Vaidya',
        'subject': 'rdbms',
        'description': 'Learn relational database management systems, SQL, and PL/SQL concepts with practical examples.'
    },
    {
        'title': 'Computer Networking: A Top-Down Approach',
        'author': 'James F. Kurose, Keith W. Ross',
        'subject': 'computer_network',
        'description': 'An introduction to computer networks, covering protocols, architectures, and applications.'
    },
]

for book in books:
    Book.objects.create(**book)

print("Books added successfully!")