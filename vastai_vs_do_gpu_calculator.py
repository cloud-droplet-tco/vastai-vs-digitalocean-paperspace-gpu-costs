#!/usr/bin/env python3
"""Vast.ai vs DigitalOcean Paperspace GPU TCO Calculator 2026."""
import argparse

def calculate(hours=100):
    # Vast.ai Spot RTX 3090 / 4090: ~$0.25 - $0.40/hr on-demand.
    vast_rate = 0.35
    vast_total = hours * vast_rate

    # DigitalOcean Paperspace: Dedicated A4000/A5000 ~$0.75 - $1.20/hr.
    paperspace_rate = 0.85
    paperspace_total = hours * paperspace_rate

    savings = paperspace_total - vast_total

    print("=" * 65)
    print(f"Vast.ai vs DigitalOcean Paperspace: {hours} Compute Hours")
    print("=" * 65)
    print(f"Vast.ai Spot GPU:          ${vast_total:.2f} (@${vast_rate:.2f}/hr)")
    print(f"DO Paperspace Dedicated:   ${paperspace_total:.2f} (@${paperspace_rate:.2f}/hr)")
    print(f"Cost Difference:           ${savings:.2f} (Vast.ai is 58.8% cheaper)")
    print(f"Reliability Assessment:    Paperspace guarantees tier-3 data center SLA")
    print("=" * 65)
    return vast_total, paperspace_total, savings

if __name__ == "__main__":
    calculate()
