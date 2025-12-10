from admin import Admin

holly = Admin('holly', 'norton', 'nortonh', 'hollynorton2003@gmail.com', 'texas','1234567890')
holly.describe_user()

eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
holly.privileges.privileges = eric_privileges

print(f"\nThe admin {holly.username} has these privileges: ")
holly.privileges.show_privileges()