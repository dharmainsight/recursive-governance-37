#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

REQUIRED_OBS = ["body", "feeling", "mind", "dhamma"]
IMPROVEMENT_MODES = {"REMOVE", "PREVENT", "DEVELOP", "MAINTAIN"}
FACULTIES = ("faith", "energy", "mindfulness", "concentration", "wisdom")
POWER_OPPOSITES = {
    "faith": "不信",
    "energy": "懈怠",
    "mindfulness": "放逸",
    "concentration": "掉挙",
    "wisdom": "無明",
}
FACULTY_FIELDS = ("explicit_reference", "correct_application")
POWER_FIELDS = (
    "unstated_or_disturbed_case",
    "autonomous_response",
    "opposing_tendency_resistance",
    "verification",
)


def nonempty(value):
    return bool(value) and value not in ("unknown", "UNKNOWN")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run_record")
    args = parser.parse_args()
    data = json.loads(Path(args.run_record).read_text(encoding="utf-8"))
    checks = []

    def add(name, ok, detail):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})

    add("schema_version", data.get("schema_version") == "2.0.0", "run record must use schema 2.0.0")

    task = data.get("task", {})
    add("goal", nonempty(task.get("goal")), "explicit goal required")
    add("acceptance_criteria", bool(task.get("acceptance_criteria")), "at least one acceptance criterion")

    observations = data.get("observations", {})
    for key in REQUIRED_OBS:
        add(
            "satipatthana." + key,
            key in observations,
            f"{key} observation channel must exist; [] requires N/A explanation elsewhere",
        )

    modes = set(data.get("improvement_modes", []))
    add(
        "right_effort_modes",
        modes <= IMPROVEMENT_MODES and bool(modes),
        "use one or more of REMOVE/PREVENT/DEVELOP/MAINTAIN",
    )

    accomplishment = data.get("accomplishment", {})
    add(
        "four_iddhipada",
        all(
            key in accomplishment
            for key in (
                "desire_goal_salience",
                "energy_resources",
                "mind_working_set",
                "investigation_hypotheses",
            )
        ),
        "all four accomplishment controls represented",
    )

    kernel = data.get("kernel_closure", {})
    kernel_fields = (
        "initial_observation",
        "selected_improvement",
        "mobilized_action",
        "changed_state",
        "reobservation",
        "acceptance_result",
    )
    add(
        "kernel_closed",
        kernel.get("closed") is True and all(nonempty(kernel.get(key)) for key in kernel_fields),
        "4+4+4 requires action, changed state, reobservation, and acceptance evidence",
    )

    faculties = data.get("faculties", {})
    add(
        "five_faculties_shape",
        set(faculties) == set(FACULTIES),
        "all five faculties must appear at one structural level",
    )
    for name in FACULTIES:
        finding = faculties.get(name, {})
        add(
            f"faculty.{name}",
            isinstance(finding, dict)
            and all(nonempty(finding.get(field)) for field in FACULTY_FIELDS),
            "requires explicit_reference and correct_application evidence",
        )

    powers = data.get("powers", {})
    add(
        "five_powers_shape",
        set(powers) == set(FACULTIES),
        "all five powers must appear at one structural level",
    )
    for name, opposing in POWER_OPPOSITES.items():
        finding = powers.get(name, {})
        add(
            f"power.{name}",
            isinstance(finding, dict)
            and finding.get("opposing_tendency") == opposing
            and all(nonempty(finding.get(field)) for field in POWER_FIELDS)
            and finding.get("human_coaching_required") is False,
            (
                f"requires {opposing} resistance, an unstated/disturbed case, autonomous response, "
                "verification, and no case-specific human coaching"
            ),
        )

    meta = data.get("meta_control", {})
    add(
        "seven_factors",
        all(
            key in meta
            for key in (
                "mindfulness",
                "investigation",
                "energy",
                "joy",
                "tranquility",
                "concentration",
                "equanimity",
            )
        ),
        "all seven adaptive-control channels represented",
    )

    path = data.get("integrated_path", {})
    add(
        "eightfold_path",
        all(
            key in path
            for key in (
                "view_context",
                "intention",
                "speech_communication",
                "action",
                "livelihood_loop",
                "effort_improvement",
                "mindfulness_observability",
                "concentration_harness",
            )
        ),
        "all eight integrated-governance channels represented",
    )

    add("validation", bool(data.get("validation")), "record deterministic or explicit validation evidence")

    passed = sum(1 for check in checks if check["pass"])
    result = {
        "overall_pass": passed == len(checks),
        "score": passed / len(checks),
        "checks": checks,
        "note": (
            "Structural evidence-contract evaluation only. Semantic correctness, historical ordering, "
            "and safety still require repository-specific review."
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())


