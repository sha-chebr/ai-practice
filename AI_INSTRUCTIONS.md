# AI Assistant Instructions

This document provides guidelines for AI assistants working in this data engineering workspace. Follow these instructions to provide consistent and effective assistance.

## Project Overview

This is a data engineering practice project that:
- Generates sample retail data
- Processes data using PySpark
- Loads data into PostgreSQL
- Uses Airflow for workflow orchestration

## Key Components to Consider

### 1. Data Pipeline Structure
```
Generator → CSV Files → PySpark ETL → PostgreSQL
```
When working with pipeline components:
- Verify data file locations in `/data`
- Check PySpark script in `/scripts/etl_pyspark.py`
- Review DAG definition in `/dags/etl_dag.py`

### 2. Technology Stack Awareness
When providing assistance, consider:
- Docker and Docker Compose environment
- Python 3.11 compatibility
- PySpark requirements (including Java dependencies)
- Airflow 2.8.4 specifics
- PostgreSQL interaction patterns

### 3. Critical Files and Directories

```
workspace
├── dags/
│   └── etl_dag.py         # Airflow DAG definitions
├── data/
│   ├── customers.csv      # Input datasets
│   ├── orders.csv
│   └── products.csv
├── docker/
│   └── airflow/
│       └── Dockerfile     # Container configuration
├── scripts/
│   ├── etl_pyspark.py    # Main ETL logic
│   └── generate_data.py   # Data generation script
└── docker-compose.yml     # Service orchestration
```

## Guidelines for AI Assistance

### 1. Error Resolution
When helping with errors:
1. Check logs in `/logs` directory
2. Verify Docker container status
3. Validate Java/PySpark environment
4. Ensure database connectivity
5. Review Airflow task configurations

### 2. Code Modifications
When modifying code:
1. Preserve existing error handling
2. Maintain logging patterns
3. Follow PySpark best practices
4. Consider Airflow task dependencies
5. Validate Docker environment impact

### 3. Environment Management
When working with the environment:
1. Use docker-compose commands for service management
2. Verify Dockerfile changes impact all services
3. Consider PostgreSQL port mappings (5433)
4. Check Airflow web interface accessibility (port 9090)

### 4. Data Handling
When working with data:
1. Respect the established schema
2. Maintain data types consistency
3. Consider sample data generation patterns
4. Validate ETL transformations
5. Check PostgreSQL table definitions

## Best Practices

### 1. Docker Operations
```bash
# Preferred build command
docker compose build

# Starting services
docker compose up -d

# Stopping services
docker compose down
```

### 2. Code Changes
- Keep PySpark transformations readable
- Maintain clear DAG task dependencies
- Document any schema changes
- Update logs appropriately

### 3. Testing Considerations
- Verify ETL pipeline end-to-end
- Check data quality after transformations
- Validate Airflow task execution
- Ensure proper error handling

## Common Issues to Watch

1. Java Environment
- JAVA_HOME configuration
- JDK availability in containers
- PySpark Java gateway connection

2. Data Pipeline
- File paths in containers
- Data type mismatches
- Transform logic errors
- PostgreSQL connection issues

3. Airflow Configuration
- DAG scheduling
- Task dependencies
- Resource availability
- Log accessibility

## Support and Documentation

Reference these resources when providing assistance:
1. Local project documentation in `startup.md`
2. Apache Airflow 2.8.4 documentation
3. PySpark 3.4.1 documentation
4. PostgreSQL 15 documentation

## Versioning and Updates

When making changes:
1. Document significant updates
2. Update version-specific references
3. Maintain backwards compatibility
4. Consider impact on all components

## Security Considerations

1. Never expose:
- Database credentials
- Airflow admin passwords
- Internal network details
- Sensitive data patterns

2. Always:
- Use environment variables for secrets
- Follow least privilege principles
- Validate input data
- Maintain secure defaults

---

Note: Keep this file updated as the project evolves. Changes to core components should be reflected here to maintain effective AI assistance.