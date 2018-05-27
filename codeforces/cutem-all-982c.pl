use Data::Dumper;

$n = <>;
%graph = map { $_ => [] } (1..$n);
for (2..$n) {
	($u, $v) = split ' ', <>;
	push @{$graph{$u}}, $v;
	push @{$graph{$v}}, $u;
}

sub dfs {
	my $v = shift || 1;
	my $par = shift || -1;
	(my $removed, my $size) = (0, 1);
	for my $u (@{$graph{$v}}) {
		if ($u != $par) {
			my $child = dfs($u, $v); # [removed, size]
			$removed += $child->[0];
			if (($child->[1]) % 2 == 0) {
				$removed += 1;
			}
			$size += $child->[1];
		}
	}
	return [$removed, $size];
}

$removed = dfs()->[0];
print ($n % 2 == 0 ? $removed : -1);