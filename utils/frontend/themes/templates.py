import plotly.io as pio
import plotly.express as px
#Load template basis
plotly_template = pio.templates["plotly_dark"]
#Examine template
# print(plotly_template.layout)
#Make changes
#Set default title
plotly_template.layout.title = 'Default chart title'
#Change plot and boarder background default color
plotly_template.layout.paper_bgcolor='rgb(46, 56, 88)'
plotly_template.layout.plot_bgcolor='rgb(46, 56, 88)'

#Chnage plot color scales
plotly_template.layout.colorscale.sequential = px.colors.sequential.dense
# Examine template after changes
# print(plotly_template.layout)

#Register theme
pio.templates['custom_dark'] = plotly_template
#Set as default
pio.templates.default = 'custom_dark'

