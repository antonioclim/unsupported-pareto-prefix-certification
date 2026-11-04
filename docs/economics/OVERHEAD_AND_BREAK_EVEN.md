<a name="heading-economics-overhead_and_break_even-measured-local-overhead-and-conditional-accounting"></a>


# Measured local overhead and conditional accounting
<a name="s12-4-overhead"></a>

[Documentation index](../README.md)

**Role:** Extended retained CPU protocol and conditional accounting; the core supplement retains the relevant outcome synopsis and economic conditions. **Source:** UPPC P61, S12.4, Antonio Clim. Documentation for companion version 1.2.0. Source prose retains its existing manuscript/supplement rights; moving it to MD grants no additional licence.

**Path convention:** scientific commands and scientific-file paths below start at the frozen companion's `reproduction/` root unless a different working directory is expressly stated. In a GitHub source checkout, the equivalent working directory is the repository root; the command paths are identical. Run commands from that software root, not from this `docs/` directory. Retained results are not a claim of a fresh execution. References to manuscript sections and statements use their scientific identifiers; the separately supplied review documents contain the essential proofs.

<a name="heading-economics-overhead_and_break_even-s12-4-measured-local-overhead-and-conditional-break-even-accounting"></a>

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.


### S12.4. Measured local overhead and conditional break-even accounting
The additional APEX timing diagnostic ran each implementation once for warm-up and then nine times on the same 1,536-task cohort, rotating and reversing execution order. CPU process time includes local next-row calls, rational arithmetic and bookkeeping, but excludes archive loading and transport. The measured median CPU times were $0.087615668$ seconds for full groupwise census, $0.762751566$ seconds for census with FALSE stopping and $0.956054590$ seconds for screened deterministic acquisition with FALSE stopping. The respective observed ranges were $[0.080700124,0.286775860]$, $[0.680230609,4.018544470]$ and $[0.868180009,1.585645396]$ seconds. This shared-container diagnostic, including its large outliers, is not a stable hardware or deployed-service benchmark. In particular, fewer purchased records did not imply less local computation.

The difference between the latter two medians is $0.193303024$ seconds. In an assumed additive sequential model with equal external access latency per record and no batching, overlap or caching, its 850 saved disclosures would offset that difference when access latency exceeds

$$
\frac{0.193303024}{850}\ \mathrm{s}
\simeq0.2274\ \mathrm{ms}
$$

per record. This is a conditional calculation from the reported diagnostic, not a measured end-to-end speedup or a portable latency threshold.

For a monetary evaluation, let $c$ be a common charge per returned record and let $H$ be the additional total computation, setup and service cost of the wrapped screened implementation relative to wrapped census on this same cohort. Its net saving is

$$
850c-H,
$$

which is positive exactly when $H<850c$. Neither $c$ nor $H$ was measured. For heterogeneous tariffs, compute each policy's total from the actual disclosed locations; two different wrapped policies need not have nested transcripts, so the unweighted difference 850 cannot simply be multiplied by an arbitrary average price. Lemma S15's pathwise comparison applies to a policy and its own wrapper.

More generally, if a proposed workload has positive frequency $\pi$, conditional expected reductions $d_+$ and $d_-$ against a declared baseline, common disclosure price $c$ and expected additional overhead $h$, the expected net gain is the accounting identity

$$
c\bigl[\pi d_++(1-\pi)d_-\bigr]-h.
$$

The observed APEX fraction $41/1536$ is not an estimate of future prevalence. Against its own base, the wrapper has $d_+=0$ and $d_-\geq0$; comparing distinct policies requires a separate calculation. Section S5.7 provides a complementary theoretical route to positive-input disclosure savings through explicit geometric margins. Such constructed guarantees do not turn the archived replays into measured economic benefits.
