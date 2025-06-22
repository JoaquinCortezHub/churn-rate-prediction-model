# Customer Churn Analysis: Executive Summary

## Key Findings

### 🚨 Critical Business Metrics

- **Overall Churn Rate:** 26.5%
- **Revenue at Risk:** $1,66 million annually
- **High-Risk Segments Identified:** 3 customer groups

### Critical insights by segment

- **High Value (+$80):**
    Total customers: 2,677
    Churned: 199 (34%)

- **Medium Value ($50-79):**
    Total customers: 2,072
    Churned: 598 (28.9%)

- **Low-Medium Value ($30-49):**
    Total customers: 641
    Churned: 199 (31%)

- **Low Value (<$30):**
    Total customers: 1,653
    Churned: 162 (9.8%)

> [!WARNING]
> TOTAL ANNUAL REVENUE AT RISK: **USD 1,662,777**

- High Value (+$80) Segment:
   - Risk Level: 🔴 HIGH RISK (34.0% churn)
   - Customer Base: 2,677 customers
   - Average Monthly Value: $95.36
   - Customers Lost: 910
   - Annual Revenue at Risk: **$1,041,340**

- Medium Value ($50-79) Segment:
   - Risk Level: 🟡 MEDIUM RISK (28.9% churn)
   - Customer Base: 2,072 customers
   - Average Monthly Value: $66.55
   - Customers Lost: 598
   - Annual Revenue at Risk: **$477,577**

- Low-Medium Value ($30-49) Segment:
   - Risk Level: 🔴 HIGH RISK (31.0% churn)
   - Customer Base: 641 customers
   - Average Monthly Value: $42.74
   - Customers Lost: 199
   - Annual Revenue at Risk: **$102,057**

- Low Value (<$30) Segment:
   - Risk Level: 🟢 LOW RISK (9.8% churn)
   - Customer Base: 1,653 customers
   - Average Monthly Value: $21.50
   - Customers Lost: 162
   - Annual Revenue at Risk: **$41,803**

### Recommendations based on insights

- **ALERT #1**: High Value (+$80)
   - Churn Rate: 34.0% (ABOVE 25% THRESHOLD)
   - Revenue at Risk: $1,041,340 annually
   - Recommended Action: **IMMEDIATE RETENTION STRATEGY**
- **ALERT #2**: Medium Value ($50-79)
   - Churn Rate: 28.9% (ABOVE 25% THRESHOLD)
   - Revenue at Risk: $477,577 annually
   - Recommended Action: **IMMEDIATE RETENTION STRATEGY**
- **ALERT #3**: Low-Medium Value ($30-49)
   - Churn Rate: 31.0% (ABOVE 25% THRESHOLD)
   - Revenue at Risk: $102,057 annually
   - Recommended Action: **IMMEDIATE RETENTION STRATEGY**

## Revenue risk based on contract lenght

| Contract Type     | Total Customers | Churned Customers | Total Monthly Revenue | Avg Monthly Charge | Avg Tenure | Churn Rate | Annual Revenue Lost |
|:------------------|-------------------:|---------------------:|-------------------------:|----------------------:|--------------:|--------------:|----------------------:|
| Two year          | 1,695              | 48                   | $103,006                 | $61                   | 56.74         | 2.8%          | $35,004               |
| Month-to-month    | 3,875              | 1,655                | $257,294                 | $66                   | 18.04         | 42.7%         | $1,318,674            |
| One year          | 1,473              | 166                  | $95,817                  | $65                   | 42.04         | 11.3%         | $129,577              |

### Key contract insights

1. Month-to-month contracts lose **$1,318,674** annually
2. This represents **88.9%** of total revenue loss
3. Contract length is a **critical retention factor**
4. Longer contracts significantly reduce churn risk

### Recommended Actions

- Immediate contract strategy review needed
- Consider incentives for longer-term contracts
- Target month-to-month customers with retention campaigns
