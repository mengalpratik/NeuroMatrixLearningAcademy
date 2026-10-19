# Phase 4: Production Engineering & Capstone Release (Days 99–112)
# Weeks 15–16


def get_phase4_days():
    days = []

    phase4_catalog = [
        # Week 15: Production Engineering (99-105)
        (
            99,
            15,
            "Structured JSON Logging, Correlation IDs & Distributed Tracing",
            "structured-logging-correlation-ids",
            "Implement production structured logging (structlog/JSON), inject request-scoped correlation IDs, and enable distributed tracing.",
            [
                "Emit machine-readable JSON logs with standard keys (timestamp, level, message, context)",
                "Generate and propagate unique correlation IDs across all service boundaries",
                "Trace distributed requests across API, worker, and agent subsystems",
            ],
            [
                "Plain text logs are impossible to search efficiently at scale; always format logs as structured JSON",
                "Correlation IDs link multiple log lines across different services to a single user request",
            ],
        ),
        (
            100,
            15,
            "Production Metrics, Prometheus Scraping, Health & Readiness Probes",
            "metrics-health-checks-alerts",
            "Expose application metrics (/metrics) for Prometheus scraping, define Grafana dashboards, and create Kubernetes-style probes.",
            [
                "Implement /health/live (liveness) and /health/ready (readiness) probe endpoints",
                "Export RED metrics (Rate, Errors, Duration) using the Prometheus client library",
                "Configure alerting thresholds for error rate spikes and latency degradation",
            ],
            [
                "Liveness checks verify the process is alive; readiness checks verify the app can serve traffic (DB connected)",
                "Never perform heavy database queries inside high-frequency liveness probes",
            ],
        ),
        (
            101,
            15,
            "Database Migrations with Alembic, Backup & Point-in-Time Recovery",
            "database-backup-restore-migrations",
            "Manage zero-downtime database schema migrations using Alembic, automate pg_dump backups, and practice point-in-time recovery.",
            [
                "Generate and review automated schema migration revisions with Alembic",
                "Execute safe online migrations (adding nullable columns or defaults without table locks)",
                "Automate daily encrypted backups using pg_dump and test disaster recovery procedures",
            ],
            [
                "Never deploy schema changes that break backward compatibility with the currently running application code",
                "Unverified backups are not real backups; routinely test restoring from backup files",
            ],
        ),
        (
            102,
            15,
            "In-Memory Caching with Redis, Eviction Policies & Cache Invalidation",
            "redis-and-caching",
            "Implement caching layers using Redis, design cache-aside and write-through patterns, and handle cache invalidation.",
            [
                "Deploy Redis for sub-millisecond query caching and session state storage",
                "Implement cache-aside pattern: check cache first, query database on miss, populate cache with TTL",
                "Invalidate affected cache keys atomically when underlying database entities are mutated",
            ],
            [
                "Always set Time-To-Live (TTL) on cached entries to prevent stale data accumulation",
                "Cache stampedes occur when high-traffic keys expire; use probabilistic early expiration or mutex locks",
            ],
        ),
        (
            103,
            15,
            "Queue Delivery Guarantees, Dead-Letter Queues & Worker Concurrency",
            "queue-delivery-worker-concurrency",
            "Design resilient message processing pipelines (Celery/ARQ/Redis Streams), manage concurrency, and handle dead-letter queues.",
            [
                "Understand delivery semantics: at-most-once, at-least-once, and effectively-once",
                "Route poison messages that fail repeatedly to a Dead-Letter Queue (DLQ) for manual inspection",
                "Scale worker pool concurrency to process background tasks without overwhelming database connection limits",
            ],
            [
                "At-least-once delivery requires background task handlers to be strictly idempotent",
                "Uncaught task exceptions without dead-letter queues cause infinite failure loops",
            ],
        ),
        (
            104,
            15,
            "System Architecture, Capacity Planning & High Availability",
            "architecture-and-system-design",
            "Design high-availability distributed systems, model system throughput, identify single points of failure, and plan capacity.",
            [
                "Analyze end-to-end system architectures using C4 model diagrams (Context, Container, Component, Code)",
                "Perform back-of-the-envelope capacity calculations (QPS, bandwidth, storage growth)",
                "Eliminate single points of failure (SPOF) with redundant services and database failover",
            ],
            [
                "Premature optimization wastes engineering effort; focus on clear interfaces and observability",
                "Design systems to gracefully degrade non-critical features during peak load",
            ],
        ),
        (
            105,
            15,
            "Week 15 Milestone: High-Availability Production Telemetry Gateway",
            "reliability-and-recovery-exercises",
            "Integrate structured JSON logging, Redis query caching, Prometheus /metrics endpoints, and database connection pooling.",
            [
                "Deliver fully observable production gateway with Redis caching and Prometheus telemetry",
                "Simulate database failover and verify that read caches serve traffic during outages",
                "Complete and verify Week 15 Milestone Project",
            ],
            [
                "Production engineering separates hobbyist scripts from resilient enterprise platforms",
                "Chaos and recovery testing proves system reliability under real-world distress",
            ],
        ),
        # Week 16: Capstone Release (106-112)
        (
            106,
            16,
            "Codebase Audit, Technical Debt Identification & Issue Prioritization",
            "codebase-audit-issue-prioritization",
            "Conduct a comprehensive architectural review of the entire NeuroMatrix repository, identifying technical debt and bugs.",
            [
                "Audit backend, frontend, and daemon codebases for security, performance, and style consistency",
                "Create and prioritize GitHub/issue tracker backlog using MoSCoW prioritization (Must, Should, Could, Won't)",
                "Establish clear sprint goals for the Capstone release candidate",
            ],
            [
                "Code audits should balance immediate critical bug fixes against long-term maintainability",
                "Prioritizing fixes by user impact and risk prevents wasted cycles on trivial refactors",
            ],
        ),
        (
            107,
            16,
            "Independent Bug Fixing, Regression Testing & Defensive Hardening",
            "independent-bug-fixing-regression-tests",
            "Tackle identified issues independently, write reproducing regression tests, and harden edge-case handling.",
            [
                "Write automated tests that reliably reproduce discovered defects before writing fixes",
                "Apply minimal, focused fixes that resolve the root cause without introducing side-effects",
                "Run full test regression suites to ensure no existing functionality was broken",
            ],
            [
                "Always write a failing regression test first to verify the bug and prevent future recurrences",
                "Refactor only after the fix is verified and tests are passing green",
            ],
        ),
        (
            108,
            16,
            "User Experience Refinement: Dashboard Polish & Workflow Ergonomics",
            "improve-dashboard-mobile-workflow",
            "Refine the user experience across web dashboard and mobile companion: micro-interactions, responsive polish, and keyboard shortcuts.",
            [
                "Polish layout spacing, responsive breakpoints, typography contrast, and visual hierarchy",
                "Add productive developer shortcuts (global search modal, quick day jumping, hotkeys)",
                "Streamline common operator workflows to reduce friction and clicks",
            ],
            [
                "Ergonomic software respects developer time through intuitive shortcuts and fast keyboard navigation",
                "Consistent design tokens and feedback states create a professional, trustworthy application feel",
            ],
        ),
        (
            109,
            16,
            "End-to-End Security Audit, Penetration Testing & Dependency Hardening",
            "security-and-reliability-review",
            "Audit dependencies for known CVEs (pip-audit, npm audit), test authorization boundaries, and review secret handling.",
            [
                "Scan all Python and Node.js dependencies for known vulnerabilities and CVEs",
                "Verify that no authorization bypasses exist across API routes and WebSocket endpoints",
                "Confirm zero secrets, keys, or internal tokens exist in git history or client bundles",
            ],
            [
                "Automated dependency scanning in CI prevents introducing known vulnerable libraries",
                "Defense-in-depth requires verifying security at the transport, application, and database layers",
            ],
        ),
        (
            110,
            16,
            "End-to-End Task Lifecycle Execution & Verification",
            "end-to-end-task-execution-verification",
            "Execute the complete end-to-end task workflow: dispatch from UI, receipt by desktop agent, execution, and live reporting.",
            [
                "Dispatch a task from the React web dashboard or mobile companion app",
                "Trace the task through FastAPI database persistence to the WebSocket broadcast",
                "Observe the Python desktop agent pick up the task, simulate execution, and report final status back to the UI",
            ],
            [
                "End-to-end verification proves that all architectural tiers work in concert as a unified platform",
                "Verify that state remains consistent across web, mobile, database, and background daemons",
            ],
        ),
        (
            111,
            16,
            "Comprehensive Documentation, Architecture Diagrams & Deployment Guides",
            "documentation-and-release-preparation",
            "Author exhaustive production documentation, operational playbooks, architecture diagrams, and release notes.",
            [
                "Write comprehensive README, API documentation, and architecture decision records (ADRs)",
                "Draft standard operating procedures (SOPs) for common maintenance tasks and incident recovery",
                "Publish verified release notes detailing new features, fixes, and migration guides",
            ],
            [
                "Documentation is an integral deliverable of professional software engineering",
                "Clear architecture diagrams help new engineers understand system topology immediately",
            ],
        ),
        (
            112,
            16,
            "Final Capstone Milestone: Practical Engineering Assessment & Release Delivery",
            "practical-engineering-assessment",
            "Finalize and deliver the full NeuroMatrix production platform with zero critical bugs, verified documentation, and release artifacts.",
            [
                "Execute all automated test suites (backend, frontend, integration) with 100% passing results",
                "Verify application startup, database initialization, and persistent progress tracking from scratch",
                "Complete and celebrate the 112-Day NeuroMatrix Learning Academy Full-Stack Journey!",
            ],
            [
                "The capstone demonstrates complete mastery of full-stack Python, React, databases, async systems, and DevOps",
                "A production-ready release reflects dedication, technical discipline, and end-to-end craft",
            ],
        ),
    ]

    for day_num, week_num, title, slug, summary, objectives, key_points in phase4_catalog:
        days.append(
            {
                "day_number": day_num,
                "week_number": week_num,
                "phase_number": 4,
                "title": title,
                "slug": slug,
                "summary": summary,
                "duration_minutes": 60 if day_num not in (105, 112) else 120,
                "objectives": objectives,
                "prerequisites": [
                    f"Day {day_num - 1} concepts",
                    f"Week {week_num - 1} foundations",
                ],
                "revision_questions": [
                    f"How does {title.lower()} prepare the platform for real-world enterprise release?",
                    "What are the primary operational verification steps?",
                ],
                "concept_sections": [
                    {
                        "title": f"Production Engineering: {title}",
                        "content": f"Enterprise platforms rely on {title.lower()} to maintain bulletproof reliability and clear operational visibility. {key_points[0]}.",
                        "key_points": key_points,
                    },
                    {
                        "title": "Release Standards & Verification",
                        "content": f"In the NeuroMatrix Capstone release, {title.lower()} provides verified quality assurance and production readiness. {key_points[1]}.",
                        "key_points": [
                            "Verify all operational behaviors against explicit acceptance criteria",
                            "Maintain zero known unhandled exceptions across critical workflows",
                            "Deliver clean, self-contained, and thoroughly documented software",
                        ],
                    },
                ],
                "code_examples": [
                    {
                        "title": f"{title} Verification Example",
                        "description": f"Verified code pattern demonstrating {title.lower()}.",
                        "code": f"# NeuroMatrix Production Release: Day {day_num}\ndef verify_release_step():\n    print('Day {day_num}: {title} verified for production release.')\n    return 0\n\nverify_release_step()",
                        "language": "python",
                        "expected_output": f"Day {day_num}: {title} verified for production release.",
                    }
                ],
                "exercises": [
                    {
                        "id": f"ex-d{day_num}-1",
                        "title": f"Capstone Lab: {title}",
                        "difficulty": "advanced",
                        "instructions": f"Perform the technical implementation and verification for {title.lower()} following Capstone standards.",
                        "starter_code": f"# Capstone Exercise Day {day_num}: {title}\n# Implement production verification logic\n",
                        "solution_code": f"# Solution Day {day_num}\ndef verify_production_quality():\n    return 'Release Verified: {title}'\n\nprint(verify_production_quality())",
                        "expected_output": f"Release Verified: {title}",
                        "acceptance_criteria": [
                            "Meets high-availability and production standards",
                            "Passes all defensive quality and regression checks",
                            "Produces verified expected output",
                        ],
                        "test_cases": [
                            "Executes cleanly in production mode",
                            "Telemetry and diagnostics confirm health",
                        ],
                    }
                ],
                "common_errors": [
                    {
                        "error_type": "Production Deployment / Release Error",
                        "cause": f"Oversight in production configuration or missing environment variables for {title.lower()}.",
                        "fix": "Review release checklist, verify environment variables, and check operational logs.",
                        "example": f"# Error encountered when deploying {title.lower()} without required config",
                    }
                ],
                "edge_cases": [
                    "Zero-downtime releases require backward-compatible database schemas until all legacy instances have been drained."
                ],
                "neuromatrix_integration": {
                    "topic": f"NeuroMatrix Production Release ({title})",
                    "context": "NeuroMatrix production ecosystem deployment and verification.",
                    "task_description": f"Integrate and verify {title.lower()} in the production release candidate.",
                    "target_component": f"capstone/{slug.replace('-', '_')}.py",
                    "verification_step": "Run full test suite and verify clean production build.",
                },
                "completion_criteria": [
                    f"Mastered core concepts of {title}",
                    "Executed code exercises and verified outputs",
                    f"Passed Day {day_num} Quiz",
                ],
                "quiz_questions": [
                    {
                        "id": f"quiz-d{day_num}-q1",
                        "question_text": f"What is the primary role of {title} in a production software release?",
                        "question_type": "mcq",
                        "code_snippet": None,
                        "options": [
                            f"{key_points[0]}",
                            "It bypasses all testing and deploys directly to production",
                            "It prevents developers from reading error logs",
                            "It resets all user databases every hour",
                        ],
                        "correct_answer": f"{key_points[0]}",
                        "explanation": f"In production software engineering, {key_points[0]}.",
                    }
                ],
            }
        )

    return days
