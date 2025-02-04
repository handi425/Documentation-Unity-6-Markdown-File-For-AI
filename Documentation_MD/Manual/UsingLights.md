[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UsingLights.html)
  * [中文](/cn/current/Manual/UsingLights.html)
  * [日本語](/ja/current/Manual/UsingLights.html)
  * [한국어](/kr/current/Manual/UsingLights.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UsingLights.html)
  * [中文](/cn/current/Manual/UsingLights.html)
  * [日本語](/ja/current/Manual/UsingLights.html)
  * [한국어](/kr/current/Manual/UsingLights.html)

  * [Lighting](LightingOverview.html)
  * [Light sources](lighting-light-sources.html)
  * [Light components](lighting-light-components.html)
  * Place Light components

[](PerPixelLights.html)

Per-pixel and per-vertex lights

[](lighting-light-components-configuring.html)

Configuring Light components

# Place Light components

Lights are easy to use in Unity - you need to create a light of the desired
type (for example, from the menu **GameObject > Light > Point Light**) and
place it where you want it in the scene. If you enable scene view lighting
(the “lightbulb” button on the toolbar) then you can see a preview of how the
lighting will look as you move light objects and set their parameters.

A directional light can be placed anywhere in the **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) (unless it’s using a Cookie) with the
forward/Z axis indicating the direction. A Spot Light also has a direction but
since it has a limited range, its position _does_ matter. The shape parameters
of spot, point, and area lights can be adjusted from the **inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) or by using the lights’ **Gizmos**
A graphic overlay associated with a GameObject in a Scene, and displayed in
the Scene View. Built-in scene tools such as the move tool are Gizmos, and you
can create custom Gizmos using textures or scripting. Some Gizmos are only
drawn when the GameObject is selected, while other Gizmos are drawn by the
Editor regardless of which GameObjects are selected. [More
info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) directly in the **scene view** An
interactive view into the world you are creating. You use the Scene View to
select and position scenery, characters, cameras, lights, and all other types
of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView).

![A Spot Light with Gizmos visible](../uploads/Main/LightUsageSpotGizmo.png) A
Spot Light with Gizmos visible

## Guidelines for Placing Lights

A directional light often represents the sun and has a significant effect on
the look of a scene. The direction of the light should point slightly
downwards but you will usually want to make sure that it also makes a slight
angle with major objects in the scene. For example, a roughly cubic object
will be more interestingly shaded and appear to “pop” out in 3D much more if
the light isn’t coming head-on to one of the faces.

Spot lights and point lights usually represent artificial light sources and so
their positions are usually determined by scene objects. One common pitfall
with these lights is that they appear to have no effect at all when you first
add them to the scene. This happens when you adjust the range of the light to
fit neatly within the scene. The range of a light is the limit at which the
light’s brightness dims to zero. If you set, say, a spot light so the base of
the cone neatly lands on the floor then the light will have little or no
effect unless another object passes underneath it. If you want the level
geometry to be illuminated then you should expand point and spot lights so
they pass through the walls and floors.

## Color and Intensity

A light’s color and intensity (brightness) are properties you can set from the
inspector. The default intensity and white color are fine for “ordinary”
lighting that you use to apply shading to objects but you might want to vary
the properties to produce special effects. For example, a glowing green
forcefield might be bright enough to bathe surrounding objects in intense
green light; car headlights (especially on older cars) typically have a slight
yellow color rather than brilliant white. These effects are most often used
with point and spot lights but you might change the color of a directional
light if, say, your game is set on a distant planet with a red sun.

[](PerPixelLights.html)

Per-pixel and per-vertex lights

[](lighting-light-components-configuring.html)

Configuring Light components

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

