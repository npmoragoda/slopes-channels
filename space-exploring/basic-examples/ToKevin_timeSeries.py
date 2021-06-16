#my attempt
fluxSeries=[]
for x in range(runtime//dt):

    flux = mg.at_node['sediment__flux']
    g, = np.where(flux == flux.max())
    print(g)

    h = flux[g]
    fluxSeries.append(h)
    print(h)

time = np.linspace(0,runtime,runtime//dt)

plt.plot(time, fluxSeries)
plt.xlabel("Time (yr)")
plt.ylabel("Sediment Flux (m^3/yr")
plt.show()