####
# export_webgl101.py
# Copyright © 2013 Vainware.com
# 
# This function exports mesh data from Blender 2.6 to a file in the format used by Erik Möller in his WebGL101 lessons.
####

def exportWebGL101(meshName, saveFile):
	# Grab referense to the Blender object and mesh
	obj = bpy.data.objects[meshName]
	mesh = bpy.data.meshes[obj.name]

	indicesList = []
	vertPositions = []
	vertNormals = []
	vertColors = []
	vertCount = 0

	# Main loop
	for face in mesh.faces:
		for vertIndex in face.vertices:
			vertPositions.extend(mesh.vertices[vertIndex].co)
			vertNormals.extend(face.normal)
			vertColors.extend(obj.data.materials[face.material_index].diffuse_color)
		# Build the face using a triangle fan approach.
		for x in range(1, len(face.vertices)-1):
			indicesList.extend([vertCount, vertCount+x, vertCount+x+1])
		vertCount += len(face.vertices)

	# Format numbers to seven places after the decimal. I do not care about 64-bit precision. This also cuts down on file size.
	nicePositions = ['{0:.7f}'.format(flt) for flt in vertPositions]
	niceNormals = ['{0:.7f}'.format(flt) for flt in vertNormals]
	niceColors = ['{0:.7f}'.format(flt) for flt in vertColors]

	# Write mesh data as JSON
	with open(saveFile, 'w') as file:
		file.write('{\n');
		# materials
		file.write('"materials" : [ {"vertexshader" : "shaders/FILL_ME_IN", "fragmentshader" : "shaders/FILL_ME_IN", "numindices" : ' + str(len(indicesList)) + '} ],\n')
		# indices
		file.write('"indices" : ' + str(indicesList) + ',\n')
		# vertex positions
		file.write('"vertexPositions" : [')
		for x in range(0,len(nicePositions)-1):
			file.write(nicePositions[x] + ', ')
		file.write(nicePositions[len(nicePositions)-1] + '],\n')
		# vertex normals 
		file.write('"vertexNormals" : [')
		for x in range(0,len(niceNormals)-1):
			file.write(niceNormals[x] + ', ')
		file.write(niceNormals[len(niceNormals)-1] + '],\n')
		# vertex colors
		file.write('"vertexDiffuse" : [')
		for x in range(0,len(niceColors)-1):
			file.write(niceColors[x] + ' ,')
		file.write(niceColors[len(niceColors)-1] + ']\n')
		# JSON housekeeping
		file.write('}\n');
		file.close

	print('Mesh ' + mesh.name + ' exported.')
