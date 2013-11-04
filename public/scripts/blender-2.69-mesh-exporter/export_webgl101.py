####
# export_webgl101.py
# Copyright © 2013 Vainware.com
# 
# This function exports mesh data from Blender 2.6 to a file in the format used by Erik Möller in his WebGL101 lessons.
####

# works with Blender 2.63+
# modified by joates (Nov-2013)

def exportWebGL101(objName, saveFile):
    # Grab referense to the Blender object
    obj = bpy.data.objects[objName]
    mesh = obj.to_mesh(bpy.context.scene, True, 'PREVIEW')
    uv_layer = mesh.uv_layers.active.data

    indicesList = []
    vertPositions = []
    vertNormals = []
    #vertColors = []
    vertTexCoords = []
    vertCount = 0

    # Main loop
    for poly in mesh.polygons:
        for idx in poly.loop_indices:
            vertexIndex = mesh.loops[idx].vertex_index
            vertPositions.extend(mesh.vertices[vertexIndex].co)
            vertNormals.extend(mesh.vertices[vertexIndex].normal)
            #vertColors.extend(obj.data.materials[face.material_index].diffuse_color)
            vertTexCoords.extend(uv_layer[idx].uv)
        # Build the face using a triangle fan approach.
        for x in range(1, len(poly.vertices)-1):
            indicesList.extend([vertCount, vertCount+x, vertCount+x+1])
        vertCount += len(poly.vertices)

    # Format numbers to seven places after the decimal. I do not care about 64-bit precision. This also cuts down on file size.
    nicePositions = ['{0:.7f}'.format(flt) for flt in vertPositions]
    niceNormals = ['{0:.7f}'.format(flt) for flt in vertNormals]
    #niceColors = ['{0:.7f}'.format(flt) for flt in vertColors]
    niceTexCoords = ['{0:.7f}'.format(flt) for flt in vertTexCoords]

    # Write mesh data as JSON
    with open(saveFile, 'w') as file:
        file.write('{\n');

        # materials
        file.write('  "materials": [ {"vertexshader": "shaders/vshader.txt", "fragmentshader": "shaders/fshader.txt", "numindices": ' + str(len(indicesList)) + ', "diffuse": "textures/diffuse.jpg", "emissive": "textures/emissive.jpg" } ],\n')

        # indices
        file.write('  "indices": ' + str(indicesList) + ',\n')

        # vertex positions
        file.write('  "vertexPositions": [')
        for x in range(0,len(nicePositions)-1):
            file.write(nicePositions[x] + ', ')
        file.write(nicePositions[len(nicePositions)-1] + '],\n')

        # vertex normals 
        file.write('  "vertexNormals": [')
        for x in range(0,len(niceNormals)-1):
            file.write(niceNormals[x] + ', ')
        file.write(niceNormals[len(niceNormals)-1] + '],\n')

        # vertex colors
        #file.write('  "vertexDiffuse": [')
        #for x in range(0,len(niceColors)-1):
        #    file.write(niceColors[x] + ' ,')
        #file.write(niceColors[len(niceColors)-1] + '],\n')

        # vertex texture coords
        file.write('  "vertexTextureCoords": [')
        for x in range(0,len(niceTexCoords)-1):
            file.write(niceTexCoords[x] + ' ,')
        file.write(niceTexCoords[len(niceTexCoords)-1] + ']\n')

        # JSON housekeeping
        file.write('}\n');
        file.close

    print('Mesh ' + obj.name + ' exported.')
