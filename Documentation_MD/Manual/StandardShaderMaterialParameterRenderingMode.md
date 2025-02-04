[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StandardShaderMaterialParameterRenderingMode.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterRenderingMode.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterRenderingMode.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterRenderingMode.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StandardShaderMaterialParameterRenderingMode.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterRenderingMode.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterRenderingMode.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterRenderingMode.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](shader-built-in-birp.html)
  * [Standard Shader in the Built-In Render Pipeline](shader-StandardShader-landing.html)
  * [Configuring material properties in the Standard Shader in the Built-In Render Pipeline](StandardShaderChangeProperties.html)
  * Set the Rendering Mode in the Standard Shader using a script

[](StandardShaderMaterialParameterSmoothness.html)

Configure smoothness with the Standard Shader

[](StandardShaderMaterialCharts.html)

Standard Shader realistic settings in the Built-In Render Pipeline reference

# Set the Rendering Mode in the Standard Shader using a script

When you change the **Rendering Mode** , Unity applies a number of changes to
the Material. There is no single C# API to change the Rendering Mode of a
Material, but you can make the same changes in your code.

To see the changes that Unity makes when you change the **Rendering Mode** :

  1. Download the source code for Unity’s built-in **shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). See [Make your own
shader](https://docs.unity3d.com/Manual/StandardShaderMakeYourOwn.html) for
instructions.

  2. Open the file _StandardShaderGUI.cs_.
  3. Locate the area of the file that looks like this, and observe the changes for each **Rendering Mode**.

    
    
    switch (blendMode)
            {
                case BlendMode.Opaque:
                   // Changes associated with Opaque Rendering Mode are here
                    break;
                case BlendMode.Cutout:
                    // Changes associated with Cutout Rendering Mode are here
                    break;
                case BlendMode.Fade:
                    // Changes associated with Fade Rendering Mode are here
                    break;
                case BlendMode.Transparent:
                    // Changes associated with Transparent Rendering Mode are here
                    break;
            }
    
    

![The helmet visor in this image is rendered using the Transparent mode,
because it is supposed to represent a real physical object that has
transparent properties. Here the visor is reflecting the skybox in the scene.
](../uploads/Main/StandardShaderTransparencySkyBoxReflection.jpg) The helmet
visor in this image is rendered using the Transparent mode, because it is
supposed to represent a real physical object that has transparent properties.
Here the visor is reflecting the skybox in the scene.  ![These windows use
Transparent mode, but have some fully opaque areas defined in the texture
\(the window frames\). The Specular reflection from the light sources reflects
off the transparent areas and the opaque
areas.](../uploads/Main/StandardShaderTransparentWindow.jpg) These windows use
Transparent mode, but have some fully opaque areas defined in the texture (the
window frames). The Specular reflection from the light sources reflects off
the transparent areas and the opaque areas. ![The hologram in this image is
rendered using the Fade mode, because it is supposed to represent an opaque
object that is partially faded
out.](../uploads/Main/StandardShaderFadeHologram.jpg) The hologram in this
image is rendered using the Fade mode, because it is supposed to represent an
opaque object that is partially faded out. ![The grass in this image is
rendered using the Cutout mode. This gives clear sharp edges to objects which
is defined by specifying a cut-off threshold. All parts of the image with the
alpha value above this threshold are 100% opaque, and all parts below the
threshold are invisible. To the right in the image you can see the material
settings and the alpha channel of the texture
used.](../uploads/Main/StandardShaderCutoutGrassExample.jpg) The grass in this
image is rendered using the Cutout mode. This gives clear sharp edges to
objects which is defined by specifying a cut-off threshold. All parts of the
image with the alpha value above this threshold are 100% opaque, and all parts
below the threshold are invisible. To the right in the image you can see the
material settings and the alpha channel of the texture used.

[](StandardShaderMaterialParameterSmoothness.html)

Configure smoothness with the Standard Shader

[](StandardShaderMaterialCharts.html)

Standard Shader realistic settings in the Built-In Render Pipeline reference

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

