[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/create-light-2d.html)
  * [中文](/cn/current/Manual/urp/create-light-2d.html)
  * [日本語](/ja/current/Manual/urp/create-light-2d.html)
  * [한국어](/kr/current/Manual/urp/create-light-2d.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/create-light-2d.html)
  * [中文](/cn/current/Manual/urp/create-light-2d.html)
  * [日本語](/ja/current/Manual/urp/create-light-2d.html)
  * [한국어](/kr/current/Manual/urp/create-light-2d.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * [Types of 2D lights](../urp/LightTypes.html)
  * Prepare your project for 2D lighting

[](../urp/Lights-2D-intro.html)

Introduction to the 2D lighting system in URP

[](../urp/2DLightProperties.html)

Light 2D component reference for URP

# Prepare your project for 2D lighting

Follow the steps below to prepare your project for 2D lighting and 2D lighting
effects.

The following is the general workflow to include 2D lighting in your project.

  1. Prepare your **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../sprite/sprite-landing.html)  
See in [Glossary](../Glossary.html#Sprite) for lighting. For details, see
[Prepare and upgrade sprites for 2D lighting in URP](PrepShader.html).

  2. Set up **normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](../Glossary.html#Normalmap) and mask Textures. 2D Lights can
interact with normal map and mask Textures linked to Sprites to create
advanced lighting effects, such as [normal
mapping](https://en.wikipedia.org/wiki/Normal_mapping). See [Add normal map
and mask textures to a sprite in URP](SecondaryTextures.html).

  3. Create a 2D Light **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject); see [Light 2D component
reference for URP](2DLightProperties.html).

  4. Configure the 2D Renderer Data asset; see [Configuring the 2D Renderer Asset](2DRendererData-overview.html). 

  5. To define the shape and properties that a Light uses to determine the shadows it casts, use the [Shadow Caster 2D component](2DShadows.html). 

  6. (Optional) if you want to apply 2D Light effects to a **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel) art game, see [Precise pixel scaling
and rotation via the Pixel Perfect Camera in URP](2d-pixelperfect.html).

## Create a Light 2D GameObject

Create a **2D Light** GameObject by going to **GameObject > Light** and
selecting one of the four available types.

![](../../uploads/urp/2D/2d-lights-gameobject-menu.png)

## Additional resources

  * [Light 2D component reference for URP](2DLightProperties.html)
  * [Configure a 2D light](2d-light-properties-explained.html)
  * [Lighting in URP Learn tutorial](https://learn.unity.com/tutorial/editing-lighting-in-the-lightweight-render-pipeline#)

[](../urp/Lights-2D-intro.html)

Introduction to the 2D lighting system in URP

[](../urp/2DLightProperties.html)

Light 2D component reference for URP

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

