import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "split-layer"
        self.alias = "split-layer"

        # List of tool classes associated with this toolbox
        self.tools = [SplitLayer]


class SplitLayer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "split-layer"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName='Layer',
            name='inputLayer',
            datatype='GPLayer',
            parameterType='Required',
            direction='Input')
        
		
        param1 = arcpy.Parameter(
            displayName='Field',
            name='field',
            datatype='Field',
            parameterType='Required',
            direction='Input')
        param1.parameterDependencies = [param0.name]
		
        params = [param0, param1]

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
		
        field_filter = self.params[1].filter
		
        if self.params[0].value:
            field_filter.list = arcpy.ListFields(params[0].parameter)
			
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return
