[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/material-validator-introduction.html)
  * [中文](/cn/current/Manual/material-validator-introduction.html)
  * [日本語](/ja/current/Manual/material-validator-introduction.html)
  * [한국어](/kr/current/Manual/material-validator-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/material-validator-introduction.html)
  * [中文](/cn/current/Manual/material-validator-introduction.html)
  * [日本語](/ja/current/Manual/material-validator-introduction.html)
  * [한국어](/kr/current/Manual/material-validator-introduction.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Materials](Materials.html)
  * [Material Validator in the Built-In Render Pipeline](materials-troubleshooting.html)
  * Material Validator in the Built-In Render Pipeline 

[](materials-troubleshooting.html)

Material Validator in the Built-In Render Pipeline

[](material-validator-validate.html)

Validate and correct materials in the Built-In Render Pipeline

# Material Validator in the Built-In Render Pipeline

The Physically Based Rendering Material Validator is a draw mode in the
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) View. It allows you to make sure your
materials use values which fall within the recommended reference values for
physically-based **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). If **pixel** The smallest unit in a
computer image. Pixel size depends on your screen resolution. Pixel lighting
is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) values in a particular material fall
outside of the reference ranges, the Material Validator highlights the pixels
in different colors to indicate failure.

**Note** : You can also check the recommended values with [Unity’s Material
Charts](StandardShaderMaterialCharts.html). You still need to use these charts
when authoring Materials to decide your **albedo** and **metal specular**
values. However, the Material Validator provides you with a visual, in-editor
way of quickly checking whether your Materials’ values are valid once your
Assets are in the Scene.

**Also note** : The validator only works in Linear color space. Physically
Based Rendering is not intended for use with Gamma color space, so if you are
using Physically Based Rendering and the PBR Material Validator, you should
also be using [Linear color space](color-spaces-landing.html).

## Open the Material Validator

To use the Material Validator, select the **Scene View** An interactive view
into the world you are creating. You use the Scene View to select and position
scenery, characters, cameras, lights, and all other types of Game Object.
[More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView)’s **draw mode** drop-down menu,
which is is usually set to **Shaded** by default.

![The scene views draw mode drop-down
menu](../uploads/Main/materialValidator1.png) The scene view’s draw mode drop-
down menu

Navigate to the **Material Validation** section. The Material Validator has
two modes: **Validate Albedo** and **Validate Metal Specular**.

![The material validation options in the scene view draw mode drop-down
menu](../uploads/Main/materialValidator2.png) The material validation options
in the scene view draw mode drop-down menu

[](materials-troubleshooting.html)

Material Validator in the Built-In Render Pipeline

[](material-validator-validate.html)

Validate and correct materials in the Built-In Render Pipeline

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

