# What should a funder pay to add incentives to vaccination camps?

Should a funder spend an extra **$12 per eligible child** to add family incentives to reliable vaccination camps in Bauchi, Nigeria? In a randomized trial in Rajasthan, adding incentives raised completion by **20.8 percentage points** (95% confidence interval **9.3 to 32.3**). After allowing for uncertainty in that trial and differences between settings, the central scenario implies **4.6 additional completions per 100 eligible children** in Bauchi. If the extra visit delivers a first measles dose, its direct under-five mortality benefit supports **$0.32 extra per eligible child** at GiveWell’s 6× funding bar, so I would decline the $12 bid on this evidence. If the bid also delivers the broader vaccine mix seen in northwest Nigeria, it could clear the bar at $12 if just over **41%** of the Rajasthan completion gain transfers, compared with **22%** in the central scenario. [Trial and appendices](https://www.povertyactionlab.org/sites/default/files/research-paper/Improving%20immunisation%20coverage%20in%20rural%20India.pdf) · [Funding bar](https://www.givewell.org/how-we-work/our-criteria/cost-effectiveness/cost-effectiveness-models) · [Budget calculations](results/mortality_bridge.csv)

## What changes when families receive an incentive?

The Rajasthan villages already had a regularly scheduled mobile camp. Adding lentils for vaccination and plates for completion made little difference to **starting** the series. The clearest difference was in families coming back. [Trial, Table 2](https://www.povertyactionlab.org/sites/default/files/research-paper/Improving%20immunisation%20coverage%20in%20rural%20India.pdf)

| Children aged 12–36 months in villages with camps | Camp only | Camp plus incentives |
| --- | ---: | ---: |
| At least one reported shot | 294/379 (77.6%) | 283/382 (74.1%) |
| BCG scar among children examined and classifiable | 167/334 (50.0%) | 168/336 (50.0%) |
| Completed the series among all with known shot count | 68/379 (17.9%) | 148/382 (38.7%) |
| Completed among children who started | 68/294 (23.1%) | 148/283 (52.3%) |

The scar is a physical sign of the early tuberculosis vaccine. Agreement across arms gives a second reason to doubt a large initiation gain. The last row describes dropout among observed starters. Assignment could change which families started, so that row alone cannot establish the causal effect among the same starters. [Endline file](https://dataverse.harvard.edu/api/access/datafile/1581016) · [Reconstructed outcomes](results/mechanism.csv)

**Catchment and staffing matter to the budget.** Completion in neighboring villages was 28/265 (10.6%) near camp-only sites and 61/302 (20.2%) near incentive sites. Table 3 reports a relative risk of 1.9 (95% CI 1.1–2.8). The budget credits only children in the direct catchment. Neighboring benefits could increase value if families are counted once and the added visits and supplies are costed. Camp logs recorded **4.5 versus 13.4 shots per camp-day**. Higher attendance spread fixed staff costs in the trial. At a busy clinic, the same demand could lengthen queues or displace other care. Ask for staffing, stockout and waiting-time records before pricing a rollout. [Trial, Table 3 and camp logs](https://www.povertyactionlab.org/sites/default/files/research-paper/Improving%20immunisation%20coverage%20in%20rural%20India.pdf) · [Near-camp counts](results/mechanism.csv)

## What does a completion buy in Bauchi?

An additional completion tells us that a child finished the series. The health gain depends on **which doses that child would otherwise miss and when**. GiveWell models a **5.7%** risk of death before age five from vaccine-preventable causes for an unvaccinated Bauchi child, including indirect deaths, and a **52%** reduction for its vaccine package. A child who has already received most doses has already acquired some protection. I priced two distinct service patterns. [GiveWell’s Bauchi analysis, sections 3–4](https://www.givewell.org/international/technical/programs/new-incentives)

| At the illustrative $12 incremental bid | Additional completions per $ | Under-five deaths averted per $ | Under-five deaths averted per 1,000 eligible | Value per $ relative to benchmark | Maximum extra $ per eligible child |
| --- | ---: | ---: | ---: | ---: | ---: |
| Each extra completion delivers a timely first measles dose | 0.00384 | 0.00000460 | 0.055 | 0.16× | $0.32 |
| Broad Nigerian dose pattern transfers with the completion gain | 0.00384 | 0.0000928 | 1.11 | 3.23× | $6.47 |
| Legacy sensitivity at $100 per extra completion | 0.00384 | — | — | — | $4.61 |

The first row counts direct measles deaths. GiveWell’s workbook gives a **0.173%** direct measles mortality risk after vaccination age for an unvaccinated Bauchi child and **69.1%** efficacy for a first dose. The second row credits the pattern of gains across doses in the Nigerian trial, including gains among children who never finish. GiveWell estimates a 22-point gain on its mortality-weighted coverage measure, while IDinsight found a 27-point full-completion gain. Applying their ratio to the local completion gain is a consequential assumption. Establishing a broad local dose mix could justify a larger budget. These scenarios are examples, not bounds on the true effect. [GiveWell workbook, Disease burden I208 and Vaccine efficacy H31](https://docs.google.com/spreadsheets/d/1mTKQuZRyVMie-K_KUppeCq7eBbXX15Of3jV7uo3z-PM/edit) · [Nigerian dose analysis](https://www.givewell.org/international/technical/programs/new-incentives) · [IDinsight report](https://files.givewell.org/files/DWDA%202009/NewIncentives/IDinsight_Impact_Evaluation_of_New_Incentives_Final_Report.pdf)

GiveWell changed its benchmark in **November 2025**. One unit values doubling one year’s consumption for one person starting around **$2.15/day in 2017 purchasing-power terms**. Its benchmark delivers about **0.00333 units per dollar** and its published funding bar is **6×**. This calculation values an under-five death averted at approximately **116 units**, following GiveWell’s New Incentives analysis. Divide mortality value per dollar by the benchmark. This screen omits household consumption, morbidity, benefits after age five and costs shifted to other providers. A funding decision would need those items and a local incremental bid. [Benchmark and funding policy](https://www.givewell.org/how-we-work/our-criteria/cost-effectiveness/cost-effectiveness-models) · [Benchmark calculation, B11](https://docs.google.com/spreadsheets/d/1o0l0xucYBa8rjVKwDHh_K5PZTN6GeoenaKz77bTMXa4/edit) · [Mortality valuation](https://www.givewell.org/international/technical/programs/new-incentives) · [Formulas](DESIGN.md)

**Comparison with New Incentives.** At $12 the two scenarios imply about **$217,500** and **$10,800** per under-five death averted. GiveWell’s October 2026 top-charities page reports **$4,500 per life saved** across its 2022–24 funding for New Incentives. Its Bauchi worked example puts child mortality alone at about **$3,300 per death averted**. Its November 2020 analysis estimated **5.5 under-five deaths averted per 1,000 infants in program areas**. These are modeled estimates for a broader program. They differ in year, geography, vaccine mix and denominator. Treating $4,500 as a local camp price would skip those differences. [2022–24 grant average](https://www.givewell.org/charities/top-charities) · [Bauchi case](https://www.givewell.org/international/technical/programs/new-incentives) · [2020 cohort estimate](https://www.givewell.org/international/technical/programs/new-incentives/november-2020-version)

## How much of the trial gain might transfer?

The central calculation multiplies **0.628 × 0.591 × 0.597 = 0.222**. The values below are explicit judgments anchored to data. They are neither measured probabilities nor confidence limits. The budget columns vary one assumption at a time while holding the others at their central values. [Inputs and source locations](data/bridge_inputs.csv) · [Sensitivity calculations](results/validity_sensitivity.csv)

| Adjustment and rationale | Low / central / high multiplier | Measles-only maximum, low / central / high | $100 completion maximum, low / central / high |
| --- | --- | --- | --- |
| Statistical shrinkage. Pull a single noisy estimate toward zero. Gains in the Kenyan and Nigerian trials set three possible widths for that prior belief. | 0.338 / 0.628 / 0.957 | $0.17 / $0.32 / $0.49 | $2.48 / $4.61 / $7.03 |
| Recall. A selected group with vaccination cards showed a difference between arms in net overreporting. Apply all, half, or none of that difference to the pooled estimate. | 0.183 / 0.591 / 1.000 | $0.10 / $0.32 / $0.54 | $1.43 / $4.61 / $7.80 |
| External validity. More children already complete vaccination in Bauchi, leaving fewer children for the incentive to reach. Scale by the fraction still able to gain. | 0.217 / 0.597 / 1.000 | $0.12 / $0.32 / $0.54 | $1.67 / $4.61 / $7.72 |

Rajasthan started below **2%** full immunization before the interventions. The right comparison for *adding* incentives is the **17.9%** completion achieved with reliable camps alone. The 2024 Nigeria DHS reports **51%** basic vaccination in Bauchi. This statewide survey is a proxy for what a proposed clinic would achieve without incentives. A local camp-only comparison would be more informative. [Trial, baseline and Table 2](https://www.povertyactionlab.org/sites/default/files/research-paper/Improving%20immunisation%20coverage%20in%20rural%20India.pdf) · [2024 Nigeria DHS, basic-antigen coverage map](https://health.gov.ng/wp-content/uploads/2025/10/NDHS-2024-Final-Report_Disseminated17102025.pdf) · [Construction of all nine cases](DESIGN.md)

## Why use a wider interval than the paper?

Village assignment means children attending the same camp share staffing, supply and other local conditions. The paper’s Table 2 reports **21 points (15 to 28)** using a mixed model, which makes assumptions about how outcomes vary across groups. Its archived code enters the household code first, then the village within that code. Household codes recur across villages. Re-fitting that hierarchy gives **21.16 points (14.58 to 27.75)**. Putting villages first instead gives **18.24 (7.22 to 29.25)**. This shows that the grouping assumption changes the answer. [Table 2](https://www.povertyactionlab.org/sites/default/files/research-paper/Improving%20immunisation%20coverage%20in%20rural%20India.pdf) · [Authors’ code](https://dataverse.harvard.edu/api/access/datafile/2435322) · [Hierarchy replay](audit_interval.py)

| Comparison | Gain in percentage points | Approximate 95% interval | Maximum at $100/completion, full transfer → central transfer | Trial gain needed locally for a $12 bid at $100/completion |
| --- | ---: | --- | ---: | ---: |
| Give each observed child equal weight | 20.80 | 9.34 to 32.27 | $20.80 → $4.61 | 57.7% |
| Give each observed village equal weight | 16.11 | — | $16.11 → $3.57 | 74.5% |
| Compare children within the same geographic block, account for village assignment | 21.39 | 10.71 to 32.07 | — | — |

For a bid priced per eligible child, I use the child-weighted estimate and let outcomes within a village be correlated without specifying their pattern. The block check also accounts for the geographic grouping used at randomization. Its similar interval supports using the wider range for this decision. Equal village weighting answers the question for a typical village. The table holds the adjustment factors fixed to show what weighting alone changes. [Block-adjusted calculation](results/block_robustness.csv) · [Weighting and prices](results/weighting_budget.csv)

## Other evidence

- **North West Nigeria.** IDinsight randomized **167 clinic catchments**. The New Incentives package raised strict full immunization by **27 points (95% CI 23–31)**. Education, cash and clinic support were part of the package, so this estimate cannot isolate a completion incentive on top of reliable camps. GiveWell’s 2020 projection was about **$38 per enrolled child**, compared with approximately **$18** from actual 2021–23 costs and enrollments. The 2023 figure alone was **$15.41**. Enrollment cost and cost per additional fully vaccinated child have different denominators. [Trial](https://files.givewell.org/files/DWDA%202009/NewIncentives/IDinsight_Impact_Evaluation_of_New_Incentives_Final_Report.pdf) · [Grant lookback](https://www.givewell.org/research/lookbacks/New-Incentives-2025) · [2023 spending and enrollments](https://www.givewell.org/international/technical/programs/new-incentives/september-2024-version)
- **Haryana, India.** In the authors’ 2020 evaluation, payments that rose over the vaccination schedule cost **$61 per additional fully immunized child** under the low-payment design and **$93** under the high-payment design. A payer’s spending objective can favor a different design from the one that produces the most vaccinations. The later paper found that community information hubs plus reminders performed best on immunizations per dollar. [Cost comparison, executive summary](https://files.givewell.org/files/DWDA%202009/Interventions/SMS_reminders_for_vaccination/Banerjee_et_al.%22Evaluating_the_impact_of_interventions_to_improve_full_immunisation_rates_in_Haryana_India%2C%222020.pdf) · [Later published analysis](https://economics.mit.edu/sites/default/files/2025-07/ecta200717%20%281%29.pdf)
- **Kenya.** In Gibson and colleagues’ M-SIMU trial, **364/406** children in the SMS-plus-200-shilling group completed vaccination by 12 months, compared with **332/388** receiving SMS alone and **296/360** in the control group. A setting with high initial coverage leaves less room to improve. The two Kenyan comparisons also show why it matters whether a funder is buying reminders plus cash, or adding cash to an existing service. [Gibson et al., 2017](https://pubmed.ncbi.nlm.nih.gov/28288747/)

## Before committing funds

Request a clinic-level count of **all eligible children**, all incremental costs including capacity, and dated records by dose from comparable clinics during a phased rollout. Count returning families and neighboring children once. **[[VERIFY: Establish which doses Bauchi children would otherwise miss and their timing under reliable camp-only service.]]** This is the missing evidence most likely to change which mortality scenario applies.

## Reproduce or price a bid

With Python 3.11, run from the repository root. The first block uses only the committed grouped data after installing dependencies.

```sh
python -m pip install -r requirements.txt
python analyze.py
python trial_extension.py
python grant_model.py
python verify.py
python price_bid.py --incremental-cost 12000 --eligible 1000 --ceiling 100
python figure.py
```

To rebuild the grouped inputs or reproduce the mixed-model comparison, run `python prepare_data.py` and `python audit_interval.py`. Each checks the downloaded endline file’s SHA-256 before use. The original sensitivity grid and chart remain available. [Methods and source correction](METHODS.md) · [Original budget grid](results/budget.csv) · [Original pricing chart](results/budget-threshold.png)

**Authorship.** For this revision I chose the funding question, the camp-only comparison, and the three validity adjustments to examine. AI tools helped propose the numerical scenarios, write code and draft the interpretation for my review. The judgment calls are documented in the design note. Banerjee, Duflo, Glennerster, Kothari and their partners conducted the Rajasthan trial.
