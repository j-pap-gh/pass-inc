from typing import List

from .models import IncomeStream, IncomeSummary, Recommendation


def period_to_year_multiplier(period: str) -> float:
    period = period.lower()
    if period == "daily":
        return 365
    if period == "weekly":
        return 52
    if period == "monthly":
        return 12
    if period == "yearly":
        return 1
    # default to monthly if unknown
    return 12


def summarize_income(streams: List[IncomeStream], currency: str = "USD") -> IncomeSummary:
    yearly_total = 0.0
    for s in streams:
        yearly_total += s.amount_per_period * period_to_year_multiplier(s.period)
    monthly_total = yearly_total / 12
    return IncomeSummary(total_monthly=monthly_total, total_yearly=yearly_total, currency=currency)


def baseline_recommendations(streams: List[IncomeStream]) -> List[Recommendation]:
    """
    Simple heuristics-based recommendations (non-AI).
    Later you can layer AI/paywalled logic on top.
    """
    total_yearly = summarize_income(streams).total_yearly

    recs: List[Recommendation] = [
        Recommendation(
            title="Start a simple digital product",
            description=(
                "Create a low-maintenance digital product (template, ebook, or mini-course) "
                "and sell it on existing platforms. Start small and iterate."
            ),
            difficulty="beginner",
            estimated_monthly=50.0,
            category="digital products",
            paywalled=False,
        ),
        Recommendation(
            title="Automate savings into index funds/ETFs",
            description=(
                "Set up an automatic monthly investment into a diversified index fund or ETF. "
                "This is a common foundation for long-term passive income."
            ),
            difficulty="beginner",
            estimated_monthly=0.0,  # investment, not income
            category="investing",
            paywalled=False,
        ),
    ]

    # Example: show an advanced, paywalled idea when user already has some income
    if total_yearly > 1000:
        recs.append(
            Recommendation(
                title="Advanced content & audience funnel",
                description=(
                    "Design a multi-step content funnel (newsletter, YouTube, or blog) "
                    "feeding into a higher-ticket product. Use analytics to optimize."
                ),
                difficulty="advanced",
                estimated_monthly=300.0,
                category="audience building",
                paywalled=True,
            )
        )

    return recs
