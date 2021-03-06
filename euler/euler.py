
class Euler():
	def euler(f, init, range_a, range_b, step):
		assert range_a < range_b
		#assert type(f) == type(lambda:0)

		points = []
		y = init
		x = range_a
		while x <= range_b:
			points.append([x, y])
			y += step*f(x, y)
			x += step
		return points
	
	def rungeKutta1(f, init, range_a, range_b, step):
		assert range_a < range_b
		
		points = []
		y = init
		x = range_a
		sd2 = step / 2
		while x <= range_b:
			points.append([x, y])
			y += sd2*(f(x,y)+f(x+step,y + step*f(x,y)))
			x += step
		return points
	
	
	def rungeKutta4(f, init, range_a, range_b, step):
		assert range_a < range_b
		
		points = []
		y = init
		x = range_a
		sd2 = step / 2
		sd6 = step / 6
		while x <= range_b:
			points.append([x, y])
			k0 = f(x,y)
			k1 = f(x+sd2,y+sd2*k0)
			k2 = f(x+sd2,y+sd2*k1)
			k3 = f(x+step,y+step*k2)
			y += sd6*(k0 + 2*k1 + 2*k2 + k3)
			x += step
		return points