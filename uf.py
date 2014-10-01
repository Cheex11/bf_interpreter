import sys

program = open(sys.argv[1]).read()
memory_cursor = 0
ip = 0
main_memory = [0,0,0,0,0,0,0,0,0,0]

while ip < len(program):
    cmd_char = program[ip]
    ip += 1

    if cmd_char == '>':
        memory_cursor += 1
        print memory_cursor
    elif cmd_char == "<":
        memory_cursor -= 1
    elif cmd_char == "+":
        main_memory[memory_cursor] += 1
    elif cmd_char == "-":
        main_memory[memory_cursor] -= 1
    elif cmd_char == ".":
        print chr(main_memory[memory_cursor])
    elif cmd_char == ",":
        main_memory[memory_cursor] = STDIN.getc
    elif cmd_char == "[":
        if main_memory[memory_cursor] == 0:
            count = 0
            while count == 0 and program[ip] == "]":
                if program[ip] == "[":
                    count += 1
                elif program[ip] == "]":
                    count -= 1
                ip += 1
            ip += 1
    elif cmd_char == "]":
        if main_memory[memory_cursor] != 0:
            count = 0
            ip -= 2
        while count == 0 and program[ip] == "[":
            if program[ip] == "]":
                count += 1
            elif program[ip] == "[":
                count -= 1
            ip -= 1
        ip += 1
    print main_memory
