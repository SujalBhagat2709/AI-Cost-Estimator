# AI Cost Estimator

## Overview

AI Cost Estimator is a terminal-based Python application that estimates the cost of AI API usage across multiple Large Language Models (LLMs).

It calculates request costs based on input tokens, output tokens, selected AI model, and request volume while maintaining estimation history and usage statistics.

The project demonstrates AI API cost planning, budgeting, and usage analysis.

---

## Features

- AI Model Selection
- Input Token Cost
- Output Token Cost
- Multiple Request Estimation
- Cost Breakdown
- Estimation History
- Usage Statistics
- JSON Storage

---

## Project Structure

ai-cost-estimator/

├── cost_estimator.py

├── estimation_studio.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

```bash
python estimation_studio.py
```

---

## Menu

```
1. Estimate AI Cost

2. View Cost History

3. Cost Statistics

4. Delete History

5. Exit
```

---

## Supported Models

- GPT-4o
- GPT-4.1
- GPT-4.1 Mini
- GPT-5
- GPT-5 Mini
- Gemini 2.5 Flash
- Claude Sonnet

---

## Example

Model

```
GPT-5
```

Input Tokens

```
12000
```

Output Tokens

```
3500
```

Requests

```
250
```

---

## Output

```
Estimated Cost

$9.05

Average Cost Per Request

$0.0362
```

---

## Statistics

```
Estimations : 12

Total Requests : 4200

Total Estimated Cost : $146.287500

Average Estimate : $12.190625
```

---

## Generated Files

cost_history.json

Stores estimation history.

---

## Applications

- AI API Budget Planning
- Token Cost Estimation
- LLM Cost Analysis
- AI Project Budgeting
- AI Usage Monitoring
- Cost Forecasting

---

## Future Improvements

- Monthly Cost Forecast
- Daily Usage Tracker
- Budget Alerts
- Currency Conversion
- Provider Comparison
- Cost Optimization Suggestions
- Token Estimation From Text
- Batch Cost Estimation
- CSV Report Export
- Cost Trend Charts
- Team Usage Analytics
- Model Recommendation Based on Budget

---

## License

MIT License