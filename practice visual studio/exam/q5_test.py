def sequence_gen():
    pass

def test_fib():
    fib = sequence_gen(0,1)
    assert fib.next()== 0
    assert fib.next()== 1
    assert fib.next()== 1
    assert fib.next()== 2
    assert fib.next()== 3
    assert fib.next()== 5
    assert fib.next()== 8
    assert [fib.next() for _ in range(10)] == [13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

def test_trib():
    trib = sequence_gen(0,1,1)
    assert trib.next()==  0
    assert trib.next()==  1
    assert trib.next()==  1
    assert trib.next()==  2
    assert trib.next()==  4
    assert trib.next()==  7
    assert trib.next()==  13
    assert trib.next()==  24
    assert trib.next()==  44
    assert trib.next()==  81
    assert trib.next()==  149
    assert trib.next()==  274
    assert trib.next()==  504
    assert trib.next()==  927
    assert trib.next()==  1705

def test_lucas():
    lucas = sequence_gen(2,1)
    assert [lucas.next() for _ in range(100)] == [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778, 9349, 15127, 24476, 39603, 64079, 103682, 167761, 271443, 439204, 710647, 1149851, 1860498, 3010349, 4870847, 7881196, 12752043, 20633239, 33385282, 54018521, 87403803, 141422324, 228826127, 370248451, 599074578, 969323029, 1568397607, 2537720636, 4106118243, 6643838879, 10749957122, 17393796001, 28143753123, 45537549124, 73681302247, 119218851371, 192900153618, 312119004989, 505019158607, 817138163596, 1322157322203, 2139295485799, 3461452808002, 5600748293801, 9062201101803, 14662949395604, 23725150497407, 38388099893011, 62113250390418, 100501350283429, 162614600673847, 263115950957276, 425730551631123, 688846502588399, 1114577054219522, 1803423556807921, 2918000611027443, 4721424167835364, 7639424778862807, 12360848946698171, 20000273725560978, 32361122672259149, 52361396397820127, 84722519070079276, 137083915467899403, 221806434537978679, 358890350005878082, 580696784543856761, 939587134549734843, 1520283919093591604, 2459871053643326447, 3980154972736918051, 6440026026380244498, 10420180999117162549, 16860207025497407047, 27280388024614569596, 44140595050111976643, 71420983074726546239, 115561578124838522882, 186982561199565069121, 302544139324403592003, 489526700523968661124]
    assert lucas.next()==  792070839848372253127
    assert lucas.next()==  1281597540372340914251
    assert lucas.next()==  2073668380220713167378
    assert lucas.next()==  3355265920593054081629
    assert lucas.next()==  5428934300813767249007
    assert lucas.next()==  8784200221406821330636
    assert lucas.next()==  14213134522220588579643
    assert lucas.next()==  22997334743627409910279
    assert lucas.next()==  37210469265847998489922
    assert lucas.next()==  60207804009475408400201
    assert lucas.next()==  97418273275323406890123
    assert lucas.next()==  157626077284798815290324
    assert lucas.next()==  255044350560122222180447
    assert lucas.next()==  412670427844921037470771
    assert lucas.next()==  667714778405043259651218

def test_pointless():
    pointless = sequence_gen(1)
    assert [pointless.next() for _ in range(1000)] == [1] * 1000
