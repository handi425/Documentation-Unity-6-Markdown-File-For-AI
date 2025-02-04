[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html)
  * [中文](/cn/current/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html)
  * [日本語](/ja/current/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html)
  * [한국어](/kr/current/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html)
  * [中文](/cn/current/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html)
  * [日本語](/ja/current/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html)
  * [한국어](/kr/current/Manual/sprite/sort-sprites/sort-sprites-using-scripts.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Sprites sorting order](../../sprite/sort-sprites/sort-sprites-landing.html)
  * Sort sprites using scripts

[](../../sprite/sort-sprites/sort-sprites.html)

Sort sprites

[](../../sprite/sort-sprites/sprites-sorting-reference.html)

Sprites sorting reference

# Sort sprites using scripts

You can sort **sprites** A 2D graphic objects. If you are used to working in
3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite) per **camera** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) through **scripts** A piece of
code that allows you to create your own Components, trigger game events,
modify Component properties over time and respond to user input in any way you
like. [More info](../../creating-scripts.html)  
See in [Glossary](../../Glossary.html#Scripts), by modifying the following
properties in Camera:

  * [TransparencySortMode](../../../ScriptReference/Camera-transparencySortMode.html) (corresponds with **Transparency Sort Mode**)

  * [TransparencySortAxis](../../../ScriptReference/Camera-transparencySortAxis.html) (corresponds with **Transparency Sort Axis**)

For example:

    
    
    var camera = GetComponent<Camera>();
    
    camera.transparencySortMode = TransparencySortMode.CustomAxis;
    
    camera.transparencySortAxis = new Vector3(0.0f, 1.0f, 0.0f);
    

[](../../sprite/sort-sprites/sort-sprites.html)

Sort sprites

[](../../sprite/sort-sprites/sprites-sorting-reference.html)

Sprites sorting reference

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

