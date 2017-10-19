import plotly 
plotly.tools.set_credentials_file(username='Hwayongg', api_key='SwpYA6ZMAn26IX8itcyN')


import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

token_1,token_2,token_3  = '6x9ndzxs9y','afqrpkyjnw', '9fduglqxfr'

stream_id1 = dict(token=token_1, maxpoints=100)
stream_id2 = dict(token=token_2, maxpoints=100)
stream_id3 = dict(token=token_3, maxpoints=100)

trace1 = go.Scatter(x=[], y=[], stream=stream_id1, name='sin^2',mode='lines',
    line=dict(width=0.5, color='rgb(131, 90, 241)'), fill='tonexty')
trace2 = go.Scatter(x=[], y=[], stream=stream_id2, name='cos^2',mode='lines',
    line=dict(width=0.5, color='rgb(111, 231, 219)'), fill='tonexty')
trace3 = go.Scatter(x=[], y=[], stream=stream_id3, name='sin^2 + cos^2', mode='lines',
    line=dict(width=0.5, color='rgb(184, 247, 212)'), fill='tonexty')

data = [trace1, trace2, trace3]
layout = go.Layout( title='sin^2 + cos^2 = 1' )

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='example_2017sopython')

s_1 = py.Stream(stream_id=token_1)
s_2 = py.Stream(stream_id=token_2)
s_3 = py.Stream(stream_id=token_3)

s_1.open()
s_2.open()
s_3.open()


import datetime
import time
import random
import math

time.sleep(1)

degree=0

while True:

    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    degree += 1

    y1 = math.sin(math.radians(degree))**2
    y2 = math.cos(math.radians(degree))**2
    y3 = math.sin(math.radians(degree))**2 + math.cos(math.radians(degree))**2
    s_1.write(dict(x=x,y=y1))
    s_2.write(dict(x=x,y=y2))
    s_3.write(dict(x=x,y=y3))

    time.sleep(0.3)

s_1.close()
s_2.close()
s_3.close()
