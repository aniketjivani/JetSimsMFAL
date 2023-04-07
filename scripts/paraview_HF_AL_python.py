# trace generated using paraview version 5.11.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *


import os

runDir = "/work/e734/e734/shared/ajivani/JetSimsMFAL/runs_HF_batch_01"
exportDir = "/work/e734/e734/shared/ajivani/JetSimsMFAL/results_HF_batch_01"

try:
    os.mkdir(exportDir)
except FileExistsError:
    pass

runID1 = 1
runID2 = 15

for runID in range(runID1, runID2 + 1):
    runIDPath = os.path.join(exportDir, "run" + "{:03d}".format(runID))
    try:
        os.mkdir(runIDPath)
    except FileExistsError:
        pass


for runID in range(runID1, runID2 + 1):
    flowFileName = os.path.join(runDir, "run" + "%03d" % runID, "flow_100001.vtu")

    print("Reading {}".format(flowFileName))
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'XML Unstructured Grid Reader'
    flow_100001vtu = XMLUnstructuredGridReader(registrationName='flow_100001.vtu',FileName=[flowFileName])
    flow_100001vtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient', 'Laminar_Viscosity', 'Skin_Friction_Coefficient', 'Heat_Flux', 'Y_Plus', 'MeanDensity', 'MeanVelocity', 'MeanPressure', 'RMS[u]', 'RMS[v]', 'RMS[uv]', 'RMS[Pressure]', "u'u'", "v'v'", "u'v'", "p'p'", 'RMS[w]', 'RMS[uw]', 'RMS[vw]', "w'w'", "w'u'", "w'v'"]

    # Properties modified on flow_100001vtu
    flow_100001vtu.TimeArray = 'None'

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    flow_100001vtuDisplay = Show(flow_100001vtu, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    flow_100001vtuDisplay.Representation = 'Surface'
    flow_100001vtuDisplay.ColorArrayName = [None, '']
    flow_100001vtuDisplay.SelectTCoordArray = 'None'
    flow_100001vtuDisplay.SelectNormalArray = 'None'
    flow_100001vtuDisplay.SelectTangentArray = 'None'
    flow_100001vtuDisplay.OSPRayScaleArray = 'Density'
    flow_100001vtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    flow_100001vtuDisplay.SelectOrientationVectors = 'MeanVelocity'
    flow_100001vtuDisplay.ScaleFactor = 7.6000000000000005
    flow_100001vtuDisplay.SelectScaleArray = 'Density'
    flow_100001vtuDisplay.GlyphType = 'Arrow'
    flow_100001vtuDisplay.GlyphTableIndexArray = 'Density'
    flow_100001vtuDisplay.GaussianRadius = 0.38
    flow_100001vtuDisplay.SetScaleArray = ['POINTS', 'Density']
    flow_100001vtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    flow_100001vtuDisplay.OpacityArray = ['POINTS', 'Density']
    flow_100001vtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    flow_100001vtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
    flow_100001vtuDisplay.PolarAxes = 'PolarAxesRepresentation'
    flow_100001vtuDisplay.ScalarOpacityUnitDistance = 1.0106759524215592
    flow_100001vtuDisplay.OpacityArrayName = ['POINTS', 'Density']
    flow_100001vtuDisplay.SelectInputVectors = ['POINTS', 'MeanVelocity']
    flow_100001vtuDisplay.WriteLog = ''

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    flow_100001vtuDisplay.ScaleTransferFunction.Points = [0.05430471897125244, 0.0, 0.5, 0.0, 0.08193886280059814, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    flow_100001vtuDisplay.OpacityTransferFunction.Points = [0.05430471897125244, 0.0, 0.5, 0.0, 0.08193886280059814, 1.0, 0.5, 0.0]

    # reset view to fit data
    renderView1.ResetCamera(False)

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Plot Over Line'
    plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=flow_100001vtu)
    plotOverLine1.Point1 = [-6.0, -30.899999618530273, -30.899999618530273]
    plotOverLine1.Point2 = [70.0, 30.899999618530273, 30.899999618530273]

    # Properties modified on plotOverLine1
    plotOverLine1.Resolution = 199
    plotOverLine1.Point1 = [0.0, 0.0, 0.503]
    plotOverLine1.Point2 = [20.0, 0.0, 0.503]

    # show data in view
    plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    plotOverLine1Display.Representation = 'Surface'
    plotOverLine1Display.ColorArrayName = [None, '']
    plotOverLine1Display.SelectTCoordArray = 'None'
    plotOverLine1Display.SelectNormalArray = 'None'
    plotOverLine1Display.SelectTangentArray = 'None'
    plotOverLine1Display.OSPRayScaleArray = 'Density'
    plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    plotOverLine1Display.SelectOrientationVectors = 'MeanVelocity'
    plotOverLine1Display.ScaleFactor = 2.0
    plotOverLine1Display.SelectScaleArray = 'Density'
    plotOverLine1Display.GlyphType = 'Arrow'
    plotOverLine1Display.GlyphTableIndexArray = 'Density'
    plotOverLine1Display.GaussianRadius = 0.1
    plotOverLine1Display.SetScaleArray = ['POINTS', 'Density']
    plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
    plotOverLine1Display.OpacityArray = ['POINTS', 'Density']
    plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
    plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
    plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'
    plotOverLine1Display.SelectInputVectors = ['POINTS', 'MeanVelocity']
    plotOverLine1Display.WriteLog = ''

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    plotOverLine1Display.ScaleTransferFunction.Points = [0.06723541766405106, 0.0, 0.5, 0.0, 0.07654758542776108, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    plotOverLine1Display.OpacityTransferFunction.Points = [0.06723541766405106, 0.0, 0.5, 0.0, 0.07654758542776108, 1.0, 0.5, 0.0]

    # Create a new 'Line Chart View'
    lineChartView1 = CreateView('XYChartView')

    # show data in view
    plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

    # trace defaults for the display properties.
    plotOverLine1Display_1.UseIndexForXAxis = 0
    plotOverLine1Display_1.XArrayName = 'arc_length'
    plotOverLine1Display_1.SeriesVisibility = ['Density', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'MeanDensity', 'MeanPressure', 'MeanVelocity_Magnitude', 'Momentum_Magnitude', "p'p'", 'Pressure', 'Pressure_Coefficient', 'RMS[Pressure]', 'RMS[u]', 'RMS[uv]', 'RMS[uw]', 'RMS[v]', 'RMS[vw]', 'RMS[w]', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', "u'u'", "u'v'", "v'v'", "w'u'", "w'v'", "w'w'", 'Y_Plus']
    plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Density', 'Density', 'Energy', 'Energy', 'Heat_Flux', 'Heat_Flux', 'Laminar_Viscosity', 'Laminar_Viscosity', 'Mach', 'Mach', 'MeanDensity', 'MeanDensity', 'MeanPressure', 'MeanPressure', 'MeanVelocity_X', 'MeanVelocity_X', 'MeanVelocity_Y', 'MeanVelocity_Y', 'MeanVelocity_Z', 'MeanVelocity_Z', 'MeanVelocity_Magnitude', 'MeanVelocity_Magnitude', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', "p'p'", "p'p'", 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'RMS[Pressure]', 'RMS[Pressure]', 'RMS[u]', 'RMS[u]', 'RMS[uv]', 'RMS[uv]', 'RMS[uw]', 'RMS[uw]', 'RMS[v]', 'RMS[v]', 'RMS[vw]', 'RMS[vw]', 'RMS[w]', 'RMS[w]', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Temperature', "u'u'", "u'u'", "u'v'", "u'v'", "v'v'", "v'v'", 'vtkValidPointMask', 'vtkValidPointMask', "w'u'", "w'u'", "w'v'", "w'v'", "w'w'", "w'w'", 'Y_Plus', 'Y_Plus', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Heat_Flux', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Laminar_Viscosity', '0.6', '0.3100022888532845', '0.6399938963912413', 'Mach', '1', '0.5000076295109483', '0', 'MeanDensity', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'MeanPressure', '0', '0', '0', 'MeanVelocity_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'MeanVelocity_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'MeanVelocity_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'MeanVelocity_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'Momentum_X', '1', '0.5000076295109483', '0', 'Momentum_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Momentum_Z', '0', '0', '0', 'Momentum_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', "p'p'", '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Pressure', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Pressure_Coefficient', '0.6', '0.3100022888532845', '0.6399938963912413', 'RMS[Pressure]', '1', '0.5000076295109483', '0', 'RMS[u]', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'RMS[uv]', '0', '0', '0', 'RMS[uw]', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'RMS[v]', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'RMS[vw]', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'RMS[w]', '0.6', '0.3100022888532845', '0.6399938963912413', 'Skin_Friction_Coefficient_X', '1', '0.5000076295109483', '0', 'Skin_Friction_Coefficient_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Skin_Friction_Coefficient_Z', '0', '0', '0', 'Skin_Friction_Coefficient_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Temperature', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', "u'u'", '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', "u'v'", '0.6', '0.3100022888532845', '0.6399938963912413', "v'v'", '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', "w'u'", '0', '0', '0', "w'v'", '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', "w'w'", '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Y_Plus', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude', '0', '0', '0']
    plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1.0', 'Density', '1.0', 'Energy', '1.0', 'Heat_Flux', '1.0', 'Laminar_Viscosity', '1.0', 'Mach', '1.0', 'MeanDensity', '1.0', 'MeanPressure', '1.0', 'MeanVelocity_X', '1.0', 'MeanVelocity_Y', '1.0', 'MeanVelocity_Z', '1.0', 'MeanVelocity_Magnitude', '1.0', 'Momentum_X', '1.0', 'Momentum_Y', '1.0', 'Momentum_Z', '1.0', 'Momentum_Magnitude', '1.0', "p'p'", '1.0', 'Pressure', '1.0', 'Pressure_Coefficient', '1.0', 'RMS[Pressure]', '1.0', 'RMS[u]', '1.0', 'RMS[uv]', '1.0', 'RMS[uw]', '1.0', 'RMS[v]', '1.0', 'RMS[vw]', '1.0', 'RMS[w]', '1.0', 'Skin_Friction_Coefficient_X', '1.0', 'Skin_Friction_Coefficient_Y', '1.0', 'Skin_Friction_Coefficient_Z', '1.0', 'Skin_Friction_Coefficient_Magnitude', '1.0', 'Temperature', '1.0', "u'u'", '1.0', "u'v'", '1.0', "v'v'", '1.0', 'vtkValidPointMask', '1.0', "w'u'", '1.0', "w'v'", '1.0', "w'w'", '1.0', 'Y_Plus', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
    plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'MeanVelocity_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', "p'p'", '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine1Display_1.SeriesLabelPrefix = ''
    plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Density', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'MeanDensity', '1', 'MeanPressure', '1', 'MeanVelocity_X', '1', 'MeanVelocity_Y', '1', 'MeanVelocity_Z', '1', 'MeanVelocity_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', "p'p'", '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'RMS[Pressure]', '1', 'RMS[u]', '1', 'RMS[uv]', '1', 'RMS[uw]', '1', 'RMS[v]', '1', 'RMS[vw]', '1', 'RMS[w]', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', "u'u'", '1', "u'v'", '1', "v'v'", '1', 'vtkValidPointMask', '1', "w'u'", '1', "w'v'", '1', "w'w'", '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Density', '2', 'Energy', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'MeanDensity', '2', 'MeanPressure', '2', 'MeanVelocity_X', '2', 'MeanVelocity_Y', '2', 'MeanVelocity_Z', '2', 'MeanVelocity_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', "p'p'", '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'RMS[Pressure]', '2', 'RMS[u]', '2', 'RMS[uv]', '2', 'RMS[uw]', '2', 'RMS[v]', '2', 'RMS[vw]', '2', 'RMS[w]', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Temperature', '2', "u'u'", '2', "u'v'", '2', "v'v'", '2', 'vtkValidPointMask', '2', "w'u'", '2', "w'v'", '2', "w'w'", '2', 'Y_Plus', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'MeanVelocity_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', "p'p'", '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'Density', '4', 'Energy', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'MeanDensity', '4', 'MeanPressure', '4', 'MeanVelocity_X', '4', 'MeanVelocity_Y', '4', 'MeanVelocity_Z', '4', 'MeanVelocity_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Momentum_Magnitude', '4', "p'p'", '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'RMS[Pressure]', '4', 'RMS[u]', '4', 'RMS[uv]', '4', 'RMS[uw]', '4', 'RMS[v]', '4', 'RMS[vw]', '4', 'RMS[w]', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Temperature', '4', "u'u'", '4', "u'v'", '4', "v'v'", '4', 'vtkValidPointMask', '4', "w'u'", '4', "w'v'", '4', "w'w'", '4', 'Y_Plus', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

    # get layout
    layout1 = GetLayoutByName("Layout #1")

    # add view to a layout so it's visible in UI
    AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1', 'Density', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'MeanDensity', '1', 'MeanPressure', '1', 'MeanVelocity_X', '1', 'MeanVelocity_Y', '1', 'MeanVelocity_Z', '1', 'MeanVelocity_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', "p'p'", '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'RMS[Pressure]', '1', 'RMS[u]', '1', 'RMS[uv]', '1', 'RMS[uw]', '1', 'RMS[v]', '1', 'RMS[vw]', '1', 'RMS[w]', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', "u'u'", '1', "u'v'", '1', "v'v'", '1', 'vtkValidPointMask', '1', "w'u'", '1', "w'v'", '1', "w'w'", '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine1Display_1.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_Magnitude', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Y_Plus', '0', 'arc_length', '0', "p'p'", '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0']
    plotOverLine1Display_1.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'MeanDensity', '1', 'MeanPressure', '1', 'MeanVelocity_Magnitude', '1', 'MeanVelocity_X', '1', 'MeanVelocity_Y', '1', 'MeanVelocity_Z', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'RMS[Pressure]', '1', 'RMS[u]', '1', 'RMS[uv]', '1', 'RMS[uw]', '1', 'RMS[v]', '1', 'RMS[vw]', '1', 'RMS[w]', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Temperature', '1', 'Y_Plus', '1', 'arc_length', '1', "p'p'", '1', "u'u'", '1', "u'v'", '1', "v'v'", '1', 'vtkValidPointMask', '1', "w'u'", '1', "w'v'", '1', "w'w'", '1']
    plotOverLine1Display_1.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'MeanDensity', '2', 'MeanPressure', '2', 'MeanVelocity_Magnitude', '2', 'MeanVelocity_X', '2', 'MeanVelocity_Y', '2', 'MeanVelocity_Z', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'RMS[Pressure]', '2', 'RMS[u]', '2', 'RMS[uv]', '2', 'RMS[uw]', '2', 'RMS[v]', '2', 'RMS[vw]', '2', 'RMS[w]', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Temperature', '2', 'Y_Plus', '2', 'arc_length', '2', "p'p'", '2', "u'u'", '2', "u'v'", '2', "v'v'", '2', 'vtkValidPointMask', '2', "w'u'", '2', "w'v'", '2', "w'w'", '2']
    plotOverLine1Display_1.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_Magnitude', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Y_Plus', '0', 'arc_length', '0', "p'p'", '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0']
    plotOverLine1Display_1.SeriesMarkerSize = ['Density', '4', 'Energy', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'MeanDensity', '4', 'MeanPressure', '4', 'MeanVelocity_Magnitude', '4', 'MeanVelocity_X', '4', 'MeanVelocity_Y', '4', 'MeanVelocity_Z', '4', 'Momentum_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'RMS[Pressure]', '4', 'RMS[u]', '4', 'RMS[uv]', '4', 'RMS[uw]', '4', 'RMS[v]', '4', 'RMS[vw]', '4', 'RMS[w]', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Temperature', '4', 'Y_Plus', '4', 'arc_length', '4', "p'p'", '4', "u'u'", '4', "u'v'", '4', "v'v'", '4', 'vtkValidPointMask', '4', "w'u'", '4', "w'v'", '4', "w'w'", '4']

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['arc_length', 'Density', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'MeanDensity', 'MeanPressure', 'MeanVelocity_Magnitude', 'MeanVelocity_X', 'MeanVelocity_Y', 'MeanVelocity_Z', 'Momentum_Magnitude', 'Momentum_X', 'Momentum_Y', 'Momentum_Z', "p'p'", 'Points_Magnitude', 'Points_X', 'Points_Y', 'Points_Z', 'Pressure', 'Pressure_Coefficient', 'RMS[Pressure]', 'RMS[u]', 'RMS[uv]', 'RMS[uw]', 'RMS[v]', 'RMS[vw]', 'RMS[w]', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Temperature', "u'u'", "u'v'", "v'v'", 'vtkValidPointMask', "w'u'", "w'v'", "w'w'", 'Y_Plus']

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = []

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.XArrayName = 'Points_X'

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['MeanVelocity_X']

    # set active source
    SetActiveSource(flow_100001vtu)

    # toggle interactive widget visibility (only when running from the GUI)
    HideInteractiveWidgets(proxy=plotOverLine1)

    # split cell
    layout1.SplitVertical(2, 0.5)

    # set active view
    SetActiveView(None)

    # create a new 'Plot Over Line'
    plotOverLine2 = PlotOverLine(registrationName='PlotOverLine2', Input=flow_100001vtu)
    plotOverLine2.Point1 = [-6.0, -30.899999618530273, -30.899999618530273]
    plotOverLine2.Point2 = [70.0, 30.899999618530273, 30.899999618530273]

    # Properties modified on plotOverLine2
    plotOverLine2.Resolution = 199
    plotOverLine2.Point1 = [0.0, 0.0, 0.503]
    plotOverLine2.Point2 = [20.0, 0.0, 0.503]

    # Create a new 'Line Chart View'
    lineChartView2 = CreateView('XYChartView')

    # show data in view
    plotOverLine2Display = Show(plotOverLine2, lineChartView2, 'XYChartRepresentation')

    # trace defaults for the display properties.
    plotOverLine2Display.UseIndexForXAxis = 0
    plotOverLine2Display.XArrayName = 'arc_length'
    plotOverLine2Display.SeriesVisibility = ['Density', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'MeanDensity', 'MeanPressure', 'MeanVelocity_Magnitude', 'Momentum_Magnitude', "p'p'", 'Pressure', 'Pressure_Coefficient', 'RMS[Pressure]', 'RMS[u]', 'RMS[uv]', 'RMS[uw]', 'RMS[v]', 'RMS[vw]', 'RMS[w]', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', "u'u'", "u'v'", "v'v'", "w'u'", "w'v'", "w'w'", 'Y_Plus']
    plotOverLine2Display.SeriesLabel = ['arc_length', 'arc_length', 'Density', 'Density', 'Energy', 'Energy', 'Heat_Flux', 'Heat_Flux', 'Laminar_Viscosity', 'Laminar_Viscosity', 'Mach', 'Mach', 'MeanDensity', 'MeanDensity', 'MeanPressure', 'MeanPressure', 'MeanVelocity_X', 'MeanVelocity_X', 'MeanVelocity_Y', 'MeanVelocity_Y', 'MeanVelocity_Z', 'MeanVelocity_Z', 'MeanVelocity_Magnitude', 'MeanVelocity_Magnitude', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', "p'p'", "p'p'", 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'RMS[Pressure]', 'RMS[Pressure]', 'RMS[u]', 'RMS[u]', 'RMS[uv]', 'RMS[uv]', 'RMS[uw]', 'RMS[uw]', 'RMS[v]', 'RMS[v]', 'RMS[vw]', 'RMS[vw]', 'RMS[w]', 'RMS[w]', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Temperature', "u'u'", "u'u'", "u'v'", "u'v'", "v'v'", "v'v'", 'vtkValidPointMask', 'vtkValidPointMask', "w'u'", "w'u'", "w'v'", "w'v'", "w'w'", "w'w'", 'Y_Plus', 'Y_Plus', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Heat_Flux', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Laminar_Viscosity', '0.6', '0.3100022888532845', '0.6399938963912413', 'Mach', '1', '0.5000076295109483', '0', 'MeanDensity', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'MeanPressure', '0', '0', '0', 'MeanVelocity_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'MeanVelocity_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'MeanVelocity_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'MeanVelocity_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'Momentum_X', '1', '0.5000076295109483', '0', 'Momentum_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Momentum_Z', '0', '0', '0', 'Momentum_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', "p'p'", '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Pressure', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Pressure_Coefficient', '0.6', '0.3100022888532845', '0.6399938963912413', 'RMS[Pressure]', '1', '0.5000076295109483', '0', 'RMS[u]', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'RMS[uv]', '0', '0', '0', 'RMS[uw]', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'RMS[v]', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'RMS[vw]', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'RMS[w]', '0.6', '0.3100022888532845', '0.6399938963912413', 'Skin_Friction_Coefficient_X', '1', '0.5000076295109483', '0', 'Skin_Friction_Coefficient_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Skin_Friction_Coefficient_Z', '0', '0', '0', 'Skin_Friction_Coefficient_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Temperature', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', "u'u'", '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', "u'v'", '0.6', '0.3100022888532845', '0.6399938963912413', "v'v'", '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', "w'u'", '0', '0', '0', "w'v'", '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', "w'w'", '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Y_Plus', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude', '0', '0', '0']
    plotOverLine2Display.SeriesOpacity = ['arc_length', '1.0', 'Density', '1.0', 'Energy', '1.0', 'Heat_Flux', '1.0', 'Laminar_Viscosity', '1.0', 'Mach', '1.0', 'MeanDensity', '1.0', 'MeanPressure', '1.0', 'MeanVelocity_X', '1.0', 'MeanVelocity_Y', '1.0', 'MeanVelocity_Z', '1.0', 'MeanVelocity_Magnitude', '1.0', 'Momentum_X', '1.0', 'Momentum_Y', '1.0', 'Momentum_Z', '1.0', 'Momentum_Magnitude', '1.0', "p'p'", '1.0', 'Pressure', '1.0', 'Pressure_Coefficient', '1.0', 'RMS[Pressure]', '1.0', 'RMS[u]', '1.0', 'RMS[uv]', '1.0', 'RMS[uw]', '1.0', 'RMS[v]', '1.0', 'RMS[vw]', '1.0', 'RMS[w]', '1.0', 'Skin_Friction_Coefficient_X', '1.0', 'Skin_Friction_Coefficient_Y', '1.0', 'Skin_Friction_Coefficient_Z', '1.0', 'Skin_Friction_Coefficient_Magnitude', '1.0', 'Temperature', '1.0', "u'u'", '1.0', "u'v'", '1.0', "v'v'", '1.0', 'vtkValidPointMask', '1.0', "w'u'", '1.0', "w'v'", '1.0', "w'w'", '1.0', 'Y_Plus', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
    plotOverLine2Display.SeriesPlotCorner = ['arc_length', '0', 'Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'MeanVelocity_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', "p'p'", '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine2Display.SeriesLabelPrefix = ''
    plotOverLine2Display.SeriesLineStyle = ['arc_length', '1', 'Density', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'MeanDensity', '1', 'MeanPressure', '1', 'MeanVelocity_X', '1', 'MeanVelocity_Y', '1', 'MeanVelocity_Z', '1', 'MeanVelocity_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', "p'p'", '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'RMS[Pressure]', '1', 'RMS[u]', '1', 'RMS[uv]', '1', 'RMS[uw]', '1', 'RMS[v]', '1', 'RMS[vw]', '1', 'RMS[w]', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', "u'u'", '1', "u'v'", '1', "v'v'", '1', 'vtkValidPointMask', '1', "w'u'", '1', "w'v'", '1', "w'w'", '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine2Display.SeriesLineThickness = ['arc_length', '2', 'Density', '2', 'Energy', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'MeanDensity', '2', 'MeanPressure', '2', 'MeanVelocity_X', '2', 'MeanVelocity_Y', '2', 'MeanVelocity_Z', '2', 'MeanVelocity_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', "p'p'", '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'RMS[Pressure]', '2', 'RMS[u]', '2', 'RMS[uv]', '2', 'RMS[uw]', '2', 'RMS[v]', '2', 'RMS[vw]', '2', 'RMS[w]', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Temperature', '2', "u'u'", '2', "u'v'", '2', "v'v'", '2', 'vtkValidPointMask', '2', "w'u'", '2', "w'v'", '2', "w'w'", '2', 'Y_Plus', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine2Display.SeriesMarkerStyle = ['arc_length', '0', 'Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'MeanVelocity_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', "p'p'", '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine2Display.SeriesMarkerSize = ['arc_length', '4', 'Density', '4', 'Energy', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'MeanDensity', '4', 'MeanPressure', '4', 'MeanVelocity_X', '4', 'MeanVelocity_Y', '4', 'MeanVelocity_Z', '4', 'MeanVelocity_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Momentum_Magnitude', '4', "p'p'", '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'RMS[Pressure]', '4', 'RMS[u]', '4', 'RMS[uv]', '4', 'RMS[uw]', '4', 'RMS[v]', '4', 'RMS[vw]', '4', 'RMS[w]', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Temperature', '4', "u'u'", '4', "u'v'", '4', "v'v'", '4', 'vtkValidPointMask', '4', "w'u'", '4', "w'v'", '4', "w'w'", '4', 'Y_Plus', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

    # add view to a layout so it's visible in UI
    AssignViewToLayout(view=lineChartView2, layout=layout1, hint=6)

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesOpacity = ['arc_length', '1', 'Density', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'MeanDensity', '1', 'MeanPressure', '1', 'MeanVelocity_X', '1', 'MeanVelocity_Y', '1', 'MeanVelocity_Z', '1', 'MeanVelocity_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', "p'p'", '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'RMS[Pressure]', '1', 'RMS[u]', '1', 'RMS[uv]', '1', 'RMS[uw]', '1', 'RMS[v]', '1', 'RMS[vw]', '1', 'RMS[w]', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', "u'u'", '1', "u'v'", '1', "v'v'", '1', 'vtkValidPointMask', '1', "w'u'", '1', "w'v'", '1', "w'w'", '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine2Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_Magnitude', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Y_Plus', '0', 'arc_length', '0', "p'p'", '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0']
    plotOverLine2Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'MeanDensity', '1', 'MeanPressure', '1', 'MeanVelocity_Magnitude', '1', 'MeanVelocity_X', '1', 'MeanVelocity_Y', '1', 'MeanVelocity_Z', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'RMS[Pressure]', '1', 'RMS[u]', '1', 'RMS[uv]', '1', 'RMS[uw]', '1', 'RMS[v]', '1', 'RMS[vw]', '1', 'RMS[w]', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Temperature', '1', 'Y_Plus', '1', 'arc_length', '1', "p'p'", '1', "u'u'", '1', "u'v'", '1', "v'v'", '1', 'vtkValidPointMask', '1', "w'u'", '1', "w'v'", '1', "w'w'", '1']
    plotOverLine2Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'MeanDensity', '2', 'MeanPressure', '2', 'MeanVelocity_Magnitude', '2', 'MeanVelocity_X', '2', 'MeanVelocity_Y', '2', 'MeanVelocity_Z', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'RMS[Pressure]', '2', 'RMS[u]', '2', 'RMS[uv]', '2', 'RMS[uw]', '2', 'RMS[v]', '2', 'RMS[vw]', '2', 'RMS[w]', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Temperature', '2', 'Y_Plus', '2', 'arc_length', '2', "p'p'", '2', "u'u'", '2', "u'v'", '2', "v'v'", '2', 'vtkValidPointMask', '2', "w'u'", '2', "w'v'", '2', "w'w'", '2']
    plotOverLine2Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_Magnitude', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Y_Plus', '0', 'arc_length', '0', "p'p'", '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0']
    plotOverLine2Display.SeriesMarkerSize = ['Density', '4', 'Energy', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'MeanDensity', '4', 'MeanPressure', '4', 'MeanVelocity_Magnitude', '4', 'MeanVelocity_X', '4', 'MeanVelocity_Y', '4', 'MeanVelocity_Z', '4', 'Momentum_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'RMS[Pressure]', '4', 'RMS[u]', '4', 'RMS[uv]', '4', 'RMS[uw]', '4', 'RMS[v]', '4', 'RMS[vw]', '4', 'RMS[w]', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Temperature', '4', 'Y_Plus', '4', 'arc_length', '4', "p'p'", '4', "u'u'", '4', "u'v'", '4', "v'v'", '4', 'vtkValidPointMask', '4', "w'u'", '4', "w'v'", '4', "w'w'", '4']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['arc_length', 'Density', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'MeanDensity', 'MeanPressure', 'MeanVelocity_Magnitude', 'MeanVelocity_X', 'MeanVelocity_Y', 'MeanVelocity_Z', 'Momentum_Magnitude', 'Momentum_X', 'Momentum_Y', 'Momentum_Z', "p'p'", 'Points_Magnitude', 'Points_X', 'Points_Y', 'Points_Z', 'Pressure', 'Pressure_Coefficient', 'RMS[Pressure]', 'RMS[u]', 'RMS[uv]', 'RMS[uw]', 'RMS[v]', 'RMS[vw]', 'RMS[w]', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Temperature', "u'u'", "u'v'", "v'v'", 'vtkValidPointMask', "w'u'", "w'v'", "w'w'", 'Y_Plus']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = []

    plotOverLine3Display.XArrayName = 'Points_X'

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ["u'u'"]

    # set active view
    SetActiveView(renderView1)

    # set active source
    SetActiveSource(flow_100001vtu)

    # toggle interactive widget visibility (only when running from the GUI)
    HideInteractiveWidgets(proxy=plotOverLine2)

    # create a new 'Plot Over Line'
    plotOverLine3 = PlotOverLine(registrationName='PlotOverLine3', Input=flow_100001vtu)
    plotOverLine3.Point1 = [-6.0, -30.899999618530273, -30.899999618530273]
    plotOverLine3.Point2 = [70.0, 30.899999618530273, 30.899999618530273]

    # split cell
    layout1.SplitVertical(1, 0.5)

    # set active view
    SetActiveView(None)

    # Properties modified on plotOverLine3
    plotOverLine3.Resolution = 199
    plotOverLine3.Point1 = [0.0, 0.0, 0.503]
    plotOverLine3.Point2 = [20.0, 0.0, 0.503]

    # Create a new 'Line Chart View'
    lineChartView3 = CreateView('XYChartView')

    # show data in view
    plotOverLine3Display = Show(plotOverLine3, lineChartView3, 'XYChartRepresentation')

    # trace defaults for the display properties.
    plotOverLine3Display.UseIndexForXAxis = 0
    plotOverLine3Display.XArrayName = 'arc_length'
    plotOverLine3Display.SeriesVisibility = ['Density', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'MeanDensity', 'MeanPressure', 'MeanVelocity_Magnitude', 'Momentum_Magnitude', "p'p'", 'Pressure', 'Pressure_Coefficient', 'RMS[Pressure]', 'RMS[u]', 'RMS[uv]', 'RMS[uw]', 'RMS[v]', 'RMS[vw]', 'RMS[w]', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', "u'u'", "u'v'", "v'v'", "w'u'", "w'v'", "w'w'", 'Y_Plus']
    plotOverLine3Display.SeriesLabel = ['arc_length', 'arc_length', 'Density', 'Density', 'Energy', 'Energy', 'Heat_Flux', 'Heat_Flux', 'Laminar_Viscosity', 'Laminar_Viscosity', 'Mach', 'Mach', 'MeanDensity', 'MeanDensity', 'MeanPressure', 'MeanPressure', 'MeanVelocity_X', 'MeanVelocity_X', 'MeanVelocity_Y', 'MeanVelocity_Y', 'MeanVelocity_Z', 'MeanVelocity_Z', 'MeanVelocity_Magnitude', 'MeanVelocity_Magnitude', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', "p'p'", "p'p'", 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'RMS[Pressure]', 'RMS[Pressure]', 'RMS[u]', 'RMS[u]', 'RMS[uv]', 'RMS[uv]', 'RMS[uw]', 'RMS[uw]', 'RMS[v]', 'RMS[v]', 'RMS[vw]', 'RMS[vw]', 'RMS[w]', 'RMS[w]', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Temperature', "u'u'", "u'u'", "u'v'", "u'v'", "v'v'", "v'v'", 'vtkValidPointMask', 'vtkValidPointMask', "w'u'", "w'u'", "w'v'", "w'v'", "w'w'", "w'w'", 'Y_Plus', 'Y_Plus', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Heat_Flux', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Laminar_Viscosity', '0.6', '0.3100022888532845', '0.6399938963912413', 'Mach', '1', '0.5000076295109483', '0', 'MeanDensity', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'MeanPressure', '0', '0', '0', 'MeanVelocity_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'MeanVelocity_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'MeanVelocity_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'MeanVelocity_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'Momentum_X', '1', '0.5000076295109483', '0', 'Momentum_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Momentum_Z', '0', '0', '0', 'Momentum_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', "p'p'", '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Pressure', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Pressure_Coefficient', '0.6', '0.3100022888532845', '0.6399938963912413', 'RMS[Pressure]', '1', '0.5000076295109483', '0', 'RMS[u]', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'RMS[uv]', '0', '0', '0', 'RMS[uw]', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'RMS[v]', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'RMS[vw]', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'RMS[w]', '0.6', '0.3100022888532845', '0.6399938963912413', 'Skin_Friction_Coefficient_X', '1', '0.5000076295109483', '0', 'Skin_Friction_Coefficient_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Skin_Friction_Coefficient_Z', '0', '0', '0', 'Skin_Friction_Coefficient_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Temperature', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', "u'u'", '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', "u'v'", '0.6', '0.3100022888532845', '0.6399938963912413', "v'v'", '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', "w'u'", '0', '0', '0', "w'v'", '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', "w'w'", '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Y_Plus', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude', '0', '0', '0']
    plotOverLine3Display.SeriesOpacity = ['arc_length', '1.0', 'Density', '1.0', 'Energy', '1.0', 'Heat_Flux', '1.0', 'Laminar_Viscosity', '1.0', 'Mach', '1.0', 'MeanDensity', '1.0', 'MeanPressure', '1.0', 'MeanVelocity_X', '1.0', 'MeanVelocity_Y', '1.0', 'MeanVelocity_Z', '1.0', 'MeanVelocity_Magnitude', '1.0', 'Momentum_X', '1.0', 'Momentum_Y', '1.0', 'Momentum_Z', '1.0', 'Momentum_Magnitude', '1.0', "p'p'", '1.0', 'Pressure', '1.0', 'Pressure_Coefficient', '1.0', 'RMS[Pressure]', '1.0', 'RMS[u]', '1.0', 'RMS[uv]', '1.0', 'RMS[uw]', '1.0', 'RMS[v]', '1.0', 'RMS[vw]', '1.0', 'RMS[w]', '1.0', 'Skin_Friction_Coefficient_X', '1.0', 'Skin_Friction_Coefficient_Y', '1.0', 'Skin_Friction_Coefficient_Z', '1.0', 'Skin_Friction_Coefficient_Magnitude', '1.0', 'Temperature', '1.0', "u'u'", '1.0', "u'v'", '1.0', "v'v'", '1.0', 'vtkValidPointMask', '1.0', "w'u'", '1.0', "w'v'", '1.0', "w'w'", '1.0', 'Y_Plus', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
    plotOverLine3Display.SeriesPlotCorner = ['arc_length', '0', 'Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'MeanVelocity_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', "p'p'", '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine3Display.SeriesLabelPrefix = ''
    plotOverLine3Display.SeriesLineStyle = ['arc_length', '1', 'Density', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'MeanDensity', '1', 'MeanPressure', '1', 'MeanVelocity_X', '1', 'MeanVelocity_Y', '1', 'MeanVelocity_Z', '1', 'MeanVelocity_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', "p'p'", '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'RMS[Pressure]', '1', 'RMS[u]', '1', 'RMS[uv]', '1', 'RMS[uw]', '1', 'RMS[v]', '1', 'RMS[vw]', '1', 'RMS[w]', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', "u'u'", '1', "u'v'", '1', "v'v'", '1', 'vtkValidPointMask', '1', "w'u'", '1', "w'v'", '1', "w'w'", '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine3Display.SeriesLineThickness = ['arc_length', '2', 'Density', '2', 'Energy', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'MeanDensity', '2', 'MeanPressure', '2', 'MeanVelocity_X', '2', 'MeanVelocity_Y', '2', 'MeanVelocity_Z', '2', 'MeanVelocity_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', "p'p'", '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'RMS[Pressure]', '2', 'RMS[u]', '2', 'RMS[uv]', '2', 'RMS[uw]', '2', 'RMS[v]', '2', 'RMS[vw]', '2', 'RMS[w]', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Temperature', '2', "u'u'", '2', "u'v'", '2', "v'v'", '2', 'vtkValidPointMask', '2', "w'u'", '2', "w'v'", '2', "w'w'", '2', 'Y_Plus', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine3Display.SeriesMarkerStyle = ['arc_length', '0', 'Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'MeanVelocity_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', "p'p'", '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine3Display.SeriesMarkerSize = ['arc_length', '4', 'Density', '4', 'Energy', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'MeanDensity', '4', 'MeanPressure', '4', 'MeanVelocity_X', '4', 'MeanVelocity_Y', '4', 'MeanVelocity_Z', '4', 'MeanVelocity_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Momentum_Magnitude', '4', "p'p'", '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'RMS[Pressure]', '4', 'RMS[u]', '4', 'RMS[uv]', '4', 'RMS[uw]', '4', 'RMS[v]', '4', 'RMS[vw]', '4', 'RMS[w]', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Temperature', '4', "u'u'", '4', "u'v'", '4', "v'v'", '4', 'vtkValidPointMask', '4', "w'u'", '4', "w'v'", '4', "w'w'", '4', 'Y_Plus', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

    # add view to a layout so it's visible in UI
    AssignViewToLayout(view=lineChartView3, layout=layout1, hint=4)

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesOpacity = ['arc_length', '1', 'Density', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'MeanDensity', '1', 'MeanPressure', '1', 'MeanVelocity_X', '1', 'MeanVelocity_Y', '1', 'MeanVelocity_Z', '1', 'MeanVelocity_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', "p'p'", '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'RMS[Pressure]', '1', 'RMS[u]', '1', 'RMS[uv]', '1', 'RMS[uw]', '1', 'RMS[v]', '1', 'RMS[vw]', '1', 'RMS[w]', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', "u'u'", '1', "u'v'", '1', "v'v'", '1', 'vtkValidPointMask', '1', "w'u'", '1', "w'v'", '1', "w'w'", '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine3Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_Magnitude', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Y_Plus', '0', 'arc_length', '0', "p'p'", '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0']
    plotOverLine3Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'MeanDensity', '1', 'MeanPressure', '1', 'MeanVelocity_Magnitude', '1', 'MeanVelocity_X', '1', 'MeanVelocity_Y', '1', 'MeanVelocity_Z', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'RMS[Pressure]', '1', 'RMS[u]', '1', 'RMS[uv]', '1', 'RMS[uw]', '1', 'RMS[v]', '1', 'RMS[vw]', '1', 'RMS[w]', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Temperature', '1', 'Y_Plus', '1', 'arc_length', '1', "p'p'", '1', "u'u'", '1', "u'v'", '1', "v'v'", '1', 'vtkValidPointMask', '1', "w'u'", '1', "w'v'", '1', "w'w'", '1']
    plotOverLine3Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'MeanDensity', '2', 'MeanPressure', '2', 'MeanVelocity_Magnitude', '2', 'MeanVelocity_X', '2', 'MeanVelocity_Y', '2', 'MeanVelocity_Z', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'RMS[Pressure]', '2', 'RMS[u]', '2', 'RMS[uv]', '2', 'RMS[uw]', '2', 'RMS[v]', '2', 'RMS[vw]', '2', 'RMS[w]', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Temperature', '2', 'Y_Plus', '2', 'arc_length', '2', "p'p'", '2', "u'u'", '2', "u'v'", '2', "v'v'", '2', 'vtkValidPointMask', '2', "w'u'", '2', "w'v'", '2', "w'w'", '2']
    plotOverLine3Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'MeanDensity', '0', 'MeanPressure', '0', 'MeanVelocity_Magnitude', '0', 'MeanVelocity_X', '0', 'MeanVelocity_Y', '0', 'MeanVelocity_Z', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'RMS[Pressure]', '0', 'RMS[u]', '0', 'RMS[uv]', '0', 'RMS[uw]', '0', 'RMS[v]', '0', 'RMS[vw]', '0', 'RMS[w]', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Y_Plus', '0', 'arc_length', '0', "p'p'", '0', "u'u'", '0', "u'v'", '0', "v'v'", '0', 'vtkValidPointMask', '0', "w'u'", '0', "w'v'", '0', "w'w'", '0']
    plotOverLine3Display.SeriesMarkerSize = ['Density', '4', 'Energy', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'MeanDensity', '4', 'MeanPressure', '4', 'MeanVelocity_Magnitude', '4', 'MeanVelocity_X', '4', 'MeanVelocity_Y', '4', 'MeanVelocity_Z', '4', 'Momentum_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'RMS[Pressure]', '4', 'RMS[u]', '4', 'RMS[uv]', '4', 'RMS[uw]', '4', 'RMS[v]', '4', 'RMS[vw]', '4', 'RMS[w]', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Temperature', '4', 'Y_Plus', '4', 'arc_length', '4', "p'p'", '4', "u'u'", '4', "u'v'", '4', "v'v'", '4', 'vtkValidPointMask', '4', "w'u'", '4', "w'v'", '4', "w'w'", '4']

    # update the view to ensure updated data information
    lineChartView2.Update()

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['arc_length', 'Density', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'MeanDensity', 'MeanPressure', 'MeanVelocity_Magnitude', 'MeanVelocity_X', 'MeanVelocity_Y', 'MeanVelocity_Z', 'Momentum_Magnitude', 'Momentum_X', 'Momentum_Y', 'Momentum_Z', "p'p'", 'Points_Magnitude', 'Points_X', 'Points_Y', 'Points_Z', 'Pressure', 'Pressure_Coefficient', 'RMS[Pressure]', 'RMS[u]', 'RMS[uv]', 'RMS[uw]', 'RMS[v]', 'RMS[vw]', 'RMS[w]', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Temperature', "u'u'", "u'v'", "v'v'", 'vtkValidPointMask', "w'u'", "w'v'", "w'w'", 'Y_Plus']

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = []

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.XArrayName = 'Points_X'

    # # Properties modified on plotOverLine3Display
    # plotOverLine3Display.XArrayName = 'Y_Plus'

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ["w'u'"]

    export_hf_file = os.path.join(exportDir, "run" + "{:03d}".format(runID), "export_HF_data.csv")

    # save data
    SaveData(export_hf_file, proxy=plotOverLine3, ChooseArraysToWrite=1,
             PointDataArrays=['MeanVelocity', "u'u'", "w'u'"],
             Precision=23,
             UseScientificNotation=1)

    # set active view
    SetActiveView(lineChartView2)

    # set active view
    SetActiveView(lineChartView3)

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(1317, 817)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [29.863474568717393, 0.0, 223.73858735662557]
    renderView1.CameraFocalPoint = [32.0, 0.0, 0.0]
    renderView1.CameraParallelScale = 57.91044770031002

    #--------------------------------------------
    # uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).

    Delete(plotOverLine1)
    del plotOverLine1
    Delete(plotOverLine2)
    del plotOverLine2
    Delete(plotOverLine3)
    del plotOverLine3

    Delete(flow100001vtu)
    del flow100001vtu


    print("Processed {}".format(flowFileName))
    
print("Finished post-processing of flow solutions")
print("To see result files, go to: {}".format(exportDir))

