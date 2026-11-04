#!/usr/bin/env python3
"""Post-preregistered Round201 T5: finite kernel levels and transition images.

Exact enumeration of scalar congruences only. Does not compute a
characteristic-zero nonarchimedean inverse limit or prove the general lemma.
"""
import json
from math import prod


def kernel_values(d,p,m):
    modulus=p**m
    return tuple(x for x in range(modulus) if d*x%modulus==0)


def reduction_image(d,p,m):
    target=p**m
    a=kernel_values(d,p,m+1)
    return set(x%target for x in a)


def scalar_checks():
    p=3
    levels=[]
    for m in range(1,5):
        z=kernel_values(3,p,m)
        expect=tuple(i*3**(m-1) for i in range(3))
        assert z==expect
        image=reduction_image(3,p,m)
        assert image=={0}
        zero=kernel_values(0,p,m)
        assert len(zero)==3**m
        assert reduction_image(0,p,m)==set(range(3**m))
        levels.append({"m":m,"kernel_for_3":list(z),
                       "kernel_for_0_size":len(zero),
                       "image_next_to_current_for_3":sorted(image),
                       "image_next_to_current_for_0_size":3**m})
    return levels


def diagonal_checks():
    out={}
    for label, diag in [("C",[1,3,27]),("E",[1,9,9])]:
        levels=[]
        for m in range(1,5):
            kernels=[kernel_values(d,3,m) for d in diag]
            images=[reduction_image(d,3,m) for d in diag]
            source_count=prod(len(k) for k in kernels)
            image_count=prod(len(im) for im in images)
            # The image is a subgroup of the target, not the target itself.
            assert image_count<=source_count
            levels.append({"m":m,
                           "K_m_size":source_count,
                           "im_K_(m+1)_to_K_m_size":image_count,
                           "surjective":source_count==image_count})
        out[label]=levels
    assert [v["K_m_size"] for v in out["C"]]==[9,27,81,81]
    assert [v["im_K_(m+1)_to_K_m_size"] for v in out["C"]]==[3,9,9,9]
    assert [v["K_m_size"] for v in out["E"]]==[9,81,81,81]
    return out


if __name__=="__main__":
    result={"T5a_T5b":scalar_checks(),"T5c":diagonal_checks()}
    print(json.dumps(result,indent=2))
    print("ROUND201_T5_TRANSITION_EXACT_PASS")
