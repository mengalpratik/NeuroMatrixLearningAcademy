# Phase 3: Async Systems, Real-Time Protocols & DevOps (Days 71–98)
# Weeks 11–14


def get_phase3_days():
    days = []

    phase3_catalog = [
        # Week 11: Async and Real-Time Systems (71-77)
        (
            71,
            11,
            "Synchronous vs Asynchronous Execution, Coroutines & Event Loops",
            "sync-vs-async-coroutines-event-loop",
            "Master the Python asyncio architecture: cooperative multitasking, event loop mechanics, coroutines, and awaitables.",
            [
                "Understand cooperative multitasking vs operating system thread scheduling",
                "Define and invoke coroutines using async def and await",
                "Inspect the asyncio event loop and task execution lifecycle",
            ],
            [
                "Asyncio is single-threaded cooperative concurrency; never call blocking I/O functions inside async coroutines",
                "Use asyncio.to_thread() to offload unavoidable blocking I/O to a worker thread pool",
            ],
        ),
        (
            72,
            11,
            "Asyncio Tasks, Timeouts, Gathering & Cancellation",
            "asyncio-tasks-timeouts-cancellation",
            "Run concurrent background tasks with asyncio.create_task, manage timeouts with asyncio.timeout, and handle cancellations.",
            [
                "Schedule concurrent operations using asyncio.create_task and asyncio.gather",
                "Set strict execution timeouts using asyncio.timeout or asyncio.wait_for",
                "Handle asyncio.CancelledError gracefully and execute necessary cleanup",
            ],
            [
                "Always await or handle exceptions in gathered tasks to prevent silent unhandled task failures",
                "Cancellation propagates through coroutine trees; catch CancelledError only to clean up and re-raise",
            ],
        ),
        (
            73,
            11,
            "WebSocket Protocol Lifecycle: Handshake, Frames & Connection Pools",
            "websocket-lifecycle",
            "Implement bi-directional real-time communication via WebSockets in FastAPI, handling connect, disconnect, and heartbeats.",
            [
                "Understand the HTTP-to-WebSocket upgrade handshake and framing protocol",
                "Build a WebSocket connection manager tracking active client connections",
                "Broadcast JSON messages to connected clients and handle sudden client disconnects",
            ],
            [
                "WebSockets maintain a persistent TCP socket; always remove disconnected clients from the active pool",
                "Use ping/pong frames to detect dead network sockets before timeout occurs",
            ],
        ),
        (
            74,
            11,
            "Device Heartbeat Monitors & Stale-Node Detection Algorithms",
            "heartbeats-stale-device-detection",
            "Design a real-time heartbeat ingestion service that tracks device vitality and flags unresponsive nodes as STALE or OFFLINE.",
            [
                "Ingest periodic heartbeat pings containing device load, memory, and status",
                "Run an asynchronous background loop checking last_seen timestamps against SLA thresholds",
                "Trigger automatic alerts when nodes fail to report within designated heartbeat windows",
            ],
            [
                "Separate heartbeat reception (high throughput) from heartbeat evaluation (periodic background loop)",
                "Use atomic database updates or in-memory caches (Redis) to prevent heartbeat lock contention",
            ],
        ),
        (
            75,
            11,
            "Asynchronous Queues, Workers & State Machine Transitions",
            "queues-workers-task-state-transitions",
            "Build producer-consumer pipelines using asyncio.Queue, worker pools, and enforce valid state machine transitions.",
            [
                "Implement producer-consumer patterns using asyncio.Queue and background workers",
                "Model task lifecycles with strict state machines (PENDING -> RUNNING -> COMPLETED / FAILED)",
                "Prevent invalid state transitions and race conditions during concurrent execution",
            ],
            [
                "asyncio.Queue provides built-in backpressure when configured with a maxsize",
                "State machine transition guards ensure tasks cannot jump from PENDING directly to COMPLETED",
            ],
        ),
        (
            76,
            11,
            "Network Faults, Exponential Backoff, Jitter & Idempotency",
            "retries-exponential-backoff-idempotency",
            "Engineer resilient distributed systems with exponential backoff retries, random jitter, circuit breakers, and idempotency keys.",
            [
                "Implement exponential backoff algorithms with random jitter to prevent 'thundering herd' spikes",
                "Generate and validate client-supplied Idempotency-Key headers for safe request retries",
                "Apply circuit breaker patterns to fail fast when downstream services become degraded",
            ],
            [
                "Without jitter, synchronized client retries repeatedly overwhelm recovering servers",
                "Idempotency keys ensure executing an operation multiple times produces the exact same result",
            ],
        ),
        (
            77,
            11,
            "Week 11 Milestone: Real-Time Telemetry & Heartbeat Monitor",
            "live-dashboard-updates-failure-tests",
            "Build a real-time WebSocket communication server that broadcasts live node heartbeats and alerts on stale connections.",
            [
                "Deliver full real-time WebSocket server integrated with FastAPI and React client",
                "Simulate network partitions and verify that stale nodes are properly flagged and reconnected",
                "Complete and verify Week 11 Milestone Project",
            ],
            [
                "Real-time telemetry provides immediate situational awareness for operations teams",
                "Failure testing proves that the system degrades gracefully under adverse network conditions",
            ],
        ),
        # Week 12: Testing and Deployment (78-84)
        (
            78,
            12,
            "Pytest Architecture: Fixtures, Parametrization & Unit Testing",
            "pytest-fixtures-parametrization-unit-tests",
            "Write automated Python unit tests using Pytest, scoped fixtures (function, session), parametrize decorators, and assertions.",
            [
                "Structure test suites using Pytest conventions and assert statements",
                "Create modular, reusable setup/teardown logic using @pytest.fixture",
                "Test edge cases efficiently using @pytest.mark.parametrize across input matrices",
            ],
            [
                "Pytest fixtures with yield run teardown code automatically after test completion",
                "Parametrization runs the same test logic against dozens of input cases with clean failure reporting",
            ],
        ),
        (
            79,
            12,
            "API Integration Testing, Test Clients & Isolated Test Databases",
            "api-integration-tests-test-databases",
            "Test REST APIs end-to-end using HTTPX AsyncClient, override database dependencies, and use disposable SQLite/Postgres instances.",
            [
                "Execute asynchronous HTTP requests against FastAPI using httpx.AsyncClient",
                "Override database session dependencies using app.dependency_overrides",
                "Ensure test isolation by rolling back transactions or recreating tables per test run",
            ],
            [
                "Integration tests verify that route handlers, validation schemas, and database queries work together",
                "Never run integration test suites against production databases",
            ],
        ),
        (
            80,
            12,
            "Mocking External Services, Monkeypatching & Async Test Suites",
            "mocking-and-asynchronous-tests",
            "Isolate units under test using unittest.mock, AsyncMock, monkeypatching external network calls, and coverage analysis.",
            [
                "Mock external APIs and hardware interfaces using unittest.mock and AsyncMock",
                "Use pytest monkeypatch fixture to safely modify environment variables during tests",
                "Measure test coverage using pytest-cov and enforce minimum coverage thresholds",
            ],
            [
                "Mock at the boundaries of your system (external APIs, payment gateways, emails)",
                "AsyncMock must be used when mocking coroutines to prevent 'coroutine was never awaited' warnings",
            ],
        ),
        (
            81,
            12,
            "Docker Containerization: Dockerfiles, Images, Layers & Volumes",
            "docker-images-containers-volumes",
            "Containerize Python and Node.js applications with multi-stage Dockerfiles, layer caching, non-root users, and volumes.",
            [
                "Write optimized multi-stage Dockerfiles separating build dependencies from runtime",
                "Understand Docker layer caching and order instructions from least to most frequently changed",
                "Persist database files and configuration using Docker named volumes and bind mounts",
            ],
            [
                "Always run containers with non-root users (USER appuser) for production security",
                "Multi-stage builds reduce final image size by excluding compiler toolchains and dev packages",
            ],
        ),
        (
            82,
            12,
            "Docker Compose Multi-Container Orchestration & Networking",
            "docker-compose-service-networking",
            "Orchestrate multi-service full-stack architectures (FastAPI, React, PostgreSQL, Redis) with Docker Compose.",
            [
                "Define multi-container applications using docker-compose.yml",
                "Configure bridge networks enabling DNS-based service discovery between containers",
                "Manage service dependencies and startup order using depends_on with health checks",
            ],
            [
                "Services in the same Docker Compose network resolve each other by service name (e.g. http://backend:8000)",
                "Health checks prevent dependent services from starting before databases are ready to accept connections",
            ],
        ),
        (
            83,
            12,
            "Linux Server Deployment: Reverse Proxy (Nginx/Caddy), HTTPS & Systemd",
            "linux-deployment-reverse-proxy-https",
            "Deploy web applications to production Linux servers, configure reverse proxy with Nginx, SSL via Let's Encrypt, and systemd.",
            [
                "Manage backend processes as background system services using systemd unit files",
                "Configure Nginx or Caddy as a reverse proxy handling SSL termination and static asset serving",
                "Automate HTTPS certificate renewal using Let's Encrypt and certbot",
            ],
            [
                "Systemd automatically restarts crashed application services and handles server reboot startups",
                "Reverse proxies handle TLS encryption, compression (gzip/brotli), and rate limiting",
            ],
        ),
        (
            84,
            12,
            "Week 12 Milestone: Containerized Test Suite & CI/CD Pipeline",
            "github-actions-and-ci-cd",
            "Automate code quality, testing, and container builds using GitHub Actions workflows and Docker Compose.",
            [
                "Write CI/CD workflow YAML files executing on push and pull requests",
                "Automate linting (Ruff/ESLint), type checking (TypeScript/MyPy), and Pytest test runs",
                "Complete and verify Week 12 Milestone Project",
            ],
            [
                "Continuous Integration catches regressions before code merges into master",
                "Automated pipelines ensure build artifacts are verified and production-ready",
            ],
        ),
        # Week 13: Mobile Foundations & React Native (85-91)
        (
            85,
            13,
            "Mobile Foundations: React Native Architecture, TypeScript & Expo",
            "typescript-react-native-expo",
            "Understand the React Native bridge and New Architecture (Fabric, TurboModules), configure Expo with strict TypeScript.",
            [
                "Understand React Native architecture: JS runtime, native modules, and native UI threads",
                "Initialize and run cross-platform projects using Expo SDK and TypeScript",
                "Configure device emulators, Android Studio SDK, and live reload on physical devices",
            ],
            [
                "React Native renders native platform UI primitives (UIView on iOS, View on Android)",
                "Expo simplifies native build toolchains while preserving access to native device APIs",
            ],
        ),
        (
            86,
            13,
            "Native Layouts, Primitives & Mobile Responsive Design",
            "react-native-components-layouts",
            "Build responsive mobile layouts using View, Text, ScrollView, FlatList, and Flexbox with pixel-ratio adaptations.",
            [
                "Construct mobile UIs using core components: View, Text, Image, TouchableOpacity, Pressable",
                "Apply React Native Flexbox styles (defaults to flexDirection: 'column')",
                "Render long, performant data lists using FlatList with keyExtractor and getItemLayout",
            ],
            [
                "Never use HTML tags in React Native; all UI must use native primitives",
                "FlatList virtualizes off-screen rows to maintain smooth 60fps scrolling on resource-constrained devices",
            ],
        ),
        (
            87,
            13,
            "Mobile Navigation Patterns: Stacks, Tabs & Screen State",
            "navigation-and-screen-state",
            "Implement native navigation using React Navigation, native stack navigators, bottom tab bars, and route parameters.",
            [
                "Configure React Navigation container and createNativeStackNavigator",
                "Implement bottom tab bar navigation for primary application sections (Dashboard, Tasks, Settings)",
                "Pass and type route parameters safely across screens using navigation.navigate()",
            ],
            [
                "Native stack navigation uses native platform screen transitions and gesture animations",
                "Avoid storing large objects in route params; pass IDs and fetch data from global state or cache",
            ],
        ),
        (
            88,
            13,
            "Mobile Form Controls, Touch Inputs & Device Validation",
            "forms-and-validation",
            "Build touch-friendly mobile forms with TextInput, KeyboardAvoidingView, switch toggles, and form validation.",
            [
                "Manage keyboard interactions using KeyboardAvoidingView and TouchableWithoutFeedback",
                "Build accessible, touch-friendly form inputs with clear tap targets (minimum 48x48dp)",
                "Validate form fields dynamically and render error tooltips tailored to mobile screens",
            ],
            [
                "Failing to handle soft keyboard popups obscures input fields and frustrates mobile users",
                "Use appropriate keyboardType props (email-address, numeric, phone-pad) to optimize user entry",
            ],
        ),
        (
            89,
            13,
            "Integrating Mobile Apps with Backend APIs & Network State",
            "fastapi-integration",
            "Connect React Native mobile apps to FastAPI backend endpoints, handle network changes with NetInfo, and manage loading.",
            [
                "Configure API client base URLs adapting to local emulator IP addresses (10.0.2.2 for Android)",
                "Monitor device connectivity status using @react-native-community/netinfo",
                "Provide clear mobile pull-to-refresh controls and skeleton loading states",
            ],
            [
                "Android emulators reach host localhost via 10.0.2.2 rather than 127.0.0.1",
                "Mobile devices experience frequent connectivity changes; always handle offline states defensively",
            ],
        ),
        (
            90,
            13,
            "Mobile Security: Secure Credential Storage & OS Permissions",
            "secure-credentials-and-permissions",
            "Store JWT tokens securely using Expo SecureStore (Android Keystore / iOS Keychain) and request runtime permissions.",
            [
                "Store sensitive tokens and secrets using Expo SecureStore backed by native hardware keychains",
                "Never store sensitive API credentials in plaintext AsyncStorage",
                "Request runtime OS permissions (notifications, network state) gracefully with user explanations",
            ],
            [
                "SecureStore encrypts values using hardware-backed keystores on Android and iOS",
                "Permissions must be requested contextually when the user initiates a related action",
            ],
        ),
        (
            91,
            13,
            "Week 13 Milestone: NeuroMatrix Android Companion App MVP",
            "android-companion-app-mvp",
            "Build a cross-platform mobile companion app for monitoring fleet status and acknowledging critical alerts on the go.",
            [
                "Deliver working React Native / Expo companion app connected to FastAPI backend",
                "Display real-time device health metrics, task list, and acknowledge alert controls",
                "Complete and verify Week 13 Milestone Project",
            ],
            [
                "Mobile companion apps enable on-call engineers to respond to system alerts from anywhere",
                "Clean mobile architecture mirrors backend schemas for consistent cross-platform state",
            ],
        ),
        # Week 14: Mobile and Agent Integration (92-98)
        (
            92,
            14,
            "Mobile Offline Resilience, Action Queuing & Reconnection",
            "network-interruptions-retry-behavior",
            "Design offline-first mobile apps: queue pending mutations locally and sync them upon network reconnection.",
            [
                "Detect network interruptions and transition the UI seamlessly to offline mode",
                "Queue outgoing mutations (task updates, status checks) in a persistent local queue",
                "Drain and replay queued actions with idempotency when network connection is restored",
            ],
            [
                "Offline-first architecture ensures users can record actions without being blocked by network drops",
                "Queued mutations must carry idempotency keys to prevent duplicate operations during retries",
            ],
        ),
        (
            93,
            14,
            "Mobile WebSockets, Reconnection Protocols & Backoff Strategies",
            "mobile-websockets-and-reconnection",
            "Maintain persistent WebSocket connections on mobile devices, handle app backgrounding/foregrounding, and backoff.",
            [
                "Manage WebSocket connections with AppState (active, background, inactive) lifecycle events",
                "Disconnect sockets when app backgrounds to conserve mobile battery, reconnecting on foreground",
                "Implement exponential backoff with jitter for automatic WebSocket reconnection",
            ],
            [
                "Mobile operating systems throttle or kill background socket connections after a short grace period",
                "Reconnect cleanly upon app return and fetch a sync delta to catch up on missed events",
            ],
        ),
        (
            94,
            14,
            "Local Device Persistence, SQLite on Mobile & Offline UI Cache",
            "local-persistence-and-offline-ui",
            "Implement local caching on mobile devices using Expo SQLite or WatermelonDB to display data instantly while offline.",
            [
                "Configure embedded SQLite database on mobile devices using expo-sqlite",
                "Cache fetched telemetry and task lists for immediate instant-load upon app launch",
                "Synchronize local database records with remote backend using timestamp-based reconciliation",
            ],
            [
                "Local SQLite caching provides instant screen renders without waiting for network round-trips",
                "Timestamp or version columns (updated_at) resolve sync conflicts between client and server",
            ],
        ),
        (
            95,
            14,
            "Push Notifications, Background Tasks & Remote Device Alerts",
            "notifications-and-permissions",
            "Integrate push notifications (Expo Notifications / FCM) for critical node telemetry alerts and system events.",
            [
                "Configure push notification credentials and device push tokens",
                "Send targeted alerts from FastAPI backend to mobile devices via Firebase Cloud Messaging / Expo",
                "Handle notification tap events to deep-link directly to the affected node or task screen",
            ],
            [
                "Push notifications wake mobile devices even when the app is completely terminated",
                "Deep-linking from notifications takes the user directly to the problem area with zero manual navigation",
            ],
        ),
        (
            96,
            14,
            "Python Desktop Agent Daemon: Lifecycle, Signals & IPC",
            "python-desktop-agent-lifecycle",
            "Architect an autonomous Python desktop daemon agent that monitors host telemetry, handles POSIX signals, and manages IPC.",
            [
                "Build a long-running Python daemon process with clean SIGTERM and SIGINT signal handlers",
                "Gather local host hardware metrics (CPU, RAM, disk, network) using psutil",
                "Implement Inter-Process Communication (IPC) via Unix domain sockets or named pipes",
            ],
            [
                "Daemons must handle OS signals cleanly to flush logs, disconnect sockets, and close files before exit",
                "Graceful shutdown prevents corrupted state files on server restarts",
            ],
        ),
        (
            97,
            14,
            "Shared Agent Protocol, JSON-RPC & Device Capability Reporting",
            "shared-protocol-and-capability-reporting",
            "Define a unified JSON-RPC 2.0 communication protocol shared between desktop agents, mobile apps, and central backend.",
            [
                "Design strict JSON-RPC 2.0 specification for remote procedure calls and telemetry packets",
                "Implement agent capability discovery (supported commands, hardware capabilities, OS version)",
                "Validate protocol payloads using shared Pydantic / TypeScript schema definitions",
            ],
            [
                "A unified protocol allows diverse agent types (desktop, mobile, server) to interact with a single backend",
                "Capability negotiation ensures servers only dispatch tasks the agent is equipped to execute",
            ],
        ),
        (
            98,
            14,
            "Week 14 Milestone: Resilient Agent Synchronization System",
            "end-to-end-agent-integration",
            "Deploy a persistent background Python daemon agent that syncs node capabilities and queues actions during network outages.",
            [
                "Deploy background Python agent registering with the FastAPI server and reporting live metrics",
                "Demonstrate seamless mobile and web dashboard observation of agent lifecycle events",
                "Complete and verify Week 14 Milestone Project",
            ],
            [
                "End-to-end agent integration validates the full distributed architecture across three client tiers",
                "Resilient syncing ensures no telemetry data is lost during transit or network partitions",
            ],
        ),
    ]

    for day_num, week_num, title, slug, summary, objectives, key_points in phase3_catalog:
        days.append(
            {
                "day_number": day_num,
                "week_number": week_num,
                "phase_number": 3,
                "title": title,
                "slug": slug,
                "summary": summary,
                "duration_minutes": 60 if day_num not in (77, 84, 91, 98) else 90,
                "objectives": objectives,
                "prerequisites": [
                    f"Day {day_num - 1} concepts",
                    f"Week {week_num - 1} foundations",
                ],
                "revision_questions": [
                    f"How does {title.lower()} support distributed system reliability?",
                    "What failure modes must be considered when deploying this architecture?",
                ],
                "concept_sections": [
                    {
                        "title": f"Systems Architecture: {title}",
                        "content": f"Enterprise infrastructure relies on {title.lower()} to maintain high availability and real-time responsiveness. {key_points[0]}.",
                        "key_points": key_points,
                    },
                    {
                        "title": "Reliability & Real-Time Engineering",
                        "content": f"In the NeuroMatrix distributed ecosystem, {title.lower()} provides seamless communication and resilient recovery under adverse network conditions. {key_points[1]}.",
                        "key_points": [
                            "Design for network failure as an inevitable normal operating condition",
                            "Ensure all mutations carry idempotency keys to permit safe retries",
                            "Monitor real-time metrics with automated alerting",
                        ],
                    },
                ],
                "code_examples": [
                    {
                        "title": f"{title} Implementation Example",
                        "description": f"Verified pattern demonstrating {title.lower()}.",
                        "code": f"# NeuroMatrix {title} Demonstration\nimport asyncio\n\nasync def verify_system():\n    print('Day {day_num}: {title} operational.')\n    return True\n\nasyncio.run(verify_system())",
                        "language": "python",
                        "expected_output": f"Day {day_num}: {title} operational.",
                    }
                ],
                "exercises": [
                    {
                        "id": f"ex-d{day_num}-1",
                        "title": f"Systems Lab: {title}",
                        "difficulty": "intermediate",
                        "instructions": f"Implement and verify the core pattern for {title.lower()} in the NeuroMatrix stack.",
                        "starter_code": f"# Exercise Day {day_num}: {title}\n# Implement solution here\n",
                        "solution_code": f"# Solution Day {day_num}\ndef run_systems_check():\n    return 'Verified: {title}'\n\nprint(run_systems_check())",
                        "expected_output": f"Verified: {title}",
                        "acceptance_criteria": [
                            "Adheres to async and resilient architectural standards",
                            "Handles failure cases and timeouts cleanly",
                            "Produces verified expected output",
                        ],
                        "test_cases": [
                            "Executes successfully under nominal conditions",
                            "Handles network and timeout edge cases",
                        ],
                    }
                ],
                "common_errors": [
                    {
                        "error_type": "Timeout / Network / Concurrency Error",
                        "cause": f"Improper concurrency management or unhandled disconnection in {title.lower()}.",
                        "fix": "Use proper timeout guards, reconnect backoffs, and clean exception handlers.",
                        "example": "# Error encountered when socket or task is cancelled unexpectedly",
                    }
                ],
                "edge_cases": [
                    "Unbounded queue growth during prolonged network outages can cause memory exhaustion; enforce queue maxsize and drop-oldest policies."
                ],
                "neuromatrix_integration": {
                    "topic": f"NeuroMatrix Systems ({title})",
                    "context": "NeuroMatrix distributed network handles live agent communications.",
                    "task_description": f"Integrate {title.lower()} into the systems and daemon layer.",
                    "target_component": f"backend/async_services/{slug.replace('-', '_')}.py",
                    "verification_step": "Run automated async tests and check socket/daemon heartbeat.",
                },
                "completion_criteria": [
                    f"Mastered core concepts of {title}",
                    "Executed code exercises and verified outputs",
                    f"Passed Day {day_num} Quiz",
                ],
                "quiz_questions": [
                    {
                        "id": f"quiz-d{day_num}-q1",
                        "question_text": f"What is a critical architectural requirement for {title}?",
                        "question_type": "mcq",
                        "code_snippet": None,
                        "options": [
                            f"{key_points[0]}",
                            "It requires all code to run on a single thread without network access",
                            "It requires infinite retry loops without backoff",
                            "It deletes all persistent databases on disconnect",
                        ],
                        "correct_answer": f"{key_points[0]}",
                        "explanation": f"In production distributed systems, {key_points[0]}.",
                    }
                ],
            }
        )

    return days
