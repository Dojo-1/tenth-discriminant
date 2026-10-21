\\ Exact large-scale check of the determinant lemmas on ellipse point sets (general rho).
\\ G = 2(A A~ + D B B~), rows indexed (r,s), columns (point, j), entry d^j/dz^j (z^r z'^s) = A + B sqrt(-D).
F(p,R,S) = sum(r=0,R-1, my(k=r\p); if(k<=S-1, k*S - k*(k+1)/2, S*(S-1)/2));
check(D,R,S,rho2,J) = {
  my(P=List(), w, lines=0, L=0, A, B, G, d, rho, ok=1, inert=List(), nrow, ncol, row, n, i, col);
  forstep(y=-sqrtint(rho2\D), sqrtint(rho2\D), 1, w=sqrtint(rho2-D*y^2); lines++; L=max(L,2*w+1);
          for(x=-w,w, listput(P,[x,y])));
  n=#P; if(J < L+lines || n*J <= 2*R*S + J*(R+S), return([0,"hyp-fails",n,L+lines]));
  nrow=R*S; ncol=n*J; A=matrix(nrow,ncol); B=matrix(nrow,ncol);
  for(r=0,R-1, for(s=0,S-1, row=r*S+s+1;
    for(i=1,n, my(x=P[i][1], y=P[i][2], z=x+y*quadgen(-4*D)*0, zz, t);
      for(j=0,min(J-1,r), t=(r!/(r-j)!) * (x+y*'w)^(r-j) * (x-y*'w)^s; t=lift(Mod(t,'w^2+D));
        col=(i-1)*J+j+1; A[row,col]=polcoeff(t,0,'w); B[row,col]=polcoeff(t,1,'w)))));
  G=2*(A*A~ + D*B*B~); d=matdet(G);
  if(d<=0, return([0,"det<=0"]));
  if(d > prod(k=1,nrow,G[k,k]), return([0,"hadamard"]));
  forprime(p=3,R, if(D%p && kronecker(-D,p)==-1, listput(inert,p);
     if(valuation(d,p) < 2*F(p,R,S), return([0,Str("vp ",p)]))));
  [1, n, nrow, #inert, if(#inert, vecmax(apply(p->2*F(p,R,S),Vec(inert))), 0), log(prod(k=1,nrow,G[k,k]))/log(d)];
}
{
  my(cnt=0, bad=0, res, cases=[[7,24,3,170],[11,30,3,300],[19,30,4,450],[43,36,3,900],[67,40,3,1400],[163,30,4,2400],[1009,24,3,12000],[23,40,4,500],[47,36,4,700]]);
  for(k=1,#cases, my(c=cases[k], D=c[1], R=c[2], S=c[3], rho2=c[4], J);
    \\ smallest J satisfying the line-slicing hypothesis
    J=1; res=check(D,R,S,rho2,J);
    while(res[1]==0 && res[2]=="hyp-fails", J=max(J+1, res[4]); res=check(D,R,S,rho2,J); if(J>400,break));
    cnt++; if(res[1]==0, bad++);
    printf("D=%5d R=%3d S=%d rho2=%5d J=%3d -> %s\n", D,R,S,rho2,J, res));
  printf("%d cases, %d failures\n", cnt, bad);
}
