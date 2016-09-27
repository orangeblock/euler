constant @fib-lazy = 1, 1, *+* ... *;

sub nth-digit-fib($n){
  for @fib-lazy.kv -> $i, $num {
    return ($i+1, $num) if $num >= 10**($n-1);
  }
}

say nth-digit-fib(1000)[0];
