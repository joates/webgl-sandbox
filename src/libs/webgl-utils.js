
  // adapted from..
  // webgl-utils.js
  // by Erik Möller (WebGL 101)

  module.exports = function(gl) {

    return {

      createShader: function(str, type) {
        var shader = gl.createShader(type)
        gl.shaderSource(shader, str)
        gl.compileShader(shader)
        if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
          throw gl.getShaderInfoLog(shader)
        }
        return shader
      },

      createProgram: function(vstr, fstr) {
        var program = gl.createProgram()
        var vshader = this.createShader(vstr, gl.VERTEX_SHADER)
        var fshader = this.createShader(fstr, gl.FRAGMENT_SHADER)
        gl.attachShader(program, vshader)
        gl.attachShader(program, fshader)
        gl.linkProgram(program)
        if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
          throw gl.getProgramInfoLog(program)
        }
        return program
      },

      screenQuad: function() {
        var vertexPosBuffer = gl.createBuffer()
        gl.bindBuffer(gl.ARRAY_BUFFER, vertexPosBuffer)
        var vertices = [-1, -1, 1, -1, -1, 1, 1, 1]
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW)
        vertexPosBuffer.itemSize = 2
        vertexPosBuffer.numItems = 4
        /*
         2___3
         |\  |
         | \ |
         |__\|
         0   1
        */
        return vertexPosBuffer
      },

      linkProgram: function(program) {
        var vshader = this.createShader(program.vshaderSource, gl.VERTEX_SHADER)
        var fshader = this.createShader(program.fshaderSource, gl.FRAGMENT_SHADER)
        gl.attachShader(program, vshader)
        gl.attachShader(program, fshader)
        gl.linkProgram(program)
        if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
          throw gl.getProgramInfoLog(program)
        }
      },

      loadFile: function(file, callback, isCached, isJson) {
        var request = new XMLHttpRequest()
        request.onreadystatechange = function() {
          if (request.readyState == 1) {
            if (isJson) {
              request.overrideMimeType('application/json')
            }
            request.send()
          } else if (request.readyState == 4) {
            if (request.status == 200) {
              callback(request.responseText)
            } else if (request.status == 404) {
              throw 'File "' + file + '" does not exist.'
            } else {
              throw 'XHR error ' + request.status + '.'
            }
          }
        }
        var url = file

	// Note: intentionally bypass the caching mechanism
        // if (!isCached) {
        //   url += '?' + (new Date()).getTime()
        // }

        request.open('GET', url, true)
      },

      loadProgram: function(vs, fs, callback) {
        var program = gl.createProgram()
        var that = this
        function vshaderLoaded(str) {
          program.vshaderSource = str
          if (program.fshaderSource) {
            that.linkProgram(program)
            callback(program)
          }
        }
        function fshaderLoaded(str) {
          program.fshaderSource = str
          if (program.vshaderSource) {
            that.linkProgram(program)
            callback(program)
          }
        }
        // cache enabled (for production)
        //this.loadFile(vs, vshaderLoaded, true)
        //this.loadFile(fs, fshaderLoaded, true)
        
        // cache disabled (for development)
        this.loadFile(vs, vshaderLoaded, false)
        this.loadFile(fs, fshaderLoaded, false)
        return program
      }
    }
  }

  window.onerror = function(msg, url, lineno) {
    alert(url + '(' + lineno + '): ' + msg);
  }

