
  // webgl-sandbox
  // index.js: by joates (Oct-2013)

  var domready = require('domready')
    , raf = require('raf')

  setTimeout(function() { domready(function() {

    var canvas = document.createElement('canvas')
    canvas.width  = window.innerWidth
    canvas.height = window.innerHeight
    document.body.appendChild(canvas)

    var gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl')
      , Mesh   = require('./libs/Mesh.js')
      , vecMat = require('./libs/vector-math.js')

    gl.enable(gl.DEPTH_TEST)
    gl.clearColor(0, 0, 0, 1)

    var mesh = new Mesh(gl)
		  , camera = new vecMat.Matrix4x3()
		  , rotMat = new vecMat.Matrix4x3()
		  , rotZ = 0
      , meshLoaded = false

    function drawFrame(dt) {
			gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT)
			vecMat.modelMatrix().makeRotate(rotZ, 1, 0, 0)
			vecMat.modelMatrix().multiply(rotMat.makeRotate(rotZ, 0, 1, 0))
			vecMat.modelMatrix().multiply(rotMat.makeRotate(rotZ, 0, 0, 1))
			camera.d[14] = 5 + Math.sin(rotZ)
			vecMat.viewMatrix().makeInverseRigidBody(camera)
			mesh.draw()
			rotZ += 0.01
    }

    raf(canvas).on('data', function(dt) {
      if (meshLoaded) drawFrame(dt)
    })

    mesh.load('/models/cube_uvtex.json', function() { meshLoaded = true })

  })}, 0)

