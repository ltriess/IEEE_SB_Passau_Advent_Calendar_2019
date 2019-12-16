#!/usr/bin/env python3

import sys

DEBUG = True


def main():

    if DEBUG:
        sys.stdin = open("samples/11_input.txt")

    """
    <Transition> := <Id>' --{'<Operation>'}-> '<Id>
    <Operation> := <Noop>|<Read>|<Assignment>|<Condition>|<Assertion>
    <Noop> := ''
    <Read> := <Variable>' := *;'
    <Assignment> := <Variable>' := '<Expression>';'
    <Condition> := '['<Expression>']'
    <Assertion> := 'assert '<Expression>';'
    <Variable> := [a-zA-Z][a-zA-Z0-9]*
    <Expression> := <Literal>|<Variable>|<Negation>|<BinaryExpression>|'('<Expression>')'
    <Literal> := '0'|'1'
    <Negation> := '!'<Expression>
    <BinaryExpression> := <Or>|<And>|Xor
    <Or> := <Expression>' | '<Expression>
    <And> := <Expression>' & '<Expression>
    <Xor> := <Expression>' ^ '<Expression>
    """

    cft = int(input())
    for _ in range(cft):
        line = input()

        cfs_pre = int(line.split(" --")[0])
        cfs_post = int(line.split("-> ")[-1])

        expr = line.split("{")[1].split("}")[0]

        print(cfs_pre, "-", expr, "-", cfs_post)

    entry = int(input())
    print("Start: {0}".format(entry))

    raise NotImplementedError


if __name__ == "__main__":
    main()
