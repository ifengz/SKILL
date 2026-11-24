---
name: btreview
description: Use when the user asks for read-only BaoTa/BT Panel, 宝塔, Linux server, deployed service, reverse proxy, Docker, PM2, port, log, disk, SSH, browser-terminal, or fixed health endpoint inspection without changing production state.
---

# BaoTa Review

Review production state from evidence without modifying it. This Skill only investigates and reports. Start from the fixed production entry point and named service; treat the user's suspected cause as a hypothesis, not the diagnosis.

## Hard Boundary

Never edit files, reload or restart services, install packages, change panel settings, invoke `bt` / `btcli` actions, create backups, clean disk, rotate logs, alter Chrome/SSH access, inspect browser secrets, or prepare a mutation sequence.

Never print passwords, private keys, tokens, database URLs, `.env` contents, cookies, saved credentials, or full config dumps. Redact evidence.

Never use temporary IP:port probes, random port scans, TLS bypass, broad network discovery, or panel-terminal guesswork to decide whether a database is broken. Database conclusions need fixed-entry, runtime/proxy, and dependency evidence.

## Scope Gate

Before running checks, identify:

- target host;
- named domain, service, process, container, or panel area;
- requested question;
- fixed health URL or port when the issue is externally reachable;
- expected healthy result.

Stop if the target, expected result, or safe fixed entry point is unknown. Do not reuse a past server or project by default. If deployed code or config is being interpreted, read the nearest repository `AGENTS.md` or `CLAUDE.md` first.

If the user suggests a cause such as "database is broken", first verify the fixed public entry point for the named service, then check only the smallest runtime/proxy/dependency surface needed to explain that result.

## Evidence Rules

Every reported fact needs a command/action record and readable output. A submitted command, click, focused terminal, exit code, or panel success toast is not enough.

Evidence levels:

- `semantic`: complete relevant terminal output is readable from text/DOM/accessibility.
- `visual`: an authorized screenshot visibly shows command markers, key output, end marker, and prompt.
- `unverified`: output is missing, partial, obscured, unreadable, or not tied to the intended host.

For BaoTa browser terminal, wrap compact read-only checks:

```bash
printf '__BT_REVIEW_BEGIN_<nonce>__\n'
# minimal read-only checks for the stated question only
printf '__BT_REVIEW_END_<nonce>__\n'
```

If output cannot be read, do one screenshot/read attempt and stop as `unverified`. Never OCR, infer, reconstruct, or send extra server commands to compensate.

## Access Path

- Prefer Codex Chrome integration for the user's already logged-in BaoTa tab.
- Use authorized SSH only when the user supplied it and host identity can be proved.
- Treat BaoTa web terminal as canvas/xterm, not a semantic text API.
- Use Playwright or Chrome DevTools only for isolated browser tests or explicit web-debugging. They do not inherit the Codex Chrome extension session.

Do not inspect browser storage, profiles, cookies, passwords, or session files. Do not create another panel login because the current path lacks evidence. Do not enable Chrome remote debugging to bridge tool boundaries.

## Minimal Check Menu

Run only the smallest group that answers the question.

Host identity, only when needed:

```bash
id
hostname
date -Is
uname -srmo
```

Fixed public entry point, when supplied:

```bash
curl --fail --silent --show-error --max-time 10 \
  --output /dev/null --write-out '%{http_code} %{time_total}\n' \
  'https://<expected-domain>/<health-path>'
```

Runtime/proxy, only for the named target:

```bash
systemctl is-active <service>
systemctl status <service> --no-pager --lines=50
journalctl -u <service> --since '30 minutes ago' --no-pager --lines=100

nginx -t
systemctl is-active nginx

docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
docker compose ps

pm2 status
```

Database dependency, only when runtime/log evidence points there or the user explicitly scoped the review to database health:

```bash
systemctl is-active <database-service>
journalctl -u <database-service> --since '30 minutes ago' --no-pager --lines=80
```

Capacity, only when capacity is in scope:

```bash
df -hT
df -ih
free -h
journalctl --disk-usage
```

Do not use `pm2 env`, broad `ps`, `docker inspect`, response-body dumps, unbounded logs, unknown health paths, TLS bypass, port scans, or temporary IP:port probes when the fixed domain is the real target.

## Output Contract

Report:

- target and timestamp;
- exact checks run;
- fixed-entry result, if checked;
- named runtime/proxy/capacity state, only if checked;
- relevant error signature, if present;
- evidence level: `semantic`, `visual`, or `unverified`;
- explicit `no changes made`;
- next smallest read-only check when uncertainty remains.

Do not claim production is normal unless the expected entry point and required runtime dependencies are both verified. Do not claim a terminal command succeeded merely because it was submitted. Do not claim "database broken" unless the evidence specifically supports it; report "not yet verified" instead of inferring a cause from symptoms.

## Stop Conditions

Stop rather than compensating when authentication fails, host identity differs, output is unreadable, the fixed health endpoint is unknown, the review would require secrets/session data/remote-debugging changes/writes, or the safe read-only path is unavailable. Return the failed check and exact evidence. Do not silently switch host, port, IP, tool, or diagnosis.

## Official BaoTa Sources

Use current BaoTa documentation for version-sensitive panel behavior and APIs:

- https://docs.bt.cn/llms.txt
- https://docs.bt.cn/user-guide/xterm/
- https://docs.bt.cn/getting-started/bt-command-line-tool/
- https://docs.bt.cn/api/xterm/

BaoTa officially documents panel-AI skills `btpanel`, `btwaf`, and `btpanel_mail`, plus the OpenClaw security-review Skill `btclawscan`. They belong to BaoTa/OpenClaw; they are not Codex-installable replacements for this Skill. Do not import them or grant their panel/API permissions under `$btreview`.
