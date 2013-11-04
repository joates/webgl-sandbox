Flat shaded:

![Screenshot](https://raw.github.com/joates/webgl-sandbox/master/screenshot.png)

Diffuse and Emissive textured:

![Screenshot](https://raw.github.com/joates/webgl-sandbox/master/screenshot2.png)

This is a very minimal implementation of WebGL ported to run with node.js/npm modules. The code is only about 26k without the textures. It's completely inspired by the techniques demonstrated by Erik Möller's fantastic 2.5 hour video on YouTube [WebGL 101](http://www.youtube.com/watch?v=me3BviH3nZc), the vast majority of code is all Erik's i have just added a few node.js things to make it easier to deploy with the command ```npm install webgl-sandbox```, ( _i have included Erik's original license in the repo_ ), also follow the links to additional resources if you are interested in getting started using WebGL in the browser.

There are 2 Blender model exporters included in [public/scripts](https://github.com/joates/webgl-sandbox/tree/master/public/scripts)

to run them you need to to use 2 commands in the Blender ```Python Console```:
* exec(open('/path/to/script/export_webgl101.py').read())
* exportWebGL101('ModelName', '/path/to/exported/model/files/modelname.json')

_change the model name in the 2nd command to select a model from the Blender scene_


####The WebGL 101 samples are available live at
* http://emoller.github.com/WebGL101/01-minimal.html
* http://emoller.github.com/WebGL101/02-minimal-draw.html
* http://emoller.github.com/WebGL101/03-minimal-shader.html
* http://emoller.github.com/WebGL101/04-fragmentshader.html
* http://emoller.github.com/WebGL101/05-texturing.html
* http://emoller.github.com/WebGL101/06-xhr-shaders.html
* http://emoller.github.com/WebGL101/07-xhr-mesh.html
* http://emoller.github.com/WebGL101/08-flat-shading.html
* http://emoller.github.com/WebGL101/09-leaving-flatland.html
* http://emoller.github.com/WebGL101/10-perspective-projection.html
* http://emoller.github.com/WebGL101/11-camera.html
* http://emoller.github.com/WebGL101/12-scene-graph.html
* http://emoller.github.com/WebGL101/13-textured-mesh.html
* http://emoller.github.com/WebGL101/14-real-mesh.html

####The two slides from the video are available at
* http://emoller.github.com/WebGL101/documents/opengl-timeline.html
* http://emoller.github.com/WebGL101/documents/programmable-pipeline.html

####The WebGL Reference Card is available at
* http://www.khronos.org/files/webgl/webgl-reference-card-1_0.pdf

####The WebGL Specification is available at
* https://www.khronos.org/registry/webgl/specs/1.0/

####The Odin demo mentioned in the video is available at
* https://github.com/operasoftware/Odin

####The Emberwind game mentioned in the video is available at
* https://github.com/operasoftware/Emberwind
