import ast

with open("pynguin_output/test_program_under_test.py", 'r') as f:
    content = f.read()

tree = ast.parse(content)



def execute_expression(expression, variables_):
    code = compile(ast.Expression(expression), "<ast>", "eval")
    return eval(code, variables_)


for entry in tree.body:
    if not isinstance(entry, ast.FunctionDef):
        continue
    inputs = []
    node_set = ast.walk(entry)
    variables = {}
    for node in node_set:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name):
                var_name = target.id
                assigned_val = node.value
                if isinstance(assigned_val, ast.Call):
                    continue
                try:
                    var_value = execute_expression(node.value, variables)
                    variables[var_name] = var_value
                except Exception as e:
                    continue

        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == 'search':
                arguments = []
                for arg in node.args:
                    if isinstance(arg, ast.Name):
                        var_name = arg.id
                        if var_name in variables:
                            arguments.append(variables[var_name])
                        else:
                            continue
                    elif isinstance(arg, ast.Constant):
                        arguments.append(arg.value)
                inputs.append(arguments)
    print(inputs)
    print("-----------------------")

