# Customer Churn Analysis: Executive Summary

## Key Findings

### 🚨 Critical Business Metrics

- **Overall Churn Rate:** 26.5%
- **Revenue at Risk:** $1,66 million annually
- **High-Risk Segments Identified:** 3 customer groups

![Financial Impact Analysis](../figures/01_Customer%20Churn%20Rate%20Analysis%20Graph.png)

# Revenue Risk based on customer segments

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

![Revenue Risk by segment graph](../figures/revenue%20risk%20by%20segment.png)

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

# Revenue risk based on contract lenght

![Revenue risk by contract length](../figures/revenue%20risk%20by%20contract.png)

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

# Revenue risk based on payment method

![Revenue risk by paymet method](../figures/revenue%20risk%20by%20payment%20method.png)

| Payment Method | Total Customers | Churned Customers | Total Monthly Revenue | Avg Monthly Charge | Churn Rate | Annual Revenue at Risk |
|----------------|-----------------|-------------------|----------------------|-------------------|------------|----------------------|
| Electronic check | 2,365 | 1,071 | $180,345 | $76.26 | 45.3% | $980,039 |
| Mailed check | 1,612 | 308 | $70,794 | $43.92 | 19.1% | $162,317 |
| Bank transfer (automatic) | 1,544 | 258 | $103,745 | $67.19 | 16.7% | $208,028 |
| Credit card (automatic) | 1,522 | 232 | $101,232 | $66.51 | 15.2% | $185,170 |

### Risk Level Classification

| Risk Level | Payment Methods | Churn Rate Range | Revenue Impact |
|------------|-----------------|------------------|----------------|
| 🔴 High Risk | Electronic check | 45.3% | $980,039 |
| 🟡 Medium Risk | Mailed check | 19.1% | $162,317 |
| 🟢 Low Risk | Bank transfer, Credit card | 15.2% - 16.7% | $393,198 |

### 🚨 Critical Payment Method Findings

- **Electronic check** represents the highest churn risk at **45.3%**
- **Annual revenue loss** from electronic check users: **$980,039** (63% of total payment-related losses)
- **Automatic payment methods** show significantly better retention:
  - Credit card (automatic): 15.2% churn
  - Bank transfer (automatic): 16.7% churn
- **Payment friction hypothesis**: Manual payment methods correlate with higher churn
- **Opportunity**: Migrating electronic check users could save **$490,000+ annually**

### 💡 Strategic Recommendations

1. **Immediate**: Launch electronic check user migration campaign
2. **Incentivize**: Offer discounts for automatic payment adoption
3. **Investigate**: Payment process friction for electronic check users
4. **Target**: Focus retention efforts on electronic check customer segment

# Revenue risk based on adopted services

![Revenue risk by adopted services](../figures/revenue%20risk%20by%20service%20amount.png)

| Internet Service | Total Customers | Churned Customers | Avg Monthly Charge | Total Monthly Revenue | Churn Rate | Annual Revenue at Risk |
|-----------------|-----------------|-------------------|-------------------|----------------------|------------|----------------------|
| Fiber optic | 3,096 | 1,297 | $78.89 | $244,320 | 41.9% | $1,228,067 |
| DSL | 2,421 | 459 | $56.47 | $136,705 | 19.0% | $310,656 |
| No | 1,526 | 113 | $37.13 | $56,653 | 7.4% | $50,292 |

### Churn rate by number of adopted services

| Total Services | Customers | Churned | Avg Monthly | Churn Rate | Annual Revenue at Risk |
|----------------|-----------|---------|-------------|------------|----------------------|
| 0 | 159 | 25 | $32.90 | 15.7% | $9,870 |
| 1 | 1,110 | 274 | $43.58 | 24.7% | $143,191 |
| 2 | 1,367 | 390 | $58.12 | 28.5% | $271,609 |
| 3 | 1,351 | 383 | $67.35 | 28.4% | $309,350 |
| 4 | 1,240 | 344 | $73.91 | 27.7% | $304,763 |
| 5 | 1,070 | 302 | $79.11 | 28.2% | $286,459 |
| 6 | 846 | 211 | $85.59 | 24.9% | $216,499 |
| 7 | 900 | 240 | $95.22 | 26.7% | $273,633 |

### Individual Service Analysis

| Service | Total Customers | Churned Customers | Churn Rate |
|---------|-----------------|-------------------|------------|
| StreamingMovies | 2,732 | 1,062 | 38.9% |
| StreamingTV | 2,707 | 1,039 | 38.4% |
| TechSupport | 2,044 | 671 | 32.8% |
| OnlineBackup | 2,429 | 783 | 32.2% |
| DeviceProtection | 2,496 | 803 | 32.2% |
| OnlineSecurity | 2,019 | 615 | 30.5% |
| PhoneService | 6,361 | 1,726 | 27.1% |

### Risk Level Classification

| Risk Level | Service Categories | Churn Rate Range | Primary Action Needed |
|------------|-------------------|------------------|----------------------|
| 🔴 Critical | Fiber Internet, Streaming Services | 38.9% - 41.9% | Immediate intervention |
| 🟡 Medium | 2-5 Service Bundles, Tech Support | 27.7% - 32.8% | Strategy optimization |
| 🟢 Low | No Internet, Phone Service | 7.4% - 27.1% | Maintain current approach |

### 🚨 Critical Service Adoption Findings:

#### Internet Service Impact:
- **Fiber optic customers** show the highest churn at **41.9%** (vs 19.0% for DSL)
- **Fiber optic revenue at risk**: **$1,228,067 annually** (77% of internet-related losses)
- **No internet service** customers have the lowest churn at **7.4%**

#### Service Bundle Analysis:
- **Optimal service count**: 0 services (15.7% churn) - indicates base service retention
- **Highest risk**: 2-3 services (28.4-28.5% churn)
- **Service bundle paradox**: More services don't always mean better retention
- **6 services**: Sweet spot at 24.9% churn for bundled customers

#### Individual Service Performance:
- **Most problematic services**: 
  - Streaming Movies (38.9% churn)
  - Streaming TV (38.4% churn)
- **Best performing service**: Phone Service (27.1% churn)
- **Security services** show better retention than entertainment services

### 💡 Strategic Recommendations

1. **Fiber Service Investigation**:
   - Immediate quality and pricing review for fiber optic
   - Customer satisfaction analysis for fiber users
   - Consider service level improvements

2. **Service Bundle Optimization**:
   - Reconsider bundling strategy effectiveness
   - Focus on 6-service packages (best bundled retention)
   - Investigate why 2-3 service bundles perform poorly

3. **Entertainment Service Strategy**:
   - Review streaming service value proposition
   - Consider streaming service pricing and quality
   - Bundle entertainment services more effectively

4. **Revenue Protection**:
   - Priority focus on fiber customers (highest revenue impact)
   - Develop retention programs for 2-3 service customers
   - Investigate service adoption friction points
