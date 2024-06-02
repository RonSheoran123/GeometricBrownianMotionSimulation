def gbm(s0,mu,sigma,dt,T,n):
    paths=[]
    for i in range(n):
        prices=[s0]
        time=0
        while(time+dt<=T):
            prices.append(prices[-1] * np.exp((mu-0.5*(sigma**2))*dt + sigma * np.random.normal(0,np.sqrt(dt))))
            time+=dt
        if(T>time):
            prices.append(prices[-1] * np.exp((mu-0.5*(sigma**2))*(T-time) + sigma * np.random.normal(0,np.sqrt(T-time))))
        paths.append(prices)
    return paths
