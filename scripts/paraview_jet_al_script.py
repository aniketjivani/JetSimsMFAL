# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10


#### import the simple module from the paraview
from paraview.simple import *


import os
runDir = "/work/e734/e734/shared/ajivani/JetSimsMFAL/runs_LF_batch_test"
exportDir = "/home/e734/e734/ajivani/jet_LF_batch_test"

try:
    os.mkdir(exportDir)
except FileExistsError:
    pass

runID1 = 1
runID2 = 8

for runID in range(runID1, runID2 + 1):
    runIDPath = os.path.join(exportDir, "run" + str(runID))
    try:
        os.mkdir(runIDPath)
    except FileExistsError:
        pass


for runID in range(runID1, runID2 + 1):
    flowFileName = os.path.join(runDir, "run" + "%03d" % runID, "flow.vtu")
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()
    # create a new 'XML Unstructured Grid Reader'
    flowvtu = XMLUnstructuredGridReader(registrationName='flow.vtu', FileName=[flowFileName])
    flowvtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Nu_Tilde', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient', 'Laminar_Viscosity', 'Skin_Friction_Coefficient', 'Heat_Flux', 'Y_Plus', 'Eddy_Viscosity', 'Vorticity', 'Q_Criterion']

    # Properties modified on flowvtu
    flowvtu.TimeArray = 'None'

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    flowvtuDisplay = Show(flowvtu, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    flowvtuDisplay.Representation = 'Surface'
    flowvtuDisplay.ColorArrayName = [None, '']
    flowvtuDisplay.SelectTCoordArray = 'None'
    flowvtuDisplay.SelectNormalArray = 'None'
    flowvtuDisplay.SelectTangentArray = 'None'
    flowvtuDisplay.OSPRayScaleArray = 'Density'
    flowvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    flowvtuDisplay.SelectOrientationVectors = 'Momentum'
    flowvtuDisplay.ScaleFactor = 7.6000000000000005
    flowvtuDisplay.SelectScaleArray = 'Density'
    flowvtuDisplay.GlyphType = 'Arrow'
    flowvtuDisplay.GlyphTableIndexArray = 'Density'
    flowvtuDisplay.GaussianRadius = 0.38
    flowvtuDisplay.SetScaleArray = ['POINTS', 'Density']
    flowvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    flowvtuDisplay.OpacityArray = ['POINTS', 'Density']
    flowvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    flowvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
    flowvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
    flowvtuDisplay.ScalarOpacityUnitDistance = 1.0106759524215592
    flowvtuDisplay.OpacityArrayName = ['POINTS', 'Density']

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    flowvtuDisplay.ScaleTransferFunction.Points = [0.07034882158041, 0.0, 0.5, 0.0, 0.07241223007440567, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    flowvtuDisplay.OpacityTransferFunction.Points = [0.07034882158041, 0.0, 0.5, 0.0, 0.07241223007440567, 1.0, 0.5, 0.0]

    # reset view to fit data
    renderView1.ResetCamera(False)

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Calculator'
    calculator1 = Calculator(registrationName='Calculator1', Input=flowvtu)
    calculator1.Function = ''

    # Properties modified on calculator1
    calculator1.ResultArrayName = 'Velocity'
    calculator1.Function = 'Momentum/Density'

    # show data in view
    calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    calculator1Display.Representation = 'Surface'
    calculator1Display.ColorArrayName = [None, '']
    calculator1Display.SelectTCoordArray = 'None'
    calculator1Display.SelectNormalArray = 'None'
    calculator1Display.SelectTangentArray = 'None'
    calculator1Display.OSPRayScaleArray = 'Density'
    calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator1Display.SelectOrientationVectors = 'Velocity'
    calculator1Display.ScaleFactor = 7.6000000000000005
    calculator1Display.SelectScaleArray = 'Density'
    calculator1Display.GlyphType = 'Arrow'
    calculator1Display.GlyphTableIndexArray = 'Density'
    calculator1Display.GaussianRadius = 0.38
    calculator1Display.SetScaleArray = ['POINTS', 'Density']
    calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator1Display.OpacityArray = ['POINTS', 'Density']
    calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator1Display.PolarAxes = 'PolarAxesRepresentation'
    calculator1Display.ScalarOpacityUnitDistance = 1.0106759524215592
    calculator1Display.OpacityArrayName = ['POINTS', 'Density']

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator1Display.ScaleTransferFunction.Points = [0.07034882158041, 0.0, 0.5, 0.0, 0.07241223007440567, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator1Display.OpacityTransferFunction.Points = [0.07034882158041, 0.0, 0.5, 0.0, 0.07241223007440567, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(flowvtu, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Gradient'
    gradient1 = Gradient(registrationName='Gradient1', Input=calculator1)
    gradient1.ScalarArray = ['POINTS', 'Density']

    # Properties modified on gradient1
    gradient1.ScalarArray = ['POINTS', 'Velocity']

    # show data in view
    gradient1Display = Show(gradient1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    gradient1Display.Representation = 'Surface'
    gradient1Display.ColorArrayName = [None, '']
    gradient1Display.SelectTCoordArray = 'None'
    gradient1Display.SelectNormalArray = 'None'
    gradient1Display.SelectTangentArray = 'None'
    gradient1Display.OSPRayScaleArray = 'Density'
    gradient1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    gradient1Display.SelectOrientationVectors = 'Velocity'
    gradient1Display.ScaleFactor = 7.6000000000000005
    gradient1Display.SelectScaleArray = 'Density'
    gradient1Display.GlyphType = 'Arrow'
    gradient1Display.GlyphTableIndexArray = 'Density'
    gradient1Display.GaussianRadius = 0.38
    gradient1Display.SetScaleArray = ['POINTS', 'Density']
    gradient1Display.ScaleTransferFunction = 'PiecewiseFunction'
    gradient1Display.OpacityArray = ['POINTS', 'Density']
    gradient1Display.OpacityTransferFunction = 'PiecewiseFunction'
    gradient1Display.DataAxesGrid = 'GridAxesRepresentation'
    gradient1Display.PolarAxes = 'PolarAxesRepresentation'
    gradient1Display.ScalarOpacityUnitDistance = 1.0106759524215592
    gradient1Display.OpacityArrayName = ['POINTS', 'Density']

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    gradient1Display.ScaleTransferFunction.Points = [0.07034882158041, 0.0, 0.5, 0.0, 0.07241223007440567, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    gradient1Display.OpacityTransferFunction.Points = [0.07034882158041, 0.0, 0.5, 0.0, 0.07241223007440567, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(calculator1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Calculator'
    calculator2 = Calculator(registrationName='Calculator2', Input=gradient1)
    calculator2.Function = ''

    # RenameProxy('ReynoldsStressUU', 'sources', calculator2)

    # # rename source object
    # RenameSource('ReynoldsStressUU', calculator2)

    # Properties modified on calculator2
    calculator2.ResultArrayName = 'ReynoldsStressUU'
    calculator2.Function = '(-1/Density)*Eddy_Viscosity*("Gradient_0" + "Gradient_0"-(2/3)*("Gradient_0"+"Gradient_4"+"Gradient_8"))'

    # show data in view
    calculator2Display = Show(calculator2, renderView1, 'UnstructuredGridRepresentation')

    # get color transfer function/color map for 'ReynoldsStressUU'
    reynoldsStressUULUT = GetColorTransferFunction('ReynoldsStressUU')

    # get opacity transfer function/opacity map for 'ReynoldsStressUU'
    reynoldsStressUUPWF = GetOpacityTransferFunction('ReynoldsStressUU')

    # trace defaults for the display properties.
    calculator2Display.Representation = 'Surface'
    calculator2Display.ColorArrayName = ['POINTS', 'ReynoldsStressUU']
    calculator2Display.LookupTable = reynoldsStressUULUT
    calculator2Display.SelectTCoordArray = 'None'
    calculator2Display.SelectNormalArray = 'None'
    calculator2Display.SelectTangentArray = 'None'
    calculator2Display.OSPRayScaleArray = 'ReynoldsStressUU'
    calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator2Display.SelectOrientationVectors = 'Velocity'
    calculator2Display.ScaleFactor = 7.6000000000000005
    calculator2Display.SelectScaleArray = 'ReynoldsStressUU'
    calculator2Display.GlyphType = 'Arrow'
    calculator2Display.GlyphTableIndexArray = 'ReynoldsStressUU'
    calculator2Display.GaussianRadius = 0.38
    calculator2Display.SetScaleArray = ['POINTS', 'ReynoldsStressUU']
    calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator2Display.OpacityArray = ['POINTS', 'ReynoldsStressUU']
    calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator2Display.PolarAxes = 'PolarAxesRepresentation'
    calculator2Display.ScalarOpacityFunction = reynoldsStressUUPWF
    calculator2Display.ScalarOpacityUnitDistance = 1.0106759524215592
    calculator2Display.OpacityArrayName = ['POINTS', 'ReynoldsStressUU']

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator2Display.ScaleTransferFunction.Points = [-54.38664406994252, 0.0, 0.5, 0.0, 233.92620165753584, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator2Display.OpacityTransferFunction.Points = [-54.38664406994252, 0.0, 0.5, 0.0, 233.92620165753584, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(gradient1, renderView1)

    # show color bar/color legend
    calculator2Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(gradient1)

    # create a new 'Calculator'
    calculator2_1 = Calculator(registrationName='Calculator2', Input=gradient1)
    calculator2_1.Function = ''

    # set active source
    SetActiveSource(gradient1)

    # destroy calculator2_1
    Delete(calculator2_1)
    del calculator2_1

    # create a new 'Calculator'
    calculator2_1 = Calculator(registrationName='Calculator2', Input=gradient1)
    calculator2_1.Function = ''

    # RenameProxy('ReynoldsStressUW', 'sources', calculator2_1)

    # # rename source object
    # RenameSource('ReynoldsStressUW', calculator2_1)

    # Properties modified on calculator2_1
    calculator2_1.ResultArrayName = 'ReynoldsStressUW'
    calculator2_1.Function = '(-1/Density)*Eddy_Viscosity*("Gradient_2"+"Gradient_6"-(2/3)*("Gradient_0"+"Gradient_4"+"Gradient_8"))'

    # show data in view
    calculator2_1Display = Show(calculator2_1, renderView1, 'UnstructuredGridRepresentation')

    # get color transfer function/color map for 'ReynoldsStressUW'
    reynoldsStressUWLUT = GetColorTransferFunction('ReynoldsStressUW')

    # get opacity transfer function/opacity map for 'ReynoldsStressUW'
    reynoldsStressUWPWF = GetOpacityTransferFunction('ReynoldsStressUW')

    # trace defaults for the display properties.
    calculator2_1Display.Representation = 'Surface'
    calculator2_1Display.ColorArrayName = ['POINTS', 'ReynoldsStressUW']
    calculator2_1Display.LookupTable = reynoldsStressUWLUT
    calculator2_1Display.SelectTCoordArray = 'None'
    calculator2_1Display.SelectNormalArray = 'None'
    calculator2_1Display.SelectTangentArray = 'None'
    calculator2_1Display.OSPRayScaleArray = 'ReynoldsStressUW'
    calculator2_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator2_1Display.SelectOrientationVectors = 'Velocity'
    calculator2_1Display.ScaleFactor = 7.6000000000000005
    calculator2_1Display.SelectScaleArray = 'ReynoldsStressUW'
    calculator2_1Display.GlyphType = 'Arrow'
    calculator2_1Display.GlyphTableIndexArray = 'ReynoldsStressUW'
    calculator2_1Display.GaussianRadius = 0.38
    calculator2_1Display.SetScaleArray = ['POINTS', 'ReynoldsStressUW']
    calculator2_1Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator2_1Display.OpacityArray = ['POINTS', 'ReynoldsStressUW']
    calculator2_1Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator2_1Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator2_1Display.PolarAxes = 'PolarAxesRepresentation'
    calculator2_1Display.ScalarOpacityFunction = reynoldsStressUWPWF
    calculator2_1Display.ScalarOpacityUnitDistance = 1.0106759524215592
    calculator2_1Display.OpacityArrayName = ['POINTS', 'ReynoldsStressUW']

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator2_1Display.ScaleTransferFunction.Points = [-905.5465945044825, 0.0, 0.5, 0.0, 906.5971503645628, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator2_1Display.OpacityTransferFunction.Points = [-905.5465945044825, 0.0, 0.5, 0.0, 906.5971503645628, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(gradient1, renderView1)

    # show color bar/color legend
    calculator2_1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # hide data in view
    Hide(calculator2, renderView1)

    # hide data in view
    Hide(calculator2_1, renderView1)

    # set active source
    SetActiveSource(calculator2)

    # create a new 'Plot Over Line'
    plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=calculator2)
    plotOverLine1.Point1 = [-6.0, -30.899999618530273, -30.899999618530273]
    plotOverLine1.Point2 = [70.0, 30.899999618530273, 30.899999618530273]

    # Properties modified on plotOverLine1
    plotOverLine1.Point1 = [0.0, 0.0, 0.5]
    plotOverLine1.Point2 = [20.0, 0.0, 0.5]
    plotOverLine1.Resolution = 199

    # show data in view
    plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    plotOverLine1Display.Representation = 'Surface'
    plotOverLine1Display.ColorArrayName = ['POINTS', 'ReynoldsStressUU']
    plotOverLine1Display.LookupTable = reynoldsStressUULUT
    plotOverLine1Display.SelectTCoordArray = 'None'
    plotOverLine1Display.SelectNormalArray = 'None'
    plotOverLine1Display.SelectTangentArray = 'None'
    plotOverLine1Display.OSPRayScaleArray = 'ReynoldsStressUU'
    plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    plotOverLine1Display.SelectOrientationVectors = 'Velocity'
    plotOverLine1Display.ScaleFactor = 2.0
    plotOverLine1Display.SelectScaleArray = 'ReynoldsStressUU'
    plotOverLine1Display.GlyphType = 'Arrow'
    plotOverLine1Display.GlyphTableIndexArray = 'ReynoldsStressUU'
    plotOverLine1Display.GaussianRadius = 0.1
    plotOverLine1Display.SetScaleArray = ['POINTS', 'ReynoldsStressUU']
    plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
    plotOverLine1Display.OpacityArray = ['POINTS', 'ReynoldsStressUU']
    plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
    plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
    plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    plotOverLine1Display.ScaleTransferFunction.Points = [-30.369977387246973, 0.0, 0.5, 0.0, 104.56717202148467, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    plotOverLine1Display.OpacityTransferFunction.Points = [-30.369977387246973, 0.0, 0.5, 0.0, 104.56717202148467, 1.0, 0.5, 0.0]

    # Create a new 'Line Chart View'
    lineChartView1 = CreateView('XYChartView')

    # show data in view
    plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

    # trace defaults for the display properties.
    plotOverLine1Display_1.UseIndexForXAxis = 0
    plotOverLine1Display_1.XArrayName = 'arc_length'
    plotOverLine1Display_1.SeriesVisibility = ['Density', 'Eddy_Viscosity', 'Energy', 'Gradient_Magnitude', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum_Magnitude', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Q_Criterion', 'ReynoldsStressUU', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Velocity_Magnitude', 'Vorticity_Magnitude', 'Y_Plus']
    plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Density', 'Density', 'Eddy_Viscosity', 'Eddy_Viscosity', 'Energy', 'Energy', 'Gradient_0', 'Gradient_0', 'Gradient_1', 'Gradient_1', 'Gradient_2', 'Gradient_2', 'Gradient_3', 'Gradient_3', 'Gradient_4', 'Gradient_4', 'Gradient_5', 'Gradient_5', 'Gradient_6', 'Gradient_6', 'Gradient_7', 'Gradient_7', 'Gradient_8', 'Gradient_8', 'Gradient_Magnitude', 'Gradient_Magnitude', 'Heat_Flux', 'Heat_Flux', 'Laminar_Viscosity', 'Laminar_Viscosity', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Nu_Tilde', 'Nu_Tilde', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Q_Criterion', 'Q_Criterion', 'ReynoldsStressUU', 'ReynoldsStressUU', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Temperature', 'Velocity_X', 'Velocity_X', 'Velocity_Y', 'Velocity_Y', 'Velocity_Z', 'Velocity_Z', 'Velocity_Magnitude', 'Velocity_Magnitude', 'Vorticity_X', 'Vorticity_X', 'Vorticity_Y', 'Vorticity_Y', 'Vorticity_Z', 'Vorticity_Z', 'Vorticity_Magnitude', 'Vorticity_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Y_Plus', 'Y_Plus', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Eddy_Viscosity', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Gradient_0', '0.6', '0.3100022888532845', '0.6399938963912413', 'Gradient_1', '1', '0.5000076295109483', '0', 'Gradient_2', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Gradient_3', '0', '0', '0', 'Gradient_4', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Gradient_5', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Gradient_6', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Gradient_7', '0.6', '0.3100022888532845', '0.6399938963912413', 'Gradient_8', '1', '0.5000076295109483', '0', 'Gradient_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Heat_Flux', '0', '0', '0', 'Laminar_Viscosity', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Momentum_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Momentum_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Momentum_Z', '1', '0.5000076295109483', '0', 'Momentum_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Nu_Tilde', '0', '0', '0', 'Pressure', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Pressure_Coefficient', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Q_Criterion', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'ReynoldsStressUU', '0.6', '0.3100022888532845', '0.6399938963912413', 'Skin_Friction_Coefficient_X', '1', '0.5000076295109483', '0', 'Skin_Friction_Coefficient_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Skin_Friction_Coefficient_Z', '0', '0', '0', 'Skin_Friction_Coefficient_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Temperature', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Velocity_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Velocity_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Velocity_Z', '1', '0.5000076295109483', '0', 'Velocity_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Vorticity_X', '0', '0', '0', 'Vorticity_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Vorticity_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Vorticity_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Y_Plus', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
    plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Nu_Tilde', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUU', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Vorticity_Magnitude', '0', 'vtkValidPointMask', '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine1Display_1.SeriesLabelPrefix = ''
    plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Density', '1', 'Eddy_Viscosity', '1', 'Energy', '1', 'Gradient_0', '1', 'Gradient_1', '1', 'Gradient_2', '1', 'Gradient_3', '1', 'Gradient_4', '1', 'Gradient_5', '1', 'Gradient_6', '1', 'Gradient_7', '1', 'Gradient_8', '1', 'Gradient_Magnitude', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Nu_Tilde', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Q_Criterion', '1', 'ReynoldsStressUU', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'Velocity_Magnitude', '1', 'Vorticity_X', '1', 'Vorticity_Y', '1', 'Vorticity_Z', '1', 'Vorticity_Magnitude', '1', 'vtkValidPointMask', '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Density', '2', 'Eddy_Viscosity', '2', 'Energy', '2', 'Gradient_0', '2', 'Gradient_1', '2', 'Gradient_2', '2', 'Gradient_3', '2', 'Gradient_4', '2', 'Gradient_5', '2', 'Gradient_6', '2', 'Gradient_7', '2', 'Gradient_8', '2', 'Gradient_Magnitude', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Nu_Tilde', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Q_Criterion', '2', 'ReynoldsStressUU', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Temperature', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'Velocity_Magnitude', '2', 'Vorticity_X', '2', 'Vorticity_Y', '2', 'Vorticity_Z', '2', 'Vorticity_Magnitude', '2', 'vtkValidPointMask', '2', 'Y_Plus', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Nu_Tilde', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUU', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Vorticity_Magnitude', '0', 'vtkValidPointMask', '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'Density', '4', 'Eddy_Viscosity', '4', 'Energy', '4', 'Gradient_0', '4', 'Gradient_1', '4', 'Gradient_2', '4', 'Gradient_3', '4', 'Gradient_4', '4', 'Gradient_5', '4', 'Gradient_6', '4', 'Gradient_7', '4', 'Gradient_8', '4', 'Gradient_Magnitude', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Momentum_Magnitude', '4', 'Nu_Tilde', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'Q_Criterion', '4', 'ReynoldsStressUU', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Temperature', '4', 'Velocity_X', '4', 'Velocity_Y', '4', 'Velocity_Z', '4', 'Velocity_Magnitude', '4', 'Vorticity_X', '4', 'Vorticity_Y', '4', 'Vorticity_Z', '4', 'Vorticity_Magnitude', '4', 'vtkValidPointMask', '4', 'Y_Plus', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

    # get layout
    layout1 = GetLayoutByName("Layout #1")

    # add view to a layout so it's visible in UI
    AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesPlotCorner = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Nu_Tilde', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUU', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Vorticity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Y_Plus', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
    plotOverLine1Display_1.SeriesLineStyle = ['Density', '1', 'Eddy_Viscosity', '1', 'Energy', '1', 'Gradient_0', '1', 'Gradient_1', '1', 'Gradient_2', '1', 'Gradient_3', '1', 'Gradient_4', '1', 'Gradient_5', '1', 'Gradient_6', '1', 'Gradient_7', '1', 'Gradient_8', '1', 'Gradient_Magnitude', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Nu_Tilde', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Q_Criterion', '1', 'ReynoldsStressUU', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Temperature', '1', 'Velocity_Magnitude', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'Vorticity_Magnitude', '1', 'Vorticity_X', '1', 'Vorticity_Y', '1', 'Vorticity_Z', '1', 'Y_Plus', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
    plotOverLine1Display_1.SeriesLineThickness = ['Density', '2', 'Eddy_Viscosity', '2', 'Energy', '2', 'Gradient_0', '2', 'Gradient_1', '2', 'Gradient_2', '2', 'Gradient_3', '2', 'Gradient_4', '2', 'Gradient_5', '2', 'Gradient_6', '2', 'Gradient_7', '2', 'Gradient_8', '2', 'Gradient_Magnitude', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Nu_Tilde', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Q_Criterion', '2', 'ReynoldsStressUU', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Temperature', '2', 'Velocity_Magnitude', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'Vorticity_Magnitude', '2', 'Vorticity_X', '2', 'Vorticity_Y', '2', 'Vorticity_Z', '2', 'Y_Plus', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
    plotOverLine1Display_1.SeriesMarkerStyle = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Nu_Tilde', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUU', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Vorticity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Y_Plus', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
    plotOverLine1Display_1.SeriesMarkerSize = ['Density', '4', 'Eddy_Viscosity', '4', 'Energy', '4', 'Gradient_0', '4', 'Gradient_1', '4', 'Gradient_2', '4', 'Gradient_3', '4', 'Gradient_4', '4', 'Gradient_5', '4', 'Gradient_6', '4', 'Gradient_7', '4', 'Gradient_8', '4', 'Gradient_Magnitude', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'Momentum_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Nu_Tilde', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'Q_Criterion', '4', 'ReynoldsStressUU', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Temperature', '4', 'Velocity_Magnitude', '4', 'Velocity_X', '4', 'Velocity_Y', '4', 'Velocity_Z', '4', 'Vorticity_Magnitude', '4', 'Vorticity_X', '4', 'Vorticity_Y', '4', 'Vorticity_Z', '4', 'Y_Plus', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

    # set active source
    SetActiveSource(flowvtu)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=plotOverLine1)

    # show data in view
    flowvtuDisplay_1 = Show(flowvtu, lineChartView1, 'XYChartRepresentation')

    # trace defaults for the display properties.
    flowvtuDisplay_1.XArrayName = 'Density'
    flowvtuDisplay_1.SeriesVisibility = ['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum_Magnitude', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Q_Criterion', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Vorticity_Magnitude', 'Y_Plus']
    flowvtuDisplay_1.SeriesLabel = ['Density', 'Density', 'Eddy_Viscosity', 'Eddy_Viscosity', 'Energy', 'Energy', 'Heat_Flux', 'Heat_Flux', 'Laminar_Viscosity', 'Laminar_Viscosity', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Nu_Tilde', 'Nu_Tilde', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Q_Criterion', 'Q_Criterion', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Temperature', 'Vorticity_X', 'Vorticity_X', 'Vorticity_Y', 'Vorticity_Y', 'Vorticity_Z', 'Vorticity_Z', 'Vorticity_Magnitude', 'Vorticity_Magnitude', 'Y_Plus', 'Y_Plus', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    flowvtuDisplay_1.SeriesColor = ['Density', '0', '0', '0', 'Eddy_Viscosity', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Heat_Flux', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Laminar_Viscosity', '0.6', '0.3100022888532845', '0.6399938963912413', 'Mach', '1', '0.5000076295109483', '0', 'Momentum_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Momentum_Y', '0', '0', '0', 'Momentum_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Momentum_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Nu_Tilde', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Pressure', '0.6', '0.3100022888532845', '0.6399938963912413', 'Pressure_Coefficient', '1', '0.5000076295109483', '0', 'Q_Criterion', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Skin_Friction_Coefficient_X', '0', '0', '0', 'Skin_Friction_Coefficient_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Skin_Friction_Coefficient_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Skin_Friction_Coefficient_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Temperature', '0.6', '0.3100022888532845', '0.6399938963912413', 'Vorticity_X', '1', '0.5000076295109483', '0', 'Vorticity_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Vorticity_Z', '0', '0', '0', 'Vorticity_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Y_Plus', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Z', '1', '0.5000076295109483', '0', 'Points_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867']
    flowvtuDisplay_1.SeriesPlotCorner = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Nu_Tilde', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Vorticity_Magnitude', '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    flowvtuDisplay_1.SeriesLabelPrefix = ''
    flowvtuDisplay_1.SeriesLineStyle = ['Density', '1', 'Eddy_Viscosity', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Nu_Tilde', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Q_Criterion', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', 'Vorticity_X', '1', 'Vorticity_Y', '1', 'Vorticity_Z', '1', 'Vorticity_Magnitude', '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    flowvtuDisplay_1.SeriesLineThickness = ['Density', '2', 'Eddy_Viscosity', '2', 'Energy', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Nu_Tilde', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Q_Criterion', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Temperature', '2', 'Vorticity_X', '2', 'Vorticity_Y', '2', 'Vorticity_Z', '2', 'Vorticity_Magnitude', '2', 'Y_Plus', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    flowvtuDisplay_1.SeriesMarkerStyle = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Nu_Tilde', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Vorticity_Magnitude', '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    flowvtuDisplay_1.SeriesMarkerSize = ['Density', '4', 'Eddy_Viscosity', '4', 'Energy', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Momentum_Magnitude', '4', 'Nu_Tilde', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'Q_Criterion', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Temperature', '4', 'Vorticity_X', '4', 'Vorticity_Y', '4', 'Vorticity_Z', '4', 'Vorticity_Magnitude', '4', 'Y_Plus', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

    # Properties modified on flowvtuDisplay_1
    flowvtuDisplay_1.SeriesPlotCorner = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Nu_Tilde', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Vorticity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Y_Plus', '0']
    flowvtuDisplay_1.SeriesLineStyle = ['Density', '1', 'Eddy_Viscosity', '1', 'Energy', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Nu_Tilde', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Q_Criterion', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Temperature', '1', 'Vorticity_Magnitude', '1', 'Vorticity_X', '1', 'Vorticity_Y', '1', 'Vorticity_Z', '1', 'Y_Plus', '1']
    flowvtuDisplay_1.SeriesLineThickness = ['Density', '2', 'Eddy_Viscosity', '2', 'Energy', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Nu_Tilde', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Q_Criterion', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Temperature', '2', 'Vorticity_Magnitude', '2', 'Vorticity_X', '2', 'Vorticity_Y', '2', 'Vorticity_Z', '2', 'Y_Plus', '2']
    flowvtuDisplay_1.SeriesMarkerStyle = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Nu_Tilde', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Vorticity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Y_Plus', '0']
    flowvtuDisplay_1.SeriesMarkerSize = ['Density', '4', 'Eddy_Viscosity', '4', 'Energy', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'Momentum_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Nu_Tilde', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'Q_Criterion', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Temperature', '4', 'Vorticity_Magnitude', '4', 'Vorticity_X', '4', 'Vorticity_Y', '4', 'Vorticity_Z', '4', 'Y_Plus', '4']

    # hide data in view
    Hide(flowvtu, lineChartView1)

    # set active source
    SetActiveSource(plotOverLine1)

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['arc_length', 'Density', 'Eddy_Viscosity', 'Energy', 'Gradient_0', 'Gradient_1', 'Gradient_2', 'Gradient_3', 'Gradient_4', 'Gradient_5', 'Gradient_6', 'Gradient_7', 'Gradient_8', 'Gradient_Magnitude', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum_Magnitude', 'Momentum_X', 'Momentum_Y', 'Momentum_Z', 'Nu_Tilde', 'Points_Magnitude', 'Points_X', 'Points_Y', 'Points_Z', 'Pressure', 'Pressure_Coefficient', 'Q_Criterion', 'ReynoldsStressUU', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Temperature', 'Velocity_Magnitude', 'Velocity_X', 'Velocity_Y', 'Velocity_Z', 'Vorticity_Magnitude', 'Vorticity_X', 'Vorticity_Y', 'Vorticity_Z', 'vtkValidPointMask', 'Y_Plus']

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = []

    # Properties modified on lineChartView1
    lineChartView1.BottomAxisUseCustomRange = 0

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesVisibility = ['ReynoldsStressUU']

    # Properties modified on lineChartView1
    lineChartView1.LeftAxisUseCustomRange = 0

    # set active source
    SetActiveSource(calculator2_1)

    # create a new 'Plot Over Line'
    plotOverLine2 = PlotOverLine(registrationName='PlotOverLine2', Input=calculator2_1)
    plotOverLine2.Point1 = [-6.0, -30.899999618530273, -30.899999618530273]
    plotOverLine2.Point2 = [70.0, 30.899999618530273, 30.899999618530273]

    # Properties modified on plotOverLine2
    plotOverLine2.Point1 = [0.0, 0.0, 0.5]
    plotOverLine2.Point2 = [20.0, 0.0, 0.5]
    plotOverLine2.Resolution = 199

    # show data in view
    plotOverLine2Display = Show(plotOverLine2, lineChartView1, 'XYChartRepresentation')

    # trace defaults for the display properties.
    plotOverLine2Display.UseIndexForXAxis = 0
    plotOverLine2Display.XArrayName = 'arc_length'
    plotOverLine2Display.SeriesVisibility = ['Density', 'Eddy_Viscosity', 'Energy', 'Gradient_Magnitude', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum_Magnitude', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Q_Criterion', 'ReynoldsStressUW', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Velocity_Magnitude', 'Vorticity_Magnitude', 'Y_Plus']
    plotOverLine2Display.SeriesLabel = ['arc_length', 'arc_length', 'Density', 'Density', 'Eddy_Viscosity', 'Eddy_Viscosity', 'Energy', 'Energy', 'Gradient_0', 'Gradient_0', 'Gradient_1', 'Gradient_1', 'Gradient_2', 'Gradient_2', 'Gradient_3', 'Gradient_3', 'Gradient_4', 'Gradient_4', 'Gradient_5', 'Gradient_5', 'Gradient_6', 'Gradient_6', 'Gradient_7', 'Gradient_7', 'Gradient_8', 'Gradient_8', 'Gradient_Magnitude', 'Gradient_Magnitude', 'Heat_Flux', 'Heat_Flux', 'Laminar_Viscosity', 'Laminar_Viscosity', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Nu_Tilde', 'Nu_Tilde', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Q_Criterion', 'Q_Criterion', 'ReynoldsStressUW', 'ReynoldsStressUW', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Temperature', 'Velocity_X', 'Velocity_X', 'Velocity_Y', 'Velocity_Y', 'Velocity_Z', 'Velocity_Z', 'Velocity_Magnitude', 'Velocity_Magnitude', 'Vorticity_X', 'Vorticity_X', 'Vorticity_Y', 'Vorticity_Y', 'Vorticity_Z', 'Vorticity_Z', 'Vorticity_Magnitude', 'Vorticity_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Y_Plus', 'Y_Plus', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Eddy_Viscosity', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Gradient_0', '0.6', '0.3100022888532845', '0.6399938963912413', 'Gradient_1', '1', '0.5000076295109483', '0', 'Gradient_2', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Gradient_3', '0', '0', '0', 'Gradient_4', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Gradient_5', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Gradient_6', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Gradient_7', '0.6', '0.3100022888532845', '0.6399938963912413', 'Gradient_8', '1', '0.5000076295109483', '0', 'Gradient_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Heat_Flux', '0', '0', '0', 'Laminar_Viscosity', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Momentum_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Momentum_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Momentum_Z', '1', '0.5000076295109483', '0', 'Momentum_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Nu_Tilde', '0', '0', '0', 'Pressure', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Pressure_Coefficient', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Q_Criterion', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'ReynoldsStressUW', '0.6', '0.3100022888532845', '0.6399938963912413', 'Skin_Friction_Coefficient_X', '1', '0.5000076295109483', '0', 'Skin_Friction_Coefficient_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Skin_Friction_Coefficient_Z', '0', '0', '0', 'Skin_Friction_Coefficient_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Temperature', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Velocity_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Velocity_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Velocity_Z', '1', '0.5000076295109483', '0', 'Velocity_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Vorticity_X', '0', '0', '0', 'Vorticity_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Vorticity_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Vorticity_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Y_Plus', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
    plotOverLine2Display.SeriesPlotCorner = ['arc_length', '0', 'Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Nu_Tilde', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUW', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Vorticity_Magnitude', '0', 'vtkValidPointMask', '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine2Display.SeriesLabelPrefix = ''
    plotOverLine2Display.SeriesLineStyle = ['arc_length', '1', 'Density', '1', 'Eddy_Viscosity', '1', 'Energy', '1', 'Gradient_0', '1', 'Gradient_1', '1', 'Gradient_2', '1', 'Gradient_3', '1', 'Gradient_4', '1', 'Gradient_5', '1', 'Gradient_6', '1', 'Gradient_7', '1', 'Gradient_8', '1', 'Gradient_Magnitude', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Nu_Tilde', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Q_Criterion', '1', 'ReynoldsStressUW', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'Velocity_Magnitude', '1', 'Vorticity_X', '1', 'Vorticity_Y', '1', 'Vorticity_Z', '1', 'Vorticity_Magnitude', '1', 'vtkValidPointMask', '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine2Display.SeriesLineThickness = ['arc_length', '2', 'Density', '2', 'Eddy_Viscosity', '2', 'Energy', '2', 'Gradient_0', '2', 'Gradient_1', '2', 'Gradient_2', '2', 'Gradient_3', '2', 'Gradient_4', '2', 'Gradient_5', '2', 'Gradient_6', '2', 'Gradient_7', '2', 'Gradient_8', '2', 'Gradient_Magnitude', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Nu_Tilde', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Q_Criterion', '2', 'ReynoldsStressUW', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Temperature', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'Velocity_Magnitude', '2', 'Vorticity_X', '2', 'Vorticity_Y', '2', 'Vorticity_Z', '2', 'Vorticity_Magnitude', '2', 'vtkValidPointMask', '2', 'Y_Plus', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine2Display.SeriesMarkerStyle = ['arc_length', '0', 'Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Nu_Tilde', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUW', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Vorticity_Magnitude', '0', 'vtkValidPointMask', '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine2Display.SeriesMarkerSize = ['arc_length', '4', 'Density', '4', 'Eddy_Viscosity', '4', 'Energy', '4', 'Gradient_0', '4', 'Gradient_1', '4', 'Gradient_2', '4', 'Gradient_3', '4', 'Gradient_4', '4', 'Gradient_5', '4', 'Gradient_6', '4', 'Gradient_7', '4', 'Gradient_8', '4', 'Gradient_Magnitude', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Momentum_Magnitude', '4', 'Nu_Tilde', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'Q_Criterion', '4', 'ReynoldsStressUW', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Temperature', '4', 'Velocity_X', '4', 'Velocity_Y', '4', 'Velocity_Z', '4', 'Velocity_Magnitude', '4', 'Vorticity_X', '4', 'Vorticity_Y', '4', 'Vorticity_Z', '4', 'Vorticity_Magnitude', '4', 'vtkValidPointMask', '4', 'Y_Plus', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

    # update the view to ensure updated data information
    lineChartView1.Update()

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesPlotCorner = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Nu_Tilde', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUW', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Vorticity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Y_Plus', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
    plotOverLine2Display.SeriesLineStyle = ['Density', '1', 'Eddy_Viscosity', '1', 'Energy', '1', 'Gradient_0', '1', 'Gradient_1', '1', 'Gradient_2', '1', 'Gradient_3', '1', 'Gradient_4', '1', 'Gradient_5', '1', 'Gradient_6', '1', 'Gradient_7', '1', 'Gradient_8', '1', 'Gradient_Magnitude', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Nu_Tilde', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Q_Criterion', '1', 'ReynoldsStressUW', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Temperature', '1', 'Velocity_Magnitude', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'Vorticity_Magnitude', '1', 'Vorticity_X', '1', 'Vorticity_Y', '1', 'Vorticity_Z', '1', 'Y_Plus', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
    plotOverLine2Display.SeriesLineThickness = ['Density', '2', 'Eddy_Viscosity', '2', 'Energy', '2', 'Gradient_0', '2', 'Gradient_1', '2', 'Gradient_2', '2', 'Gradient_3', '2', 'Gradient_4', '2', 'Gradient_5', '2', 'Gradient_6', '2', 'Gradient_7', '2', 'Gradient_8', '2', 'Gradient_Magnitude', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Nu_Tilde', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Q_Criterion', '2', 'ReynoldsStressUW', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Temperature', '2', 'Velocity_Magnitude', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'Vorticity_Magnitude', '2', 'Vorticity_X', '2', 'Vorticity_Y', '2', 'Vorticity_Z', '2', 'Y_Plus', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
    plotOverLine2Display.SeriesMarkerStyle = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Nu_Tilde', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUW', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Vorticity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Y_Plus', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
    plotOverLine2Display.SeriesMarkerSize = ['Density', '4', 'Eddy_Viscosity', '4', 'Energy', '4', 'Gradient_0', '4', 'Gradient_1', '4', 'Gradient_2', '4', 'Gradient_3', '4', 'Gradient_4', '4', 'Gradient_5', '4', 'Gradient_6', '4', 'Gradient_7', '4', 'Gradient_8', '4', 'Gradient_Magnitude', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'Momentum_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Nu_Tilde', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'Q_Criterion', '4', 'ReynoldsStressUW', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Temperature', '4', 'Velocity_Magnitude', '4', 'Velocity_X', '4', 'Velocity_Y', '4', 'Velocity_Z', '4', 'Vorticity_Magnitude', '4', 'Vorticity_X', '4', 'Vorticity_Y', '4', 'Vorticity_Z', '4', 'Y_Plus', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

    # set active source
    SetActiveSource(calculator2_1)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=plotOverLine2)

    # hide data in view
    Hide(plotOverLine2, lineChartView1)

    # destroy plotOverLine2
    Delete(plotOverLine2)
    del plotOverLine2

    # split cell
    layout1.SplitVertical(2, 0.5)

    # set active view
    SetActiveView(None)

    # Create a new 'Line Chart View'
    lineChartView2 = CreateView('XYChartView')

    # assign view to a particular cell in the layout
    AssignViewToLayout(view=lineChartView2, layout=layout1, hint=6)

    # set active source
    SetActiveSource(calculator2_1)

    # create a new 'Plot Over Line'
    plotOverLine2 = PlotOverLine(registrationName='PlotOverLine2', Input=calculator2_1)
    plotOverLine2.Point1 = [-6.0, -30.899999618530273, -30.899999618530273]
    plotOverLine2.Point2 = [70.0, 30.899999618530273, 30.899999618530273]

    # Properties modified on plotOverLine2
    plotOverLine2.Point1 = [0.0, 0.0, 0.5]
    plotOverLine2.Point2 = [20.0, 0.0, 0.5]
    plotOverLine2.Resolution = 199

    # show data in view
    plotOverLine2Display = Show(plotOverLine2, lineChartView2, 'XYChartRepresentation')

    # trace defaults for the display properties.
    plotOverLine2Display.UseIndexForXAxis = 0
    plotOverLine2Display.XArrayName = 'arc_length'
    plotOverLine2Display.SeriesVisibility = ['Density', 'Eddy_Viscosity', 'Energy', 'Gradient_Magnitude', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum_Magnitude', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Q_Criterion', 'ReynoldsStressUW', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Velocity_Magnitude', 'Vorticity_Magnitude', 'Y_Plus']
    plotOverLine2Display.SeriesLabel = ['arc_length', 'arc_length', 'Density', 'Density', 'Eddy_Viscosity', 'Eddy_Viscosity', 'Energy', 'Energy', 'Gradient_0', 'Gradient_0', 'Gradient_1', 'Gradient_1', 'Gradient_2', 'Gradient_2', 'Gradient_3', 'Gradient_3', 'Gradient_4', 'Gradient_4', 'Gradient_5', 'Gradient_5', 'Gradient_6', 'Gradient_6', 'Gradient_7', 'Gradient_7', 'Gradient_8', 'Gradient_8', 'Gradient_Magnitude', 'Gradient_Magnitude', 'Heat_Flux', 'Heat_Flux', 'Laminar_Viscosity', 'Laminar_Viscosity', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Nu_Tilde', 'Nu_Tilde', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Q_Criterion', 'Q_Criterion', 'ReynoldsStressUW', 'ReynoldsStressUW', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Temperature', 'Velocity_X', 'Velocity_X', 'Velocity_Y', 'Velocity_Y', 'Velocity_Z', 'Velocity_Z', 'Velocity_Magnitude', 'Velocity_Magnitude', 'Vorticity_X', 'Vorticity_X', 'Vorticity_Y', 'Vorticity_Y', 'Vorticity_Z', 'Vorticity_Z', 'Vorticity_Magnitude', 'Vorticity_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Y_Plus', 'Y_Plus', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Eddy_Viscosity', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Gradient_0', '0.6', '0.3100022888532845', '0.6399938963912413', 'Gradient_1', '1', '0.5000076295109483', '0', 'Gradient_2', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Gradient_3', '0', '0', '0', 'Gradient_4', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Gradient_5', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Gradient_6', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Gradient_7', '0.6', '0.3100022888532845', '0.6399938963912413', 'Gradient_8', '1', '0.5000076295109483', '0', 'Gradient_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Heat_Flux', '0', '0', '0', 'Laminar_Viscosity', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Momentum_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Momentum_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Momentum_Z', '1', '0.5000076295109483', '0', 'Momentum_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Nu_Tilde', '0', '0', '0', 'Pressure', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Pressure_Coefficient', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Q_Criterion', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'ReynoldsStressUW', '0.6', '0.3100022888532845', '0.6399938963912413', 'Skin_Friction_Coefficient_X', '1', '0.5000076295109483', '0', 'Skin_Friction_Coefficient_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Skin_Friction_Coefficient_Z', '0', '0', '0', 'Skin_Friction_Coefficient_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Temperature', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Velocity_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Velocity_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Velocity_Z', '1', '0.5000076295109483', '0', 'Velocity_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Vorticity_X', '0', '0', '0', 'Vorticity_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Vorticity_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Vorticity_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vtkValidPointMask', '0.6', '0.3100022888532845', '0.6399938963912413', 'Y_Plus', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
    plotOverLine2Display.SeriesPlotCorner = ['arc_length', '0', 'Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Nu_Tilde', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUW', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Vorticity_Magnitude', '0', 'vtkValidPointMask', '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine2Display.SeriesLabelPrefix = ''
    plotOverLine2Display.SeriesLineStyle = ['arc_length', '1', 'Density', '1', 'Eddy_Viscosity', '1', 'Energy', '1', 'Gradient_0', '1', 'Gradient_1', '1', 'Gradient_2', '1', 'Gradient_3', '1', 'Gradient_4', '1', 'Gradient_5', '1', 'Gradient_6', '1', 'Gradient_7', '1', 'Gradient_8', '1', 'Gradient_Magnitude', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Nu_Tilde', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Q_Criterion', '1', 'ReynoldsStressUW', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'Velocity_Magnitude', '1', 'Vorticity_X', '1', 'Vorticity_Y', '1', 'Vorticity_Z', '1', 'Vorticity_Magnitude', '1', 'vtkValidPointMask', '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine2Display.SeriesLineThickness = ['arc_length', '2', 'Density', '2', 'Eddy_Viscosity', '2', 'Energy', '2', 'Gradient_0', '2', 'Gradient_1', '2', 'Gradient_2', '2', 'Gradient_3', '2', 'Gradient_4', '2', 'Gradient_5', '2', 'Gradient_6', '2', 'Gradient_7', '2', 'Gradient_8', '2', 'Gradient_Magnitude', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Nu_Tilde', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Q_Criterion', '2', 'ReynoldsStressUW', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Temperature', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'Velocity_Magnitude', '2', 'Vorticity_X', '2', 'Vorticity_Y', '2', 'Vorticity_Z', '2', 'Vorticity_Magnitude', '2', 'vtkValidPointMask', '2', 'Y_Plus', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine2Display.SeriesMarkerStyle = ['arc_length', '0', 'Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Nu_Tilde', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUW', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Vorticity_Magnitude', '0', 'vtkValidPointMask', '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine2Display.SeriesMarkerSize = ['arc_length', '4', 'Density', '4', 'Eddy_Viscosity', '4', 'Energy', '4', 'Gradient_0', '4', 'Gradient_1', '4', 'Gradient_2', '4', 'Gradient_3', '4', 'Gradient_4', '4', 'Gradient_5', '4', 'Gradient_6', '4', 'Gradient_7', '4', 'Gradient_8', '4', 'Gradient_Magnitude', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Momentum_Magnitude', '4', 'Nu_Tilde', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'Q_Criterion', '4', 'ReynoldsStressUW', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Temperature', '4', 'Velocity_X', '4', 'Velocity_Y', '4', 'Velocity_Z', '4', 'Velocity_Magnitude', '4', 'Vorticity_X', '4', 'Vorticity_Y', '4', 'Vorticity_Z', '4', 'Vorticity_Magnitude', '4', 'vtkValidPointMask', '4', 'Y_Plus', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

    # update the view to ensure updated data information
    lineChartView2.Update()

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesPlotCorner = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Nu_Tilde', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUW', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Vorticity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Y_Plus', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
    plotOverLine2Display.SeriesLineStyle = ['Density', '1', 'Eddy_Viscosity', '1', 'Energy', '1', 'Gradient_0', '1', 'Gradient_1', '1', 'Gradient_2', '1', 'Gradient_3', '1', 'Gradient_4', '1', 'Gradient_5', '1', 'Gradient_6', '1', 'Gradient_7', '1', 'Gradient_8', '1', 'Gradient_Magnitude', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Nu_Tilde', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Q_Criterion', '1', 'ReynoldsStressUW', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Temperature', '1', 'Velocity_Magnitude', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'Vorticity_Magnitude', '1', 'Vorticity_X', '1', 'Vorticity_Y', '1', 'Vorticity_Z', '1', 'Y_Plus', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
    plotOverLine2Display.SeriesLineThickness = ['Density', '2', 'Eddy_Viscosity', '2', 'Energy', '2', 'Gradient_0', '2', 'Gradient_1', '2', 'Gradient_2', '2', 'Gradient_3', '2', 'Gradient_4', '2', 'Gradient_5', '2', 'Gradient_6', '2', 'Gradient_7', '2', 'Gradient_8', '2', 'Gradient_Magnitude', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Nu_Tilde', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Q_Criterion', '2', 'ReynoldsStressUW', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Temperature', '2', 'Velocity_Magnitude', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'Vorticity_Magnitude', '2', 'Vorticity_X', '2', 'Vorticity_Y', '2', 'Vorticity_Z', '2', 'Y_Plus', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
    plotOverLine2Display.SeriesMarkerStyle = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Nu_Tilde', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'ReynoldsStressUW', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Vorticity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Y_Plus', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
    plotOverLine2Display.SeriesMarkerSize = ['Density', '4', 'Eddy_Viscosity', '4', 'Energy', '4', 'Gradient_0', '4', 'Gradient_1', '4', 'Gradient_2', '4', 'Gradient_3', '4', 'Gradient_4', '4', 'Gradient_5', '4', 'Gradient_6', '4', 'Gradient_7', '4', 'Gradient_8', '4', 'Gradient_Magnitude', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'Momentum_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Nu_Tilde', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'Q_Criterion', '4', 'ReynoldsStressUW', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Temperature', '4', 'Velocity_Magnitude', '4', 'Velocity_X', '4', 'Velocity_Y', '4', 'Velocity_Z', '4', 'Vorticity_Magnitude', '4', 'Vorticity_X', '4', 'Vorticity_Y', '4', 'Vorticity_Z', '4', 'Y_Plus', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['arc_length', 'Density', 'Eddy_Viscosity', 'Energy', 'Gradient_0', 'Gradient_1', 'Gradient_2', 'Gradient_3', 'Gradient_4', 'Gradient_5', 'Gradient_6', 'Gradient_7', 'Gradient_8', 'Gradient_Magnitude', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum_Magnitude', 'Momentum_X', 'Momentum_Y', 'Momentum_Z', 'Nu_Tilde', 'Points_Magnitude', 'Points_X', 'Points_Y', 'Points_Z', 'Pressure', 'Pressure_Coefficient', 'Q_Criterion', 'ReynoldsStressUW', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Temperature', 'Velocity_Magnitude', 'Velocity_X', 'Velocity_Y', 'Velocity_Z', 'Vorticity_Magnitude', 'Vorticity_X', 'Vorticity_Y', 'Vorticity_Z', 'vtkValidPointMask', 'Y_Plus']

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = []

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.XArrayName = 'Points_X'

    # Properties modified on plotOverLine2Display
    plotOverLine2Display.SeriesVisibility = ['ReynoldsStressUW']

    # set active view
    SetActiveView(lineChartView1)

    # set active source
    SetActiveSource(plotOverLine1)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=plotOverLine2)

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.XArrayName = 'Points_X'

    # set active source
    SetActiveSource(plotOverLine2)

    # set active view
    SetActiveView(lineChartView2)

    # set active source
    SetActiveSource(gradient1)

    # create a new 'Calculator'
    calculator2_2 = Calculator(registrationName='Calculator2', Input=gradient1)
    calculator2_2.Function = ''

    # set active source
    SetActiveSource(gradient1)

    # destroy calculator2_2
    Delete(calculator2_2)
    del calculator2_2

    # split cell
    layout1.SplitVertical(6, 0.5)

    # set active view
    SetActiveView(None)

    # Create a new 'Line Chart View'
    lineChartView3 = CreateView('XYChartView')

    # assign view to a particular cell in the layout
    AssignViewToLayout(view=lineChartView3, layout=layout1, hint=14)

    # resize frame
    layout1.SetSplitFraction(6, 0.35585585585585583)

    # resize frame
    layout1.SetSplitFraction(2, 0.3486547085201794)

    # create a new 'Plot Over Line'
    plotOverLine3 = PlotOverLine(registrationName='PlotOverLine3', Input=gradient1)
    plotOverLine3.Point1 = [-6.0, -30.899999618530273, -30.899999618530273]
    plotOverLine3.Point2 = [70.0, 30.899999618530273, 30.899999618530273]

    # Properties modified on plotOverLine3
    plotOverLine3.Point1 = [0.0, 0.0, 0.5]
    plotOverLine3.Point2 = [20.0, 0.0, 0.5]
    plotOverLine3.Resolution = 199

    # show data in view
    plotOverLine3Display = Show(plotOverLine3, lineChartView3, 'XYChartRepresentation')

    # trace defaults for the display properties.
    plotOverLine3Display.UseIndexForXAxis = 0
    plotOverLine3Display.XArrayName = 'arc_length'
    plotOverLine3Display.SeriesVisibility = ['Density', 'Eddy_Viscosity', 'Energy', 'Gradient_Magnitude', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum_Magnitude', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Q_Criterion', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Velocity_Magnitude', 'Vorticity_Magnitude', 'Y_Plus']
    plotOverLine3Display.SeriesLabel = ['arc_length', 'arc_length', 'Density', 'Density', 'Eddy_Viscosity', 'Eddy_Viscosity', 'Energy', 'Energy', 'Gradient_0', 'Gradient_0', 'Gradient_1', 'Gradient_1', 'Gradient_2', 'Gradient_2', 'Gradient_3', 'Gradient_3', 'Gradient_4', 'Gradient_4', 'Gradient_5', 'Gradient_5', 'Gradient_6', 'Gradient_6', 'Gradient_7', 'Gradient_7', 'Gradient_8', 'Gradient_8', 'Gradient_Magnitude', 'Gradient_Magnitude', 'Heat_Flux', 'Heat_Flux', 'Laminar_Viscosity', 'Laminar_Viscosity', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Nu_Tilde', 'Nu_Tilde', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Q_Criterion', 'Q_Criterion', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Z', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_Magnitude', 'Temperature', 'Temperature', 'Velocity_X', 'Velocity_X', 'Velocity_Y', 'Velocity_Y', 'Velocity_Z', 'Velocity_Z', 'Velocity_Magnitude', 'Velocity_Magnitude', 'Vorticity_X', 'Vorticity_X', 'Vorticity_Y', 'Vorticity_Y', 'Vorticity_Z', 'Vorticity_Z', 'Vorticity_Magnitude', 'Vorticity_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Y_Plus', 'Y_Plus', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Eddy_Viscosity', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Gradient_0', '0.6', '0.3100022888532845', '0.6399938963912413', 'Gradient_1', '1', '0.5000076295109483', '0', 'Gradient_2', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Gradient_3', '0', '0', '0', 'Gradient_4', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Gradient_5', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Gradient_6', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Gradient_7', '0.6', '0.3100022888532845', '0.6399938963912413', 'Gradient_8', '1', '0.5000076295109483', '0', 'Gradient_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Heat_Flux', '0', '0', '0', 'Laminar_Viscosity', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Momentum_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Momentum_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Momentum_Z', '1', '0.5000076295109483', '0', 'Momentum_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Nu_Tilde', '0', '0', '0', 'Pressure', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Pressure_Coefficient', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Q_Criterion', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Skin_Friction_Coefficient_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Skin_Friction_Coefficient_Y', '1', '0.5000076295109483', '0', 'Skin_Friction_Coefficient_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Skin_Friction_Coefficient_Magnitude', '0', '0', '0', 'Temperature', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Velocity_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Velocity_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Velocity_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'Velocity_Magnitude', '1', '0.5000076295109483', '0', 'Vorticity_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Vorticity_Y', '0', '0', '0', 'Vorticity_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Vorticity_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'vtkValidPointMask', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Y_Plus', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
    plotOverLine3Display.SeriesPlotCorner = ['arc_length', '0', 'Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Nu_Tilde', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Vorticity_Magnitude', '0', 'vtkValidPointMask', '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine3Display.SeriesLabelPrefix = ''
    plotOverLine3Display.SeriesLineStyle = ['arc_length', '1', 'Density', '1', 'Eddy_Viscosity', '1', 'Energy', '1', 'Gradient_0', '1', 'Gradient_1', '1', 'Gradient_2', '1', 'Gradient_3', '1', 'Gradient_4', '1', 'Gradient_5', '1', 'Gradient_6', '1', 'Gradient_7', '1', 'Gradient_8', '1', 'Gradient_Magnitude', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Nu_Tilde', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Q_Criterion', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Temperature', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'Velocity_Magnitude', '1', 'Vorticity_X', '1', 'Vorticity_Y', '1', 'Vorticity_Z', '1', 'Vorticity_Magnitude', '1', 'vtkValidPointMask', '1', 'Y_Plus', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine3Display.SeriesLineThickness = ['arc_length', '2', 'Density', '2', 'Eddy_Viscosity', '2', 'Energy', '2', 'Gradient_0', '2', 'Gradient_1', '2', 'Gradient_2', '2', 'Gradient_3', '2', 'Gradient_4', '2', 'Gradient_5', '2', 'Gradient_6', '2', 'Gradient_7', '2', 'Gradient_8', '2', 'Gradient_Magnitude', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Nu_Tilde', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Q_Criterion', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Temperature', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'Velocity_Magnitude', '2', 'Vorticity_X', '2', 'Vorticity_Y', '2', 'Vorticity_Z', '2', 'Vorticity_Magnitude', '2', 'vtkValidPointMask', '2', 'Y_Plus', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine3Display.SeriesMarkerStyle = ['arc_length', '0', 'Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Nu_Tilde', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Temperature', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Vorticity_Magnitude', '0', 'vtkValidPointMask', '0', 'Y_Plus', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine3Display.SeriesMarkerSize = ['arc_length', '4', 'Density', '4', 'Eddy_Viscosity', '4', 'Energy', '4', 'Gradient_0', '4', 'Gradient_1', '4', 'Gradient_2', '4', 'Gradient_3', '4', 'Gradient_4', '4', 'Gradient_5', '4', 'Gradient_6', '4', 'Gradient_7', '4', 'Gradient_8', '4', 'Gradient_Magnitude', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Momentum_Magnitude', '4', 'Nu_Tilde', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'Q_Criterion', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Temperature', '4', 'Velocity_X', '4', 'Velocity_Y', '4', 'Velocity_Z', '4', 'Velocity_Magnitude', '4', 'Vorticity_X', '4', 'Vorticity_Y', '4', 'Vorticity_Z', '4', 'Vorticity_Magnitude', '4', 'vtkValidPointMask', '4', 'Y_Plus', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

    # update the view to ensure updated data information
    lineChartView3.Update()

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesPlotCorner = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Nu_Tilde', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Vorticity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Y_Plus', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
    plotOverLine3Display.SeriesLineStyle = ['Density', '1', 'Eddy_Viscosity', '1', 'Energy', '1', 'Gradient_0', '1', 'Gradient_1', '1', 'Gradient_2', '1', 'Gradient_3', '1', 'Gradient_4', '1', 'Gradient_5', '1', 'Gradient_6', '1', 'Gradient_7', '1', 'Gradient_8', '1', 'Gradient_Magnitude', '1', 'Heat_Flux', '1', 'Laminar_Viscosity', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Nu_Tilde', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Q_Criterion', '1', 'Skin_Friction_Coefficient_Magnitude', '1', 'Skin_Friction_Coefficient_X', '1', 'Skin_Friction_Coefficient_Y', '1', 'Skin_Friction_Coefficient_Z', '1', 'Temperature', '1', 'Velocity_Magnitude', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'Vorticity_Magnitude', '1', 'Vorticity_X', '1', 'Vorticity_Y', '1', 'Vorticity_Z', '1', 'Y_Plus', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
    plotOverLine3Display.SeriesLineThickness = ['Density', '2', 'Eddy_Viscosity', '2', 'Energy', '2', 'Gradient_0', '2', 'Gradient_1', '2', 'Gradient_2', '2', 'Gradient_3', '2', 'Gradient_4', '2', 'Gradient_5', '2', 'Gradient_6', '2', 'Gradient_7', '2', 'Gradient_8', '2', 'Gradient_Magnitude', '2', 'Heat_Flux', '2', 'Laminar_Viscosity', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Nu_Tilde', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Q_Criterion', '2', 'Skin_Friction_Coefficient_Magnitude', '2', 'Skin_Friction_Coefficient_X', '2', 'Skin_Friction_Coefficient_Y', '2', 'Skin_Friction_Coefficient_Z', '2', 'Temperature', '2', 'Velocity_Magnitude', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'Vorticity_Magnitude', '2', 'Vorticity_X', '2', 'Vorticity_Y', '2', 'Vorticity_Z', '2', 'Y_Plus', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
    plotOverLine3Display.SeriesMarkerStyle = ['Density', '0', 'Eddy_Viscosity', '0', 'Energy', '0', 'Gradient_0', '0', 'Gradient_1', '0', 'Gradient_2', '0', 'Gradient_3', '0', 'Gradient_4', '0', 'Gradient_5', '0', 'Gradient_6', '0', 'Gradient_7', '0', 'Gradient_8', '0', 'Gradient_Magnitude', '0', 'Heat_Flux', '0', 'Laminar_Viscosity', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Nu_Tilde', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Q_Criterion', '0', 'Skin_Friction_Coefficient_Magnitude', '0', 'Skin_Friction_Coefficient_X', '0', 'Skin_Friction_Coefficient_Y', '0', 'Skin_Friction_Coefficient_Z', '0', 'Temperature', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Vorticity_Magnitude', '0', 'Vorticity_X', '0', 'Vorticity_Y', '0', 'Vorticity_Z', '0', 'Y_Plus', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
    plotOverLine3Display.SeriesMarkerSize = ['Density', '4', 'Eddy_Viscosity', '4', 'Energy', '4', 'Gradient_0', '4', 'Gradient_1', '4', 'Gradient_2', '4', 'Gradient_3', '4', 'Gradient_4', '4', 'Gradient_5', '4', 'Gradient_6', '4', 'Gradient_7', '4', 'Gradient_8', '4', 'Gradient_Magnitude', '4', 'Heat_Flux', '4', 'Laminar_Viscosity', '4', 'Mach', '4', 'Momentum_Magnitude', '4', 'Momentum_X', '4', 'Momentum_Y', '4', 'Momentum_Z', '4', 'Nu_Tilde', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Pressure', '4', 'Pressure_Coefficient', '4', 'Q_Criterion', '4', 'Skin_Friction_Coefficient_Magnitude', '4', 'Skin_Friction_Coefficient_X', '4', 'Skin_Friction_Coefficient_Y', '4', 'Skin_Friction_Coefficient_Z', '4', 'Temperature', '4', 'Velocity_Magnitude', '4', 'Velocity_X', '4', 'Velocity_Y', '4', 'Velocity_Z', '4', 'Vorticity_Magnitude', '4', 'Vorticity_X', '4', 'Vorticity_Y', '4', 'Vorticity_Z', '4', 'Y_Plus', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['arc_length', 'Density', 'Eddy_Viscosity', 'Energy', 'Gradient_0', 'Gradient_1', 'Gradient_2', 'Gradient_3', 'Gradient_4', 'Gradient_5', 'Gradient_6', 'Gradient_7', 'Gradient_8', 'Gradient_Magnitude', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum_Magnitude', 'Momentum_X', 'Momentum_Y', 'Momentum_Z', 'Nu_Tilde', 'Points_Magnitude', 'Points_X', 'Points_Y', 'Points_Z', 'Pressure', 'Pressure_Coefficient', 'Q_Criterion', 'Skin_Friction_Coefficient_Magnitude', 'Skin_Friction_Coefficient_X', 'Skin_Friction_Coefficient_Y', 'Skin_Friction_Coefficient_Z', 'Temperature', 'Velocity_Magnitude', 'Velocity_X', 'Velocity_Y', 'Velocity_Z', 'Vorticity_Magnitude', 'Vorticity_X', 'Vorticity_Y', 'Vorticity_Z', 'vtkValidPointMask', 'Y_Plus']

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = []

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.SeriesVisibility = ['Velocity_X']

    export_file_velocity = os.path.join(exportDir, "run" + str(runID), "mean_vel.csv")
    export_file_uu = os.path.join(exportDir, "run" + str(runID), "reynolds_stress_uu.csv")
    export_file_uw = os.path.join(exportDir, "run" + str(runID), "reynolds_stress_uw.csv")
    
    # save data
    SaveData(export_file_velocity, proxy=plotOverLine3, ChooseArraysToWrite=1,
        PointDataArrays=['Velocity'],
        Precision=23,
        UseScientificNotation=1)

    # set active view
    SetActiveView(lineChartView2)

    # set active source
    SetActiveSource(plotOverLine2)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=plotOverLine3)

    # set active source
    SetActiveSource(plotOverLine3)

    # set active view
    SetActiveView(lineChartView3)

    # Properties modified on plotOverLine3Display
    plotOverLine3Display.XArrayName = 'Points_X'

    # save data
    SaveData(export_file_velocity, proxy=plotOverLine3, ChooseArraysToWrite=1,
        PointDataArrays=['Velocity'],
        Precision=23,
        UseScientificNotation=1)

    # set active view
    SetActiveView(lineChartView2)

    # set active source
    SetActiveSource(plotOverLine2)

    # save data
    SaveData(export_file_uw, proxy=plotOverLine2, ChooseArraysToWrite=1,
        PointDataArrays=['ReynoldsStressUW'],
        Precision=23,
        UseScientificNotation=1)

    # set active view
    SetActiveView(lineChartView1)

    # set active source
    SetActiveSource(plotOverLine1)

    # save data
    SaveData(export_file_uu, proxy=plotOverLine1, ChooseArraysToWrite=1,
        PointDataArrays=['ReynoldsStressUU'],
        Precision=23,
        UseScientificNotation=1)

    # set active view
    SetActiveView(lineChartView3)

    # destroy lineChartView3
    Delete(lineChartView3)
    del lineChartView3

    # close an empty frame
    layout1.Collapse(14)

    # set active view
    SetActiveView(lineChartView2)

    # destroy lineChartView2
    Delete(lineChartView2)
    del lineChartView2

    # close an empty frame
    layout1.Collapse(6)

    # set active view
    SetActiveView(lineChartView1)

    # destroy lineChartView1
    Delete(lineChartView1)
    del lineChartView1

    # close an empty frame
    layout1.Collapse(2)

    # set active view
    SetActiveView(renderView1)

    # set active source
    SetActiveSource(flowvtu)

    # set active source
    SetActiveSource(calculator1)

    # set active source
    SetActiveSource(gradient1)

    # set active source
    SetActiveSource(calculator2)

    # set active source
    SetActiveSource(plotOverLine1)

    # set active source
    SetActiveSource(calculator2_1)

    # set active source
    SetActiveSource(plotOverLine2)

    # set active source
    SetActiveSource(plotOverLine3)

    # hide data in view
    Hide(plotOverLine1, renderView1)

    # show data in view
    calculator2Display = Show(calculator2, renderView1, 'UnstructuredGridRepresentation')

    # show color bar/color legend
    calculator2Display.SetScalarBarVisibility(renderView1, True)

    # destroy plotOverLine1
    Delete(plotOverLine1)
    del plotOverLine1

    # hide data in view
    Hide(calculator2, renderView1)

    # show data in view
    gradient1Display = Show(gradient1, renderView1, 'UnstructuredGridRepresentation')

    # destroy calculator2
    Delete(calculator2)
    del calculator2

    # destroy plotOverLine2
    Delete(plotOverLine2)
    del plotOverLine2

    # destroy calculator2_1
    Delete(calculator2_1)
    del calculator2_1

    # set active source
    SetActiveSource(gradient1)

    # destroy plotOverLine3
    Delete(plotOverLine3)
    del plotOverLine3

    # set active source
    SetActiveSource(calculator1)

    # hide data in view
    Hide(gradient1, renderView1)

    # show data in view
    calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

    # destroy gradient1
    Delete(gradient1)
    del gradient1

    # set active source
    SetActiveSource(flowvtu)

    # hide data in view
    Hide(calculator1, renderView1)

    # show data in view
    flowvtuDisplay = Show(flowvtu, renderView1, 'UnstructuredGridRepresentation')

    # destroy calculator1
    Delete(calculator1)
    del calculator1

    # destroy flowvtu
    Delete(flowvtu)
    del flowvtu

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(1497, 857)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [-47.86624816596016, 197.1521804794827, 69.39683241572104]
    renderView1.CameraFocalPoint = [31.99999999999999, 2.7916503803603815e-16, 1.2795064243318417e-16]
    renderView1.CameraViewUp = [0.07792917036407858, 0.35895882999215595, -0.9300944053035847]
    renderView1.CameraParallelScale = 57.91044770031002

print("Finished post-processing of flow solutions")
print("To see result files, go to: ", exportDir)

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
