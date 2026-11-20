"""Phase368: constrained Pareto research allocator, NOT a proof or truth scorer.

No model calls, network, GitHub mutations, claim-status changes, or background work.
Local typed worldlets and costs determine which *audit task* to inspect next.
Outcome events may update routing statistics only via a separate approved-receipt
registry supplied by an external verifier; this class cannot authorize claims.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from math import log, sqrt
from pathlib import Path
from typing import Mapping
import argparse
import json


class ContractError(ValueError):
    pass


@dataclass(frozen=True)
class Worldlet:
    id: str
    carrier: str
    geometry: str
    algebra: str
    state: str
    clocks: tuple[str, ...]
    observers: tuple[str, ...]
    boundary: str
    remainder_types: tuple[str, ...]
    source: str


@dataclass(frozen=True)
class Hyperedge:
    id: str
    participants: tuple[str, ...]
    obligation: str


@dataclass(frozen=True)
class Arm:
    id: str
    worldlet: str
    purpose: str
    cost: int
    source: str
    scope: str
    hyperedge: str
    transport: str
    remainder: str
    execution: str


@dataclass(frozen=True)
class Receipt:
    id: str
    arm: str
    source: str
    scope: str
    validator: str
    diagnostic: bool
    closure: bool


@dataclass
class ArmState:
    selections: int = 0
    observations: int = 0
    diagnostic_hits: int = 0
    closure_hits: int = 0


def dominates(a: tuple[float, ...], b: tuple[float, ...]) -> bool:
    """Pareto comparison; no universal scalar reward."""
    return all(x >= y for x, y in zip(a, b)) and any(x > y for x, y in zip(a, b))


class PolyBandit:
    def __init__(self, config: dict, approved_receipts: Mapping[str, Receipt] | None = None):
        self.frozen_source = str(config['frozen_source'])
        self.worldlets = {x['id']: Worldlet(**x) for x in config['worldlets']}
        self.hyperedges = {x['id']: Hyperedge(x['id'], tuple(x['participants']), x['obligation'])
                           for x in config['hyperedges']}
        self.arms = {x['id']: Arm(**x) for x in config['arms']}
        self.state = {key: ArmState() for key in self.arms}
        self.approved_receipts = dict(approved_receipts or {})
        self.seen: set[str] = set()
        self.ledger: list[tuple[str, str]] = []
        self.epoch = 0  # research actions, not a physical derivative clock
        self._validate_contract(config)

    def _validate_contract(self, config: dict) -> None:
        if len(self.worldlets) < 3 or len({c for w in self.worldlets.values() for c in w.clocks}) < 2:
            raise ContractError('plural worldlets and clocks are mandatory')
        if len(self.worldlets) != len(config['worldlets']) or len(self.arms) != len(config['arms']):
            raise ContractError('duplicate worldlet or arm ID')
        if len(self.hyperedges) != len(config['hyperedges']):
            raise ContractError('duplicate hyperedge ID')
        for w in self.worldlets.values():
            if not w.remainder_types or not w.boundary or not w.observers:
                raise ContractError('worldlet lacks observer or typed boundary')
        for e in self.hyperedges.values():
            if len(e.participants) < 3 or len(set(e.participants)) != len(e.participants):
                raise ContractError('hyperedge must have 3 distinct participants')
            if not set(e.participants).issubset(self.worldlets):
                raise ContractError('hyperedge references missing worldlet')
        for a in self.arms.values():
            if a.worldlet not in self.worldlets or a.hyperedge not in self.hyperedges:
                raise ContractError('arm references unknown worldlet/hyperedge')
            if (self.worldlets[a.worldlet].source != a.source
                    and a.purpose != 'contrast'):
                raise ContractError('arm crosses incompatible source Worldlet')
            if a.worldlet not in self.hyperedges[a.hyperedge].participants:
                raise ContractError('arm worldlet absent from its triadic obligation')
            if a.cost < 1 or a.transport not in {'exact', 'lossy', 'forbidden'}:
                raise ContractError('invalid cost or transport')
            if a.execution not in {'local', 'human'}:
                raise ContractError('invalid execution authority')
            if a.transport == 'exact' and a.remainder != 'none':
                raise ContractError('exact transport requires zero typed remainder')
            if a.transport != 'exact' and a.remainder == 'none':
                raise ContractError('lossy or forbidden transport must name remainder')
            if a.purpose == 'field_review' and (a.transport != 'lossy' or a.execution != 'human'):
                raise ContractError('field review is a request, not exact theorem transport')
        for x in ('clocks','evidence','observables','falsifiers','tendrils','identity','dynamics'):
            if x not in config:
                raise ContractError('missing architecture field: ' + x)
        if not {'fast', 'meso', 'review'}.issubset({x['id'] for x in config['clocks']}):
            raise ContractError('must distinguish fast, meso and external review clocks')

    def eligible(self, budget: int, include_human: bool = True, phase: str = 'meso',
                 include_contrast: bool = False) -> list[Arm]:
        if budget < 0 or phase not in {'fast', 'meso', 'review'}:
            raise ContractError('invalid budget or clock phase')
        active_clocks = ({'fast'} if phase == 'fast' else
                         {'fast','meso'} if phase == 'meso' else
                         {'fast','meso','review'})
        return [a for a in self.arms.values()
                if a.cost <= budget and a.transport != 'forbidden'
                and (a.source == self.frozen_source or
                     (include_contrast and a.purpose == 'contrast'))
                and (include_human or a.execution != 'human')
                and bool(active_clocks.intersection(self.worldlets[a.worldlet].clocks))
                and (a.execution != 'human' or phase == 'review')]

    def objectives(self, arm: Arm) -> tuple[float, float, float]:
        """Heuristic optimistic objectives: validated diagnostic and closure yields, minus cost.

        These are empirical scheduling indices, NOT posterior belief in the theorem;
        no regret bound for this nonstationary, correlated setting is asserted.
        """
        s = self.state[arm.id]
        bonus = sqrt(2 * log(2 + self.epoch) / (1 + s.observations))
        diagnostic = min(1.0, (1 + s.diagnostic_hits) / (2 + s.observations) + bonus)
        closure = min(1.0, (1 + s.closure_hits) / (2 + s.observations) + bonus)
        return (diagnostic, closure, -float(arm.cost))

    def frontier(self, budget: int, phase: str = 'meso',
                 include_contrast: bool = False) -> list[Arm]:
        feasible = self.eligible(budget, phase=phase,
                                 include_contrast=include_contrast)
        return [a for a in feasible if not any(
            dominates(self.objectives(b), self.objectives(a))
            for b in feasible if b.id != a.id)]

    def choose(self, budget: int, include_human: bool = True, phase: str = 'meso',
               include_contrast: bool = False) -> Arm:
        feasible = self.eligible(budget, include_human, phase, include_contrast)
        if not feasible:
            raise ContractError('no feasible arm for this budget and source')
        unseen = [a for a in feasible if self.state[a.id].selections == 0]
        if unseen:  # explicit initial coverage before any empirical optimization
            chosen = min(unseen, key=lambda a: (a.cost, a.id))
        else:
            frontier = [a for a in feasible if not any(
                dominates(self.objectives(b), self.objectives(a))
                for b in feasible if b.id != a.id)]
            chosen = min(frontier, key=lambda a: (self.state[a.id].selections,
                                                 a.cost, a.id))
        self.state[chosen.id].selections += 1
        self.epoch += 1
        self.ledger.append(('selected', chosen.id))
        return chosen

    def observe(self, proposed: Receipt) -> None:
        """Only an *out-of-process approved receipt* may change routing statistics.

        The bandit cannot authenticate the external registry itself, prove a field
        theorem, or grant an evidence-level promotion. A user-editable registry
        is a test fixture, not independent authority.
        """
        trusted = self.approved_receipts.get(proposed.id)
        if trusted is None or trusted != proposed or proposed.id in self.seen:
            raise ContractError('unapproved, altered, or repeated audit receipt')
        arm = self.arms.get(proposed.arm)
        if arm is None or arm.source != proposed.source or arm.scope != proposed.scope:
            raise ContractError('audit source and claim scope do not match arm')
        if proposed.validator not in {'lean_kernel', 'prolog_exact', 'human_external', 'fixture'}:
            raise ContractError('unrecognized validator')
        if proposed.closure and proposed.validator in {'prolog_exact', 'fixture'}:
            raise ContractError('finite or synthetic check cannot close a theorem')
        if arm.purpose == 'field_review' and proposed.validator != 'human_external':
            raise ContractError('field semantics need external independent review')
        if proposed.closure and not (
                (arm.worldlet == 'proof.lean' and proposed.validator == 'lean_kernel'
                 and proposed.scope == 'encoded_lemma') or
                (arm.purpose == 'field_review' and proposed.validator == 'human_external'
                 and proposed.scope == 'field_301_semantic')):
            raise ContractError('validator cannot discharge an obligation in this worldlet')
        self.seen.add(proposed.id)
        s = self.state[arm.id]
        s.observations += 1
        s.diagnostic_hits += int(proposed.diagnostic)
        s.closure_hits += int(proposed.closure)
        self.ledger.append(('audited_observation', proposed.id))

    def export(self) -> dict:
        # Only selection statistics; this API has NO field for promoted claims.
        return {'frozen_source': self.frozen_source, 'epoch': self.epoch,
                'states': {k: vars(v) for k,v in sorted(self.state.items())},
                'ledger': self.ledger}


def load(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding='utf-8'))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', default=str(Path(__file__).with_name('manifest.json')))
    parser.add_argument('--budget', type=int, default=4)
    parser.add_argument('--rounds', type=int, default=5)
    parser.add_argument('--phase', choices=['fast','meso','review'], default='meso')
    parser.add_argument('--include-contrast', action='store_true', default=False)
    args = parser.parse_args()
    b = PolyBandit(load(args.manifest))
    for _ in range(args.rounds):
        a = b.choose(args.budget, phase=args.phase,
                     include_contrast=args.include_contrast)
        print(json.dumps({'epoch': b.epoch, 'arm': a.id, 'worldlet': a.worldlet,
                          'purpose': a.purpose, 'execution': a.execution,
                          'transport_remainder': a.remainder}, sort_keys=True))
    print('SIMULATED_ALLOCATION_ONLY; no repository execution or claim promotion')


if __name__ == '__main__':
    main()