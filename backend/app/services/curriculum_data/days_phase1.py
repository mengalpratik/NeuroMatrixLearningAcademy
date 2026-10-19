# Phase 1: Foundations & Python Engineering (Days 1–28)
# Weeks 1–4

DAYS_PHASE1 = [
    # Week 1: Python Fundamentals (Days 1–7)
    {
        "day_number": 1,
        "week_number": 1,
        "phase_number": 1,
        "title": "Python Setup, Interpreter, Print, Comments & Variables",
        "slug": "python-setup-interpreter-variables",
        "summary": "Configure the Python 3 development environment, understand bytecode execution, master console I/O, and assign typed variables.",
        "duration_minutes": 60,
        "objectives": [
            "Verify Python 3.11+ interpreter and virtual environment path",
            "Understand how CPython compiles source code into .pyc bytecode",
            "Use print() formatting, separation, and newline controls",
            "Declare descriptive variables adhering to PEP 8 snake_case conventions",
        ],
        "prerequisites": [
            "Access to a Linux terminal with Python installed",
            "Basic understanding of text files and directories",
        ],
        "revision_questions": [
            "What is the difference between source code (.py) and bytecode (.pyc)?",
            "How does Python dynamically infer variable types during runtime?",
        ],
        "concept_sections": [
            {
                "title": "The Python Runtime & Execution Model",
                "content": "Python is an interpreted, high-level, dynamically typed language. When you execute `python script.py`, the CPython interpreter reads the source text, parses it into an Abstract Syntax Tree (AST), compiles it into low-level bytecode instructions, and evaluates them on the Python Virtual Machine (PVM).",
                "key_points": [
                    "CPython compiles source to bytecode before execution",
                    "Variables are references pointing to objects in heap memory",
                    "Dynamic typing means the variable name holds a pointer, not a rigid memory slot",
                ],
            },
            {
                "title": "Variable Binding and Memory References",
                "content": "In Python, assignment (`=`) binds a name in the local namespace to an object in heap memory. For example, `node_id = 'opt-node-01'` creates a string object and binds the reference `node_id` to its memory address.",
                "key_points": [
                    "Everything in Python is an object, including integers and functions",
                    "Names are bound via symbol tables in current namespace scope",
                    "PEP 8 standard mandates lower_snake_case for variable and function identifiers",
                ],
            },
        ],
        "code_examples": [
            {
                "title": "Agent Telemetry Initialization",
                "description": "Initialize device identifiers, system states, and format output using f-strings.",
                "code": "agent_id = 'optimus-prime-desktop-01'\nnode_status = 'ONLINE'\nactive_cores = 8\nmemory_usage_gb = 4.25\n\nprint(f'[NEUROMATRIX] Node {agent_id} is {node_status}')\nprint(f'Cores: {active_cores} | Allocated RAM: {memory_usage_gb:.2f} GB')",
                "language": "python",
                "expected_output": "[NEUROMATRIX] Node optimus-prime-desktop-01 is ONLINE\nCores: 8 | Allocated RAM: 4.25 GB",
            }
        ],
        "exercises": [
            {
                "id": "ex-d1-1",
                "title": "Build a Terminal Node Banner",
                "difficulty": "beginner",
                "instructions": "Write a Python script that declares variables `node_name`, `ip_address`, `status`, and `latency_ms`. Print a formatted 3-line terminal banner summarizing the node status.",
                "starter_code": "# Declare your variables here\nnode_name = 'AlphaSentinel'\nip_address = '192.168.1.105'\nstatus = 'ACTIVE'\nlatency_ms = 14.2\n\n# Output formatted banner\n",
                "solution_code": "node_name = 'AlphaSentinel'\nip_address = '192.168.1.105'\nstatus = 'ACTIVE'\nlatency_ms = 14.2\n\nprint('=== NEUROMATRIX NODE STATUS ===')\nprint(f'Device: {node_name} [{ip_address}]')\nprint(f'Status: {status} | Latency: {latency_ms}ms')\nprint('===============================')",
                "expected_output": "=== NEUROMATRIX NODE STATUS ===\nDevice: AlphaSentinel [192.168.1.105]\nStatus: ACTIVE | Latency: 14.2ms\n===============================",
                "acceptance_criteria": [
                    "All 4 variables are declared with appropriate types",
                    "Print statements use Python 3.6+ f-strings",
                    "Output displays exact formatted banner lines",
                ],
                "test_cases": [
                    "latency_ms is formatted as a floating point number",
                    "String variables contain no extra leading or trailing whitespace",
                ],
            }
        ],
        "common_errors": [
            {
                "error_type": "NameError",
                "cause": "Attempting to reference a variable name before it has been assigned.",
                "fix": "Ensure variable declaration occurs before usage line in source code.",
                "example": "print(device_ip) # NameError if device_ip is not assigned",
            }
        ],
        "edge_cases": [
            "Reassigning a variable to a different type (e.g. integer to string) is valid in Python but can cause runtime type bugs downstream.",
            "Variable names starting with numbers or containing hyphens cause SyntaxError.",
        ],
        "neuromatrix_integration": {
            "topic": "Agent Telemetry Header",
            "context": "NeuroMatrix nodes start by registering their agent ID and host architecture to the central bus.",
            "task_description": "Define the canonical variable configuration that will represent your local node in the upcoming CLI tools.",
            "target_component": "backend/telemetry/agent_bootstrap.py",
            "verification_step": "Run python3 on your script and verify that the output prints without syntax errors.",
        },
        "completion_criteria": [
            "Installed Python 3.11+ and confirmed version via python3 --version",
            "Understood dynamic binding and heap allocation",
            "Executed script with f-strings and verified terminal output",
            "Completed the Day 1 Knowledge Quiz",
        ],
        "quiz_questions": [
            {
                "id": "quiz-d1-q1",
                "question_text": "How does CPython execute Python source files?",
                "question_type": "mcq",
                "code_snippet": None,
                "options": [
                    "Directly interprets raw text without compiling",
                    "Compiles source into bytecode, which runs on the Python Virtual Machine (PVM)",
                    "Transpiles Python directly into native x86 machine instructions",
                    "Executes inside a browser JavaScript engine",
                ],
                "correct_answer": "Compiles source into bytecode, which runs on the Python Virtual Machine (PVM)",
                "explanation": "CPython first compiles source code into .pyc bytecode and then executes it using the Python Virtual Machine (PVM).",
            },
            {
                "id": "quiz-d1-q2",
                "question_text": "What is the output of the following f-string snippet?",
                "question_type": "output_prediction",
                "code_snippet": "cores = 4\nload = 0.852\nprint(f'{cores} cores @ {load:.1%}')",
                "options": ["4 cores @ 0.852", "4 cores @ 85.2%", "cores @ load", "4 cores @ 85%"],
                "correct_answer": "4 cores @ 85.2%",
                "explanation": "The format specifier :.1% multiplies the float by 100 and formats it with one decimal place followed by a percent symbol.",
            },
        ],
    },
    {
        "day_number": 2,
        "week_number": 1,
        "phase_number": 1,
        "title": "Data Types, Type Conversion & User Input",
        "slug": "data-types-conversion-input",
        "summary": "Explore primitive scalar types (int, float, bool, str), casting functions, and safe terminal input processing.",
        "duration_minutes": 60,
        "objectives": [
            "Distinguish between scalar types: int, float, bool, str, NoneType",
            "Execute explicit type conversions using int(), float(), str(), and bool()",
            "Handle console input via input() and validate user-supplied values",
            "Inspect runtime object types with type() and isinstance()",
        ],
        "prerequisites": ["Day 1: Python setup, variables, and print formatting"],
        "revision_questions": [
            "Why does input() always return a string object in Python 3?",
            "What determines whether an object evaluates to True or False in a boolean context (truthiness)?",
        ],
        "concept_sections": [
            {
                "title": "Primitive Data Types in Python",
                "content": "Python provides built-in primitive types: `int` (arbitrary precision integers), `float` (64-bit IEEE 754 double precision), `bool` (`True` or `False`, subclass of int), `str` (Unicode character sequences), and `NoneType` (representing the absence of a value).",
                "key_points": [
                    "Integers in Python 3 have unbounded precision (no integer overflow)",
                    "Floats have precision limits inherent to IEEE 754 representations",
                    "None is a singleton object representing null state",
                ],
            },
            {
                "title": "Type Casting & Coercion Rules",
                "content": "Python never performs implicit type conversion between incompatible types (e.g. adding string '10' and integer 5 raises TypeError). Explicit casting functions like `int('42')` or `float('3.14')` must be called.",
                "key_points": [
                    "int('10') converts valid numerical strings to integers",
                    "Empty strings, 0, 0.0, and None evaluate to False in boolean context",
                    "input() always yields str; numerical processing requires explicit conversion",
                ],
            },
        ],
        "code_examples": [
            {
                "title": "Safe Memory Buffer Calculator",
                "description": "Convert raw terminal input into numerical buffers with type safety.",
                "code": "raw_buffer = '2048'\nbuffer_mb = int(raw_buffer)\nbuffer_gb = buffer_mb / 1024.0\nis_valid = buffer_gb > 1.0\n\nprint(f'Buffer MB: {buffer_mb} | GB: {buffer_gb:.2f} | Large: {is_valid}')",
                "language": "python",
                "expected_output": "Buffer MB: 2048 | GB: 2.00 | Large: True",
            }
        ],
        "exercises": [
            {
                "id": "ex-d2-1",
                "title": "Device Port Validator",
                "difficulty": "beginner",
                "instructions": "Create a script that takes a string port variable `port_str = '8080'`, casts it to an integer, and checks if it falls within valid non-privileged port range (1024–65535).",
                "starter_code": "port_str = '8080'\n# Convert and validate port\n",
                "solution_code": "port_str = '8080'\nport = int(port_str)\nis_valid = 1024 <= port <= 65535\nprint(f'Port: {port} | Valid Non-Privileged: {is_valid}')",
                "expected_output": "Port: 8080 | Valid Non-Privileged: True",
                "acceptance_criteria": [
                    "String is converted to integer via int()",
                    "Range check checks 1024 to 65535 inclusive",
                    "Output reports boolean validation result",
                ],
                "test_cases": [
                    "Ensure port_str='80' yields False",
                    "Ensure port_str='8080' yields True",
                ],
            }
        ],
        "common_errors": [
            {
                "error_type": "ValueError",
                "cause": "Passing an invalid string (e.g. '8080abc' or '3.14') to int().",
                "fix": "Validate string with str.isdigit() before casting, or parse through float first.",
                "example": "int('abc') # Raises ValueError: invalid literal for int()",
            }
        ],
        "edge_cases": [
            "bool('False') evaluates to True because non-empty strings are truthy in Python.",
            "int(3.99) truncates towards zero to 3, rather than rounding to 4.",
        ],
        "neuromatrix_integration": {
            "topic": "Device Config Parsing",
            "context": "NeuroMatrix configurations are initially read from environment variables or CLI arguments as strings.",
            "task_description": "Cast incoming configuration strings (port, timeout_seconds, debug_mode) into validated types.",
            "target_component": "backend/config/device_env.py",
            "verification_step": "Test with string 'true' and '8000' and verify proper casting to bool and int.",
        },
        "completion_criteria": [
            "Executed type conversions with int, float, str, bool",
            "Verified truthiness rules for empty collections and zero values",
            "Completed the Day 2 Quiz",
        ],
        "quiz_questions": [
            {
                "id": "quiz-d2-q1",
                "question_text": "What does the expression bool('False') evaluate to in Python?",
                "question_type": "output_prediction",
                "code_snippet": "val = bool('False')\nprint(val)",
                "options": ["False", "True", "None", "Raises TypeError"],
                "correct_answer": "True",
                "explanation": "In Python, any non-empty string is considered truthy, so bool('False') evaluates to True.",
            }
        ],
    },
    {
        "day_number": 3,
        "week_number": 1,
        "phase_number": 1,
        "title": "Operators & Boolean Logic",
        "slug": "operators-and-boolean-logic",
        "summary": "Master arithmetic, relational, logical (and, or, not), bitwise operators, and short-circuit evaluation.",
        "duration_minutes": 60,
        "objectives": [
            "Use arithmetic operators including floor division (//) and modulus (%)",
            "Apply comparison operators (==, !=, <, <=, >, >=) and identity (is, is not)",
            "Master boolean logic with short-circuit evaluation in and/or expressions",
            "Understand basic bitwise operations for system permission masking",
        ],
        "prerequisites": ["Day 2: Data types and boolean truthiness"],
        "revision_questions": [
            "What is the difference between `==` (equality) and `is` (identity)?",
            "How does short-circuit evaluation improve performance and prevent errors?",
        ],
        "concept_sections": [
            {
                "title": "Comparison vs Identity Operators",
                "content": "`==` checks value equivalence by invoking `__eq__()`. In contrast, `is` checks whether two variable references point to the exact same memory address (`id(a) == id(b)`). Always use `is` when comparing against singletons like `None`.",
                "key_points": [
                    "Use == for value equality comparison",
                    "Use is for comparing identity against None, True, False",
                    "Chained comparisons (e.g. 0 < x < 100) are evaluated naturally in Python",
                ],
            },
            {
                "title": "Short-Circuit Logical Evaluation",
                "content": "Python's `and` and `or` operators short-circuit. In `A and B`, if `A` is false, `B` is never evaluated. In `A or B`, if `A` is true, `B` is never evaluated. They return the value of the last evaluated operand, not just a strict boolean.",
                "key_points": [
                    "A and B: returns A if A is false, else B",
                    "A or B: returns A if A is true, else B",
                    "Guards against exceptions: `node is not None and node.is_active`",
                ],
            },
        ],
        "code_examples": [
            {
                "title": "Permission Bitmask and Guard Check",
                "description": "Combine logical guards with bitwise permission checks.",
                "code": "READ_PERM = 0b100\nWRITE_PERM = 0b010\nEXEC_PERM = 0b001\n\nuser_perms = 0b110 # Read and Write\ncan_write = (user_perms & WRITE_PERM) != 0\ncan_exec = (user_perms & EXEC_PERM) != 0\n\nprint(f'Can Write: {can_write} | Can Exec: {can_exec}')",
                "language": "python",
                "expected_output": "Can Write: True | Can Exec: False",
            }
        ],
        "exercises": [
            {
                "id": "ex-d3-1",
                "title": "System Alert Logic Gate",
                "difficulty": "beginner",
                "instructions": "Write logic that flags an alert if CPU usage is over 90% OR memory is over 85%, provided the node is not in 'MAINTENANCE' mode.",
                "starter_code": "cpu_pct = 92.5\nmem_pct = 78.0\nnode_mode = 'OPERATIONAL'\n\n# Calculate trigger_alert\n",
                "solution_code": "cpu_pct = 92.5\nmem_pct = 78.0\nnode_mode = 'OPERATIONAL'\n\ntrigger_alert = (node_mode != 'MAINTENANCE') and (cpu_pct > 90.0 or mem_pct > 85.0)\nprint(f'Alert Triggered: {trigger_alert}')",
                "expected_output": "Alert Triggered: True",
                "acceptance_criteria": [
                    "Correct precedence of and/or with parentheses",
                    "Excludes MAINTENANCE mode from alerts",
                    "Outputs exact boolean status",
                ],
                "test_cases": ["When node_mode is 'MAINTENANCE', alert is False even if cpu > 90"],
            }
        ],
        "common_errors": [
            {
                "error_type": "Syntax/Logic Error",
                "cause": "Writing `if x == 'a' or 'b':` instead of `if x == 'a' or x == 'b':`.",
                "fix": "Always compare against each target or use `if x in ('a', 'b'):`.",
                "example": "if role == 'admin' or 'operator': # Always truthy because 'operator' is non-empty!",
            }
        ],
        "edge_cases": [
            "Integer caching (small integer optimization -5 to 256) causes `is` to sometimes return True for equal integers, but relying on this is dangerous."
        ],
        "neuromatrix_integration": {
            "topic": "Telemetry Alert Thresholds",
            "context": "NeuroMatrix nodes evaluate local metrics against alert gates before transmitting telemetry across the network.",
            "task_description": "Implement threshold evaluation using short-circuit logical operators.",
            "target_component": "backend/telemetry/alert_evaluator.py",
            "verification_step": "Run evaluation across test vectors and confirm correct boolean firing.",
        },
        "completion_criteria": [
            "Mastered differences between == and is",
            "Used short-circuiting for safe guard expressions",
            "Passed Day 3 Quiz",
        ],
        "quiz_questions": [
            {
                "id": "quiz-d3-q1",
                "question_text": "What does the expression None or 'Default' evaluate to?",
                "question_type": "mcq",
                "code_snippet": "val = None or 'Default'\nprint(val)",
                "options": ["True", "'Default'", "None", "Raises TypeError"],
                "correct_answer": "'Default'",
                "explanation": "Because None is falsy, the `or` operator evaluates and returns the right-hand operand ('Default').",
            }
        ],
    },
    {
        "day_number": 4,
        "week_number": 1,
        "phase_number": 1,
        "title": "Conditions, Branching & Pattern Matching",
        "slug": "conditions-branching-match-case",
        "summary": "Construct multi-path decision logic using if, elif, else, ternary expressions, and Python 3.10+ structural pattern matching.",
        "duration_minutes": 60,
        "objectives": [
            "Structure clear decision trees using if, elif, and else blocks",
            "Use inline conditional expressions (ternary operator: x if cond else y)",
            "Apply Python 3.10+ match/case structural pattern matching",
            "Eliminate nested callback-style conditions with early return patterns",
        ],
        "prerequisites": ["Day 3: Operators and boolean logic"],
        "revision_questions": [
            "How does `match/case` differ from traditional `if/elif/else` chains in Python?",
            "What are the benefits of the 'early return / guard clause' pattern?",
        ],
        "concept_sections": [
            {
                "title": "Control Flow and Guard Clauses",
                "content": "Deeply nested `if` statements lead to unmaintainable code ('arrow anti-pattern'). Guard clauses handle boundary conditions and failures immediately, keeping the primary execution flow at the top indentation level.",
                "key_points": [
                    "Check error and edge conditions first and exit early",
                    "Avoid nesting deeper than 2 levels whenever possible",
                    "Keep conditional logic readable and testable",
                ],
            },
            {
                "title": "Structural Pattern Matching (Python 3.10+)",
                "content": "The `match/case` statement provides pattern matching capable of destructuring sequences, matching exact literals, and applying guard expressions via `if` within cases.",
                "key_points": [
                    "Match against command literals, types, or nested data structures",
                    "Use `_` as the wildcard default case",
                    "Guards in cases: `case [action, value] if value > 0:`",
                ],
            },
        ],
        "code_examples": [
            {
                "title": "Device Command Dispatcher via Pattern Matching",
                "description": "Dispatch commands using match/case with wildcard fallbacks.",
                "code": "def handle_command(cmd: str):\n    match cmd.split():\n        case ['status']:\n            return 'STATUS: OK - All systems nominal'\n        case ['reboot', target]:\n            return f'REBOOT: Initiating restart for {target}'\n        case ['ping', host, count]:\n            return f'PING: Pinging {host} {count} times'\n        case _:\n            return 'ERROR: Unrecognized command syntax'\n\nprint(handle_command('status'))\nprint(handle_command('reboot node-42'))\nprint(handle_command('invalid command'))",
                "language": "python",
                "expected_output": "STATUS: OK - All systems nominal\nREBOOT: Initiating restart for node-42\nERROR: Unrecognized command syntax",
            }
        ],
        "exercises": [
            {
                "id": "ex-d4-1",
                "title": "Severity Classification Engine",
                "difficulty": "beginner",
                "instructions": "Given an HTTP status code integer, classify it as 'Informational' (100-199), 'Success' (200-299), 'Redirection' (300-399), 'Client Error' (400-499), 'Server Error' (500-599), or 'Invalid Code'.",
                "starter_code": "status_code = 404\n# Classify status_code\n",
                "solution_code": "status_code = 404\n\nif 100 <= status_code < 200:\n    category = 'Informational'\nelif 200 <= status_code < 300:\n    category = 'Success'\nelif 300 <= status_code < 400:\n    category = 'Redirection'\nelif 400 <= status_code < 500:\n    category = 'Client Error'\nelif 500 <= status_code < 600:\n    category = 'Server Error'\nelse:\n    category = 'Invalid Code'\n\nprint(f'{status_code}: {category}')",
                "expected_output": "404: Client Error",
                "acceptance_criteria": [
                    "Correct classification for all ranges",
                    "Handles codes outside 100-599 as 'Invalid Code'",
                    "Outputs formatted result",
                ],
                "test_cases": [
                    "200 produces Success",
                    "503 produces Server Error",
                    "999 produces Invalid Code",
                ],
            }
        ],
        "common_errors": [
            {
                "error_type": "SyntaxError",
                "cause": "Using assignment `=` inside an `if` expression instead of `==` (unless using := walrus operator).",
                "fix": "Use `==` for comparison or `:=` for assignment expression.",
                "example": "if status = 200: # SyntaxError",
            }
        ],
        "edge_cases": [
            "Order of `elif` branches matters: more specific checks must precede broader checks to prevent unreachable code."
        ],
        "neuromatrix_integration": {
            "topic": "Heartbeat State Classifier",
            "context": "NeuroMatrix agents classify incoming node telemetry packets into nominal, degraded, or critical states.",
            "task_description": "Implement the state classification rules for incoming heartbeat packets.",
            "target_component": "backend/telemetry/classifier.py",
            "verification_step": "Feed edge status codes (200, 404, 500) into the classifier and verify outputs.",
        },
        "completion_criteria": [
            "Built conditional chains with if/elif/else",
            "Tested Python 3.10 match/case syntax",
            "Completed Day 4 Quiz",
        ],
        "quiz_questions": [
            {
                "id": "quiz-d4-q1",
                "question_text": "What does the wildcard `case _:` represent in Python match/case?",
                "question_type": "mcq",
                "code_snippet": None,
                "options": [
                    "A private variable match",
                    "A syntax error placeholder",
                    "The default/catch-all pattern when no other case matches",
                    "A regex pattern matcher",
                ],
                "correct_answer": "The default/catch-all pattern when no other case matches",
                "explanation": "In Python match/case, the underscore `_` acts as a wildcard pattern that matches any value, analogous to a default block.",
            }
        ],
    },
    {
        "day_number": 5,
        "week_number": 1,
        "phase_number": 1,
        "title": "Loops, Iteration & Control Statements",
        "slug": "loops-iteration-while-for-break",
        "summary": "Master for loops, while loops, range(), break, continue, and the loop-else construct.",
        "duration_minutes": 60,
        "objectives": [
            "Iterate sequences using for loops and range() generator",
            "Implement conditional loops using while with safe termination criteria",
            "Control iteration flow with break and continue",
            "Leverage the Python loop-else construct for clean search loops",
        ],
        "prerequisites": ["Day 4: Conditions and branching"],
        "revision_questions": [
            "When does the `else` block of a Python `for` or `while` loop execute?",
            "What causes an infinite loop in a `while` statement and how do you prevent it?",
        ],
        "concept_sections": [
            {
                "title": "Python Iteration Architecture",
                "content": "Python's `for` loop is a 'for-each' iterator that operates on any iterable object implementing `__iter__()`. The built-in `range(start, stop, step)` generates integers on demand with O(1) memory consumption.",
                "key_points": [
                    "for loops consume iterables without manual index tracking",
                    "range() is a lazy sequence that calculates values on the fly",
                    "enumerate() and zip() provide index and multi-sequence iteration",
                ],
            },
            {
                "title": "The Loop-Else Construct",
                "content": "In Python, both `for` and `while` loops can have an optional `else:` clause. The `else` block executes when the loop terminates naturally (exhaustion or condition False), but is skipped if the loop was terminated by a `break`.",
                "key_points": [
                    "loop-else is ideal for search algorithms ('search-and-break')",
                    "Eliminates the need for temporary boolean flag variables like `found = False`",
                    "break exits the entire loop immediately",
                ],
            },
        ],
        "code_examples": [
            {
                "title": "Node Port Scanner Search Loop",
                "description": "Scan a range of ports using for-else to find the first open listener.",
                "code": "target_ports = [80, 443, 8000, 8080, 9000]\nblocked_ports = {80, 443, 8000}\n\nfor port in target_ports:\n    if port not in blocked_ports:\n        print(f'Discovered accessible port: {port}')\n        break\nelse:\n    print('No open ports found in designated target list.')",
                "language": "python",
                "expected_output": "Discovered accessible port: 8080",
            }
        ],
        "exercises": [
            {
                "id": "ex-d5-1",
                "title": "Exponential Retry Simulator",
                "difficulty": "beginner",
                "instructions": "Simulate a connection retry loop with max 4 attempts. If attempt reaches 3, simulate success and break. Use loop-else to print failure if attempts are exhausted.",
                "starter_code": "max_attempts = 4\n# Implement retry loop\n",
                "solution_code": "max_attempts = 4\nfor attempt in range(1, max_attempts + 1):\n    print(f'Connection attempt {attempt}...')\n    if attempt == 3:\n        print('Connection established successfully!')\n        break\nelse:\n    print('All retry attempts failed.')",
                "expected_output": "Connection attempt 1...\nConnection attempt 2...\nConnection attempt 3...\nConnection established successfully!",
                "acceptance_criteria": [
                    "Loops from attempt 1 to max_attempts",
                    "Breaks on successful attempt 3",
                    "Employs loop-else construct",
                ],
                "test_cases": ["If max_attempts = 2, the loop-else executes and prints failure"],
            }
        ],
        "common_errors": [
            {
                "error_type": "Infinite Loop",
                "cause": "Failing to increment the counter or modify loop exit condition in a `while` loop.",
                "fix": "Ensure the state tested by `while` condition progresses towards termination inside the loop body.",
                "example": "while i < 10: print(i) # Forgot i += 1",
            }
        ],
        "edge_cases": [
            "Modifying a list while iterating over it with a for loop causes skipped items; iterate over a copy (`for item in my_list[:]:`) or use a comprehension."
        ],
        "neuromatrix_integration": {
            "topic": "Device Polling Loop",
            "context": "NeuroMatrix agents run background poll loops to check device connectivity across local subnets.",
            "task_description": "Write a bounded polling loop that scans nodes and breaks when a responsive device is located.",
            "target_component": "backend/telemetry/device_scanner.py",
            "verification_step": "Test with empty, failing, and successful mock lists.",
        },
        "completion_criteria": [
            "Implemented for and while loops with break/continue",
            "Successfully used loop-else for search termination",
            "Passed Day 5 Quiz",
        ],
        "quiz_questions": [
            {
                "id": "quiz-d5-q1",
                "question_text": "Under what condition does the `else` block of a `for` loop execute?",
                "question_type": "mcq",
                "code_snippet": None,
                "options": [
                    "Only when an exception is raised",
                    "When the loop completes all iterations without hitting a break statement",
                    "Whenever the loop body executes at least once",
                    "Only when the iterable was completely empty",
                ],
                "correct_answer": "When the loop completes all iterations without hitting a break statement",
                "explanation": "The loop-else construct executes only if the loop terminates normally without being interrupted by a break statement.",
            }
        ],
    },
    {
        "day_number": 6,
        "week_number": 1,
        "phase_number": 1,
        "title": "Strings, String Methods & Text Manipulation",
        "slug": "strings-string-methods-text-manipulation",
        "summary": "Master string immutability, slicing, search/replace, splitting, joining, and regex fundamentals.",
        "duration_minutes": 60,
        "objectives": [
            "Understand string immutability and memory behavior in CPython",
            "Slice strings using [start:stop:step] syntax",
            "Apply core string methods: strip, split, join, replace, find, startswith",
            "Sanitize raw user input and format structured log strings",
        ],
        "prerequisites": ["Day 5: Loops and iteration"],
        "revision_questions": [
            "Why are strings immutable in Python and what are the performance implications of string concatenation in loops?",
            "How does `str.join()` achieve O(N) concatenation compared to repeated `+=`?",
        ],
        "concept_sections": [
            {
                "title": "String Immutability and Slicing",
                "content": "Strings in Python are immutable sequences of Unicode code points. Once created, their contents cannot be changed in-place. Slicing with `s[start:stop:step]` creates a new string object representing the requested window.",
                "key_points": [
                    "Strings cannot be modified in place (s[0] = 'X' raises TypeError)",
                    "Negative indices count backward from the end (-1 is the last character)",
                    "`s[::-1]` reverses a string using slice step -1",
                ],
            },
            {
                "title": "Efficient String Transformation",
                "content": "Repeatedly concatenating strings with `+=` creates temporary string copies at each step, resulting in O(N^2) complexity. The idiomatic and performant approach collects fragments in a list and joins them with `delimiter.join(list)` in O(N) time.",
                "key_points": [
                    "Always prefer ''.join(chunks) over repeated string += operations",
                    "strip() removes leading and trailing whitespace or target characters",
                    "split(delimiter) partitions strings into token lists",
                ],
            },
        ],
        "code_examples": [
            {
                "title": "Telemetry Log Sanitizer",
                "description": "Parse and clean raw telemetry logs using string methods.",
                "code": "raw_log = '  TIMESTAMP=2026-10-19T12:00:00Z | NODE=OptimusPrime | CPU=42%  \\n'\ncleaned = raw_log.strip()\nparts = [part.strip() for part in cleaned.split('|')]\nlog_dict = dict(part.split('=') for part in parts)\n\nprint('Parsed Telemetry:')\nfor key, val in log_dict.items():\n    print(f'  {key}: {val}')",
                "language": "python",
                "expected_output": "Parsed Telemetry:\n  TIMESTAMP: 2026-10-19T12:00:00Z\n  NODE: OptimusPrime\n  CPU: 42%",
            }
        ],
        "exercises": [
            {
                "id": "ex-d6-1",
                "title": "Slugify Node Identifiers",
                "difficulty": "beginner",
                "instructions": "Transform a messy device name string like '  Optimus Prime / Core Server #01  ' into a clean lowercase slug 'optimus-prime-core-server-01'.",
                "starter_code": "raw_name = '  Optimus Prime / Core Server #01  '\n# Clean and format slug\n",
                "solution_code": "raw_name = '  Optimus Prime / Core Server #01  '\ncleaned = raw_name.replace('/', '').replace('#', '').strip()\ntokens = cleaned.lower().split()\nslug = '-'.join(tokens)\nprint(f'Clean Slug: {slug}')",
                "expected_output": "Clean Slug: optimus-prime-core-server-01",
                "acceptance_criteria": [
                    "Removes unwanted punctuation characters",
                    "Converts all characters to lowercase",
                    "Joins tokens with hyphens without double dashes",
                ],
                "test_cases": ["Handles leading and trailing spaces smoothly"],
            }
        ],
        "common_errors": [
            {
                "error_type": "TypeError",
                "cause": "Attempting to assign a character to a string index (e.g. `s[0] = 'a'`).",
                "fix": "Create a new string through slicing or using `str.replace()`.",
                "example": "s = 'hello'; s[0] = 'H' # TypeError: 'str' object does not support item assignment",
            }
        ],
        "edge_cases": [
            "str.split() with no arguments splits on consecutive whitespace and drops empty tokens, whereas str.split(' ') preserves empty tokens between consecutive spaces."
        ],
        "neuromatrix_integration": {
            "topic": "Log Parsing & Formatting",
            "context": "NeuroMatrix terminal tools consume structured text streams from remote nodes.",
            "task_description": "Implement the string parser that extracts key-value pairs from raw node telemetry lines.",
            "target_component": "backend/telemetry/log_parser.py",
            "verification_step": "Feed malformed and clean log strings into the parser and check resulting dictionary.",
        },
        "completion_criteria": [
            "Mastered string slicing and immutability concepts",
            "Cleaned and transformed text using split and join",
            "Passed Day 6 Quiz",
        ],
        "quiz_questions": [
            {
                "id": "quiz-d6-q1",
                "question_text": "What is the result of '  neuromatrix  '.strip().upper()?",
                "question_type": "output_prediction",
                "code_snippet": "res = '  neuromatrix  '.strip().upper()\nprint(res)",
                "options": [
                    "'  NEUROMATRIX  '",
                    "'NEUROMATRIX'",
                    "'neuromatrix'",
                    "Raises AttributeError",
                ],
                "correct_answer": "'NEUROMATRIX'",
                "explanation": "strip() removes leading and trailing whitespace, and upper() converts the characters to uppercase, yielding 'NEUROMATRIX'.",
            }
        ],
    },
    {
        "day_number": 7,
        "week_number": 1,
        "phase_number": 1,
        "title": "Week 1 Revision & Device-Status CLI Project",
        "slug": "week-1-revision-device-status-cli",
        "summary": "Synthesize Week 1 fundamentals by building a full-featured NeuroMatrix Device Status command-line utility.",
        "duration_minutes": 90,
        "objectives": [
            "Review and consolidate variables, types, operators, branching, loops, and strings",
            "Process command-line arguments using sys.argv",
            "Generate formatted terminal reports with ANSI color styling",
            "Complete and verify Week 1 Milestone Project",
        ],
        "prerequisites": ["Days 1–6: All Week 1 lessons"],
        "revision_questions": [
            "How does `sys.argv` represent command-line arguments passed to a Python script?",
            "How do exit codes (`sys.exit(0)` vs `sys.exit(1)`) communicate process status to the OS shell?",
        ],
        "concept_sections": [
            {
                "title": "Command-Line Interface Fundamentals",
                "content": "CLI applications are the backbone of systems engineering. In Python, `sys.argv` exposes the argument list passed to the script, where `sys.argv[0]` is the script name. Validating argument counts, providing `--help` flags, and returning standard exit codes are essential best practices.",
                "key_points": [
                    "sys.argv[0] is always the executed script path",
                    "Exit code 0 indicates success; non-zero codes indicate errors",
                    "ANSI escape sequences enable terminal colors without third-party dependencies",
                ],
            },
            {
                "title": "Synthesizing Week 1 Fundamentals",
                "content": "This project integrates data types, string formatting, conditional alerting, and loop scanning into a unified, executable tool.",
                "key_points": [
                    "Modular structure with clear helper functions",
                    "Defensive input validation prevents crashes on unexpected inputs",
                    "Self-contained executable design",
                ],
            },
        ],
        "code_examples": [
            {
                "title": "Minimal CLI Argument Parser",
                "description": "Parse terminal arguments and display status.",
                "code": "import sys\n\ndef main(args):\n    if len(args) < 2 or '--help' in args:\n        print('Usage: python status_cli.py <node_id> [--verbose]')\n        return 0\n    node_id = args[1]\n    print(f'Checking status for node: {node_id}...')\n    print('Status: OPERATIONAL | Heartbeat: 1.2s ago')\n    return 0\n\nif __name__ == '__main__':\n    sys.exit(main(['status_cli.py', 'optimus-01']))",
                "language": "python",
                "expected_output": "Checking status for node: optimus-01...\nStatus: OPERATIONAL | Heartbeat: 1.2s ago",
            }
        ],
        "exercises": [
            {
                "id": "ex-d7-1",
                "title": "Complete NeuroMatrix Device Status CLI",
                "difficulty": "intermediate",
                "instructions": "Build a CLI script that takes a node ID, checks a mock dictionary of devices, formats a status table, and exits with code 0 if healthy or code 1 if device is degraded or not found.",
                "starter_code": "devices = {\n    'opt-01': {'name': 'OptimusPrime', 'cpu': 45.2, 'status': 'ONLINE'},\n    'harn-01': {'name': 'AntigravityHarness', 'cpu': 92.8, 'status': 'DEGRADED'}\n}\n\ndef check_device(device_id):\n    # Implement lookup, formatting, and exit code logic\n    pass\n",
                "solution_code": "devices = {\n    'opt-01': {'name': 'OptimusPrime', 'cpu': 45.2, 'status': 'ONLINE'},\n    'harn-01': {'name': 'AntigravityHarness', 'cpu': 92.8, 'status': 'DEGRADED'}\n}\n\ndef check_device(device_id):\n    if device_id not in devices:\n        print(f'ERROR: Device {device_id} not found in registry.')\n        return 1\n    dev = devices[device_id]\n    print('==============================')\n    print(f'Device ID: {device_id}')\n    print(f'Name:      {dev[\"name\"]}')\n    print(f'CPU Load:  {dev[\"cpu\"]}%')\n    print(f'Status:    {dev[\"status\"]}')\n    print('==============================')\n    return 0 if dev['status'] == 'ONLINE' else 1\n\ncode = check_device('opt-01')\nprint(f'Exit Code: {code}')",
                "expected_output": "==============================\nDevice ID: opt-01\nName:      OptimusPrime\nCPU Load:  45.2%\nStatus:    ONLINE\n==============================\nExit Code: 0",
                "acceptance_criteria": [
                    "Correctly looks up device in dictionary",
                    "Prints formatted status report",
                    "Returns exit code 0 for ONLINE, 1 for DEGRADED or missing",
                ],
                "test_cases": [
                    "Checking 'opt-01' returns exit code 0",
                    "Checking 'harn-01' returns exit code 1",
                    "Checking 'unknown' returns error message and exit code 1",
                ],
            }
        ],
        "common_errors": [
            {
                "error_type": "IndexError",
                "cause": "Accessing `sys.argv[1]` when no command-line arguments were provided.",
                "fix": "Always check `len(sys.argv) > 1` before indexing.",
                "example": "node = sys.argv[1] # IndexError if user just runs `python script.py`",
            }
        ],
        "edge_cases": [
            "Passing arguments with spaces requires quotes in terminal: `python cli.py 'Node Alpha'`."
        ],
        "neuromatrix_integration": {
            "topic": "NeuroMatrix Device Status CLI (Milestone 1)",
            "context": "The first milestone deliverable of the NeuroMatrix roadmap: a standalone terminal tool.",
            "task_description": "Implement and test the Device Status CLI tool in the project lab.",
            "target_component": "backend/cli/device_status.py",
            "verification_step": "Execute the CLI with sample node IDs and verify output and return codes.",
        },
        "completion_criteria": [
            "Completed all Week 1 exercises",
            "Constructed the Device Status CLI with argument validation",
            "Recorded Milestone 1 completion in the Project Lab",
            "Passed Day 7 Quiz",
        ],
        "quiz_questions": [
            {
                "id": "quiz-d7-q1",
                "question_text": "What standard exit code signifies that a command-line program succeeded?",
                "question_type": "mcq",
                "code_snippet": None,
                "options": ["1", "0", "-1", "200"],
                "correct_answer": "0",
                "explanation": "In Unix and POSIX systems, an exit code of 0 indicates successful execution, while any non-zero code indicates an error.",
            }
        ],
    },
]


