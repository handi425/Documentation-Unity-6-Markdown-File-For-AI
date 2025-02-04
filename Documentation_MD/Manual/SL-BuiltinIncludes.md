[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-BuiltinIncludes.html)
  * [中文](/cn/current/Manual/SL-BuiltinIncludes.html)
  * [日本語](/ja/current/Manual/SL-BuiltinIncludes.html)
  * [한국어](/kr/current/Manual/SL-BuiltinIncludes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-BuiltinIncludes.html)
  * [中文](/cn/current/Manual/SL-BuiltinIncludes.html)
  * [日本語](/ja/current/Manual/SL-BuiltinIncludes.html)
  * [한국어](/kr/current/Manual/SL-BuiltinIncludes.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Shader methods in the Built-In Render Pipeline](use-built-in-shader-methods-birp.html)
  * Import a file from the shader library in the Built-In Render Pipeline

[](use-built-in-shader-methods-birp.html)

Shader methods in the Built-In Render Pipeline

[](SL-BuiltinFunctions.html)

Use built-in shader functions in the Built-In Render Pipeline

# Import a file from the shader library in the Built-In Render Pipeline

Unity contains several files that can be used by your [shader
programs](writing-shader-writing-shader-programs-hlsl.html) to bring in
predefined variables and helper functions. This is done by the standard
`#include` directive, e.g.:

    
    
    CGPROGRAM
    // ...
    #include "UnityCG.cginc"
    // ...
    ENDCG
    

Shader include files in Unity are with `.cginc` extension, and the built-in
ones are:

  * `HLSLSupport.cginc` \- _(automatically included)_ It declares various [preprocessor macros](shader-branching-built-in-macros.html) to aid in multi-platform **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) development.

  * `UnityShaderVariables.cginc` \- _(automatically included in CGPROGRAM shaders)_ It declares various [built-in global variables](SL-UnityShaderVariables.html) that are commonly used in shaders.
  * `UnityCG.cginc` \- commonly used [built-in helper functions](SL-BuiltinFunctions.html) and data structures.
  * `AutoLight.cginc` \- lighting & shadowing functionality, e.g. [surface shaders](SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) use this file internally.

  * `Lighting.cginc` \- standard [surface shader](SL-SurfaceShaders.html) lighting models; automatically included when you’re writing surface shaders.
  * `TerrainEngine.cginc` \- helper functions for **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) & Vegetation shaders.

These files are found inside Unity application (**{unity install
path}/Data/CGIncludes/UnityCG.cginc** on Windows,
**/Applications/Unity/Unity.app/Contents/CGIncludes/UnityCG.cginc** on Mac),
if you want to take a look at what exactly is done in any of the helper code.

[](use-built-in-shader-methods-birp.html)

Shader methods in the Built-In Render Pipeline

[](SL-BuiltinFunctions.html)

Use built-in shader functions in the Built-In Render Pipeline

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

