[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/use-built-in-shader-methods-import.html)
  * [中文](/cn/current/Manual/urp/use-built-in-shader-methods-import.html)
  * [日本語](/ja/current/Manual/urp/use-built-in-shader-methods-import.html)
  * [한국어](/kr/current/Manual/urp/use-built-in-shader-methods-import.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/use-built-in-shader-methods-import.html)
  * [中文](/cn/current/Manual/urp/use-built-in-shader-methods-import.html)
  * [日本語](/ja/current/Manual/urp/use-built-in-shader-methods-import.html)
  * [한국어](/kr/current/Manual/urp/use-built-in-shader-methods-import.html)

  * [Materials and shaders](../materials-and-shaders.html)
  * [Shaders](../Shaders.html)
  * [Shaders in URP](../urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](../urp/writing-custom-shaders-urp.html)
  * [Shader methods in URP](../urp/use-built-in-shader-methods.html)
  * Import a file from the URP shader library

[](../urp/use-built-in-shader-methods.html)

Shader methods in URP

[](../urp/use-built-in-shader-methods-transformations.html)

Transform positions in a custom URP shader

# Import a file from the URP shader library

The High-Level **Shader** A program that runs on the GPU. [More
info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) Language (HLSL) shader files for
the Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) are in the
`Packages/com.unity.render-pipelines.universal/ShaderLibrary/` folder in your
project.

To import a shader file into a custom shader file, add an `#include` directive
inside the `HLSLPROGRAM` in your shader file. For example:

    
    
    HLSLPROGRAM
    ...
    #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
    ...
    ENDHLSL
    

You can then use the helper methods from the file. For example:

    
    
    float3 cameraPosition = GetCameraPositionWS();
    

Refer to [Shader methods in URP](use-built-in-shader-methods.html) for more
information about the different shader files.

You can also import shader files from the core Scriptable Render Pipeline
(SRP). Refer to [Shader methods in Scriptable Render Pipeline (SRP)
Core](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@17.0/manual/built-in-shader-methods.html).

## Examples

Refer to [Writing custom shaders](writing-custom-shaders-urp.html) for
examples of using variables and helper methods from the files in the URP
shader library.

## Additional resources

  * [include and include_with_pragmas directives in HLSL](https://docs.unity3d.com/Manual/shader-include-directives.html)

[](../urp/use-built-in-shader-methods.html)

Shader methods in URP

[](../urp/use-built-in-shader-methods-transformations.html)

Transform positions in a custom URP shader

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

