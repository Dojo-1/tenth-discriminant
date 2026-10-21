\\ ground truth: for each H, the largest |disc| of an imaginary quadratic field with h <= H, scanning to N
N=2*10^6; H=[1,2,3,5,10,20,50,100]; mx=vector(#H);
for(d=3,N, if(isfundamental(-d), my(c=qfbclassno(-d)); for(k=1,#H, if(c<=H[k], mx[k]=d))));
for(k=1,#H, printf("H=%d maxD(h<=H, D<=%d)=%d\n",H[k],N,mx[k]));
