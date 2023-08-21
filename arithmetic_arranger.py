def arithmetic_arranger(problems, val=False):
    equations = list()
    operators = list()
    first_operand = list()
    second_operand = list()
    sum_total = list()
    dashes = list()
    valid_operators = ["+", "-"]
    operators_correct = True
    integers_correct = True
    lenth_correct = True
    arranged_problems = str()

    for problem in problems:
        problem_split = problem.split()
        equations.append(problem_split)

        first_operand.append(problem_split[0])
        operators.append(problem_split[1])
        second_operand.append(problem_split[2])

        if (len(problem_split[0]) - len(problem_split[2])) >= 0:
            dashes.append("-" * (2 + (len(problem_split[0]))))
        else: 
            dashes.append("-" * (2 + (len(problem_split[2]))))
    
    all_operands = first_operand + second_operand

    for operator in operators:
        if operator not in valid_operators:
            operators_correct = False
            break

    for operand in all_operands:
        try:
            int(operand)
        except:
            integers_correct = False
            break

    for operand in all_operands:
        if len(operand) > 4:
            lenth_correct = False


    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
    elif operators_correct == False:
        arranged_problems = "Error: Operator must be '+' or '-'."
    elif integers_correct == False:
        arranged_problems = 'Error: Numbers must only contain digits.'
    elif lenth_correct == False:
        arranged_problems = 'Error: Numbers cannot be more than four digits.'
    else:
        for problem in problems:
            sum = eval(problem)
            sum_total.append(sum)

        top_indents = list()
        bottom_indents = list()
        for index in range(len(first_operand)):
            if len(first_operand[index]) > len(second_operand[index]):
                top_indents.append(2 + len(first_operand[index]))
                bottom_indents.append(1 + len(first_operand[index]))
            else:
                top_indents.append(2 + len(second_operand[index]))
                bottom_indents.append(1 + len(second_operand[index]))

        for index in range(len(first_operand)):
            if index == 0:
                arranged_problems = f"{(first_operand[index].rjust(top_indents[index]))}"
            else:
                arranged_problems += f"    {(first_operand[index].rjust(top_indents[index]))}"
        for index in range(len(first_operand)):
            if index == 0:
                arranged_problems += f"\n{operators[index]}{second_operand[index].rjust(bottom_indents[index])}"
            else:
                arranged_problems += f"    {operators[index]}{second_operand[index].rjust(bottom_indents[index])}"
        for index in range(len(first_operand)):
            if index == 0:
                arranged_problems += f"\n{dashes[index]}"
            else:
                arranged_problems += f"    {dashes[index]}"
        if val:
            for index in range(len(first_operand)):
                if index == 0:
                    arranged_problems += f"\n{str(sum_total[index]).rjust(top_indents[index])}"
                else:
                    arranged_problems += f"    {str(sum_total[index]).rjust(top_indents[index])}"


    return arranged_problems