# Postmortem: Train Ticketing and Booking System Outage (TrainBuk)

## Issue Summary:

Duration: The outage occurred on June 22, 2024, from 10:00 AM to 2:00 PM UTC.
Impact: Users were unable to access the booking system, check train schedules, or make reservations. Approximately 80% of users were affected.
Root Cause: Database server failure due to increased traffic.

## Timeline:

Issue Detected: 10:00 AM UTC
Detection Method: Monitoring alert indicating server unresponsiveness.
Actions Taken: Investigated database server, suspected capacity exceeded due to traffic surge.
Misleading Paths: Initially thought to be a network connectivity issue.
Escalation: Incident was escalated to the DevOps team for further investigation.
Resolution: Database server capacity was expanded to handle traffic influx.
## Root Cause and Resolution:

Cause: The database server failed due to a surge in user activity, exceeding its capacity to process requests.
Resolution: Database server capacity was increased, allowing for smoother processing of user transactions.

## Corrective and Preventative Measures:

Improvements/Fixes: Enhance scaling mechanisms, conduct regular load testing, improve monitoring and alerting systems.
Task List:
**Implement automatic scaling mechanisms.
Perform regular load testing to identify bottlenecks.
Enhance monitoring for early issue detection.
Develop an incident response plan.**

By addressing the root cause of the outage and implementing proactive measures, we aim to improve the system's resilience and provide uninterrupted service to users.
