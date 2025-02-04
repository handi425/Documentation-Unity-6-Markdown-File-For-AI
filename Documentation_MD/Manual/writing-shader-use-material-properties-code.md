[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-use-material-properties-code.html)
  * [中文](/cn/current/Manual/writing-shader-use-material-properties-code.html)
  * [日本語](/ja/current/Manual/writing-shader-use-material-properties-code.html)
  * [한국어](/kr/current/Manual/writing-shader-use-material-properties-code.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-use-material-properties-code.html)
  * [中文](/cn/current/Manual/writing-shader-use-material-properties-code.html)
  * [日本語](/ja/current/Manual/writing-shader-use-material-properties-code.html)
  * [한국어](/kr/current/Manual/writing-shader-use-material-properties-code.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Adding material properties to shaders](writing-shader-change-properties.html)
  * Access material properties in a script

[](material-properties-texture-properties.html)

Texture properties

[](writing-shader-use-material-properties.html)

Set shader variables with material property values

# Access material properties in a script

Material properties are represented in C# code by the
[MaterialProperty](../ScriptReference/MaterialProperty.html) class.

To access variables defined in your HLSL code, you can call
[Material.GetFloat](../ScriptReference/Material.GetFloat.html),
[Material.SetFloat](../ScriptReference/Material.SetFloat.html). There are
other, similar methods; see the [Material API
documentation](../ScriptReference/Material.html) for a full list. When you
access HLSL variables using these APIs, it doesn’t matter whether the variable
is a material property or not.

[](material-properties-texture-properties.html)

Texture properties

[](writing-shader-use-material-properties.html)

Set shader variables with material property values

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

