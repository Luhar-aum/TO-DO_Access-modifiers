# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Task Dashboard</title>
# </head>
# <body>
#     <h1>Task Dashboard</h1>

#     <h2>Public Tasks</h2>
#     <ul>
#         {% for task in public_tasks %}
#             <li>{{ task.title }} - {{ task.due_date }}</li>
#         {% empty %}
#             <p>No public tasks available.</p>
#         {% endfor %}
#     </ul>

#     <h2>Private Tasks</h2>
#     <ul>
#         {% for task in private_tasks %}
#             <li>{{ task.title }} - {{ task.due_date }}</li>
#         {% empty %}
#             <p>No private tasks available.</p>
#         {% endfor %}
#     </ul>

#     <h2>Protected Tasks</h2>
#     <ul>
#         {% for task in protected_tasks %}
#             <li>{{ task.title }} - {{ task.due_date }}</li>
#         {% empty %}
#             <p>No protected tasks available.</p>
#         {% endfor %}
#     </ul>
# </body>
# </html>
