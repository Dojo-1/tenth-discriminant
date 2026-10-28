# Runner correction before the Phase82 audit

The registered protocol requires input/audit checks capped at180seconds.
Initial registered runner9e3f5e5 accidentally encoded182 in its default
mode branch because a broad80->82string replacement also changed180.
The actual input invocation already completed PASS in43.1749583seconds,
so its execution satisfies the registered180second duration, but its
outer enforcement limit was182. That mismatch is preserved explicitly;
no claim of an exactly180-enforced input run, and no rewrite or rerun.

Before the not-yet-invoked audit, change ONLY default{182}to{180} in the
runner. This reduces the future cap to the registered value; target600,
root1200,cumulative1200,memory8192 and all source/proof/statement/input
checks remain unchanged. No resource stop occurred. Register this addendum
and corrected runner before audit execution. PHASE82_RUNNER_ORIGINAL.ps1
preserves exact original registration bytes in addition to Git9e3f5e5.
The already saved input result retains time_limit_seconds182. The saved
evidence verifier must check its actual duration<=180 and report the
nominal-cap discrepancy. All futurePhase82default-mode invocations use180;
the one-shot guard forbids a second input invocation.

Future phase renumbering must replace phase identifiers explicitly,
not globally replace numeral substrings that occur in budget constants.
