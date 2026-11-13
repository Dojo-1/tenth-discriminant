#!/usr/bin/env python3
"""Phase308-C: filtered Picard Worldlets and honest forgetful functors.

This is a finite model of a theorem about *explicit split filtered projective
modules* over a Dedekind domain. Steinitz classification and associated-
graded invariance are mathematical dependencies, not proven by this script.
The original integer-row Gram source is NEVER replaced.
"""
from dataclasses import dataclass

from adaptive_torsion_family import source_family


class FilterTypeError(ValueError):
    pass


@dataclass(frozen=True)
class PicardFlag:
    """Explicit split filtered bundle: successive rank1 Picard class powers."""
    field_d: int
    class_order: int
    graded_class_powers: tuple

    def __post_init__(self):
        if self.class_order<1 or self.field_d<=0 or not self.graded_class_powers:
            raise FilterTypeError("invalid filtered projective object")
        if any(not isinstance(x,int) for x in self.graded_class_powers):
            raise FilterTypeError("Picard exponent labels must be integers")

    @property
    def rank(self):
        return len(self.graded_class_powers)

    @property
    def canonical_grades(self):
        return tuple(v%self.class_order for v in self.graded_class_powers)

    @property
    def determinant_class(self):
        return sum(self.canonical_grades)%self.class_order

    @property
    def underlying_module_free_by_steinitz(self):
        """Imported theorem; no explicit global integral basis claimed."""
        return self.determinant_class==0

    @property
    def filtered_standard_flag_equivalence(self):
        """For these explicitly split flags: each named line must be free."""
        return all(x==0 for x in self.canonical_grades)

    def forget_filtration(self):
        return (self.field_d,self.rank,self.determinant_class)

    def deweave(self):
        """Typed information LOST by the forgetful functor."""
        return {
            "ordered_associated_graded_Picard_classes":self.canonical_grades,
            "first_nontrivial_grade":next(
                (i+1 for i,x in enumerate(self.canonical_grades) if x),None),
            "transport_remainder":"ordered-local-line-classes",
            "not_reconstructible_from_only_rank_and_determinant":(self.rank>1 and self.class_order>1 and any(self.canonical_grades)),
            "not_original_integer_source":True,
        }

    def filtered_isomorphic_to(self,other):
        """Only classwise test for corresponding split rank-one graded fibers.

        A genuine filtered O-isomorphism necessarily preserves each grade.
        The converse for these explicitly split modules follows from
        choosing individual rank-one isomorphisms; no matrices are produced.
        """
        if not isinstance(other,PicardFlag) or self.field_d!=other.field_d:
            raise FilterTypeError("not comparable over the same quadratic ring")
        return self.canonical_grades==other.canonical_grades


def standard_flag(d,order,rank):
    if rank<1:
        raise FilterTypeError("empty standard flag")
    return PicardFlag(d,order,(0,)*rank)


def repeated_I_flag(d,order,rank):
    if rank<1:
        raise FilterTypeError("empty source rank")
    return PicardFlag(d,order,(1,)*rank)


def inverse_tendril_pair(d,order):
    """I ⊕ I^{-1}: cancellation of aggregate Picard class, not of labels."""
    return PicardFlag(d,order,(1,-1))


def representation_adaptation_control():
    rows=source_family()
    out=[]
    error_fields=[]
    for x in rows:
        d=x["field_D"]
        m=x["Picard_ideal_class_order"]
        source=repeated_I_flag(d,m,100)
        standard=standard_flag(d,m,100)
        assert source.underlying_module_free_by_steinitz==x["rank100_determinant_trivial"]
        # A determinant-only classifier can confuse a free total module
        # with every individually named original rank-one line being free.
        scalar_claim=source.underlying_module_free_by_steinitz
        actual_named_line_is_principal=(m==1)
        if scalar_claim!=actual_named_line_is_principal:
            error_fields.append(d)
        # Structural adaptation: keep associated-graded Picard classes.
        refined_claim=source.filtered_standard_flag_equivalence
        assert refined_claim==actual_named_line_is_principal
        assert source.filtered_isomorphic_to(standard)==refined_claim
        row={
          "D":d,"ideal_class_order":m,
          "rank100_underlying_module_free":source.underlying_module_free_by_steinitz,
          "rank100_standard_filtered_flag_equivalent":refined_claim,
          "grade1_class":source.canonical_grades[0],
          "forgetfulness_obstruction":source.deweave()["first_nontrivial_grade"],
        }
        out.append(row)

    assert error_fields==[187,203]
    paired=[]
    for d,m in ((187,2),(203,4),(167,11)):
        f=inverse_tendril_pair(d,m)
        std=standard_flag(d,m,2)
        assert f.determinant_class==0
        assert f.underlying_module_free_by_steinitz
        assert not f.filtered_isomorphic_to(std)
        assert f.canonical_grades==(1,m-1)
        paired.append({"D":d,"class_order":m,
                       "paired_grades":f.canonical_grades,
                       "unfiltered_free":True,
                       "filtered_standard_flag_equivalence":False,
                       "first_grade_obstruction":1})
    positive=inverse_tendril_pair(163,1)
    assert positive.filtered_isomorphic_to(standard_flag(163,1,2))
    return {
        "four_rank100_cases":out,
        "scalar_only_false_positive_fields":error_fields,
        "pairwise_I_plus_inverse_cancellation":paired,
        "principal_D163_positive_pair_control":True,
        "genuine_mathematical_difference_between_filtered_and_unfiltered_categories":True,
        "representation_refinement_changes_in_sample_false_positive_count":True,
        "NOT_a_general_intelligence_benchmark":True,
        "no_original_Gram_or_field_cutoff_modified":True,
    }


def main():
    print("PHASE308_FILTERED_WORLDLET_ADAPTATION_PASS",
          representation_adaptation_control(),flush=True)


if __name__=="__main__":
    main()
