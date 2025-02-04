[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/webgl-texture-compression.html)
  * [中文](/cn/current/Manual/webgl-texture-compression.html)
  * [日本語](/ja/current/Manual/webgl-texture-compression.html)
  * [한국어](/kr/current/Manual/webgl-texture-compression.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/webgl-texture-compression.html)
  * [中文](/cn/current/Manual/webgl-texture-compression.html)
  * [日本語](/ja/current/Manual/webgl-texture-compression.html)
  * [한국어](/kr/current/Manual/webgl-texture-compression.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * Texture compression in Web

[](webgl-video.html)

Video playback in Web

[](webgl-embeddedresources.html)

Embedded resources in Web

# Texture compression in Web

Use texture **compression** A method of storing data that reduces the amount
of storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) in the Web platform to create
builds that target platforms based on the **texture compression** 3D Graphics
hardware requires Textures to be compressed in specialized formats which are
optimized for fast Texture sampling. [More info](class-
TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression) formats they support.

## Texture compression formats

Desktop and mobile devices support different texture compression formats. If
you want your Web application to use compressed textures on both types of
browsers, you must first choose a supported texture compression format.

To run your game on both desktop and mobile browsers with compressed textures,
you might want to create two builds targeting:

  * Desktop browsers with DXT set as the texture compression format.
  * Mobile browsers with adaptable scalable texture compression (ASTC) set as the texture compression format.

## Precedence for compression format settings

You can set the default texture compression format for your Web application
from either the [Web Build Settings](web-build-settings.html) window or the
Web [Player Settings](class-PlayerSettingsWebGL.html)Settings that let you set
various player-specific options for the final game built by Unity. [More
info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) window. Before you set the
texture compression format, it’s important to decide which of these settings
take precedence. The texture compression format value you set in Build
Settings has priority over the value you set in Player Settings. By default,
the Unity Editor sets the Build Settings value to **Use Player Settings**.

**Note:** The Editor serializes the texture compression in Build Settings in
the `Library` folder. This means that it’s not managed by **version control**
A system for managing file changes. You can use Unity in conjunction with most
common version control tools, including Perforce, Git, Mercurial and
PlasticSCM. [More info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl).

You can also customize the texture compression format for individual textures.
The value you set for an individual **texture overrides** Platform-specific
settings that allow you to set the resolution, file size with associated
memory size requirements, pixel dimensions, and quality of your Textures for
each target platform. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureOverrides) the default texture
compression format value. For information on how to change the **texture
format** A file format for handling textures during real-time rendering by 3D
graphics hardware, such as a graphics card or mobile device. [More
info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat) of individual textures, refer
to [Texture Import Settings](class-TextureImporter.html).

## Set the default compression format

You can set the default texture compression format for your Web application
using either Build Settings or Player Settings. The texture compression format
value you set in Build Settings has priority over the value you set in Player
Settings. By default, the Unity Editor sets the Build Settings value to **Use
Player Settings**.

To select a default texture compression format using Build Settings:

  1. Select **File** > **Build Settings**.
  2. From the list of platforms in the **Platform** pane, select **Web**.
  3. Select a compression format from the **Texture Compression** drop-down menu.

To select a default texture compression format using Player Settings:

  1. Select **File** > **Build Settings**.
  2. From the list of platforms in the **Platform** pane, select **Web**.
  3. Select **Player Settings** > **Other Settings**.
  4. Select a compression format from the **Texture compression format** drop-down menu.

For an example on how to simultaneously create builds for both desktop
browsers and mobile browsers with their corresponding texture compression
formats, refer to Create builds for desktop and mobile browsers from a script.

## Create builds for desktop and mobile browsers from a script

You can run a build for both desktop browsers and mobile browsers with the
corresponding texture compression formats simultaneously using a script. For
example:

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEditor;
    using System.Diagnostics;
    using System.IO;
    using UnityEditor.Build.Reporting;
    
    public class comboBuild
    {
        //This creates a menu item to trigger the dual builds https://docs.unity3d.com/ScriptReference/MenuItem.html 
    
        [MenuItem("Game Build Menu/Dual Build")]
        public static void BuildGame()
        {
          //This builds the player twice: a build with desktop-specific texture settings (WebGL_Build)
          //as well as mobile-specific texture settings (WebGL_Mobile),
          //and combines the necessary files into one directory (WebGL_Build)
          
          string dualBuildPath    = "WebGLBuilds";
          string desktopBuildName = "WebGL_Build";
          string mobileBuildName  = "WebGL_Mobile";
    
          string desktopPath = Path.Combine(dualBuildPath, desktopBuildName);
          string mobilePath  = Path.Combine(dualBuildPath, mobileBuildName);
          string[] scenes = new string[] {"Assets/scene.unity"};
    
          EditorUserBuildSettings.webGLBuildSubtarget = WebGLTextureSubtarget.DXT;
          BuildPipeline.BuildPlayer(scenes, desktopPath, BuildTarget.WebGL, BuildOptions.Development); 
    
          EditorUserBuildSettings.webGLBuildSubtarget = WebGLTextureSubtarget.ASTC;
          BuildPipeline.BuildPlayer(scenes,  mobilePath, BuildTarget.WebGL, BuildOptions.Development); 
    
          // Copy the mobile.data file to the desktop build directory to consolidate them both
          FileUtil.CopyFileOrDirectory(Path.Combine(mobilePath, "Build", mobileBuildName + ".data"), Path.Combine(desktopPath, "Build", mobileBuildName + ".data"));
        }  
    }
    

You can modify the [Web template’s](webgl-templates.html) `index.html` file to
select the appropriate data file if there’s support for the texture
compression format extension:

    
    
    // choose the data file based on whether there's support for the ASTC texture compression format
          var dataFile = "/{{{ DATA_FILENAME }}}";                                  
          var c = document.createElement("canvas");                                 
          var gl = c.getContext("webgl");                                      
          var gl2 = c.getContext("webgl2");                                    
          if ((gl && gl.getExtension('WEBGL_compressed_texture_astc')) || (gl2 &&   
                  gl2.getExtension('WEBGL_compressed_texture_astc'))) {             
            dataFile =  "/WebGL_Mobile.data";                                       
          }                                                                         
    
          var buildUrl = "Build";
          var loaderUrl = buildUrl + "/{{{ LOADER_FILENAME }}}";                    
          var config = {                                                            
            dataUrl: buildUrl + dataFile,                                           
            frameworkUrl: buildUrl + "/{{{ FRAMEWORK_FILENAME }}}",                 
    #if USE_WASM                                                                    
            codeUrl: buildUrl + "/{{{ CODE_FILENAME }}}",                           
    #endif                                                                          
    #if MEMORY_FILENAME                                                             
            memoryUrl: buildUrl + "/{{{ MEMORY_FILENAME }}}",                       
    #endif
    #if SYMBOLS_FILENAME                                                            
            symbolsUrl: buildUrl + "/{{{ SYMBOLS_FILENAME }}}",                     
    #endif                                                                          
            streamingAssetsUrl: "StreamingAssets",                                
            companyName: {{{ JSON.stringify(COMPANY_NAME) }}},
            productName: {{{ JSON.stringify(PRODUCT_NAME) }}},
          productVersion: {{{ JSON.stringify(PRODUCT_VERSION) }}},                
            showBanner: unityShowBanner,                                            
         };  
    
    

## Additional resources

  * [Build your Web application](webgl-building.html)
  * [Player Settings](class-PlayerSettingsWebGL.html)

[](webgl-video.html)

Video playback in Web

[](webgl-embeddedresources.html)

Embedded resources in Web

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

