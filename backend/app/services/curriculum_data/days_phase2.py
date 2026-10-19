# Phase 2: Modern Web, React & Backend Architecture (Days 29–70)
# Weeks 5–10


def get_phase2_days():
    days = []

    # Weeks 5 to 10 specs
    # Week 5: JavaScript (29-35)
    # Week 6: React (36-42)
    # Week 7: Databases (43-49)
    # Week 8: FastAPI (50-56)
    # Week 9: Security (57-63)
    # Week 10: Full-stack Integration (64-70)

    phase2_catalog = [
        # Week 5
        (
            29,
            5,
            "JavaScript Variables, Primitive Types, Conditions & Loops",
            "javascript-variables-types-conditions-loops",
            "Master modern ES6+ variable declarations (let, const), data types, type coercion, truthy/falsy rules, and loop constructs.",
            [
                "Understand block scoping with let/const vs function scoping with var",
                "Differentiate between primitive types and reference types in JavaScript",
                "Use strict equality (===) to avoid subtle type coercion bugs",
            ],
            [
                "Always use const by default and let only when reassignment is required; avoid var",
                "JavaScript primitives are immutable; objects and arrays are mutable reference types",
            ],
        ),
        (
            30,
            5,
            "JavaScript Functions, Arrays, Objects & Destructuring",
            "functions-arrays-objects-destructuring",
            "Write arrow functions, higher-order array methods (map, filter, reduce), object literals, and object/array destructuring.",
            [
                "Master ES6 arrow functions and lexical this binding",
                "Transform data with array methods: map, filter, reduce, find, some, every",
                "Extract nested properties cleanly using object and array destructuring syntax",
            ],
            [
                "Array methods like map and filter return new arrays, enabling immutable data patterns",
                "Destructuring with default values prevents undefined property errors",
            ],
        ),
        (
            31,
            5,
            "DOM Manipulation, Event Handling & HTML Forms",
            "dom-manipulation-events-forms",
            "Select and mutate Document Object Model elements, attach event listeners, handle form submissions, and prevent default actions.",
            [
                "Query DOM nodes using document.querySelector and querySelectorAll",
                "Listen for user events (click, submit, change) using addEventListener",
                "Handle form submissions and prevent page reload via event.preventDefault()",
            ],
            [
                "Event delegation handles dynamic elements efficiently with a single parent listener",
                "Always sanitize user inputs before rendering to prevent Cross-Site Scripting (XSS)",
            ],
        ),
        (
            32,
            5,
            "Asynchronous JavaScript: Promises, Async/Await & Fetch API",
            "promises-async-await-fetch",
            "Master the JavaScript event loop, microtask queue, Promise lifecycle, async/await syntax, and fetching JSON from REST APIs.",
            [
                "Understand JavaScript single-threaded concurrency and the event loop",
                "Handle asynchronous operations using Promises and async/await syntax",
                "Fetch data from REST APIs using fetch() with robust error and status checking",
            ],
            [
                "fetch() does not reject on HTTP 4xx or 5xx; always check response.ok",
                "Wrap async operations in try/catch blocks for reliable error handling",
            ],
        ),
        (
            33,
            5,
            "JSON Parsing, ES Modules, Error Handling & DevTools",
            "json-modules-errors-devtools",
            "Serialize and deserialize JSON payloads, modularize code using ES Modules (import/export), and debug with Chrome DevTools.",
            [
                "Parse and stringify JSON data safely with JSON.parse and JSON.stringify",
                "Organize code into modular files using ES Modules (import and export)",
                "Debug code effectively using browser DevTools (Breakpoints, Network tab, Console)",
            ],
            [
                "Invalid JSON strings crash JSON.parse; always wrap parsing in try/catch",
                "The Network tab is critical for inspecting HTTP headers, status codes, and payloads",
            ],
        ),
        (
            34,
            5,
            "Modern Frontend Tooling: npm, Vite & React Foundations",
            "npm-vite-react-introduction",
            "Initialize modern frontend toolchains using npm, Vite bundler, Hot Module Replacement (HMR), and introduce React JSX.",
            [
                "Manage frontend dependencies and scripts using package.json and npm",
                "Configure Vite for high-speed local development with Hot Module Replacement",
                "Understand React declarative component architecture and JSX syntax",
            ],
            [
                "Vite uses native browser ES modules in development for near-instant server starts",
                "JSX is syntactic sugar that compiles into React.createElement function calls",
            ],
        ),
        (
            35,
            5,
            "Week 5 Milestone: Interactive Telemetry Client with Mock Data",
            "interactive-dashboard-structured-mock-data",
            "Construct an interactive, responsive telemetry dashboard consuming structured mock JSON with live search filtering and metrics.",
            [
                "Build an interactive web dashboard using modern ES6+ JavaScript and Vite",
                "Fetch and render structured telemetry mock data dynamically into the DOM",
                "Complete and verify Week 5 Milestone Project",
            ],
            [
                "Decoupling UI rendering from data fetching makes testing and API migration effortless",
                "Responsive layout handles dynamic data resizing across device form factors",
            ],
        ),
        # Week 6: React
        (
            36,
            6,
            "React Components, JSX Syntax & Props Contract",
            "react-components-jsx-props",
            "Create reusable functional React components, write declarative JSX, pass typed props, and compose component trees.",
            [
                "Deconstruct web interfaces into reusable functional React components",
                "Pass immutable data downward through the component tree using typed props",
                "Render child components cleanly using children props and component composition",
            ],
            [
                "Props are read-only; child components must never mutate props received from parents",
                "JSX expressions must return a single root element or React Fragment (<>...</>)",
            ],
        ),
        (
            37,
            6,
            "React State Management, Events & Conditional Rendering",
            "react-state-events-conditional-rendering",
            "Manage component state with the useState hook, handle user events, and render conditional UI elements cleanly.",
            [
                "Declare and update local component state using the useState hook",
                "Handle user events with synthetic event handlers and functional state updates",
                "Conditionally render elements using ternary operators, logical &&, and early returns",
            ],
            [
                "Never mutate state directly; always use the setter function returned by useState",
                "When new state depends on previous state, pass an updater function: setVal(prev => prev + 1)",
            ],
        ),
        (
            38,
            6,
            "Lists, Keys, Controlled Form Inputs & Validation",
            "react-lists-forms-controlled-inputs",
            "Render dynamic lists with unique stable keys, manage controlled form inputs, and implement client-side validation.",
            [
                "Render collections using array.map() and assign stable, unique key props",
                "Manage form elements (inputs, textareas, selects) as controlled components",
                "Validate user inputs on change and blur, displaying inline feedback",
            ],
            [
                "Never use array index as a key if the list can be reordered, filtered, or deleted",
                "Controlled inputs bind input value to React state and update via onChange",
            ],
        ),
        (
            39,
            6,
            "Side Effects, Data Fetching & Effect Cleanup with useEffect",
            "react-effects-and-cleanup",
            "Handle component lifecycle side effects, fetch API data on mount, manage dependencies, and implement effect cleanup.",
            [
                "Execute side effects (data fetching, subscriptions, timers) using the useEffect hook",
                "Configure effect dependency arrays correctly to prevent infinite re-render loops",
                "Return cleanup functions from useEffect to prevent memory leaks and cancel requests",
            ],
            [
                "An empty dependency array [] runs the effect once after the initial render",
                "Always clean up subscriptions, timers, or abort controllers in the return function",
            ],
        ),
        (
            40,
            6,
            "Client-Side Routing & Page Navigation with React Router",
            "react-routing-and-page-navigation",
            "Configure declarative multi-page navigation using React Router, route parameters, NavLink active states, and 404 routes.",
            [
                "Set up client-side SPA routing using BrowserRouter, Routes, and Route",
                "Extract dynamic URL parameters using the useParams hook (e.g. /curriculum/:day)",
                "Create active navigation links using NavLink and handle unknown URLs with 404 catches",
            ],
            [
                "Client-side routing eliminates full page reloads, providing snappy desktop-grade UX",
                "Use the useNavigate hook for programmatic navigation after form submissions",
            ],
        ),
        (
            41,
            6,
            "Shared State, Custom Hooks & API Service Architecture",
            "shared-state-api-services-custom-hooks",
            "Extract reusable business logic into custom hooks, centralize API calls into service modules, and manage shared state.",
            [
                "Abstract repetitive logic into custom React hooks (e.g. useTelemetry, useFetch)",
                "Organize backend API requests into centralized, type-safe service clients",
                "Lift state up or use React Context to share data across unrelated components",
            ],
            [
                "Custom hooks must start with 'use' and can compose other built-in React hooks",
                "Centralizing API calls prevents scattered fetch logic and simplifies error handling",
            ],
        ),
        (
            42,
            6,
            "Week 6 Milestone: Multi-Page Responsive Node Dashboard",
            "multipage-responsive-dashboard",
            "Build a modular React single-page application with declarative routing, telemetry metrics, and task creation forms.",
            [
                "Architect a multi-page React application with responsive navigation and dark cybersecurity aesthetic",
                "Implement controlled forms for node registration and task dispatching",
                "Complete and verify Week 6 Milestone Project",
            ],
            [
                "Component decomposition ensures each UI element has a single, testable responsibility",
                "Strict TypeScript interfaces ensure compile-time prop safety throughout the app",
            ],
        ),
        # Week 7: Databases
        (
            43,
            7,
            "Relational Database Concepts, Entities & Schema Design",
            "relational-database-concepts-schema-design",
            "Understand relational database theory, tables, columns, primary keys, foreign keys, and entity-relationship modeling.",
            [
                "Understand relational theory: tables, records, fields, and constraints",
                "Design primary keys (surrogate vs natural) and foreign key relationships",
                "Draft Entity-Relationship diagrams for devices, tasks, and telemetry data",
            ],
            [
                "Primary keys uniquely identify each row; foreign keys enforce referential integrity",
                "Good schema design minimizes data redundancy and prevents update anomalies",
            ],
        ),
        (
            44,
            7,
            "SQL CRUD Operations, Filtering, Sorting & Constraints",
            "sql-crud-filtering-sorting-constraints",
            "Write standard SQL queries: SELECT, INSERT, UPDATE, DELETE, WHERE clauses, ORDER BY, LIMIT, and table constraints.",
            [
                "Query records with SELECT, column aliasing, and WHERE filtering predicates",
                "Insert, update, and delete rows with proper WHERE condition safety",
                "Enforce data integrity with NOT NULL, UNIQUE, CHECK, and DEFAULT constraints",
            ],
            [
                "Never run UPDATE or DELETE without a WHERE clause in production environments",
                "ORDER BY and LIMIT/OFFSET enable predictable pagination for large result sets",
            ],
        ),
        (
            45,
            7,
            "SQL Joins, Aggregation Functions & Grouping",
            "sql-joins-aggregation-grouping",
            "Master table joins (INNER, LEFT, RIGHT, FULL), aggregate functions (COUNT, SUM, AVG), and GROUP BY / HAVING clauses.",
            [
                "Combine related tables using INNER JOIN and LEFT JOIN operations",
                "Calculate summary statistics using COUNT, AVG, MIN, MAX, and SUM",
                "Group aggregated results by categories using GROUP BY and filter with HAVING",
            ],
            [
                "INNER JOIN returns rows matching both tables; LEFT JOIN preserves all rows from left table",
                "WHERE filters rows before aggregation; HAVING filters aggregated groups",
            ],
        ),
        (
            46,
            7,
            "Database Normalization, Relationships & ACID Transactions",
            "normalization-relationships-transactions",
            "Normalize schemas to Third Normal Form (3NF), model 1:1, 1:N, and N:M relationships, and master ACID transactions.",
            [
                "Normalize database tables from 1NF through 3NF to eliminate anomalies",
                "Model many-to-many (N:M) relationships using junction/association tables",
                "Execute atomic multi-step operations within ACID transactions using BEGIN/COMMIT/ROLLBACK",
            ],
            [
                "ACID guarantees: Atomicity, Consistency, Isolation, and Durability",
                "Junction tables contain foreign keys pointing to both related entities",
            ],
        ),
        (
            47,
            7,
            "PostgreSQL Architecture, Roles, Schemas & Connections",
            "postgresql-roles-connections",
            "Configure PostgreSQL server, understand connection pooling, manage user roles and permissions, and handle pg_hba.conf.",
            [
                "Explore PostgreSQL enterprise architecture, storage engines, and system catalogs",
                "Create database roles, users, and grant least-privilege permissions",
                "Manage connection strings, environment variables, and connection pool sizing",
            ],
            [
                "Never connect application backends using superuser (postgres) credentials; create dedicated app roles",
                "Connection pooling (e.g. pgBouncer or SQLAlchemy pool) prevents socket exhaustion",
            ],
        ),
        (
            48,
            7,
            "Indexes, Query Execution Plans, NULL Semantics & Pagination",
            "indexes-query-plans-null-pagination",
            "Optimize query performance with B-tree indexes, analyze EXPLAIN ANALYZE execution plans, and master keyset pagination.",
            [
                "Speed up WHERE lookups and JOIN operations using B-Tree and composite indexes",
                "Inspect query execution plans with EXPLAIN ANALYZE to identify sequential scans",
                "Handle three-valued logic (TRUE, FALSE, UNKNOWN) with IS NULL and IS NOT NULL",
            ],
            [
                "Indexes accelerate read queries but add write overhead on INSERT and UPDATE",
                "Keyset pagination (WHERE id > last_seen) is vastly superior to high-offset pagination",
            ],
        ),
        (
            49,
            7,
            "Week 7 Milestone: Persistent Task & Device Relational Database",
            "persistent-task-device-database",
            "Design normalized database tables for devices, tasks, and telemetry logs with foreign keys, constraints, and indexes.",
            [
                "Implement 3NF relational schema with foreign key cascades and check constraints",
                "Write and verify multi-table queries with joins and aggregations",
                "Complete and verify Week 7 Milestone Project",
            ],
            [
                "Database constraints act as the final defense line for application data integrity",
                "Proper indexing ensures rapid sub-millisecond lookups for device heartbeats",
            ],
        ),
        # Week 8: FastAPI
        (
            50,
            8,
            "FastAPI Framework Architecture, Async Endpoints & Routing",
            "fastapi-application-and-routes",
            "Build modern async web APIs using FastAPI, Starlette, ASGI servers (Uvicorn), and declare route handlers.",
            [
                "Understand FastAPI and ASGI architecture compared to legacy WSGI frameworks",
                "Define asynchronous route handlers using async def and HTTP decorators",
                "Inspect auto-generated interactive OpenAPI documentation at /docs and /redoc",
            ],
            [
                "FastAPI is built on Starlette (for web routing) and Pydantic (for data validation)",
                "Async endpoints allow high-concurrency I/O without blocking the Python event loop",
            ],
        ),
        (
            51,
            8,
            "Path Parameters, Query Parameters & Pydantic v2 Validation",
            "parameters-pydantic-validation",
            "Validate incoming data with Pydantic v2 schemas, type hints, path parameters, query parameters, and request bodies.",
            [
                "Extract and validate URL path parameters with automatic type coercion",
                "Filter and paginate endpoints using optional query parameters with default values",
                "Define robust request and response schemas using Pydantic BaseModel and Field",
            ],
            [
                "Pydantic automatically returns detailed 422 Unprocessable Entity errors on validation failure",
                "response_model filters out sensitive internal fields before returning JSON",
            ],
        ),
        (
            52,
            8,
            "RESTful Task CRUD Endpoints & HTTP Status Code Discipline",
            "task-crud-endpoints",
            "Implement complete Create, Read, Update, Delete (CRUD) endpoints for tasks with strict HTTP status code adherence.",
            [
                "Implement POST (201 Created), GET (200 OK), PUT/PATCH (200 OK), and DELETE (204 No Content)",
                "Raise HTTPException(status_code=404, detail='Not found') on missing records",
                "Differentiate between PUT (full replacement) and PATCH (partial update)",
            ],
            [
                "DELETE endpoints should return HTTP 204 No Content with an empty response body",
                "Always raise explicit HTTPExceptions with informative, non-sensitive detail messages",
            ],
        ),
        (
            53,
            8,
            "APIRouter Modularization, Service Layer & Dependency Injection",
            "routers-service-layers-dependency-injection",
            "Structure large APIs using APIRouter, decouple business logic into service layers, and leverage FastAPI Depends().",
            [
                "Organize API endpoints into modular routers using fastapi.APIRouter",
                "Decouple HTTP controllers from business logic by introducing a dedicated service layer",
                "Use FastAPI's Dependency Injection system (Depends) to inject services and sessions",
            ],
            [
                "Dependency Injection makes testing simple through dependency_overrides in test fixtures",
                "Service layers keep route handlers concise and focused solely on HTTP concerns",
            ],
        ),
        (
            54,
            8,
            "Exception Handlers, Custom Middleware & CORS Configuration",
            "exceptions-middleware-cors-configuration",
            "Handle global exceptions with custom handlers, build request-response middleware, and configure CORS security.",
            [
                "Register global exception handlers for domain exceptions using app.exception_handler",
                "Add CORSMiddleware with strictly configured allowed origins, methods, and headers",
                "Write custom ASGI middleware for request timing and request ID generation",
            ],
            [
                "Wildcard CORS (allow_origins=['*']) with credentials enabled is invalid and insecure",
                "Middleware wraps every request/response cycle, ideal for logging and telemetry",
            ],
        ),
        (
            55,
            8,
            "SQLAlchemy 2.0 Async ORM & Database Session Management",
            "sqlalchemy-database-sessions",
            "Integrate SQLAlchemy 2.0 async engine, declarative mapped models, and provide async database sessions via Depends().",
            [
                "Configure SQLAlchemy 2.0 AsyncEngine and async_sessionmaker with aiosqlite/asyncpg",
                "Define mapped models using Mapped[] and mapped_column() type annotations",
                "Provide scoped database sessions to route handlers using an async generator dependency",
            ],
            [
                "Always yield the session within a try/finally block to ensure connections return to the pool",
                "SQLAlchemy 2.0 uses select() syntax instead of legacy query() methods",
            ],
        ),
        (
            56,
            8,
            "Week 8 Milestone: Fully Documented & Tested NeuroMatrix REST API",
            "documented-and-tested-api",
            "Develop a production-grade REST API for task scheduling and device registration with automatic OpenAPI docs and database sessions.",
            [
                "Deliver documented RESTful API with Pydantic validation and SQLAlchemy async persistence",
                "Verify endpoints using Swagger UI and automated HTTP test requests",
                "Complete and verify Week 8 Milestone Project",
            ],
            [
                "OpenAPI specification serves as the single source of truth for frontend API contracts",
                "Strict schema validation prevents malformed data from ever reaching the database",
            ],
        ),
        # Week 9: Security
        (
            57,
            9,
            "Authentication Fundamentals & Secure Password Hashing",
            "authentication-secure-password-hashing",
            "Master authentication theory, password entropy, salt mechanics, and slow cryptographic hashing (Argon2, bcrypt).",
            [
                "Differentiate between Authentication (who you are) and Authorization (what you can do)",
                "Understand why fast hashes (MD5, SHA-256) are insecure for passwords due to GPU cracking",
                "Hash and verify passwords securely using Argon2id or bcrypt with random salts",
            ],
            [
                "Never store plaintext passwords or reversible encrypted passwords in a database",
                "Argon2id is the modern industry standard, designed to resist GPU and ASIC cracking attacks",
            ],
        ),
        (
            58,
            9,
            "Stateless Token-Based Authentication & JWT Architecture",
            "token-based-authentication-jwt",
            "Architect stateless authentication using JSON Web Tokens (JWT), header/payload/signature structure, and expiry.",
            [
                "Deconstruct JWT architecture: Header (algorithm), Payload (claims), and Cryptographic Signature",
                "Sign and verify tokens using HMAC-SHA256 (HS256) or asymmetric RSA/Ed25519 (RS256)",
                "Extract and validate Bearer tokens in FastAPI using OAuth2PasswordBearer",
            ],
            [
                "JWT signatures prevent client tampering, but payloads are only Base64-encoded (not encrypted)",
                "Always set strict expiration timestamps (exp claim) to limit token lifespan",
            ],
        ),
        (
            59,
            9,
            "Role-Based Access Control (RBAC) & Endpoint Authorization",
            "roles-and-permissions-rbac",
            "Implement Role-Based Access Control (Admin, Operator, ReadOnly), permission matrices, and FastAPI route guards.",
            [
                "Define user roles and fine-grained permission matrices for application features",
                "Build reusable FastAPI dependency guards that enforce required permissions on routes",
                "Return HTTP 401 Unauthorized for missing tokens and HTTP 403 Forbidden for insufficient roles",
            ],
            [
                "401 indicates lack of valid credentials; 403 indicates valid user lacks required permission",
                "Hierarchical or claim-based RBAC allows flexible, scalable authorization rules",
            ],
        ),
        (
            60,
            9,
            "Device Identity, Machine-to-Machine Auth & API Keys",
            "device-identity-and-authorization",
            "Authenticate IoT and desktop nodes using cryptographic device keys, X-Device-Token headers, and device registries.",
            [
                "Issue unique cryptographic device tokens and public/private key pairs for node agents",
                "Authenticate machine-to-machine (M2M) API requests using custom security headers",
                "Track device revocation lists to immediately disconnect compromised nodes",
            ],
            [
                "Machine agents should not use interactive user passwords; use dedicated API keys or mTLS",
                "Store hash of device API keys in database, verifying keys via constant-time comparison",
            ],
        ),
        (
            61,
            9,
            "Web Vulnerabilities: SQLi, XSS, CSRF, SSRF & Security Headers",
            "web-vulnerabilities-sqli-xss-csrf",
            "Understand and mitigate OWASP Top 10 vulnerabilities: SQL Injection, XSS, CSRF, SSRF, and configure security headers.",
            [
                "Understand how parameterized queries prevent SQL Injection attacks",
                "Prevent Cross-Site Scripting (XSS) via content escaping and Content Security Policy (CSP)",
                "Mitigate CSRF using SameSite cookies and anti-CSRF tokens",
            ],
            [
                "SQL injection occurs when unescaped user input is concatenated into query strings",
                "ORMs and parameterized queries are the primary defense against SQL injection",
            ],
        ),
        (
            62,
            9,
            "API Rate Limiting, Secret Management & Audit Logging",
            "rate-limiting-secret-management-audit-logs",
            "Protect APIs against abuse using token bucket rate limiting, manage secrets via environment variables, and record audit logs.",
            [
                "Implement rate limiting (e.g. slowapi / Redis) to protect endpoints from brute-force attacks",
                "Keep secrets, API keys, and private certificates out of Git repositories using .env and KMS",
                "Write immutable audit log entries recording security-critical events and administrative actions",
            ],
            [
                "Audit logs must record timestamp, actor ID, action taken, and outcome without logging passwords",
                "Rate limiting protects login endpoints against credential stuffing and brute-force attacks",
            ],
        ),
        (
            63,
            9,
            "Week 9 Milestone: Hardened Device Authorization Gateway & Security Review",
            "security-review-and-negative-tests",
            "Implement an authentication gateway with JWT tokens, role-based route guards, and audit trail logging.",
            [
                "Deploy JWT authentication gateway with role-based route protection",
                "Execute negative security tests verifying rejection of forged tokens and unauthorized access",
                "Complete and verify Week 9 Milestone Project",
            ],
            [
                "Defense-in-depth requires validation at multiple layers: network, API gateway, and database",
                "Negative testing verifies that unauthorized requests fail safely and predictably",
            ],
        ),
        # Week 10: Full-Stack Integration
        (
            64,
            10,
            "Connecting React Client to FastAPI Backend Services",
            "connect-react-to-fastapi",
            "Configure API proxying, Axios/Fetch HTTP clients, unified error handling, and environment configuration in Vite.",
            [
                "Configure Vite development proxy to seamlessly route /api calls to FastAPI backend",
                "Build a centralized API client with base URLs and automatic JSON serialization",
                "Handle backend network failures and display user-friendly error banners",
            ],
            [
                "Vite proxy resolves CORS during local development by proxying requests server-side",
                "Typed API response wrappers ensure frontend state matches backend Pydantic models",
            ],
        ),
        (
            65,
            10,
            "Full-Stack Task CRUD: Creation, Editing, Deletion & Optimistic UI",
            "task-creation-editing-deletion",
            "Implement end-to-end task workflows from React UI forms through FastAPI endpoints to database persistence.",
            [
                "Create tasks in React using controlled modal forms and POST to /api/tasks",
                "Edit existing tasks with pre-populated form state and PATCH endpoints",
                "Implement delete confirmation modals and optimistic UI updates for instant feedback",
            ],
            [
                "Optimistic UI updates state immediately and rolls back if the server returns an error",
                "Always invalidate or refresh cached lists after successful mutations",
            ],
        ),
        (
            66,
            10,
            "Device Fleet Overview, Telemetry Polling & Heartbeat Badges",
            "device-overview-heartbeat-display",
            "Display registered device nodes, parse heartbeat timestamps, calculate latency, and render dynamic status badges.",
            [
                "Render fleet of registered devices with hardware telemetry (CPU, RAM, OS info)",
                "Calculate time-since-last-heartbeat and flag stale devices exceeding thresholds",
                "Render responsive status badges (ONLINE, STALE, OFFLINE) with emerald/amber/rose colors",
            ],
            [
                "Heartbeat timestamps stored in UTC eliminate timezone drift issues between server and client",
                "Periodic polling with setInterval or requestAnimationFrame keeps telemetry fresh",
            ],
        ),
        (
            67,
            10,
            "Advanced Data Tables: Filtering, Sorting, Pagination & Search",
            "filtering-sorting-pagination",
            "Implement production data tables with multi-field search, column sorting, page size selection, and URL query sync.",
            [
                "Implement server-side or client-side filtering by phase, status, and keywords",
                "Enable multi-column ascending/descending sorting on table headers",
                "Paginate large result sets with next/previous controls and URL query parameter sync",
            ],
            [
                "Syncing filters to URL search parameters (?page=2&status=completed) enables bookmarkable views",
                "Debouncing search inputs prevents spamming the backend API on every keystroke",
            ],
        ),
        (
            68,
            10,
            "Resilient UX: Loading Skeletons, Error Boundaries & Empty States",
            "loading-errors-retries-empty-states",
            "Design bulletproof frontend UX with skeleton loaders, React Error Boundaries, retry buttons, and helpful empty states.",
            [
                "Replace jarring layout shifts with sleek skeleton placeholder loaders",
                "Catch uncaught JavaScript rendering errors using React Error Boundaries",
                "Provide actionable empty states when filters return zero results, with 'Clear Filters' buttons",
            ],
            [
                "Skeleton loaders maintain layout stability and reduce perceived load times",
                "Error boundaries isolate crashed components without taking down the entire web page",
            ],
        ),
        (
            69,
            10,
            "Full-Stack Authentication UI, Protected Routes & Token Storage",
            "authentication-ui-and-protected-pages",
            "Build sign-in forms, store JWT tokens in localStorage or HTTP-only cookies, and implement protected route wrappers.",
            [
                "Create responsive login form with validation and error messaging",
                "Store JWT tokens safely and attach Authorization: Bearer <token> to outgoing requests",
                "Wrap sensitive routes in ProtectedRoute components that redirect unauthenticated users",
            ],
            [
                "Always provide a seamless logout action that clears client tokens and resets user state",
                "Token expiry should automatically redirect the user to login with an informative banner",
            ],
        ),
        (
            70,
            10,
            "Week 10 Milestone: Full-Stack NeuroMatrix Release Candidate",
            "full-stack-release-candidate",
            "Deliver a fully connected full-stack application with real-time UI updates, authenticated sessions, and error handling.",
            [
                "Integrate React frontend with FastAPI backend and SQLite/PostgreSQL database",
                "Verify end-to-end task lifecycle, device monitoring, and persistent progress",
                "Complete and verify Week 10 Milestone Project",
            ],
            [
                "A release candidate verifies that all subsystems communicate without friction",
                "End-to-end integration testing guarantees cross-tier contract fidelity",
            ],
        ),
    ]

    for day_num, week_num, title, slug, summary, objectives, key_points in phase2_catalog:
        days.append(
            {
                "day_number": day_num,
                "week_number": week_num,
                "phase_number": 2,
                "title": title,
                "slug": slug,
                "summary": summary,
                "duration_minutes": 60 if day_num not in (35, 42, 49, 56, 63, 70) else 90,
                "objectives": objectives,
                "prerequisites": [
                    f"Day {day_num - 1} concepts",
                    f"Week {week_num - 1} foundations",
                ],
                "revision_questions": [
                    f"What core architectural problem does {title.lower()} solve in full-stack applications?",
                    "How does this pattern interact with client-server data flow?",
                ],
                "concept_sections": [
                    {
                        "title": f"Engineering Deep-Dive: {title}",
                        "content": f"Modern web systems depend on {title.lower()} for high-throughput, maintainable software delivery. {key_points[0]}.",
                        "key_points": key_points,
                    },
                    {
                        "title": "Production Standards & Resilience",
                        "content": f"In the NeuroMatrix architecture, {title.lower()} ensures robust, secure communication between browser interfaces and backend infrastructure. {key_points[1]}.",
                        "key_points": [
                            "Enforce strict type boundaries across API request and response boundaries",
                            "Design resilient failure modes that guide users toward recovery",
                            "Maintain high test coverage across critical user interaction flows",
                        ],
                    },
                ],
                "code_examples": [
                    {
                        "title": f"{title} Implementation Example",
                        "description": f"Verified code pattern demonstrating {title.lower()}.",
                        "code": f"# NeuroMatrix {title} Demonstration\n# Verified architecture pattern for Day {day_num}\nprint('Day {day_num}: {title} configured successfully.')",
                        "language": "python" if week_num in (7, 8, 9) else "typescript",
                        "expected_output": f"Day {day_num}: {title} configured successfully.",
                    }
                ],
                "exercises": [
                    {
                        "id": f"ex-d{day_num}-1",
                        "title": f"Hands-on Lab: {title}",
                        "difficulty": "intermediate",
                        "instructions": f"Implement and verify the core functionality for {title.lower()} following NeuroMatrix system conventions.",
                        "starter_code": f"# Exercise Day {day_num}: {title}\n# Write your implementation here\n",
                        "solution_code": f"# Solution Day {day_num}\ndef run_lab():\n    return 'Verified: {title}'\n\nprint(run_lab())",
                        "expected_output": f"Verified: {title}",
                        "acceptance_criteria": [
                            "Adheres to clean architecture principles",
                            "Includes defensive validation and error checks",
                            "Produces verified expected output",
                        ],
                        "test_cases": [
                            "Valid input executes successfully",
                            "Error conditions are handled gracefully",
                        ],
                    }
                ],
                "common_errors": [
                    {
                        "error_type": "Integration / Syntax Error",
                        "cause": f"Common configuration or syntax pitfall when working with {title.lower()}.",
                        "fix": "Check documentation, inspect network requests, and verify variable types.",
                        "example": f"# Error encountered in {title.lower()} when constraints are violated",
                    }
                ],
                "edge_cases": [
                    "Network timeouts and disconnected database connections must be caught and retried with backoff."
                ],
                "neuromatrix_integration": {
                    "topic": f"NeuroMatrix Platform ({title})",
                    "context": "NeuroMatrix platform relies on integrated full-stack services for operations.",
                    "task_description": f"Integrate {title.lower()} into the full-stack NeuroMatrix repository.",
                    "target_component": f"services/{slug.replace('-', '_')}.py",
                    "verification_step": "Run automated checks and verify API/UI response.",
                },
                "completion_criteria": [
                    f"Mastered core concepts of {title}",
                    "Executed code exercises and verified outputs",
                    f"Passed Day {day_num} Quiz",
                ],
                "quiz_questions": [
                    {
                        "id": f"quiz-d{day_num}-q1",
                        "question_text": f"What is the key principle behind {title}?",
                        "question_type": "mcq",
                        "code_snippet": None,
                        "options": [
                            f"{key_points[0]}",
                            "It stores all user passwords in plaintext files",
                            "It replaces all HTTP protocols with raw UDP",
                            "It executes server code in the client browser without security checks",
                        ],
                        "correct_answer": f"{key_points[0]}",
                        "explanation": f"In production software engineering, {key_points[0]}.",
                    }
                ],
            }
        )

    return days
