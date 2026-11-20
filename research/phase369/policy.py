"""Phase369 repair candidate: pending-aware Pareto exploration.

Source/clock/evidence authorization is inherited from the frozen Phase368 policy.
This code proposes investigations only. It does not authenticate receipts,
execute tasks, score truth, or promote theorem status.
"""
from __future__ import annotations

from math import log, sqrt
from polybandit import PolyBandit, ContractError, Arm, Receipt, dominates


class PendingParetoBandit(PolyBandit):
    """Never reschedule an arm while its earlier requested work is pending.

    Cost is still an explicit Pareto coordinate, but optimistic rates are not
    hard-clipped to 1 before comparing arms. A diagnostic/closure *confidence
    index* is not itself a probability or a theorem-confidence estimate.
    """
    def __init__(self, config, approved_receipts=None):
        super().__init__(config, approved_receipts)
        self.pending: dict[str, int] = {}

    def objectives(self, arm: Arm) -> tuple[float, float, float]:
        s = self.state[arm.id]
        n = s.observations
        bonus = sqrt(2.0 * log(2.0 + self.epoch) / (1 + n))
        diag = (0.5 + s.diagnostic_hits) / (1 + n) + bonus
        closure = (0.5 + s.closure_hits) / (1 + n) + bonus
        return diag, closure, -float(arm.cost)

    def choose(self, budget: int, include_human: bool = True,
               phase: str = 'meso', include_contrast: bool = False) -> Arm:
        feasible = [a for a in self.eligible(budget, include_human, phase,
                                            include_contrast)
                    if a.id not in self.pending]
        if not feasible:
            raise ContractError('no new feasible work: existing arms await approved results')
        unseen = [a for a in feasible if self.state[a.id].selections == 0]
        if unseen:
            chosen = min(unseen, key=lambda a: (a.cost, a.id))
        else:
            scores = {a.id: self.objectives(a) for a in feasible}
            frontier = [a for a in feasible if not any(
                dominates(scores[b.id], scores[a.id])
                for b in feasible if b.id != a.id)]
            chosen = min(frontier, key=lambda a: (self.state[a.id].observations,
                                                 self.state[a.id].selections,
                                                 a.cost, a.id))
        self.state[chosen.id].selections += 1
        self.epoch += 1
        self.pending[chosen.id] = self.epoch
        self.ledger.append(('requested_pending', chosen.id))
        return chosen

    def observe(self, proposed: Receipt) -> None:
        if proposed.arm not in self.pending:
            raise ContractError('no outstanding selected investigation for receipt')
        super().observe(proposed)
        del self.pending[proposed.arm]
        self.ledger.append(('resolved_pending', proposed.arm))

    def export(self) -> dict:
        out = super().export()
        out['pending'] = sorted(self.pending)
        return out
