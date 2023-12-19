code = '''
answer = 42
'''

context = {}
exec(code, context)

print(context['answer'])
