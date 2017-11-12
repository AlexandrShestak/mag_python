# -*- coding: utf-8 -*-

priority = {"**": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1, ")": 1}
operators = {"*", "/", "+", "-", "(", ")", "**"}


def reverse_polish_notation(expression):
    """Algorithm from https://ru.wikipedia.org/wiki/Обратная_польская_запись"""
    expression = expression.replace(" ", "").replace(",", ".")
    polish_notation = []
    operations_stack = []
    iteration = 0
    while iteration < expression.__len__():
        if expression[iteration] in operators:
            if expression[iteration] == '(':
                operations_stack.append(expression[iteration])
            elif expression[iteration] == ')':
                while operations_stack and operations_stack[-1] != '(':
                    polish_notation.append(operations_stack.pop())
                operations_stack.pop()
            elif expression[iteration] == "*" \
                    and (iteration + 1 != expression.__len__() and expression[iteration + 1] == "*"):
                iteration += 1
                operations_stack.append("**")
            elif expression[iteration] == '-' \
                    and ((iteration - 1 > 0 and expression[iteration - 1] in operators) or iteration == 0):
                number = expression[iteration]
                iteration += 1
                number += expression[iteration]
                while expression[iteration] not in operators \
                        and (iteration + 1 != expression.__len__() and expression[iteration + 1] not in operators):
                    iteration += 1
                    number += expression[iteration]
                polish_notation.append(number)
            elif operations_stack:
                while operations_stack and priority[expression[iteration]] <= priority[operations_stack[-1]]:
                    polish_notation.append(operations_stack.pop())
                operations_stack.append(expression[iteration])
            else:
                operations_stack.append(expression[iteration])
        else:
            number = expression[iteration]
            while expression[iteration] not in operators \
                    and (iteration + 1 != expression.__len__() and expression[iteration + 1] not in operators):
                iteration += 1
                number += expression[iteration]
            polish_notation.append(number)
        iteration += 1

    while operations_stack:
        polish_notation.append(operations_stack.pop())
    return polish_notation


def evaluate_reverse_polish_notation(expression):
    stack = []
    for elem in expression:
        if elem not in operators:
            stack.append(elem)
        else:
            operand1 = float(stack.pop())
            operand2 = float(stack.pop())
            if elem == "+":
                stack.append(operand1 + operand2)
            elif elem == "-":
                stack.append(operand2 - operand1)
            elif elem == "/":
                stack.append(operand2 / operand1)
            elif elem == "*":
                stack.append(operand1 * operand2)
            elif elem == "**":
                stack.append(operand2 ** operand1)
            else:
                raise Exception('Unsupported operation (%s)' % elem)

    return stack.pop()


if __name__ == '__main__':
    while True:
        expression = raw_input("Enter expression: ")
        print evaluate_reverse_polish_notation(reverse_polish_notation(expression))
