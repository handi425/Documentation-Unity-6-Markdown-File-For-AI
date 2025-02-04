[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StandardShaderTransparency.html)
  * [中文](/cn/current/Manual/StandardShaderTransparency.html)
  * [日本語](/ja/current/Manual/StandardShaderTransparency.html)
  * [한국어](/kr/current/Manual/StandardShaderTransparency.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StandardShaderTransparency.html)
  * [中文](/cn/current/Manual/StandardShaderTransparency.html)
  * [日本語](/ja/current/Manual/StandardShaderTransparency.html)
  * [한국어](/kr/current/Manual/StandardShaderTransparency.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](shader-built-in-birp.html)
  * [Standard Shader in the Built-In Render Pipeline](shader-StandardShader-landing.html)
  * [Configuring material properties in the Standard Shader in the Built-In Render Pipeline](StandardShaderChangeProperties.html)
  * Make a material transparent

[](StandardShaderChangeProperties.html)

Configuring material properties in the Standard Shader in the Built-In Render
Pipeline

[](StandardShaderMaterialParameterAlbedoColor.html)

Set the color of a material in the Standard Shader

# Make a material transparent

To make a material transparent if it uses the Standard **Shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), follow these steps in the
****Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window of the material:

  1. Set **Rendering Mode** to **Transparent** or **Fade**.
  2. Select the **Albedo** swatch to open the **Color** window.
  3. Set the **Alpha** (**A**) slider. A value of 0 means fully transparent, and a value of 1 means fully opaque.

![A range of alpha values from 0 to
1](../uploads/Main/StandardShaderTransparencyGraduationTable.jpg) A range of
alpha values from 0 to 1

## Use a texture to control transparency

If you use a texture for **Albedo** instead of a color, by default the alpha
channel of the texture controls the transparency of the material. A value of 0
in the alpha channel means fully transparent, and a value of 1 means fully
opaque. You can use different values to make different areas more or less
transparent.

Unity combines the alpha channel of the texture with the alpha value you set
in the **Color** window. For example, if you set the alpha value in the
**Color** window to 0.1, opaque texture **pixels** The smallest unit in a
computer image. Pixel size depends on your screen resolution. Pixel lighting
is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) become almost fully transparent.

To check the alpha channel of a texture, follow these steps:

  1. Select the texture in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow).

  2. Go to the texture preview section and select the **Alpha** (**A**) button. The preview displays black for 0 and white for 1, with shades of gray between.

![An imported texture. On the left, RGB is selected and the texture preview
section displays all the texture channels. On the right, A is selected and the
texture preview section displays the alpha channel
only.](../uploads/Main/StandardShaderTransparencyMapRGBAlphaToggle.png) An
imported texture. On the left, **RGB** is selected and the texture preview
section displays all the texture channels. On the right, **A** is selected and
the texture preview section displays the alpha channel only. ![The window uses
a single texture to create a fully opaque window frame, partially transparent
windows, and fully transparent
gaps.](../uploads/Main/StandardShaderTransparencyMapBrokenWindow.jpg) The
window uses a single texture to create a fully opaque window frame, partially
transparent windows, and fully transparent gaps.

Refer to [Default Import Settings reference](texture-type-default.html) for
more information about texture transparency settings.

## Additional resources

  * [Material.Color](../ScriptReference/Material-color.html)

[](StandardShaderChangeProperties.html)

Configuring material properties in the Standard Shader in the Built-In Render
Pipeline

[](StandardShaderMaterialParameterAlbedoColor.html)

Set the color of a material in the Standard Shader

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

