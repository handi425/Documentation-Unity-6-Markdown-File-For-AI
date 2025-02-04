[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-server-config-nginx.html)
  * [中文](/cn/current/Manual/web-server-config-nginx.html)
  * [日本語](/ja/current/Manual/web-server-config-nginx.html)
  * [한국어](/kr/current/Manual/web-server-config-nginx.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-server-config-nginx.html)
  * [中文](/cn/current/Manual/web-server-config-nginx.html)
  * [日本語](/ja/current/Manual/web-server-config-nginx.html)
  * [한국어](/kr/current/Manual/web-server-config-nginx.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Build and distribute a Web application](webgl-building-distribution.html)
  * [Server configuration code samples](webgl-server-configuration-code-samples.html)
  * Set up your Nginx server configuration for Web builds 

[](web-server-config-iis.html)

Set up your IIS server configuration for Web builds

[](web-server-config-nodejs.html)

Set up your Node.js server configuration for Web builds

# Set up your Nginx server configuration for Web builds

Set up your Nginx server configuration file to use the Nginx server with Unity
Web builds.

You can use Nginx to serve web content you create with Unity quickly and
efficiently.

For a full code example with all file types and **compression** A method of
storing data that reduces the amount of storage space it requires. See
[Texture Compression](class-TextureImporterOverride), [Animation
Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) types included, refer to Full
code example with all file types.