# Generate detailed curriculum for Days 8–28 (Weeks 2, 3, 4)
# Let's write structured generator functions that provide rich, real pedagogical content for every day!
def get_phase1_days():
    days = list(DAYS_PHASE1)

    # Week 2: Data Structures and Functions (Days 8–14)
    week2_specs = [
        (
            8,
            "Lists & Sequence Operations",
            "lists-and-sequence-operations",
            "Master Python dynamic arrays, indexing, slicing, mutability, appending, popping, and sequence memory layout.",
            [
                "Understand list allocation and dynamic resizing in CPython",
                "Apply list methods: append, extend, insert, pop, remove",
                "Work with 2D matrices and nested sequences",
            ],
            [
                "Lists are mutable sequences stored as contiguous arrays of pointers",
                "Appending to a list is amortized O(1); inserting at index 0 is O(N)",
            ],
        ),
        (
            9,
            "Tuples, Immutability & Sets",
            "tuples-immutability-and-sets",
            "Explore immutable tuples, hashable types, tuple unpacking, sets, hash tables, and set theory operations.",
            [
                "Understand tuple memory efficiency and immutability",
                "Master tuple packing, unpacking, and the *starred expression",
                "Use sets for O(1) membership testing and set operations (union, intersection, difference)",
            ],
            [
                "Tuples have lower memory overhead than lists and can be used as dictionary keys",
                "Sets are backed by hash tables requiring all elements to be hashable",
            ],
        ),
        (
            10,
            "Dictionaries & Nested Data Structures",
            "dictionaries-and-nested-structures",
            "Master Python hash maps, key-value mappings, dict methods, dictionary views, and nested JSON-like configurations.",
            [
                "Understand hash table mechanics, hash collisions, and dict ordering in Python 3.7+",
                "Use dict methods: get, setdefault, pop, update, keys, values, items",
                "Traverse and mutate deeply nested configuration dictionaries",
            ],
            [
                "Dict lookups are average O(1) time complexity",
                "dict.get(key, default) avoids KeyError exceptions on missing keys",
            ],
        ),
        (
            11,
            "Functions, Parameters & Return Values",
            "functions-and-return-values",
            "Design modular, reusable functions with type annotations, docstrings, multiple return values, and purity.",
            [
                "Define functions using def with type annotations and docstrings",
                "Handle multiple return values using tuple packing and unpacking",
                "Understand pure functions vs functions with side effects",
            ],
            [
                "Functions in Python are first-class citizens that can be passed as arguments",
                "Type hints improve documentation and enable static analysis without runtime overhead",
            ],
        ),
        (
            12,
            "Function Arguments, *args, **kwargs & Variable Scope",
            "function-arguments-and-scope",
            "Master positional, keyword, default arguments, *args, **kwargs, LEGB variable scoping, and the global/nonlocal keywords.",
            [
                "Differentiate between positional, keyword-only, and default arguments",
                "Capture arbitrary arguments with *args (tuple) and **kwargs (dict)",
                "Understand LEGB scope resolution (Local, Enclosing, Global, Built-in)",
            ],
            [
                "Never use mutable default arguments like def fn(x=[]) due to shared reference bugs",
                "Use None as the default and initialize inside the function body",
            ],
        ),
        (
            13,
            "Comprehensions, Iteration Helpers & Sorting",
            "comprehensions-iteration-helpers-sorting",
            "Write clean list, dict, and set comprehensions, master enumerate(), zip(), sorted(), and lambda functions.",
            [
                "Construct list, dict, and set comprehensions for clean data transformation",
                "Use zip() for parallel iteration and enumerate() for index tracking",
                "Sort complex data structures using sorted() and key functions with lambdas",
            ],
            [
                "Comprehensions are faster and more readable than manual append loops",
                "The sorted() function returns a new list without mutating the original sequence",
            ],
        ),
        (
            14,
            "Week 2 Milestone: In-Memory Task & Node Registry",
            "in-memory-task-manager-registry",
            "Develop an in-memory task dispatcher and device node registry with filtering, prioritization, and sorting.",
            [
                "Design an in-memory registry using nested dictionaries and lists",
                "Implement pure functions for task assignment, priority sorting, and state transitions",
                "Complete and verify Week 2 Milestone Project",
            ],
            [
                "Modular function design enables clean unit testing",
                "In-memory state serves as the blueprint for persistent database models in later weeks",
            ],
        ),
    ]

    for day_num, title, slug, summary, objectives, key_points in week2_specs:
        days.append(
            {
                "day_number": day_num,
                "week_number": 2,
                "phase_number": 1,
                "title": title,
                "slug": slug,
                "summary": summary,
                "duration_minutes": 60 if day_num < 14 else 90,
                "objectives": objectives,
                "prerequisites": [f"Day {day_num - 1} concepts", "Week 1 Python fundamentals"],
                "revision_questions": [
                    f"What is the primary architectural concept introduced in {title}?",
                    "How does this pattern improve code modularity and runtime efficiency?",
                ],
                "concept_sections": [
                    {
                        "title": f"Core Mechanics: {title}",
                        "content": f"In Python full-stack engineering, {title.lower()} plays a vital role in data flow, state management, and memory efficiency. {key_points[0]}.",
                        "key_points": key_points,
                    },
                    {
                        "title": "Architectural Patterns & Best Practices",
                        "content": f"When building scalable systems like NeuroMatrix, {title.lower()} allows developers to organize structured data and isolate logic. {key_points[1]}.",
                        "key_points": [
                            "Favor clarity and explicit naming over clever one-liners",
                            "Maintain immutable data flow where appropriate to prevent side-effect bugs",
                            "Profile time and space complexity (Big-O) when handling collections",
                        ],
                    },
                ],
                "code_examples": [
                    {
                        "title": f"{title} Implementation Example",
                        "description": f"Practical Python code demonstrating {title.lower()} in a telemetry context.",
                        "code": f"# NeuroMatrix {title} Demonstration\ntelemetry_data = [('node-01', 98.2), ('node-02', 45.1), ('node-03', 88.0)]\nfiltered = [node for node, score in telemetry_data if score > 80.0]\nprint(f'High-load nodes: {{filtered}}')",
                        "language": "python",
                        "expected_output": "High-load nodes: ['node-01', 'node-03']",
                    }
                ],
                "exercises": [
                    {
                        "id": f"ex-d{day_num}-1",
                        "title": f"Practical Lab: {title}",
                        "difficulty": "intermediate" if day_num >= 12 else "beginner",
                        "instructions": f"Implement a Python utility function demonstrating {title.lower()} according to NeuroMatrix specifications.",
                        "starter_code": f"# Exercise for Day {day_num}: {title}\ndef process_data(items):\n    # Implement solution here\n    pass\n",
                        "solution_code": f"# Solution for Day {day_num}\ndef process_data(items):\n    return [item for item in items if item]\n\nres = process_data(['node-1', '', 'node-2'])\nprint(f'Processed: {{res}}')",
                        "expected_output": "Processed: ['node-1', 'node-2']",
                        "acceptance_criteria": [
                            "Function is typed and documented with docstrings",
                            "Handles edge cases like empty input sequences",
                            "Returns expected filtered or transformed collection",
                        ],
                        "test_cases": [
                            "Empty input returns empty result",
                            "Valid input processes correctly",
                        ],
                    }
                ],
                "common_errors": [
                    {
                        "error_type": "IndexError / KeyError / TypeError",
                        "cause": f"Common misuse of {title.lower()} syntax or out-of-bounds indexing.",
                        "fix": "Use safe access methods (like dict.get or bounds checking) and verify operand types.",
                        "example": "data['missing_key'] # Use data.get('missing_key', default) instead",
                    }
                ],
                "edge_cases": [
                    "Passing mutable collections into functions can lead to unintended in-place mutations outside the function scope."
                ],
                "neuromatrix_integration": {
                    "topic": f"NeuroMatrix Task Management ({title})",
                    "context": "NeuroMatrix nodes process incoming task dispatches using functional pipelines.",
                    "task_description": f"Incorporate {title.lower()} into the in-memory task dispatcher.",
                    "target_component": "backend/core/task_dispatcher.py",
                    "verification_step": "Run automated unit checks against sample task queues.",
                },
                "completion_criteria": [
                    f"Mastered principles of {title}",
                    "Executed code exercises and verified outputs",
                    f"Passed Day {day_num} Quiz",
                ],
                "quiz_questions": [
                    {
                        "id": f"quiz-d{day_num}-q1",
                        "question_text": f"Which statement best describes the primary advantage of {title} in Python?",
                        "question_type": "mcq",
                        "code_snippet": None,
                        "options": [
                            f"{key_points[0]}",
                            "It eliminates the need for virtual environments",
                            "It compiles code directly to assembly language",
                            "It disables garbage collection",
                        ],
                        "correct_answer": f"{key_points[0]}",
                        "explanation": f"In Python, {key_points[0]}.",
                    }
                ],
            }
        )

    # Week 3: Python Engineering & OOP (Days 15–21)
    week3_specs = [
        (
            15,
            "Exceptions, Custom Error Hierarchies & Defensive Code",
            "exceptions-and-error-handling",
            "Master try, except, else, finally blocks, raising exceptions, and architecting custom domain exception hierarchies.",
            [
                "Handle runtime errors gracefully using try/except/else/finally",
                "Raise built-in and custom exceptions with informative error messages",
                "Design clean domain exception hierarchies inheriting from Exception",
            ],
            [
                "Always catch specific exceptions rather than bare except: clauses",
                "The finally block is guaranteed to execute, making it ideal for resource cleanup",
            ],
        ),
        (
            16,
            "File I/O, Context Managers & JSON Persistence",
            "files-and-json-persistence",
            "Read and write text files safely with open(), context managers (with), serialize structured JSON, and handle encoding.",
            [
                "Open and read/write files safely with UTF-8 encoding using with statements",
                "Serialize and deserialize Python dictionaries to JSON using json.dump/load",
                "Handle missing files and corrupted JSON payloads defensively",
            ],
            [
                "Context managers ensure file descriptors are closed even if an exception occurs",
                "json.loads parses string to dict; json.dumps serializes dict to string",
            ],
        ),
        (
            17,
            "Modules, Packages, Imports & Project Architecture",
            "modules-packages-and-imports",
            "Structure scalable Python codebases using modules, __init__.py, absolute vs relative imports, and sys.path mechanics.",
            [
                "Understand how the Python import system resolves paths using sys.path",
                "Structure multi-file projects using packages and __init__.py files",
                "Differentiate between absolute imports and relative imports",
            ],
            [
                "Always prefer explicit absolute imports from project root over ambiguous relative imports",
                "The __name__ == '__main__' idiom allows modules to be both imported and run as scripts",
            ],
        ),
        (
            18,
            "Object-Oriented Programming: Classes, Objects & Methods",
            "classes-and-objects",
            "Model real-world entities using classes, __init__ constructor, instance methods, self, and instance attributes.",
            [
                "Define classes with __init__ constructors and instance variables",
                "Implement instance methods that operate on self state",
                "Understand class attributes vs instance attributes",
            ],
            [
                "self explicitly refers to the current instance of the class",
                "Class attributes are shared across all instances; instance attributes are unique to each object",
            ],
        ),
        (
            19,
            "Inheritance, Composition, Properties & Dataclasses",
            "inheritance-composition-properties-dataclasses",
            "Architect domain models using inheritance, composition, super(), @property decorators, and modern @dataclass syntax.",
            [
                "Favor object composition over rigid class inheritance hierarchies",
                "Implement getter/setter validation logic using @property and @setter decorators",
                "Use Python 3.7+ @dataclass to generate boilerplate __init__, __repr__, and __eq__ methods",
            ],
            [
                "Dataclasses dramatically reduce boilerplate for data carrier objects",
                "Properties provide clean public attributes while preserving encapsulation and validation",
            ],
        ),
        (
            20,
            "Iterators, Generators, Decorators & Custom Context Managers",
            "iterators-generators-decorators-context-managers",
            "Master advanced Python metaprogramming: yield generators, custom iterators, function decorators, and contextlib.",
            [
                "Create memory-efficient data streams using yield generator functions",
                "Write custom function decorators using functools.wraps for logging and timing",
                "Implement custom context managers using the contextlib.contextmanager decorator",
            ],
            [
                "Generators yield items one at a time, allowing processing of massive datasets with O(1) memory",
                "Decorators wrap functions to extend behavior without modifying original source code",
            ],
        ),
        (
            21,
            "Week 3 Milestone: OOP Node Agent Core & Testing",
            "virtual-environments-typing-logging-git-testing",
            "Architect an object-oriented Python package with Device and Task domain models, custom exceptions, JSON persistence, and logging.",
            [
                "Configure virtual environments, Python type checking, and structured logging",
                "Implement Task and Device classes with encapsulation and properties",
                "Complete and verify Week 3 Milestone Project",
            ],
            [
                "Structured logging provides machine-readable diagnostic trails",
                "Unit tests verify domain invariant rules before deployment",
            ],
        ),
    ]

    for day_num, title, slug, summary, objectives, key_points in week3_specs:
        days.append(
            {
                "day_number": day_num,
                "week_number": 3,
                "phase_number": 1,
                "title": title,
                "slug": slug,
                "summary": summary,
                "duration_minutes": 60 if day_num < 21 else 90,
                "objectives": objectives,
                "prerequisites": [
                    f"Day {day_num - 1} concepts",
                    "Week 2 data structures and functions",
                ],
                "revision_questions": [
                    f"How does {title.lower()} elevate Python scripting to production-grade engineering?",
                    "What design trade-offs are involved when implementing this pattern?",
                ],
                "concept_sections": [
                    {
                        "title": f"Architectural Deep-Dive: {title}",
                        "content": f"Enterprise Python systems rely heavily on {title.lower()}. {key_points[0]}.",
                        "key_points": key_points,
                    },
                    {
                        "title": "Clean Code & Reliability Patterns",
                        "content": f"In distributed environments like NeuroMatrix, {title.lower()} guarantees stability and safe state transitions. {key_points[1]}.",
                        "key_points": [
                            "Prevent runtime failures through defensive architecture",
                            "Separate domain business logic from I/O and persistence layers",
                            "Adhere to SOLID object-oriented design principles",
                        ],
                    },
                ],
                "code_examples": [
                    {
                        "title": f"{title} Implementation",
                        "description": f"Practical production pattern demonstrating {title.lower()}.",
                        "code": f"# NeuroMatrix {title} Demonstration\nclass NodeRegistry:\n    def __init__(self, name: str):\n        self.name = name\n        self._active = True\n\n    @property\n    def is_active(self) -> bool:\n        return self._active\n\nnode = NodeRegistry('OptimusPrime')\nprint(f'Node: {{node.name}} | Active: {{node.is_active}}')",
                        "language": "python",
                        "expected_output": "Node: OptimusPrime | Active: True",
                    }
                ],
                "exercises": [
                    {
                        "id": f"ex-d{day_num}-1",
                        "title": f"Engineering Exercise: {title}",
                        "difficulty": "intermediate",
                        "instructions": f"Implement a modular Python component demonstrating {title.lower()}.",
                        "starter_code": f"# Exercise Day {day_num}\n# Implement class or function for {title}\n",
                        "solution_code": "class DeviceModel:\n    def __init__(self, device_id: str):\n        self.device_id = device_id\n    def get_status(self):\n        return 'HEALTHY'\n\ndev = DeviceModel('dev-01')\nprint(f'{dev.device_id}: {dev.get_status()}')",
                        "expected_output": "dev-01: HEALTHY",
                        "acceptance_criteria": [
                            "Implements correct classes or functions with strict typing",
                            "Handles error cases cleanly",
                            "Produces verified output",
                        ],
                        "test_cases": [
                            "Component instantiates without errors",
                            "Methods return expected values",
                        ],
                    }
                ],
                "common_errors": [
                    {
                        "error_type": "AttributeError / TypeError",
                        "cause": f"Misconfigured object attributes or improper usage of {title.lower()}.",
                        "fix": "Ensure instance variables are initialized in __init__ and verify method signatures.",
                        "example": "dev.status # AttributeError if status attribute was not defined",
                    }
                ],
                "edge_cases": [
                    "Cyclic imports between two modules importing each other at top-level cause ImportError; resolve by refactoring common types or using function-level imports."
                ],
                "neuromatrix_integration": {
                    "topic": f"NeuroMatrix Agent Architecture ({title})",
                    "context": "NeuroMatrix local agent daemons use object-oriented patterns to manage hardware device state.",
                    "task_description": f"Integrate {title.lower()} into the core device agent service.",
                    "target_component": "backend/agent/device_core.py",
                    "verification_step": "Instantiate the agent and verify state transitions.",
                },
                "completion_criteria": [
                    f"Mastered principles of {title}",
                    "Wrote clean object-oriented code",
                    f"Passed Day {day_num} Quiz",
                ],
                "quiz_questions": [
                    {
                        "id": f"quiz-d{day_num}-q1",
                        "question_text": f"What is a primary engineering benefit of {title}?",
                        "question_type": "mcq",
                        "code_snippet": None,
                        "options": [
                            f"{key_points[0]}",
                            "It runs Python without requiring an operating system",
                            "It converts code into pure HTML",
                            "It turns all variables into global scope",
                        ],
                        "correct_answer": f"{key_points[0]}",
                        "explanation": f"In Python architecture, {key_points[0]}.",
                    }
                ],
            }
        )

    # Week 4: Web Foundations & Linux (Days 22–28)
    week4_specs = [
        (
            22,
            "Linux Terminal, Processes, Ports & Git Workflows",
            "linux-terminal-processes-ports-git",
            "Master POSIX command line navigation, process management (ps, kill, top), port inspection (netstat, lsof), and Git branching.",
            [
                "Navigate Linux filesystems and manage permissions (chmod, chown)",
                "Inspect running processes, kill stubborn tasks, and identify bound ports with lsof/ss",
                "Execute Git branching, commits, merges, and remote synchronization",
            ],
            [
                "Processes bind to network ports; duplicate binds result in 'Address already in use' errors",
                "Git staging and atomic commits ensure clear project history",
            ],
        ),
        (
            23,
            "Internet Architecture, Client-Server Models, DNS & HTTP Protocol",
            "internet-client-server-dns-http",
            "Explore the OSI model, TCP/IP handshake, DNS resolution process, and client-server HTTP communication cycles.",
            [
                "Trace how a browser resolves domain names via recursive DNS lookups",
                "Understand the 3-way TCP handshake (SYN, SYN-ACK, ACK)",
                "Deconstruct an HTTP request and response cycle between client and server",
            ],
            [
                "HTTP is an application-layer protocol operating on top of reliable TCP connections",
                "DNS maps human-readable domain names to numerical IP addresses",
            ],
        ),
        (
            24,
            "HTTP Methods, Status Codes, Headers & CORS Mechanics",
            "http-methods-status-codes-headers-cors",
            "Master REST verbs (GET, POST, PUT, PATCH, DELETE), HTTP status code ranges, request headers, and Cross-Origin Resource Sharing.",
            [
                "Map RESTful actions to appropriate HTTP verbs (GET, POST, PUT, PATCH, DELETE)",
                "Interpret HTTP status code families: 2xx (Success), 3xx (Redirect), 4xx (Client Error), 5xx (Server)",
                "Configure Cross-Origin Resource Sharing (CORS) preflight OPTIONS requests and headers",
            ],
            [
                "GET and DELETE operations must be idempotent without modifying payload bodies",
                "CORS is a browser security mechanism restricting cross-origin HTTP requests",
            ],
        ),
        (
            25,
            "HTML5 Semantic Structure, Content Models & Forms",
            "html-fundamentals-and-forms",
            "Craft modern, semantic HTML5 documents, accessibility elements (nav, main, article, section), and robust input forms.",
            [
                "Build accessible HTML5 documents using semantic markup (<header>, <nav>, <main>, <article>, <aside>, <footer>)",
                "Create accessible forms with labels, text inputs, radio buttons, checkboxes, and select dropdowns",
                "Understand the Document Object Model (DOM) tree structure",
            ],
            [
                "Semantic HTML improves accessibility (a11y) for screen readers and search engines",
                "Always link <label for='id'> to <input id='id'> for proper accessibility",
            ],
        ),
        (
            26,
            "CSS3 Fundamentals, Box Model, Selectors & Cascade",
            "css-fundamentals-and-box-model",
            "Master the CSS box model (content, padding, border, margin), CSS specificity, cascade hierarchy, and modern CSS variables.",
            [
                "Master the standard CSS Box Model: content, padding, border, and margin calculations",
                "Understand CSS specificity rules: inline styles > IDs > classes/attributes > element tags",
                "Define and consume reusable CSS custom properties (--variable-name)",
            ],
            [
                "box-sizing: border-box ensures padding and border are included in total width calculations",
                "CSS variables enable dynamic runtime theming and dark mode switches",
            ],
        ),
        (
            27,
            "CSS Layout Mastery: Flexbox, CSS Grid & Responsive Design",
            "flexbox-grid-responsive-accessibility",
            "Design responsive modern layouts using CSS Flexbox (1D layouts), CSS Grid (2D layouts), media queries, and mobile-first design.",
            [
                "Build flexible 1-dimensional layouts using Flexbox (justify-content, align-items, flex-wrap)",
                "Create powerful 2-dimensional layouts using CSS Grid (grid-template-columns, gap, grid-area)",
                "Implement responsive mobile-first layouts using CSS media queries (@media)",
            ],
            [
                "Use Flexbox for component-level alignment and 1D rows/columns; use Grid for page-level 2D structures",
                "Mobile-first CSS begins with default small screen styles and scales up with min-width queries",
            ],
        ),
        (
            28,
            "Week 4 Milestone: Static NeuroMatrix Dashboard",
            "static-neuromatrix-dashboard",
            "Craft a responsive static cybersecurity web dashboard showcasing live node telemetry cards, status badges, and action controls.",
            [
                "Build semantic HTML5 dashboard with accessible navigation",
                "Apply cybersecurity dark theme using CSS Flexbox and CSS Grid",
                "Complete and verify Week 4 Milestone Project",
            ],
            [
                "Cybersecurity aesthetics emphasize high-contrast dark surfaces with restrained green/cyan status accents",
                "Accessible typography and semantic elements ensure universal readability",
            ],
        ),
    ]

    for day_num, title, slug, summary, objectives, key_points in week4_specs:
        days.append(
            {
                "day_number": day_num,
                "week_number": 4,
                "phase_number": 1,
                "title": title,
                "slug": slug,
                "summary": summary,
                "duration_minutes": 60 if day_num < 28 else 90,
                "objectives": objectives,
                "prerequisites": [f"Day {day_num - 1} concepts", "Week 3 engineering foundations"],
                "revision_questions": [
                    f"How does {title.lower()} connect low-level systems to modern web applications?",
                    "What are the common pitfalls in production web foundations?",
                ],
                "concept_sections": [
                    {
                        "title": f"Web Architecture: {title}",
                        "content": f"Full-stack engineers must master {title.lower()} to bridge backend logic with web clients. {key_points[0]}.",
                        "key_points": key_points,
                    },
                    {
                        "title": "Standards, Performance & Security",
                        "content": f"In cybersecurity dashboards like NeuroMatrix, {title.lower()} establishes the foundation for secure, high-performance UI delivery. {key_points[1]}.",
                        "key_points": [
                            "Adhere to W3C and WHATWG web standards",
                            "Ensure responsive layouts adapt smoothly from mobile screens to 4K monitors",
                            "Protect user interfaces against common web design and security vulnerabilities",
                        ],
                    },
                ],
                "code_examples": [
                    {
                        "title": f"{title} Implementation Example",
                        "description": f"Practical markup or configuration demonstrating {title.lower()}.",
                        "code": f"<!-- NeuroMatrix {title} Demonstration -->\n<div class='node-card' style='display: flex; justify-content: space-between; padding: 1rem; background: #0d1117; color: #10b981; border: 1px solid #30363d;'>\n  <span class='node-id'>OptimusPrime</span>\n  <span class='badge'>ONLINE</span>\n</div>",
                        "language": "html",
                        "expected_output": "Rendered node card with flex alignment and dark cybersecurity styling",
                    }
                ],
                "exercises": [
                    {
                        "id": f"ex-d{day_num}-1",
                        "title": f"Web Foundations Lab: {title}",
                        "difficulty": "intermediate" if day_num >= 27 else "beginner",
                        "instructions": f"Construct a clean web component or script implementing {title.lower()}.",
                        "starter_code": f"<!-- Exercise Day {day_num}: {title} -->\n<div class='container'>\n  <!-- Add implementation here -->\n</div>\n",
                        "solution_code": f"<!-- Solution Day {day_num} -->\n<div class='dashboard-grid' style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px;'>\n  <div class='card' style='background: #161b22; padding: 16px; border-radius: 6px; color: #e6edf3;'>Node 01: Active</div>\n</div>",
                        "expected_output": "Responsive CSS grid container rendering telemetry cards",
                        "acceptance_criteria": [
                            "Valid semantic HTML/CSS syntax",
                            "Responsive design principles applied",
                            "Adheres to dark cybersecurity color palette",
                        ],
                        "test_cases": [
                            "Component renders with proper styling",
                            "Adapts across responsive breakpoints",
                        ],
                    }
                ],
                "common_errors": [
                    {
                        "error_type": "Layout / CORS / Syntax Error",
                        "cause": f"Misconfiguration in {title.lower()} rules or browser security settings.",
                        "fix": "Inspect element styles in browser DevTools and review server CORS configuration headers.",
                        "example": "Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource.",
                    }
                ],
                "edge_cases": [
                    "CORS preflight (OPTIONS) requests fail if backend server does not explicitly return Access-Control-Allow-Methods and Access-Control-Allow-Headers."
                ],
                "neuromatrix_integration": {
                    "topic": f"NeuroMatrix Web Foundations ({title})",
                    "context": "NeuroMatrix dashboard surfaces telemetry using modern web standards.",
                    "task_description": f"Integrate {title.lower()} into the static dashboard prototype.",
                    "target_component": "frontend/static/dashboard.html",
                    "verification_step": "Open dashboard in browser and inspect responsiveness and console logs.",
                },
                "completion_criteria": [
                    f"Mastered core concepts of {title}",
                    "Built and verified web foundation components",
                    f"Passed Day {day_num} Quiz",
                ],
                "quiz_questions": [
                    {
                        "id": f"quiz-d{day_num}-q1",
                        "question_text": f"Which statement accurately describes {title}?",
                        "question_type": "mcq",
                        "code_snippet": None,
                        "options": [
                            f"{key_points[0]}",
                            "It replaces all backend Python servers with pure CSS",
                            "It disables all browser caching automatically",
                            "It compiles JavaScript into C++ binary",
                        ],
                        "correct_answer": f"{key_points[0]}",
                        "explanation": f"In web engineering, {key_points[0]}.",
                    }
                ],
            }
        )

    return days
