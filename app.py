from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config['DEBUG'] = True

title = 'About'

posts = [
    {
        'id': 1,
        'author': 'Ben McGregor',
        'title': 'Lorem 1',
        'content': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni similique earum expedita facilis    unde aspernatur rem alias praesentium nam exercitationem quis ex illum, dicta vero quia placeat labore, ad facere, et tenetur id laborum rerum quam. Adipisci possimus quisquam esse corrupti reiciendis?',
        'created_at': 'January 12, 2021'
    },
    {
        'id': 2,
        'author': 'Ewan Roberts',
        'title': 'Lorem 2',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum unde enim ipsam cumque? Repellendus, perspiciatis veniam at doloribus, officiis aut explicabo porro voluptatum numquam non minus inventore? Adipisci aliquid voluptas, repellat mollitia incidunt vitae exercitationem aut numquam amet magnam enim ex tenetur, molestias labore unde? Ipsum, perferendis inventore. Quasi, dignissimos.',
        'created_at': 'January 10, 2021'
    },
    {
        'id': 3,
        'author': 'Ben Marcus',
        'title': 'Lorem 3',
        'content': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni similique earum expedita facilis    unde aspernatur rem alias praesentium nam exercitationem quis ex illum, dicta vero quia placeat labore, ad facere, et tenetur id laborum rerum quam. Adipisci possimus quisquam esse corrupti',
        'created_at': 'January 8, 2021'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title=title)