# What should a funder pay to add incentives to vaccination camps?

Should a funder spend an extra $12 per eligible child to add family incentives to reliable vaccination camps in Bauchi, Nigeria?

The Rajasthan trial found a gain of +20.8 percentage points in full-series completion (95% CI 9.3 to 32.3).

**Bottom line.** At GiveWell’s 6× funding bar, the broader vaccine mix supports $6.47 per eligible child if 22.2% of the trial gain transfers, or $9.63 at the reference assumption of 33.0%. Counting only a first measles dose gives a single-antigen floor of $0.56 or $0.83, respectively. Both comparisons include indirect under-five deaths.

**Decision.** I would decline the $12 bid on the under-five evidence. GiveWell’s full Bauchi model roughly doubles its under-five value (10.5× to 20.0×). If that same uplift applied here, the conservative ceiling would rise to $12.32. I would reconsider with local evidence on which doses children would otherwise miss, when they would miss them, and the costs of delivering them.

[Trial and appendices](https://www.povertyactionlab.org/sites/default/files/research-paper/Improving%20immunisation%20coverage%20in%20rural%20India.pdf) · [Funding bar](https://www.givewell.org/how-we-work/our-criteria/cost-effectiveness/cost-effectiveness-models) · [Under-five calculations](results/mortality_bridge.csv) · [Broader-benefit sensitivity](results/package_scope.csv)

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

An additional completion tells us a child finished the series. The health gain depends on the visits the incentive actually added. In Rajasthan the largest differences were at the third and fourth shots. Measles accounted for about 5.4% of the modeled direct risk of dying from vaccine-preventable diseases in an unvaccinated Bauchi child (0.173% out of 3.23%). The multi-dose case therefore leads the comparison. [Trial, discussion](https://www.povertyactionlab.org/sites/default/files/research-paper/Improving%20immunisation%20coverage%20in%20rural%20India.pdf) · [Disease burden, I208–I209](https://docs.google.com/spreadsheets/d/1mTKQuZRyVMie-K_KUppeCq7eBbXX15Of3jV7uo3z-PM/edit)

| Under-five protection credited | Share of trial gain retained | Deaths averted per 1,000 eligible | Value at the $12 bid, relative to benchmark | Maximum extra per eligible child at 6× |
| --- | ---: | ---: | ---: | ---: |
| Broader Nigerian dose pattern | 22.2% (conservative) | 1.11 | 3.23× | $6.47 |
| Broader Nigerian dose pattern | 33.0% (reference) | 1.66 | 4.81× | $9.63 |
| First measles dose only | 22.2% (conservative) | 0.097 | 0.28× | $0.56 |
| First measles dose only | 33.0% (reference) | 0.144 | 0.42× | $0.83 |

**How to read the table.** Both scenarios include 0.75 indirect deaths for each direct death. The package risk already includes them. The measles floor assumes a timely first dose that would otherwise be missed. It can overstate the benefit of a visit that merely happens earlier. The package calculation assumes the Nigerian pattern of gains across doses also applies in Bauchi, including doses received by children who never finish the series. [Mortality calculations](results/mortality_bridge.csv)

**How broad would benefits have to be?** The multi-dose case needs 41.1% of the trial gain to transfer for under-five benefits alone to cover the $12 bid. GiveWell’s full Bauchi Simple CEA rises from 10.5× for under-five mortality to 20.0× after other benefits and program adjustments. Applying that ratio illustratively lowers break-even retention to 21.6%. At 22.2% retention, that would just clear the bid. The camp proposal has no local estimate of these additional benefits or program adjustments. [Simple CEA, rows 21–41](https://docs.google.com/spreadsheets/d/1mTKQuZRyVMie-K_KUppeCq7eBbXX15Of3jV7uo3z-PM/edit) · [Break-even calculation](results/package_scope.csv)

**Where the dose mix comes from.** The 0.22 / 0.27 ratio combines GiveWell’s estimate of the Nigerian trial’s gain in weighted vaccination coverage with IDinsight’s 2020 strict-completion gain. GiveWell’s 2020 and 2021 analyses also reported a 22-point adjusted gain using their earlier method. I pair these older trial estimates with December 2024 Bauchi inputs of 5.7% under-five vaccine-preventable mortality and 52% package efficacy. This cross-vintage calculation is an assumption about the camp’s dose mix. [Nigerian trial, p. 28](https://files.givewell.org/files/DWDA%202009/NewIncentives/IDinsight_Impact_Evaluation_of_New_Incentives_Final_Report.pdf) · [GiveWell’s 2020 interpretation](https://www.givewell.org/international/technical/programs/new-incentives/november-2020-version) · [December 2021 analysis](https://www.givewell.org/international/technical/programs/new-incentives/december-2021-version) · [Dose weighting](https://www.givewell.org/international/technical/programs/new-incentives) · [December 2024 workbook](https://docs.google.com/spreadsheets/d/1mTKQuZRyVMie-K_KUppeCq7eBbXX15Of3jV7uo3z-PM/edit)

GiveWell changed its benchmark in **November 2025**. One unit values doubling one year’s consumption for one person starting around **$2.15/day in 2017 purchasing-power terms**. Its benchmark delivers about **0.00333 units per dollar** and its published funding bar is **6×**. This calculation values an under-five death averted at approximately **116 units**, following GiveWell’s New Incentives analysis. Divide mortality value per dollar by the benchmark. This screen omits household consumption, morbidity, benefits after age five and costs shifted to other providers. A funding decision would need those items and a local incremental bid. [Benchmark and funding policy](https://www.givewell.org/how-we-work/our-criteria/cost-effectiveness/cost-effectiveness-models) · [Benchmark calculation, B11](https://docs.google.com/spreadsheets/d/1o0l0xucYBa8rjVKwDHh_K5PZTN6GeoenaKz77bTMXa4/edit) · [Mortality valuation](https://www.givewell.org/international/technical/programs/new-incentives) · [Formulas](DESIGN.md)

**Why New Incentives itself clears the bar.** GiveWell’s Bauchi example models the full New Incentives program at $18.21 per enrolled child and 20.0× its benchmark. Its adjustments cover deaths after age five (+18%), developmental income (+28%), consumption (+5%), other program effects (+50%), grantee factors (−7%), leverage (−4%) and displacement of other funding (−9%). The camp bid buys only the addition of incentives and is priced per eligible child, including those who never enroll. Transferring the full program’s value requires evidence about those differences. [Simple CEA, H10 and rows 21–41](https://docs.google.com/spreadsheets/d/1mTKQuZRyVMie-K_KUppeCq7eBbXX15Of3jV7uo3z-PM/edit)

## How much of the trial gain might transfer?

I account for sampling uncertainty, possible reporting bias and the number of children a camp could still reach. In the reference case, 0.628 × 0.880 × 0.597 gives 33.0% retention, or 6.9 additional completions per 100 eligible children. Keeping the earlier conservative reporting assumption gives 22.2% retention, or 4.6 per 100. These are projections for Bauchi. The trial measured the effect in Rajasthan. [Inputs](data/bridge_inputs.csv) · [Sensitivity calculations](results/validity_sensitivity.csv)

| Adjustment | Low / reference / high multiplier | How the reference value was chosen |
| --- | --- | --- |
| Statistical shrinkage | 0.338 / 0.628 / 0.957 | The Kenyan incentive-plus-reminder versus control difference sets the width of a prior centered on zero. |
| Internal validity | 0.183 / 0.880 / 1.000 | I borrow GiveWell’s 12% discount for its Nigerian trial as a reference judgment. |
| External validity | 0.217 / 0.597 / 1.000 | I scale by the fraction still missing basic vaccination in Bauchi relative to the Rajasthan camp-only arm. |

The Rajasthan card comparison covered 169 children. Differences in overreporting (+9 points) and underreporting (−8 points) yield a 17-point stress test. The intervals overlap and the authors found no evidence of differential social-desirability bias. Applying half the gap gives the conservative internal-validity multiplier of 0.591. Applying the whole gap gives 0.183. Neither measures the bias in the full sample. [Appendix 1, Table A3](https://www.povertyactionlab.org/sites/default/files/research-paper/Improving%20immunisation%20coverage%20in%20rural%20India.pdf) · [Main CEA, H29](https://docs.google.com/spreadsheets/d/1mTKQuZRyVMie-K_KUppeCq7eBbXX15Of3jV7uo3z-PM/edit)

Rajasthan camp-only completion was 17.9%. Nigeria’s 2024 DHS Table 10.4 reports 51.4% basic-antigen coverage among Bauchi children aged 12–23 months. For comparability with the earlier sensitivity, the model uses the 51% displayed on Map 10.1. Statewide coverage is a proxy for what comparable clinics would achieve under reliable camp-only service. [DHS, Table 10.4 and Map 10.1](https://health.gov.ng/wp-content/uploads/2025/10/NDHS-2024-Final-Report_Disseminated17102025.pdf) · [Scenario design](DESIGN.md)

## Why use a wider interval than the paper?

Village assignment means children attending the same camp share staffing, supply and other local conditions. The paper’s Table 2 reports **21 points (15 to 28)** using a mixed model, which makes assumptions about how outcomes vary across groups. Its archived code enters the household code first, then the village within that code. Household codes recur across villages. Re-fitting that hierarchy gives **21.16 points (14.58 to 27.75)**. Putting villages first instead gives **18.24 (7.22 to 29.25)**. This shows that the grouping assumption changes the answer. [Table 2](https://www.povertyactionlab.org/sites/default/files/research-paper/Improving%20immunisation%20coverage%20in%20rural%20India.pdf) · [Authors’ code](https://dataverse.harvard.edu/api/access/datafile/2435322) · [Hierarchy replay](audit_interval.py)

| Comparison | Gain in percentage points | Approximate 95% interval | Maximum at $100/completion, full transfer → reference transfer | Trial gain needed locally for a $12 bid at $100/completion |
| --- | ---: | --- | ---: | ---: |
| Give each observed child equal weight | 20.80 | 9.34 to 32.27 | $20.80 → $6.86 | 57.7% |
| Give each observed village equal weight | 16.11 | — | $16.11 → $5.32 | 74.5% |
| Compare children within the same geographic block, account for village assignment | 21.39 | 10.71 to 32.07 | — | — |

For a bid priced per eligible child, I use the child-weighted estimate and let outcomes within a village be correlated without specifying their pattern. The block check also accounts for the geographic grouping used at randomization. Its similar interval supports using the wider range for this decision. Equal village weighting answers the question for a typical village. The table holds the adjustment factors fixed to show what weighting alone changes. [Block-adjusted calculation](results/block_robustness.csv) · [Weighting and prices](results/weighting_budget.csv)

## Other evidence

- **North West Nigeria.** IDinsight randomized 167 clinic catchments. Its package raised strict full immunization by 27 points (95% CI 23–31). It combined cash, education and clinic support. GiveWell’s April 2020 grant page reports that the cost per enrolled child fell from about $39 in 2020 to about $18 in 2024. [IDinsight trial](https://files.givewell.org/files/DWDA%202009/NewIncentives/IDinsight_Impact_Evaluation_of_New_Incentives_Final_Report.pdf) · [GiveWell’s grant update](https://www.givewell.org/research/incubation-grants/new-incentives/april-2020-grant)
- **Haryana, India.** In the authors’ 2020 evaluation, payments that rose over the vaccination schedule cost **$61 per additional fully immunized child** under the low-payment design and **$93** under the high-payment design. A payer’s spending objective can favor a different design from the one that produces the most vaccinations. The later paper found that community information hubs plus reminders performed best on immunizations per dollar. [Cost comparison, executive summary](https://files.givewell.org/files/DWDA%202009/Interventions/SMS_reminders_for_vaccination/Banerjee_et_al.%22Evaluating_the_impact_of_interventions_to_improve_full_immunisation_rates_in_Haryana_India%2C%222020.pdf) · [Later published analysis](https://economics.mit.edu/sites/default/files/2025-07/ecta200717%20%281%29.pdf)
- **Kenya.** In Gibson and colleagues’ M-SIMU trial, **364/406** children in the SMS-plus-200-shilling group completed vaccination by 12 months, compared with **332/388** receiving SMS alone and **296/360** in the control group. A setting with high initial coverage leaves less room to improve. The two Kenyan comparisons also show why it matters whether a funder is buying reminders plus cash, or adding cash to an existing service. [Gibson et al., 2017](https://pubmed.ncbi.nlm.nih.gov/28288747/)

## Before committing funds

Request a clinic-level count of **all eligible children**, all incremental costs including capacity, and dated records by dose from comparable clinics during a phased rollout. Count returning families and neighboring children once. **Key open field question.** Which doses would Bauchi children otherwise miss, and when, under reliable camp-only service? This is the missing evidence most likely to change which mortality scenario applies.

## Reproduce or price a bid

With Python 3.11+, run from the repository root. The first block uses only the committed grouped data after installing dependencies.

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

**Authorship.** I chose the funding question and camp-only comparison and take responsibility for the final model assumptions, statistical verification and funding judgment. AI tools helped with Python scaffolding and drafting under my review. Banerjee, Duflo, Glennerster, Kothari and their partners conducted the Rajasthan trial.
