[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-server-config-nodejs.html)
  * [中文](/cn/current/Manual/web-server-config-nodejs.html)
  * [日本語](/ja/current/Manual/web-server-config-nodejs.html)
  * [한국어](/kr/current/Manual/web-server-config-nodejs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-server-config-nodejs.html)
  * [中文](/cn/current/Manual/web-server-config-nodejs.html)
  * [日本語](/ja/current/Manual/web-server-config-nodejs.html)
  * [한국어](/kr/current/Manual/web-server-config-nodejs.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Build and distribute a Web application](webgl-building-distribution.html)
  * [Server configuration code samples](webgl-server-configuration-code-samples.html)
  * Set up your Node.js server configuration for Web builds

[](web-server-config-nginx.html)

Set up your Nginx server configuration for Web builds

[](Windows.html)

Windows

# Set up your Node.js server configuration for Web builds

Create a Node.js server configuration file that lets your Node.js server work
with your Unity Web build.

Node.js is an open-source runtime environment that lets you execute JavaScript
code on the server side. In Unity, you can use a Node.js app to serve your
Unity Web build.

For more information about Node.js and how to install and use it, refer to the
[Node.js documentation](https://nodejs.org/en/learn/getting-
started/introduction-to-nodejs).

## Set up your package.json file

To create a package.json file that’s ready for use with Unity Web:

  1. Create a file in a text editor or IDE. 

  2. Name the file `package.json`. 

  3. Save your file in your Node.js project directory.

  4. Paste the following code into the file: 
    
        {
      "name": "node_server_example",
      "version": "1.0.0",
      "description": "An example for serving a Unity Web build with Node.js",
      "main": "index.js",
      "dependencies": {
        "express": "^4.19.2"
      }
    }
    

Your `package.json` file is now ready for use. The code defines the `index.js`
file as your server project’s entry point, and defines the libraries your
project will depend on.

## Set up your index.js file

To prepare your index.js file for use with Unity Web:

  1. Create a file in a text editor or IDE. 

  2. Name the file `package.json`. 

  3. Save your file in your Node.js project directory.

  4. Paste the following code into the file: 
    
        #!/usr/bin/env node
    const path = require('path');
    const express = require('express');
    
    // Create express application
    const app = express();
    
    // Settings
    const hostname = 'localhost';
    const port = 8080;
    const enableCORS = true; 
    const enableWasmMultithreading = true;
    
    
    // Serve the current working directory 
    const unityBuildPath = __dirname; // Note: this makes the current working directory visible to all computers over the network.
    
    app.use((req, res, next) => {
        var path = req.url;
    
        // Provide COOP, COEP and CORP headers for SharedArrayBuffer
        // multithreading: https://web.dev/coop-coep/
        if (enableWasmMultithreading &&
            (
                path == '/' ||
                path.includes('.js') ||
                path.includes('.html') ||
                path.includes('.htm')
            )
        ) {
            res.set('Cross-Origin-Opener-Policy', 'same-origin');
            res.set('Cross-Origin-Embedder-Policy', 'require-corp');
            res.set('Cross-Origin-Resource-Policy', 'cross-origin');
        }
    
        // Set CORS headers
        if (enableCORS) {
            res.set('Access-Control-Allow-Origin', '*');
        }    
    
        // Set content encoding depending on compression
        if (path.endsWith('.br')) {
            res.set('Content-Encoding', 'br');
        } else if (path.endsWith('.gz')) {
            res.set('Content-Encoding', 'gzip');
        }
    
        // Explicitly set content type. Files can have wrong content type if build uses compression.
        if (path.includes('.wasm')) {
            res.set('Content-Type', 'application/wasm');
        } else if (path.includes('.js')) {
            res.set('Content-Type', 'application/javascript');
        } else if (path.includes('.json')) {
            res.set('Content-Type', 'application/json');
        } else if (
        path.includes('.data') ||
        path.includes('.bundle') ||
        path.endsWith('.unityweb')
        ) {
            res.set('Content-Type', 'application/octet-stream');
        }
    
        // Ignore cache-control: no-cache 
        // when if-modified-since or if-none-match is set
        // because Unity Loader will cache and revalidate manually
        if (req.headers['cache-control'] == 'no-cache' &&
        (
            req.headers['if-modified-since'] ||
            req.headers['if-none-match']
        )
        ) {       
            delete req.headers['cache-control'];
        }        
    
        next();
    });
    
    app.use('/', express.static(unityBuildPath, { immutable: true }));
    
    const server = app.listen(port, hostname, () => {
        console.log(`Web server serving directory ${unityBuildPath} at http://${hostname}:${port}`);
    });
    
    server.addListener('error', (error) => {
        console.error(error);
    });
    
    server.addListener('close', () => {
        console.log('Server stopped.');
        process.exit();
    });
    

  5. If your build loads via CORS (for example, embedded on different website), then set the following line in your code to `true`, otherwise set it to `false`: 
    
        const enableCORS = true; 
    

  6. If you created your build with multithreading support, set the following line in your code to `true`, otherwise set it to `false`:
    
        const enableWasmMultithreading = true;
    

Your server configuration is now ready for use with Unity Web builds.

## Additional resources

  * [Compressed builds and server configuration](webgl-deploying.html)
  * [Server configuration code samples](webgl-server-configuration-code-samples.html)
  * [Set up your IIS server configuration for Web builds](web-server-config-iis.html)
  * [Set up your Apache server configuration for Web builds](web-server-config-apache.html)
  * [Set up your Nginx server configuration for Web builds](web-server-config-nginx.html)

[](web-server-config-nginx.html)

Set up your Nginx server configuration for Web builds

[](Windows.html)

Windows

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

