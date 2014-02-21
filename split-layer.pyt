import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "split-layer"
        self.alias = "split-layer"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "split-layer"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
		
        p0 = arcpy.Parameter(
			displayName="Layer",
			name="Layer",
			datatype="GPLayer",
			parameterType="Required",
			direction="Input")
        p1 = arcpy.Parameter(
			displayName="Field",
			name="Field",
			datatype="Field",
			parameterType="Required",
			direction="Input",
			enabled=False)
        p1.parameterDependencies = [p0.name]
		
        return [p0, p1]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        if parameters[0].value:
			parameters[1].enabled = True
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        inputLayer = parameters[0].valueAsText
        field = parameters[1].valueAsText

		# Assign mxd, default main dataframe and input layer to variables
        openmxd = arcpy.mapping.MapDocument('CURRENT')
        df = arcpy.mapping.ListDataFrames(openmxd)[0]
        addLayer = arcpy.mapping.Layer(inputLayer)

		# list of unique values in specified field
        values = []
		
		# Create cursor, iterate through
        cursor = arcpy.SearchCursor(inputLayer)
        for row in cursor:
			if row.getValue(field) not in values:
				values.append(row.getValue(field))

        for each in values:
			arcpy.mapping.AddLayer(df, addLayer, 'TOP')
			editlyr = arcpy.mapping.ListLayers(openmxd)[0]
			editlyr.name = '_'.join([addLayer.name, field, str(each)])
			# Create value for query depending on type
			if isinstance(each, unicode):
				queryValue = "'"+str(each)+"'"
			else:
				queryValue = str(each)
			# Ensure layer supports definition query then either assign new definition query
			# or append additional query
			if editlyr.supports("DEFINITIONQUERY"):
				if editlyr.definitionQuery <> '':
					editlyr.definitionQuery = editlyr.definitionQuery + ' AND ' + '"' + field + '" = '+ queryValue
				else:
					editlyr.definitionQuery = '"' + field + '" = ' + queryValue
        return