For information about the Nginx server and how to install it, refer to the
[Nginx documentation](https://nginx.org/en/).

## Edit your Nginx server configuration file for use with Unity

Add the following configuration within your existing HTTP server
configuration.

    
    
    http {
    # ...
    
    server {
    
    # Nest inside existing location rule
    location / {
    # ...
    
    

You are now ready to add code that is specific to your build and what file
types and compression types you want your server to use.

## Add Brotli-precompressed files to your configuration file

To ensure that Brotli-precompressed files of all types are served to clients
efficiently, you need to add some code to your server configuration. But the
code will depend on your file type (data files, JavaScript files, or
WebAssembly files).

### Handle requests for data files

For on-disk Brotli-precompressed data files (data, symbols, and .json files)
add the following code:

    
    
    location ~ .+\.(data|symbols\.json)\.br$ {
        gzip off;
        add_header Content-Encoding br;
        default_type application/octet-stream;
    }
    

Because this file is already pre-compressed on disk, this code disables the
on-demand compression on it. Otherwise Nginx will attempt double compression.

### Handle requests for JavaScript code files

For on-disk Brotli-precompressed JavaScript code files, add the following
code: ` location ~ .+\.js\.br$ { gzip off; # Do not attempt dynamic gzip
compression on an already compressed file add_header Content-Encoding br;
default_type application/javascript; } `

### Handle requests for WebAssembly files

For on-disk Brotli-precompressed WebAssembly files, add the following code:

    
    
    location ~ .+\.wasm\.br$ {
        gzip off; # Do not attempt dynamic gzip compression on an already compressed file
        add_header Content-Encoding br;
        # Enable streaming WebAssembly compilation by specifying the correct MIME type for
        # Wasm files.
        default_type application/wasm;
    }
    

## Add gzip-precompressed files to your configuration files

To ensure that gzip-precompressed files of all types are served to clients
efficiently, you need to add some code to your server configuration. But the
code will depend on your file type (data files, JavaScript files, or
WebAssembly files).

### Handle requests for data files

For on-disk gzip-precompressed data files, add the following code:

    
    
    location ~ .+\.(data|symbols\.json)\.gz$ {
        gzip off; # Do not attempt dynamic gzip compression on an already compressed file
        add_header Content-Encoding gzip;
        default_type application/gzip;
    }
    

### Handle requests for JavaScript code files

For on-disk gzip-precompressed JavaScript files, add the following code:

    
    
    location ~ .+\.js\.gz$ {
        gzip off; # Do not attempt dynamic gzip compression on an already compressed file
        add_header Content-Encoding gzip; # The correct MIME type here would be application/octet-stream, but due to Safari bug https://bugs.webkit.org/show_bug.cgi?id=247421, it's preferable to use MIME Type application/gzip instead.
        default_type application/javascript;
    }
    

### Handle requests for WebAssembly files:

For on-disk gzip-precompressed WebAssembly files, add the following code:

    
    
    location ~ .+\.wasm\.gz$ {
        gzip off; # Do not attempt dynamic gzip compression on an already compressed file
        add_header Content-Encoding gzip;
        # Enable streaming WebAssembly compilation by specifying the correct MIME type for
        # Wasm files.
        default_type application/wasm;
    }
    

## Add C/C++ multithreading support

If you have **Enable Native C/C++ Multithreading** enabled in your [**Player**
settings](class-PlayerSettingsWebGL.html), add the following code to your
server configuration:

    
    
     location ~ .+\.(htm|html|js|js\.gz|js\.br)$ {
         add_header Cross-Origin-Opener-Policy same-origin;
         add_header Cross-Origin-Embedder-Policy require-corp;
         add_header Cross-Origin-Resource-Policy cross-origin;
     }
    
    

## Allow Cross-Origin Resource Sharing requests (optional)

Cross-Origin Resource Sharing (CORS) is a web browser security feature that
controls how web applications can request resources. CORS helps prevent
unauthorized requests from malicious websites, which protects sensitive data.

To allow CORS requests in your server interactions, add the following code to
your configuration file:

    
    
    add_header Access-Control-Allow-Origin *;
    

## Full code example with all file types

The following is a code sample with all files types added.

    
    
    http {
    # ...
    
    server {
    
    # Add the following config within the existing http server configuration
    # Nest inside existing location rule
    location / {
    # ...
    
    # On-disk Brotli-precompressed data files should be served with compression enabled:
    location ~ .+\.(data|symbols\.json)\.br$ {
        # Because this file is already pre-compressed on disk, disable the on-demand compression on it.
        # Otherwise nginx would attempt double compression.
        gzip off;
        add_header Content-Encoding br;
        default_type application/octet-stream;
    }
    
    # On-disk Brotli-precompressed JavaScript code files:
    location ~ .+\.js\.br$ {
        gzip off; # Do not attempt dynamic gzip compression on an already compressed file
        add_header Content-Encoding br;
        default_type application/javascript;
    }
    
    # On-disk Brotli-precompressed WebAssembly files:
    location ~ .+\.wasm\.br$ {
        gzip off; # Do not attempt dynamic gzip compression on an already compressed file
        add_header Content-Encoding br;
        # Enable streaming WebAssembly compilation by specifying the correct MIME type for
        # Wasm files.
        default_type application/wasm;
    }
    
    # On-disk gzip-precompressed data files should be served with compression enabled:
    location ~ .+\.(data|symbols\.json)\.gz$ {
        gzip off; # Do not attempt dynamic gzip compression on an already compressed file
        add_header Content-Encoding gzip;
        default_type application/gzip;
    }
    
    # On-disk gzip-precompressed JavaScript code files:
    location ~ .+\.js\.gz$ {
        gzip off; # Do not attempt dynamic gzip compression on an already compressed file
        add_header Content-Encoding gzip; # The correct MIME type here would be application/octet-stream, but due to Safari bug https://bugs.webkit.org/show_bug.cgi?id=247421, it's preferable to use MIME Type application/gzip instead.
        default_type application/javascript;
    }
    
    # On-disk gzip-precompressed WebAssembly files:
    location ~ .+\.wasm\.gz$ {
        gzip off; # Do not attempt dynamic gzip compression on an already compressed file
        add_header Content-Encoding gzip;
        # Enable streaming WebAssembly compilation by specifying the correct MIME type for
        # Wasm files.
        default_type application/wasm;
    }
    
    # Uncomment the following lines if build was created with "Enable Native C/C++ Multithreading" player settings
    # location ~ .+\.(htm|html|js|js\.gz|js\.br)$ {
    #     add_header Cross-Origin-Opener-Policy same-origin;
    #     add_header Cross-Origin-Embedder-Policy require-corp;
    #     add_header Cross-Origin-Resource-Policy cross-origin;
    # }
    
    # Uncomment the following line to allow CORS requests
    # add_header Access-Control-Allow-Origin *;
    
    }
    }
    }
    

## Additional resources

  * [Compressed builds and server configuration](webgl-deploying.html)
  * [Server configuration code samples](webgl-server-configuration-code-samples.html)
  * [Set up your IIS server configuration for Web builds](web-server-config-iis.html)
  * [Set up your Apache server configuration for Web builds](web-server-config-apache.html)
  * [Set up your Node.js server configuration for Web builds](web-server-config-nodejs.html)

[](web-server-config-iis.html)

Set up your IIS server configuration for Web builds

[](web-server-config-nodejs.html)

Set up your Node.js server configuration for Web builds

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

