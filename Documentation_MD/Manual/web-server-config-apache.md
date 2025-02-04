[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-server-config-apache.html)
  * [中文](/cn/current/Manual/web-server-config-apache.html)
  * [日本語](/ja/current/Manual/web-server-config-apache.html)
  * [한국어](/kr/current/Manual/web-server-config-apache.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-server-config-apache.html)
  * [中文](/cn/current/Manual/web-server-config-apache.html)
  * [日本語](/ja/current/Manual/web-server-config-apache.html)
  * [한국어](/kr/current/Manual/web-server-config-apache.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Build and distribute a Web application](webgl-building-distribution.html)
  * [Server configuration code samples](webgl-server-configuration-code-samples.html)
  * Set up your Apache server configuration for Web builds

[](webgl-server-configuration-code-samples.html)

Server configuration code samples

[](web-server-config-iis.html)

Set up your IIS server configuration for Web builds

# Set up your Apache server configuration for Web builds

Set up your Apache server configuration file to use the Apache server with
Unity Web builds.

Apache is an open source, cross-platform web server that you can use to serve
applications you create with Unity Web.

For more information about Apache and how to install and use it, refer to the
[Apache documentation](https://httpd.apache.org/docs/).

## Choose your Apache Web build method

You can configure Web builds in Apache using one of the two methods:

  * Virtual host in `httpd.conf`.

  * Virtual host in `.htaccess`. 

The recommended best practice is to configure a virtual host in Apache’s
`httpd.conf`, if you have access to that configuration.

### Use the virtual host in `httpd.conf` method

To configure Web builds using the virtual host in `httpd.conf` method, use the
following code in your Apache server configuration:

    
    
    <Directory /var/www/html/root/path/to/your/unity/content/>
    <IfModule mod_mime.c>
    RemoveType .gz
    AddEncoding gzip .gz
    # The correct MIME type for .data.gz would be application/octet-stream, but due to Safari bug https://bugs.webkit.org/show_bug.cgi?id=247421, it is preferable to use MIME Type application/gzip instead.
    #AddType application/octet-stream .data.gz
    AddType application/gzip .data.gz
    AddType application/wasm .wasm.gz
    AddType application/javascript .js.gz
    AddType application/octet-stream .symbols.json.gz
    
    RemoveType .br
    AddEncoding br .br
    AddType application/octet-stream .data.br
    AddType application/wasm .wasm.br
    AddType application/javascript .js.br
    AddType application/octet-stream .symbols.json.br
    
    # Insert additional code here
    
    </IfModule>
    </Directory>
    

### Use the virtual host in `.htaccess` method

If you’re unable to modify `httpd.conf`, for example, due to unavailable admin
rights to your web hosting, but your Apache supports `.htaccess`, then you can
configure `.htaccess` in the following way:

    
    
    # NOTE: "mod_mime" Apache module must be enabled for this configuration to work.
    <IfModule mod_mime.c>
    
    # The following lines are required for builds without decompression fallback, compressed with gzip
    RemoveType .gz
    AddEncoding gzip .gz
    AddType application/gzip .data.gz # The correct MIME type here would be application/octet-stream, but due to Safari bug https://bugs.webkit.org/show_bug.cgi?id=247421, it's preferable to use MIME Type application/gzip instead.
    AddType application/wasm .wasm.gz
    AddType application/javascript .js.gz
    AddType application/octet-stream .symbols.json.gz
    
    # The following lines are required for builds without decompression fallback, compressed with Brotli
    RemoveType .br
    RemoveLanguage .br
    AddEncoding br .br
    AddType application/octet-stream .data.br
    AddType application/wasm .wasm.br
    AddType application/javascript .js.br
    AddType application/octet-stream .symbols.json.br
    
    # The following line improves loading performance for uncompressed builds
    AddType application/wasm .wasm
    
    # Insert additional code here
    
    </IfModule>
    

## Improve performance for gzip-compressed builds

To improve loading performance of a gzip-compressed Web build with
decompression fallback, add the following line to your code:

    
    
    AddEncoding gzip .unityweb
    

## Improve performance for Brotli-compressed builds with decompression
fallback

To improve loading performance for Brotli-compressed builds with decompression
fallback, add the following line of code to your configuration:

    
    
     AddEncoding br .unityweb
    

## Enable native C/C++ multithreading

If you created your build with **Enable Native C/C++ Multithreading** enabled
in the [**Player** settings](class-PlayerSettingsWebGL.html), add the
following code to your configuration file:

    
    
     <FilesMatch "\.(htm|html|js|js.gz|js.br)$">
         Header add Cross-Origin-Opener-Policy "same-origin"
         Header add Cross-Origin-Embedder-Policy "require-corp"
         Header add Cross-Origin-Resource-Policy "cross-origin"
     </FilesMatch>
    

## Allow Cross-Origin Resource Sharing (CORS) requests

To allow CORS requests, add the following code to your configuration: ` Header
add Access-Control-Allow-Origin "*" `

## Additional resources

  * [Compressed builds and server configuration](webgl-deploying.html)
  * [Server configuration code samples](webgl-server-configuration-code-samples.html)
  * [Set up your IIS server configuration for Web builds](web-server-config-iis.html)
  * [Set up your Nginx server configuration for Web builds](web-server-config-nginx.html)
  * [Set up your Node.js server configuration for Web builds](web-server-config-nodejs.html)

[](webgl-server-configuration-code-samples.html)

Server configuration code samples

[](web-server-config-iis.html)

Set up your IIS server configuration for Web builds

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

