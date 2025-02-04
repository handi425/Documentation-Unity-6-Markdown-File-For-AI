[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-use-material-properties.html)
  * [中文](/cn/current/Manual/writing-shader-use-material-properties.html)
  * [日本語](/ja/current/Manual/writing-shader-use-material-properties.html)
  * [한국어](/kr/current/Manual/writing-shader-use-material-properties.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-use-material-properties.html)
  * [中文](/cn/current/Manual/writing-shader-use-material-properties.html)
  * [日本語](/ja/current/Manual/writing-shader-use-material-properties.html)
  * [한국어](/kr/current/Manual/writing-shader-use-material-properties.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Adding material properties to shaders](writing-shader-change-properties.html)
  * Set shader variables with material property values

[](writing-shader-use-material-properties-code.html)

Access material properties in a script

[](writing-shader-display-types.html)

Control material properties in the Inspector window

# Set shader variables with material property values

## Using material properties to set variables in ShaderLab code

To set the value of a variable in your **ShaderLab** Unity’s language for
defining the structure of Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) code from a material property, put
the material property name in square brackets in your ShaderLab code.

This example code demonstrates the syntax for using a material property to set
the `units` value of the ShaderLab `Offset` command.

    
    
    Shader "Examples/MaterialPropertyShaderLab"
    {
        Properties
        {
            // Change this value in the Material Inspector to affect the value of the Offset command
            _OffsetUnitScale ("Offset unit scale", Integer) = 1
        }
        SubShader
        {
            // The code that defines the rest of the SubShader goes here
    
            Pass
            {
                Offset 0, [_OffsetUnitScale]
    
               // The code that defines the rest of the Pass goes here
            }
        }
    }
    

## Using material properties to set variables in HLSL code

To set the value of a variable in HLSL code using a material property, give
the material property the same name as the **shader** A program that runs on
the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) property.

You can see this technique in the following articles, which include working
code examples:

  * [Writing vertex and fragment shaders for the Built-in Render Pipeline](built-in-shader-examples.html)
  * [Writing custom shaders for the Universal Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/manual/writing-custom-shaders-urp.html)

[](writing-shader-use-material-properties-code.html)

Access material properties in a script

[](writing-shader-display-types.html)

Control material properties in the Inspector window

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

