[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-PropertiesInPrograms.html)
  * [中文](/cn/current/Manual/SL-PropertiesInPrograms.html)
  * [日本語](/ja/current/Manual/SL-PropertiesInPrograms.html)
  * [한국어](/kr/current/Manual/SL-PropertiesInPrograms.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-PropertiesInPrograms.html)
  * [中文](/cn/current/Manual/SL-PropertiesInPrograms.html)
  * [日本語](/ja/current/Manual/SL-PropertiesInPrograms.html)
  * [한국어](/kr/current/Manual/SL-PropertiesInPrograms.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Adding material properties to shaders](writing-shader-change-properties.html)
  * Add material properties

[](writing-shader-material-properties.html)

Introduction to material properties

[](material-properties-texture-properties.html)

Texture properties

# Add material properties

To assign material properties to a **Shader** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object in **ShaderLab** Unity’s
language for defining the structure of Shader objects. [More info](SL-
Shader.html)  
See in [Glossary](Glossary.html#ShaderLab), you place a `Properties` block
inside a `Shader` block.

If you want to access some of those properties in a [shader program](writing-
shader-writing-shader-programs-hlsl.html), you need to declare a Cg/HLSL
variable with the same name and a matching type.

For example these shader properties:

    
    
    _MyColor ("Some Color", Color) = (1,1,1,1) 
    _MyVector ("Some Vector", Vector) = (0,0,0,0) 
    _MyFloat ("My float", Float) = 0.5 
    _MyTexture ("Texture", 2D) = "white" {} 
    _MyCubemap ("Cubemap", CUBE) = "" {} 
    

would be declared for access in Cg/HLSL code as:

    
    
    fixed4 _MyColor; // low precision type is usually enough for colors
    float4 _MyVector;
    float _MyFloat; 
    sampler2D _MyTexture;
    samplerCUBE _MyCubemap;
    

Cg/HLSL can also accept **uniform** keyword, but it is not necessary:

    
    
    uniform float4 _MyColor;
    

Property types in ShaderLab map to Cg/HLSL variable types this way:

  * Color and Vector properties map to **float4** , **half4** or **fixed4** variables.
  * Range and Float properties map to **float** , **half** or **fixed** variables.
  * Texture properties map to **sampler2D** variables for regular (2D) textures; **Cubemaps** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) map to **samplerCUBE** ; and 3D
textures map to **sampler3D**.

## Color spaces and color/vector shader data

When using [Linear color space](color-spaces-landing.html), all material color
properties are supplied as sRGB colors, but are converted into linear values
when passed into shaders.

For example, if your [Properties](SL-Properties.html) shader block contains a
`Color` property called “ _MyColor“, then the corresponding ”_ MyColor” HLSL
variable will get the linear color value.

For properties that are marked as `Float` or `Vector` type, no color space
conversions are done by default; it is assumed that they contain non-color
data. It is possible to add `[Gamma]` attribute for float/vector properties to
indicate that they are specified in sRGB space, just like colors (see
[Properties](SL-Properties.html)).

## Additional resources

  * [Properties block reference in ShaderLab](SL-Properties.html)
  * [Writing Shader Programs](writing-shader-writing-shader-programs-hlsl.html)

[](writing-shader-material-properties.html)

Introduction to material properties

[](material-properties-texture-properties.html)

Texture properties

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

